#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-vw',
    version='0.1.0',
    author='Florian Bruhin',
    author_email='me@the-compiler.org',
    maintainer='Florian Bruhin',
    maintainer_email='me@the-compiler.org',
    license='MIT',
    url='https://github.com/The-Compiler/pytest-vw',
    description='pytest-vw makes your failing test cases succeed under CI tools scrutiny',
    long_description=read('README.rst'),
    py_modules=['pytest_vw'],
    install_requires=['pytest>=2.8.2'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'vw = pytest_vw',
        ],
    },
)
