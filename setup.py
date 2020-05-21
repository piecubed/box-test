#!/usr/bin/python3

from setuptools import setup

with open('README.md', 'r') as f:
    desc = f.read()

setup(
    name        = 'boxtest',
    version     = '0.3stable',
    py_modules  = ['boxtest'],
    author      = 'piesquared',
    description = 'A lightweight basic testing framework.',
    url         = 'https://github.com/piecubed/box-test',
    license     = 'MIT',

    long_description              = desc,
    long_description_content_type = 'text/markdown',
    install_requires              = [],
    python_requires               = '>=3.5',

    classifiers = [
        'Intended Audience :: Developers',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries',
    ]
)