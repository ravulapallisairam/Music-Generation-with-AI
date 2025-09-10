# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 17:35:12 2025

@author: saira
"""
# -- coding: utf-8 --
"""
Created on Wed Jul 16 17:35:12 2025
@author: saira
"""

import numpy as np
from music21 import stream, note
from keras.models import Sequential
from keras.layers import LSTM, Dense

# Step 1: Sample note data
notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
sequence_length = 5

X = []
y = []

for i in range(len(notes) - sequence_length):
    seq_in = notes[i:i + sequence_length]
    seq_out = notes[i + sequence_length - 1]
    X.append([notes.index(n) for n in seq_in])
    y.append(notes.index(seq_out))

X = np.array(X).reshape(len(X), sequence_length, 1) / float(len(notes))
y = np.array(y)

# Step 2: Create LSTM model
model = Sequential()
model.add(LSTM(128, input_shape=(sequence_length, 1)))
model.add(Dense(len(notes), activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')

# Step 3: Train model
model.fit(X, y, epochs=100, verbose=0)

# Step 4: Generate new notes
start = X[0]
generated_notes = []

for _ in range(50):
    prediction = model.predict(start.reshape(1, sequence_length, 1), verbose=0)
    index = np.argmax(prediction)
    generated_notes.append(notes[index])
    start = np.append(start[1:], [[index / float(len(notes))]], axis=0)

# Step 5: Save as MIDI
output_notes = []
for n in generated_notes:
    new_note = note.Note(n)
    new_note.duration.quarterLength = 0.5
    output_notes.append(new_note)

midi_stream = stream.Stream(output_notes)
midi_stream.write('midi', fp='generated_music.mid')

print("✅ Music generated and saved as generated_music.mid")