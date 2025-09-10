# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 17:11:03 2025

@author: saira
"""

from music21 import converter, instrument, note, chord
import os
import pickle

notes = []

midi_folder = "midi_songs"  # Folder where your MIDI files are

for file in os.listdir(midi_folder):
    if file.endswith(".mid"):
        midi = converter.parse(os.path.join(midi_folder, file))
        parts = instrument.partitionByInstrument(midi)
        notes_to_parse = parts.parts[0].recurse() if parts else midi.flat.notes

        for element in notes_to_parse:
            if isinstance(element, note.Note):
                notes.append(str(element.pitch))
            elif isinstance(element, chord.Chord):
                notes.append('.'.join(str(n) for n in element.normalOrder))

# Save the notes
if not os.path.exists("data"):
    os.makedirs("data")

with open("data/notes.pkl", "wb") as f:
    pickle.dump(notes, f)