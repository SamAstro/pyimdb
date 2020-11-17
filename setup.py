# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pyimdb',
    version='0.1.0',
    description='Example package of IMDb Python API',
    long_description=readme,
    author='Samia Drappeau',
    author_email='samia.drappeau@atad-bayanat.eu',
    url='https://github.com/samastro/pyimdb',
    license=license,
    packages=find_packages(exclude=('tests', 'docs', 'data'))
)
