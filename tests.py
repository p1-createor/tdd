import unittest
from mathfunctions import MathFunctions

class SimpleTestMax(unittest.TestCase):
    def test(self):
        self.assertEqual(MathFunctions.maxint(12,1),12)
        
if __name__=='__main__':
    unittest.main()
