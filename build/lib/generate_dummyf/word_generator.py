from .validator import Validation
from .helper_functions import *
from docx import Document
from docx.shared import Pt
import os

class WordGenerator:
    def __init__(self, **kwargs):
        self.arguments = kwargs
        self.new_file_path = get_path_to_create_new_file("docx")

    def generate_file(self):
        doc = Document()
        current_file_size = 0
        while(current_file_size<=self.arguments["file_size"]): 
            word_line = generate_random_string()
            paragraph = doc.add_paragraph(word_line)
            font = paragraph.runs[0].font
            font.size = Pt(self.arguments["font_size"])
            doc.save(self.new_file_path)
            current_file_size = os.path.getsize(self.new_file_path)
    
    def main(self):
        obj = Validation(**self.arguments)
        obj.validate_args()
        if self.arguments["save_file_path"]:
            obj.validate_file_path()
            self.new_file_path = get_path_to_create_new_file("docx", user_input_path = self.arguments["save_file_path"])
        else:
            self.new_file_path = get_path_to_create_new_file("docx")
        obj.validate_file_size_limit()
        obj.validate_font_attributes()
        print(f"Generating the file at {self.new_file_path}")
        self.generate_file()
        print(f"Generated the file at {self.new_file_path}")
