# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 2019

@author: gary uppal
"""

class PianoNote:
    STANDARD_PITCH = 440 # tuning for A4 key -- above middle c, middle c is c3
    KEY_A4 = 49

    def noteToKey(self,note):
        # determine key in 4th octave:
        if note[0].upper() == 'A': 
            key = self.KEY_A4  
        elif note[0].upper() == 'B': 
            key = self.KEY_A4  + 2 # B is two above A
        elif note[0].upper() == 'C': 
            key = self.KEY_A4  + 3 # C is 3 above A
        elif note[0].upper() == 'D':
            key = self.KEY_A4  + 5
        elif note[0].upper() == 'E':
            key = self.KEY_A4  + 7
        elif note[0].upper() == 'F':
            key = self.KEY_A4  + 8
        elif note[0].upper() == 'G':
            key = self.KEY_A4  + 10

        # find octave:
        key += 12*( note[1] - 4 )
        
        # add accidental:
        if len(note) > 2:
            if note[2] == '#': # test cases
                key += 1
            elif note[2] == 'b':
                key -= 1

        return key

    def keyToFrequency(self,key):
        exponent = (key - 49)/12
        freq = (2 ** exponent) * self.STANDARD_PITCH
        return freq

    def noteToFrequency(self,note):
        key = self.noteToKey(note)
        return self.keyToFrequency(key)

    
        
    