from helper_functions import main

"""
File size argument should be in bytes
Column description and font size arguments are optional
"""

def generate_csv(file_size : int, column_description : dict = {"S.No" : "int", "Product_Name" : "str", "Product_Status": "boolean", "Delivery_Date": "datetime", "Rate": "float"}):
    main("csv", file_size=file_size, column_description=column_description)

def generate_json(file_size : int, column_description : dict = {"S.No" : "int", "Product_Name" : "str", "Product_Status": "boolean", "Delivery_Date": "datetime", "Rate": "float"}):
    main("json", file_size=file_size, column_description=column_description)

def generate_excel(file_size : int, column_description : dict = {"S.No" : "int", "Product_Name" : "str", "Product_Status": "boolean", "Delivery_Date": "datetime", "Rate": "float"}):
    main("xlsx", file_size=file_size, column_description=column_description)

def generate_txt(file_size : int):
    main("txt", file_size=file_size)

def generate_word(file_size : int, font_size : int = 12):
    main("docx", file_size=file_size, font_size=font_size)
