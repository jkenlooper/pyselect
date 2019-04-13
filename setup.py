#!/usr/bin/env python

from setuptools import setup, find_packages
__title__     = 'pyselect'
__version__   = '0.2.0'
__author__    = 'Matthew Behrens'
__license__   = 'MIT'
__copyright__ = 'Copyright 2013 Matthew Behrens'

setup(
    name                 = 'pyselect',
    version              = __version__,
    description          = 'A Python library for easily getting user input form multiple items in a list, emulating the Bash(1) builtin select.',
    long_description     = open('README.rst').read() + '\n\n' + open('HISTORY.rst').read(),

    author               = __author__,
    author_email         = 'askedrelic@gmail.com',
    url                  = 'https://github.com/askedrelic/pyselect',
    license              = open("LICENSE.txt").read(),

    # packages           = ['pyselect'],
    py_modules           = ['pyselect'],
    include_package_data = True,
    # test_suite         = 'tests',

    classifiers          = (
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3.3',
        # 'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)
