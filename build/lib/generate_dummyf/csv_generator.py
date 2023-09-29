from .validator import Validation
from .helper_functions import *
from datetime import datetime
import csv

class CsvGenerator:
    def __init__(self, **kwargs):
        self.arguments = kwargs
        self.new_file_path = ""
        self.data_type_value = {"str": generate_random_string(), "int": generate_random_int(), "datetime": datetime.now(), "float": generate_random_float(), "boolean": generate_random_boolean()}
        self.column_headers = []
        self.row = []

    def prepare_column_data(self):
        for k,v in self.arguments["column_description"].items():
            self.column_headers.append(k)
            self.row.append(self.data_type_value[v])

    def generate_file(self):
        with open(self.new_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            current_file_size = 0
            csv_writer.writerow(self.column_headers)
            while(current_file_size<=self.arguments["file_size"]): 
                csv_writer.writerow(self.row)
                current_file_size = csv_file.tell() 
    
    def main(self):
        obj = Validation(**self.arguments)
        obj.validate_args()
        if self.arguments["save_file_path"]:
            obj.validate_file_path()
            self.new_file_path = get_path_to_create_new_file("csv", user_input_path = self.arguments["save_file_path"])
        else:
            self.new_file_path = get_path_to_create_new_file("csv")
        obj.validate_file_size_limit()
        obj.validate_column_description()
        self.prepare_column_data()
        print(f"Generating the file at {self.new_file_path}")
        self.generate_file()
        print(f"Generated the file at {self.new_file_path}")
