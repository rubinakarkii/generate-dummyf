from .csv_generator import CsvGenerator
from .excel_generator import ExcelGenerator
from .json_generator import JsonGenerator
from .txt_generator import TxtGenerator
from .word_generator import WordGenerator

"""
File size argument should be in bytes
Column description, save file path and font size arguments are optional
"""

def generate_csv(file_size : int, column_description : dict = {"S.No" : "int", "Product_Name" : "str", "Product_Status": "boolean", "Delivery_Date": "datetime", "Rate": "float"}, save_file_path : str = ""):
    csv_obj = CsvGenerator(file_size=file_size, column_description=column_description, save_file_path = save_file_path)
    csv_obj.main()

def generate_json(file_size : int, column_description : dict = {"S.No" : "int", "Product_Name" : "str", "Product_Status": "boolean", "Delivery_Date": "datetime", "Rate": "float"}, save_file_path : str = ""):
    json_obj = JsonGenerator(file_size=file_size, column_description=column_description, save_file_path = save_file_path)
    json_obj.main()

def generate_excel(file_size : int, column_description : dict = {"S.No" : "int", "Product_Name" : "str", "Product_Status": "boolean", "Delivery_Date": "datetime", "Rate": "float"}, save_file_path : str = ""):
    excel_obj = ExcelGenerator(file_size=file_size, column_description=column_description, save_file_path = save_file_path)
    excel_obj.main()

def generate_txt(file_size : int, save_file_path : str = ""):
    txt_obj = TxtGenerator(file_size=file_size, save_file_path = save_file_path)
    txt_obj.main()

def generate_word(file_size : int, font_size : int = 12, save_file_path : str = ""):
    word_obj = WordGenerator(file_size=file_size, font_size=font_size, save_file_path = save_file_path)
    word_obj.main()
