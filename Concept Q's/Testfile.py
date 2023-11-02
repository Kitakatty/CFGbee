import unittest
from Q1 import is_isogram

class IsogramTestCase(unittest.TestCase):
    def test_is_isogram(self):
        # test cases with isograms
        self.assertTrue(is_isogram("isogram"), "Expected 'isogram' to be an isogram")
        self.assertTrue(is_isogram("uncopyrightable"), "Expected 'uncopyrightable' to be isogram")
        # test cases with non-isograms
        self.assertFalse(is_isogram("hello"), " Expected 'hello'' to not be an isogram")
        self.assertFalse(is_isogram("elephant"), "Expected 'elephant' to not be an isogram")

        # test an empty string 
        self.assertTrue(is_isogram(""), "Expected an empty string to be an isogram")

        # test a single characterr
        self.assertTrue(is_isogram("a"), "Expected 'a' to be an isogram")

       # Test a string with special characters
        self.assertFalse(is_isogram("hello!"), "Expected 'hello!' to not be an isogram")

if __name__ == '__main__':
    unittest.main()

