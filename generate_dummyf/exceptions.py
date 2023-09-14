class InvalidColumnDescriptionValueException(Exception):
    """Exception raised when an invalid value is encountered in a column description."""
    def __init__(self, message : str):
        self.message = message
        super().__init__(self.message)

class InvalidInputDataTypeException(Exception):
    """Exception raised when the input's data type is invalid."""
    def __init__(self, message : str):
        self.message = message
        super().__init__(self.message)

class InvalidSizeException(Exception):
    """Exception raised when an invalid size is encountered."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class InvalidPathException(Exception):
    """Exception raised when an invalid save file path is provided."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)