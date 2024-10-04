from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path: str) -> List[str]:
    '''
       This function will return a list of requirements.txt         
    '''

    # Hyphen_E_Dot = '-e .'

    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('/n', "")for req in requirements]

        # if Hyphen_E_Dot in requirements:
        #     requirements.remove(Hyphen_E_Dot)

    return requirements




setup(

    name = 'MLProject',
    version= '0.0.1',
    author= 'Abhishek Sharma',
    author_email= 'abhissharma2281@gmail.com',
    packages= find_packages(),
    install_requires= get_requirements('requirements.txt') 

    
)