from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    requirements = []

    with open(file_path) as file:
        requirements = [line.strip() for line in file if line.strip()]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="Data Science Project",
    version="0.0.1",
    author="Aishwary",
    author_email="aishwarydoye333@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)