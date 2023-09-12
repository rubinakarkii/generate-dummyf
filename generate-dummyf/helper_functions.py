import random 
import os

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