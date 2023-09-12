from validator import Validation
from helper_functions import *
from datetime import datetime

class TxtGenerator:
    def __init__(self, **kwargs):
        self.arguments = kwargs
        self.new_file_path = get_path_to_create_new_file("txt")

    def generate_file(self):
        with open(self.new_file_path, 'a') as txt_file:
            current_file_size = 0
            while(current_file_size<=self.arguments["file_size"]): 
                txt = generate_random_string()
                txt_file.write(txt+ '\n')
                current_file_size = txt_file.tell() 

    def main(self):
        obj = Validation(**self.arguments)
        obj.validate_args()
        obj.validate_file_size_limit()
        self.generate_file()