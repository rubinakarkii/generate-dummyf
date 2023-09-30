from .validator import Validation
from .helper_functions import *
import os
import openpyxl

class ExcelGenerator:
    def __init__(self, **kwargs):
        self.arguments = kwargs
        self.new_file_path = ""
        self.data_type_value = {"str": "generate_random_string", "int": "generate_random_int", "datetime": "generate_current_datetime", "float": "generate_random_float", "boolean": "generate_random_boolean"}
        self.column_headers = []
        self.column_data_type = []

    def prepare_column(self):
        for k,v in self.arguments["column_description"].items():
            self.column_headers.append(k)
            self.column_data_type.append(v)

    def prepare_row(self):
        return [globals()[self.data_type_value[i]]() for i in self.column_data_type]
    
    def generate_file(self):
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        current_file_size = 0
        worksheet.append(self.column_headers)
        while(current_file_size<=self.arguments["file_size"]): 
            workbook.save(self.new_file_path)
            current_file_size = os.path.getsize(self.new_file_path)
            worksheet.append(self.prepare_row())
        workbook.close()
    
    def main(self):
        obj = Validation(**self.arguments)
        obj.validate_args()
        if self.arguments["save_file_path"]:
            obj.validate_file_path()
            self.new_file_path = get_path_to_create_new_file("xlsx", user_input_path = self.arguments["save_file_path"])
        else:
            self.new_file_path = get_path_to_create_new_file("xlsx")
        obj.validate_file_size_limit()
        obj.validate_column_description()
        self.prepare_column()
        print(f"Generating the file at {self.new_file_path}")
        self.generate_file()
        print(f"Generated the file at {self.new_file_path}")
