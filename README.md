# generate-dummyf Python Package #

## Overview ##
   The generate-dummyf Python package is a versatile tool for generating dummy files in different formats such as JSON, Excel, DOCX, TXT, and CSV. This package 
   simplifies the process of creating sample data files for testing, development, and other purposes.

## Features ##
   Generate dummy data files in JSON, Excel, DOCX, TXT, and CSV formats. Customize the structure of the generated files. Easily specify the file size and  data 
   types. Generate a file with random data for a wide range of use cases.

## Installation ##
   You can install the package using pip:

   ```
   pip install generate-dummyf
   ```

## Usage ##
   Here's a quick guide on how to use the **generate-dummyf** package to generate dummy files: 

1. ### Import the package ###
   ```
   from generate_dummyf import DummyFileGenerator
   ```

2. ### Create a generator instance ###
   ```
   generator = DummyFileGenerator()
   ```

3. ### Generate a JSON file ###
   ```
   json_data = generator.generate_json(file_size=50000)
   json_data = generator.generate_json(file_size=50000, column_description={"Contact" : "int", "Name" : "str", "Status": "boolean", "Created_Time": "datetime", "Amount": "float"})
   ```

4. ### Generate an Excel file ###
   ```
   excel_data = generator.generate_excel(file_size=50000)
   excel_data = generator.generate_excel(file_size=50000, column_description={"Contact" : "int", "Name" : "str", "Status": "boolean", "Created_Time": "datetime", "Amount": "float"})
   ```

5. ### Generate a CSV file 
   ```
   csv_data = generator.generate_csv(file_size=5000)
   csv_data = generator.generate_csv(file_size=5000, column_description={"Contact" : "int", "Name" : "str", "Status": "boolean", "Created_Time": "datetime", "Amount": "float"})
   ```

6. ### Generate a DOCX file ###
   ```
   docx_data = generator.generate_word(file_size=50000)
   ```

7. ### Generate a TXT file ###
   ```
   docx_data = generator.generate_txt(file_size=5000)
   ```

8. ### View the generated files ###
   The generated files will be saved in the downloads directory.

## Contributing ##
   Contributions to generate-dummyf are welcome! If you'd like to contribute to this project, please follow our contribution guidelines.

## License ##
   This project is licensed under the MIT License - see the LICENSE file for details.

## Support and Contact ##
   If you have any questions, issues, or feature requests, please feel free to open an issue.