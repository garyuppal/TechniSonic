# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 2019

@author: gary uppal
"""
import unittest
from note_player import NotePlayer 
import numpy as np

class TestNotePlayer(unittest.TestCase):
    def setUp(self):
        self.player = NotePlayer()

    def tearDown(self):
        pass

    def test_getFrequencies(self):
        result = self.player.getFrequencies([('a',4), ('a',5)])
        desired = [440,880]
        self.assertListEqual(result,desired)

    # def test_getWaveForm(self):
    #     result = self.player.getWaveForm(('a',4))
    #     # desired = 
    #     np.testing.assert_allclose(result,desired)

if __name__ == '__main__':
    unittest.main()