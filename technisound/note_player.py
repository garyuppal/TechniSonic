# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 2019

@author: gary uppal
"""

import numpy as np
import sounddevice as sd
import time
from technisound.piano_note import PianoNote


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



