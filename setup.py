# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pyimdb',
    version='0.1.0',
    description='Example package of IMDb Python API',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Samia Drappeau',
    author_email='samia.drappeau@atad-bayanat.eu',
    url='https://github.com/samastro/pyimdb',
    license=license,
    packages=find_packages(exclude=('tests', 'docs', 'data')),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
