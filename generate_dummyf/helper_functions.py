from datetime import datetime
import random 
import os

def get_path_to_create_new_file(file_type, user_input_path = ""):
    try:
        if user_input_path:
            if user_input_path.endswith('/'):
                path = f'{user_input_path}Dummy.{file_type}'
            else:
                path = f'{user_input_path}/Dummy.{file_type}'
        else:
            path = f'{os.path.expanduser("~")}/Downloads/Dummy.{file_type}'
    except Exception as e:
        return e
    return path

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

def generate_current_datetime():
    return datetime.now()