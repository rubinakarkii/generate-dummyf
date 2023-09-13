import unittest
from generate_dummyf.exceptions import *
from generate_dummyf.generate import generate_txt

class TxtTestCase(unittest.TestCase):
    def test_invalid_file_size_data_type(self):
        """Case 1: function is provided an input with incorrect data type for file_size (str instead of int)"""
        self.assertRaises(InvalidInputDataTypeException, generate_txt("1000"))

    def test_invalid_file_size_value(self):
        """Case 2:  function is provided an invalid file size"""
        self.assertRaises(InvalidSizeException, generate_txt(-1000))


if __name__ == '__main__':
    unittest.main()


'''
NOTE: Here, if the exception as defined in assertRaises is raised for each test case,
then test is passed (even if the output shows FAILED(errors=2))
'''