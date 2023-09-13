from setuptools import setup

VERSION = '0.1.0' 
DESCRIPTION = 'Generate different types (json, csv, excel, word, txt) of dummy files'

# Setting up
setup(
        name="generate-dummyf",
        version=VERSION,
        author="Rubina Karki",
        author_email="rubinakarki369@gmail.com",
        description=DESCRIPTION,
        long_description=open('README.md').read(),
        packages=["generate_dummyf"],
        url='https://github.com/rubinakarkii/generate-dummyf',
        license='LICENSE.txt',
        install_requires=['openpyxl','python-docx'], 
)