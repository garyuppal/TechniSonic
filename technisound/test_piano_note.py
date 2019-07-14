import unittest
from piano_note import PianoNote


# tests checking notes are played at right frequencies
class TestNotePlayer(unittest.TestCase):
    def setUp(self):
        self.note = PianoNote()

    def tearDown(self):
        pass
    
    def test_noteToKeyA(self):
        self.assertEqual(self.note.noteToKey(('a',4,)),49)
        self.assertEqual(self.note.noteToKey(('A',4)),49)
        self.assertEqual(self.note.noteToKey(('A',3)),37)
        self.assertEqual(self.note.noteToKey(('A',5)),61)
        self.assertEqual(self.note.noteToKey(('a',-1)),-11)
        # self.assertEqual(self.note.noteToKey(('a',9)),109)

    def test_noteToKeyB(self):
        self.assertEqual(self.note.noteToKey(('b',4)),51)
        self.assertEqual(self.note.noteToKey(('B',-1)),-9)
        self.assertEqual(self.note.noteToKey(('b',3)),39)
        self.assertEqual(self.note.noteToKey(('B',9)),111)

    def test_noteToKeyC(self):
        self.assertEqual(self.note.noteToKey(('c',4)),52)
        self.assertEqual(self.note.noteToKey(('C',-1)),-8)
        self.assertEqual(self.note.noteToKey(('C',0)),4)
        self.assertEqual(self.note.noteToKey(('c',3)),40)
        self.assertEqual(self.note.noteToKey(('C',9)),112)

    def test_noteToKeyF(self):
        self.assertEqual(self.note.noteToKey(('f',4)),57)
        self.assertEqual(self.note.noteToKey(('F',-1)),-3)
        self.assertEqual(self.note.noteToKey(('f',3)),45)
        self.assertEqual(self.note.noteToKey(('F',9)),117)

    def test_noteToKey_Asharp(self):
        self.assertEqual(self.note.noteToKey(('a',4,'#')),50)
        
    def test_noteToKey_Csharp(self):
        self.assertEqual(self.note.noteToKey(('c',0,'#')),5)
 
    def test_noteToKey_Bflat(self):
        self.assertEqual(self.note.noteToKey(('B',4,'b')),50)
        
    def test_keyToFrequency(self):
        self.assertEqual(self.note.keyToFrequency(49),440)
        self.assertEqual(self.note.keyToFrequency(61),880)

    def test_noteToFrequency(self):
        self.assertEqual(self.note.noteToFrequency(('A',4)),440)
        self.assertEqual(self.note.noteToFrequency(('A',5)),880)
        self.assertEqual(self.note.noteToFrequency(('A',3)),220)

    def test_noteToFrequency_B(self):
        self.assertAlmostEqual(self.note.noteToFrequency(('b',8)), 7902.13, 2) # check to 2 decimal places

    def test_noteToFrequency_C(self):
        self.assertAlmostEqual(self.note.noteToFrequency(('c',-1)),16.35,2) # check to 2 decimal places 
        # NOTE: might not be correct notation -- may need to switch octaves between b and c


if __name__ == '__main__':
    unittest.main()
