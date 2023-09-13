class InvalidColumnTypeException(Exception):
    def __init__(self, message : str):
        self.message = message
        super().__init__(self.message)

class InvalidInputDataTypeException(Exception):
    def __init__(self, message : str):
        self.message = message
        super().__init__(self.message)

class InvalidSizeException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
