from csv_generator import CsvGenerator
from excel_generator import ExcelGenerator
from json_generator import JsonGenerator
from txt_generator import TxtGenerator
from word_generator import WordGenerator

"""
File size argument should be in bytes
Column description and font size arguments are optional
"""

def generate_csv(file_size : int, column_description : dict = {"S.No" : "int", "Product_Name" : "str", "Product_Status": "boolean", "Delivery_Date": "datetime", "Rate": "float"}):
    csv_obj = CsvGenerator(file_size=file_size, column_description=column_description)
    csv_obj.main()

def generate_json(file_size : int, column_description : dict = {"S.No" : "int", "Product_Name" : "str", "Product_Status": "boolean", "Delivery_Date": "datetime", "Rate": "float"}):
    json_obj = JsonGenerator(file_size=file_size, column_description=column_description)
    json_obj.main()

def generate_excel(file_size : int, column_description : dict = {"S.No" : "int", "Product_Name" : "str", "Product_Status": "boolean", "Delivery_Date": "datetime", "Rate": "float"}):
    excel_obj = ExcelGenerator(file_size=file_size, column_description=column_description)
    excel_obj.main()

def generate_txt(file_size : int):
    txt_obj = TxtGenerator(file_size=file_size)
    txt_obj.main()

def generate_word(file_size : int, font_size : int = 12):
    word_obj = WordGenerator(file_size=file_size, font_size=font_size)
    word_obj.main()