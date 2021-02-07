#################################
# File: test_volume.py
# Author: Benjiman Walsh
# Date: February 7, 2021
# Description: Test for volume.py  
#  for CS 362 HW4 Question 1
#################################
import unittest
import volume

class TestCase(unittest.TestCase):
    
    def test_volume1(self):
        self.assertEqual(volume.cube_volume(4), 64 )
    
    def test_volume2(self):
        with self.assertRaises(ValueError):
            volume.cube_volume(-4)

    def test_wolume3(self):
        with self.assertRaises(TypeError):
            volume.cube_volume("Hello World")


if __name__ == '__main__':
    unittest.main(verbosity=2)
