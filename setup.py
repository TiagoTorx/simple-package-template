from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="string-tools-practice",
    version="0.0.1",
    author="TiagoTorx",
    author_email="tiagotorquetoserge@gmail.com",
    description="Simple package for manipulating and analyzing strings",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TiagoTorx/simple-package-template",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)