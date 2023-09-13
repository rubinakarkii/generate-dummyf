import unittest
from generate_dummyf.exceptions import *
from generate_dummyf.generate import generate_csv

class CsvTestCase(unittest.TestCase):
    def test_invalid_file_size_data_type(self):
        """Case 1: function is provided an input with incorrect data type for file_size (str instead of int)"""
        self.assertRaises(InvalidInputDataTypeException, generate_csv("1000"))

    def test_invalid_column_description_value_data_type(self):
        """Case 2: function is provided an input with incorrect data type for column_description's values() (int as object instead of int as str)"""
        self.assertRaises(InvalidInputDataTypeException, generate_csv(3824, {"Roll No.": int}))

    def test_invalid_file_size_value(self):
        """Case 3:  function is provided an invalid file size"""
        self.assertRaises(InvalidSizeException, generate_csv(-1000))

    def test_invalid_column_description_value(self):
        """Case 4: function is given column_description's values() that do not belong to the allowed data types list"""
        self.assertRaises(InvalidColumnDescriptionValueException, generate_csv(1000, {"file": "object"}))


if __name__ == '__main__':
    unittest.main()


'''
NOTE: Here, if the exception as defined in assertRaises is raised for each test case,
then test is passed (even if the output shows FAILED(errors=4))
'''