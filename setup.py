from setuptools import setup, find_packages
import os

# Read the content of README.md for the long description, if available
this_directory = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(this_directory, 'README.md'),
              encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ''

setup(
    name='danish_holidays',
    version='0.1',
    packages=find_packages(),
    install_requires=[],  # Removed datetime as it's a built-in module.
    author='Rud Faden',
    author_email='rudfaden@gmail.com',
    description='A package to calculate Danish banking holidays',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/rudvfaden/py_dates',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Update license as needed
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
