from setuptools import find_packages,setup
from typing import List

# Returns the list of requirements
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        # Replaces the \n in each index with a blank
        requirements=[req.replace("\n","") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")
        
        return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Revanth',
    author_email='revz.mahankali@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)