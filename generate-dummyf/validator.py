class Validation:
    def __init__(self,**kwargs):
        self.arguments = kwargs
        self.column_type_mapping = {"file_size": int, "column_description" : dict, "font_size" : int}
        self.allowed_data_types = ["int","str","boolean","datetime","float"]

    def validate_args(self):
        for key, value in self.arguments.items():
            if not self.column_type_mapping[key] == type(value):
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