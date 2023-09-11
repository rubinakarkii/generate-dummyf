import random 
from datetime import datetime
import csv
import os
import json
import openpyxl
from docx import Document
from docx.shared import Pt

class Validation:
    def __init__(self,**kwargs):
        self.arguments = kwargs
        self.data_type_dict = {"file_size": int, "column_description" : dict, "font_size" : int}
        self.allowed_data_types = ["int","str","boolean","datetime","float"]

    def validate_args(self):
        for key, value in self.arguments.items():
            if not self.data_type_dict[key] == type(value):
                raise Exception(f"Error: The value of '{key}' argument should be of {self.data_type_dict[key]} data type")

    def validate_file_size_limit(self):
        if not 0 <= self.arguments["file_size"] <= 5000000000: 
            raise Exception(f"Error: The value of 'file_size' argument should be between 0 and 5GB")

    def validate_column_description(self):
        for key,value in self.arguments["column_description"].items():
            if type(key) == str and type(value) == str:
                if value in self.allowed_data_types:
                    pass
                else:
                    raise Exception(f"Error: The values of 'column_description' dictionary should belong to the set of allowed data types i.e {self.allowed_data_types}")
            else:
                raise Exception(f"Error: The keys and values of 'column_description' dictionary should have key and value of string type")
            
    def validate_font_attributes(self):
        if not 1 <= self.arguments["font_size"] <= 1683:
            raise Exception(f"Error: The value of 'font_size' argument should be between 1 and 1683")

def get_path_to_create_new_file(file_type):
    downloads_folder = f'{os.path.expanduser("~")}/Downloads/Dummy.{file_type}'
    return downloads_folder

def zero_byte_file(file_type):
    with open(f'{get_path_to_create_new_file(file_type)}',"w"):
        return None

def generate_random_string():
    string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return ''.join(random.sample(string,len(string)))

def generate_random_int():
    return random.getrandbits(32)

def generate_random_float():
    return random.random()

def generate_random_boolean():
    return random.choice([True, False])

def prepare_csv(file_type,file_size,column_description): 
    data_type_value = {"str": generate_random_string(), "int": generate_random_int(), "datetime": datetime.now(), "float": generate_random_float(), "boolean": generate_random_boolean()}
    column_headers = []
    row = []
    for k,v in column_description.items():
        column_headers.append(k)
        row.append(data_type_value[v])

    new_file_path = get_path_to_create_new_file(file_type)
    with open(new_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        current_file_size = 0
        csv_writer.writerow(column_headers)
        while(current_file_size<=file_size): 
            csv_writer.writerow(row)
            current_file_size = csv_file.tell() 
    
def prepare_json(file_type, file_size, column_description):
    data_type_value = {"str": generate_random_string(), "int": generate_random_int(), "datetime": datetime.now(), "float": generate_random_float(), "boolean": generate_random_boolean()}
    row = {k : data_type_value[v] for k,v in column_description.items()}
    new_file_path = get_path_to_create_new_file(file_type)
    data = []
    current_file_size = 0
    while(current_file_size<=file_size):
        with open(new_file_path, 'w') as json_file:            
            data.append(row)
            json.dump(data, json_file, default=str, indent=4)
            current_file_size = json_file.tell() 

def prepare_excel(file_type,file_size, column_description):
    data_type_value = {"str": generate_random_string(), "int": generate_random_int(), "datetime": datetime.now(), "float": generate_random_float(), "boolean": generate_random_boolean()}
    column_headers = []
    row = []
    for k,v in column_description.items():
        column_headers.append(k)
        row.append(data_type_value[v])

    new_file_path = get_path_to_create_new_file(file_type)
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    current_file_size = 0
    worksheet.append(column_headers)
    while(current_file_size<=file_size): 
        workbook.save(new_file_path)
        current_file_size = os.path.getsize(new_file_path)
        worksheet.append(row)
    workbook.close()

def prepare_txt(file_type,file_size):
    new_file_path = get_path_to_create_new_file(file_type)
    with open(new_file_path, 'a') as txt_file:
        current_file_size = 0
        while(current_file_size<=file_size): 
            txt = generate_random_string()
            txt_file.write(txt+ '\n')
            current_file_size = txt_file.tell() 

def prepare_docx(file_type,file_size,font_size):
    new_file_path = get_path_to_create_new_file(file_type)
    doc = Document()
    current_file_size = 0
    while(current_file_size<=file_size): 
        word_line = generate_random_string()
        paragraph = doc.add_paragraph(word_line)
        font = paragraph.runs[0].font
        font.size = font_size
        doc.save(new_file_path)
        current_file_size = os.path.getsize(new_file_path)

def main(file_type, **kwargs):
    try:
        obj = Validation(**kwargs)
        obj.validate_args()
        obj.validate_file_size_limit()
        if file_type in ["csv","json","xlsx"]: obj.validate_column_description()
        if file_type == "docx": obj.validate_font_attributes()

        print(f"Generating dummy {file_type} file of size {kwargs['file_size']} bytes")
        if kwargs["file_size"]==0: zero_byte_file(file_type)
        else:
            if file_type=="csv": prepare_csv(file_type, kwargs["file_size"], kwargs["column_description"])
            if file_type=="json": prepare_json(file_type,kwargs["file_size"], kwargs["column_description"])
            if file_type=="xlsx": prepare_excel(file_type,kwargs["file_size"], kwargs["column_description"])
            if file_type=="txt": prepare_txt(file_type,kwargs["file_size"])
            if file_type=="docx": prepare_docx(file_type,kwargs["file_size"], kwargs["font_size"])
        print(f"Generated dummy {file_type} file in your downloads folder")
    except Exception as e:
        print(e)