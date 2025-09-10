# Music Generation with AI

## Overview
A simple Python project that uses AI to generate guitar-style music from MIDI files.

## Features
- Generate new guitar-style MIDI music  
- Play and listen to generated music  
- Export results as .mid files  

## Technologies Used
- Python  
- PyTorch / TensorFlow  
- music21, pretty_midi, mido  
- numpy, sounddevice  

## How to Run
```bash
# 1. Clone repo
git clone https://github.com/ravulapallisairam/Music-Generation-with-AI.git
cd Music-Generation-with-AI

# 2. Install dependencies
pip install -r requirements.txt

# 3. Prepare dataset
python prepare_data.py

# 4. Train model
python train_model.py

# 5. Generate music
python generate_music.py

# 6. Play music
python play_music.py
