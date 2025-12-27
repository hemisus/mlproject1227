from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()  #\n을 읽어버림
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:    
            requirements.remove(HYPEN_E_DOT)   #-e . 은 requirements가 실행될때 setup.py를 실행시키기 위한 용도로, requirements에 들어갈 필요는 없음
    
    return requirements

        

setup(
name='mlproject1227',
version='0.0.1',
author='Hemisus',
author_email='hydro6323@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)