from .validator import Validation
from .helper_functions import *
import json

class JsonGenerator:
    def __init__(self, **kwargs):
        self.arguments = kwargs
        self.new_file_path = get_path_to_create_new_file("json")
        self.data_type_value = {"str": "generate_random_string", "int": "generate_random_int", "datetime": "generate_current_datetime", "float": "generate_random_float", "boolean": "generate_random_boolean"}

    def prepare_row(self):
        return {k : globals()[self.data_type_value[v]]() for k,v in self.arguments["column_description"].items()}

    def generate_file(self):
        data = []
        current_file_size = 0
        while(current_file_size<=self.arguments["file_size"]):
            with open(self.new_file_path, 'w') as json_file:  
                data.append(self.prepare_row())
                json.dump(data, json_file, default=str, indent=4)
                current_file_size = json_file.tell() 

    def main(self):
        obj = Validation(**self.arguments)
        obj.validate_args()
        if self.arguments["save_file_path"]:
            obj.validate_file_path()
            self.new_file_path = get_path_to_create_new_file("json", user_input_path = self.arguments["save_file_path"])
        else:
            self.new_file_path = get_path_to_create_new_file("json")
        obj.validate_file_size_limit()
        obj.validate_column_description()
        print(f"Generating the file at {self.new_file_path}")
        self.generate_file()
        print(f"Generated the file at {self.new_file_path}")