from setuptools import find_packages, setup
from typing import List

REQUIREMENT_FILE_NAME = "requirements.txt"
# To execute the setup.py file we use '-e .', so that we can use our project as library from anywhere
HYPHEN_E_DOT = "-e ."


# Provides information to developer that this function returns list of string
def get_requirements() -> List[str]:

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        # reading each line from the file
        requirement_list = requirement_file.readlines()
    # Removing '\n' from the list of libraries
    requirement_list = [requirement_name.replace(
        "\n", "") for requirement_name in requirement_list]

    if HYPHEN_E_DOT in requirement_list:
        # Removing '-e .' as it is not required
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list


setup(
    name="thyroid",
    version="0.0.1",
    author="Aman Gupta",
    author_email="itsamangupta365@gmail.com",
    # find_packages() will convert the folder with __init__.py file to library/package
    packages=find_packages(),
    install_requires=get_requirements()
)   # Searches and stores the list of required libraries which are needed to be inststalled to run this project
