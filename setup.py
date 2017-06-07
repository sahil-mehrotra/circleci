from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
name='example',
version='1.0',
packages=['src','tests'],
url='https://thoughtworks.com',
license='',
author='onkarshedge',
author_email='oshedge@thoughtworks.com',
description='This is test package',
install_requires = required,
test_suite = 'tests'
)