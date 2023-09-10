# test_data_manipulation.py
import unittest
from data_manipulation import calculate_average

class TestDataManipulation(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertEqual(calculate_average([]), 0)
    
    def test_non_empty_list(self):
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3.0)
    
    def test_mixed_values(self):
        self.assertEqual(calculate_average([1, -2, 3, -4, 5]), 0.6)

if __name__ == '__main__':
    unittest.main()
