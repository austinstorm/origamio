#!/usr/bin/env python

from setuptools import setup

setup(
    name='Origam.io',
    version='0.1',
    description='One webpage for everything.',
    author='Austin Storm',
    author_email='austinstorm@gmil.com',
    url='http://origam.io/',
    install_requires=['Django<=1.4', 'python-social-auth<=0.1.24', 'djangorestframework<=2.3.13'],
)
