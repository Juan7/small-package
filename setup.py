from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='calculator',
      version='1.0.1',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      author='Phinxk',
      author_email='juan.gomez.q@gmail.com',
      url='https://github.com/Juan7/small-package',
      )
