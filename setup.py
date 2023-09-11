from setuptools import setup, find_packages

VERSION = '0.1.0' 
DESCRIPTION = 'Generate different types(json, csv, excel, word, pdf) of dummy files'

# Setting up
setup(
        name="generate-dummyf",
        version=VERSION,
        author="Rubina Karki",
        author_email="rubinakarki369@gmail.com",
        description=DESCRIPTION,
        long_description=open('README.md').read(),
        packages=find_packages(),
        url='https://github.com/rubinakarkii/generate-dummyf',
        license='LICENSE.txt',
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
)