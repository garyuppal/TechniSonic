# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 2019

@author: gary uppal
"""

import numpy as np 
import sounddevice as sd 
from piano_note import PianoNote

class NotePlayer:
    notes = PianoNote()

    def getFrequencies(self,notes):
        frequencies = list()
        for note in notes:
            freq = self.notes.noteToFrequency(note)
            frequencies.append(freq)
        return frequencies # NOTE: this probably isn't the best way to do this


