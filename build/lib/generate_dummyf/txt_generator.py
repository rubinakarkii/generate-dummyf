from .validator import Validation
from .helper_functions import *

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
        if self.arguments["save_file_path"]:
            obj.validate_file_path()
            self.new_file_path = get_path_to_create_new_file("txt", user_input_path = self.arguments["save_file_path"])
        else:
            self.new_file_path = get_path_to_create_new_file("txt")
        obj.validate_file_size_limit()
        print(f"Generating the file at {self.new_file_path}")
        self.generate_file()
        print(f"Generated the file at {self.new_file_path}")
