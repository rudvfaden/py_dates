
from setuptools import setup, find_packages

setup(
    name='danish_holidays',
    version='0.1',
    packages=find_packages(),
    install_requires=['datetime'],
    author='Rud Faden',
    author_email='rudfaden@gmail.com',
    description='A package to calculate Danish banking holidays',
    url='https://github.com/rudvfaden/py_dates',
        classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Update license as needed
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
