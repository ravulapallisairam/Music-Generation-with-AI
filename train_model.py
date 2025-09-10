# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 17:26:11 2025

@author: saira
"""
import pickle
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Dense, Activation
from tensorflow.keras.utils import to_categorical

# Load notes from the preprocessed pickle file
with open("data/notes.pkl", "rb") as f:
    notes = pickle.load(f)

# Create note to int mapping
pitchnames = sorted(set(notes))
note_to_int = {note: num for num, note in enumerate(pitchnames)}

sequence_length = 100
network_input = []
network_output = []

# Prepare sequences used by the Neural Network
for i in range(len(notes) - sequence_length):
    seq_in = notes[i:i + sequence_length]
    seq_out = notes[i + sequence_length]
    network_input.append([note_to_int[char] for char in seq_in])
    network_output.append(note_to_int[seq_out])

n_patterns = len(network_input)

# Reshape input for LSTM: (samples, time steps, features)
network_input = np.reshape(network_input, (n_patterns, sequence_length, 1))

# Normalize input
network_input = network_input / float(len(pitchnames))

# One-hot encode output
network_output = to_categorical(network_output)

# Build the LSTM model
model = Sequential()
model.add(LSTM(512, input_shape=(sequence_length, 1), return_sequences=True))
model.add(Dropout(0.3))
model.add(LSTM(512))
model.add(Dropout(0.3))
model.add(Dense(256))
model.add(Activation("relu"))
model.add(Dense(len(pitchnames)))
model.add(Activation("softmax"))

# Compile the model
model.compile(loss="categorical_crossentropy", optimizer="adam")

# Train the model
model.fit(network_input, network_output, epochs=50, batch_size=64)

# Save the model
model.save("model/music_model.h5")