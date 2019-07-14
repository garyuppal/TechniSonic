import sys
sys.path.append('../')
import unittest
import technisound.file_parser as fp

# tests for parsing ``music code'' files
class TestFileParser(unittest.TestCase):
    def test_add(self):
        self.assertEqual(fp.add(3,5),8)

if __name__ == '__main__':
    unittest.main()