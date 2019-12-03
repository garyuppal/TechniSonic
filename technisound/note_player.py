# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 2019

@author: gary uppal
"""

import numpy as np
import sounddevice as sd
import time
from piano_note import PianoNote


class NotePlayer:
    notes = PianoNote()
    # sampling rate (samples per second)
    SPS = 44100
    BASE_DURATION = 1  # 1 second
    BASE_AMPLITUDE = 0.3

    def getFrequencies(self, notes):
        frequencies = list()
        for note in notes:
            freq = self.notes.noteToFrequency(note)
            frequencies.append(freq)
        return frequencies  # NOTE: this probably isn't the best way to do this

    def getWaveForm(self, notes):
        frequencies = self.getFrequencies(notes)

        tune = np.array([])
        for i in range(len(notes)):  # frequencies:
            freq_hz = frequencies[i]
            duration = self.BASE_DURATION/notes[i][3]

            samples = np.arange(duration * self.SPS)
            waveform = np.sin(2 * np.pi * samples * freq_hz / self.SPS)
            tune = np.concatenate([tune, waveform])
        return tune

    def playWaveForm(self, tune):
        sd.play(tune, self.SPS)
        sleep_time = (len(tune)/self.SPS)+5
        time.sleep(sleep_time*self.BASE_DURATION)  # needs to be as long as tune
        sd.stop()


player = NotePlayer()
# frequencies = player.getFrequencies([('a',4), ('a',5)])
# print(frequencies)

# note: key, octave, accidental, duration
first_line = [('c', 4, 'n', 4), ('c', 4, 'n', 4), ('g', 4, 'n', 4), ('g', 4, 'n', 4),
              ('a', 5, 'n', 4), ('a', 5, 'n', 4), ('g', 4, 'n', 2),
              ('f', 4, 'n', 4), ('f', 4, 'n', 4), ('e', 4, 'n', 4), ('e', 4, 'n', 4),
              ('d', 4, 'n', 4), ('d', 4, 'n', 4), ('c', 4, 'n', 2), ]
middle_line = [('g', 4, 'n', 4), ('g', 4, 'n', 4), ('f', 4, 'n', 4), ('f', 4, 'n', 4),
               ('e', 4, 'n', 4), ('e', 4, 'n', 4), ('d', 4, 'n', 2),
               ('g', 4, 'n', 4), ('g', 4, 'n', 4), ('f', 4, 'n', 4), ('f', 4, 'n', 4),
               ('e', 4, 'n', 4), ('e', 4, 'n', 4), ('d', 4, 'n', 2)]

notes = first_line + middle_line
notes = notes + first_line
print(notes)
print(len(notes))
tune = player.getWaveForm(notes)
print(tune.nbytes)

print(len(tune))
player.playWaveForm(tune)

# test git
