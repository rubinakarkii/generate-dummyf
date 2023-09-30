from setuptools import setup

VERSION = '1.1.4' 
DESCRIPTION = 'Generate different types (json, csv, excel, word, txt) of dummy files'

# Setting up
setup(
        name="generate-dummyf",
        version=VERSION,
        author="Rubina Karki",
        author_email="rubinakarki369@gmail.com",
        description=DESCRIPTION,
        long_description=open('README.md').read(),
        long_description_content_type="text/markdown",
        packages=["generate_dummyf"],
        url='https://github.com/rubinakarkii/generate-dummyf',
        license="LICENSE",
        install_requires=['openpyxl','python-docx'], 
)