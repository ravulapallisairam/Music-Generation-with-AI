# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 17:38:44 2025

@author: saira
"""
import pygame
import time

midi_file = 'generated_music.mid'

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(midi_file)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(1)