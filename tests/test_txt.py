import unittest
import os
from generate_dummyf.exceptions import *
from generate_dummyf.generate import generate_txt

class TxtTestCase(unittest.TestCase):
    def test_invalid_file_size_data_type(self):
        """Case 1: function is provided an input with incorrect data type for file_size (str instead of int)"""
        self.assertRaises(InvalidInputDataTypeException, generate_txt(file_size="1000"))

    def test_invalid_file_path(self):
        """Case 2: function is given invalid path for saving file"""
        self.assertRaises(InvalidPathException, generate_txt(file_size=1000, save_file_path="bhsdajhbfsdj"))

    def test_invalid_file_size_value(self):
        """Case 3:  function is provided an invalid file size"""
        self.assertRaises(InvalidSizeException, generate_txt(file_size=-1000))

    def test_file_generation(self):
        """Case 4: if file is generated or not """
        expected_file_path = os.path.expanduser("~")
        generate_txt(file_size=1000, save_file_path=expected_file_path)

        # Assert that the file exists --> if AssertionError is not raised, then the test is successful
        self.assertEqual(os.path.exists(f"{expected_file_path}/Dummy.txt"), True, f"File {expected_file_path}/Dummy.txt was not generated")

if __name__ == '__main__':
    unittest.main()


'''
NOTE: Here, if the exception as defined in assertRaises is raised for each test case,
then test is passed (even if the output shows FAILED(errors=2))
'''