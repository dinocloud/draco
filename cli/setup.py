#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import glob
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

version_file_path = os.path.dirname(os.path.realpath(__file__)) + '/../version.info'
with open(version_file_path, 'r') as fin:
    version = fin.read()
datadir = os.path.join('./', 'tasks')
datafiles = [(d, [os.path.join(d, f) for f in files])
             for d, folders, files in os.walk(datadir)]

config = {
    'author': 'Franco Ariel Salonia',
    'author_email': 'franco.salonia@dinocloudconsulting.com',
    'description': 'dracoctl',
    'download_url': 'https://github.intel.com/dinocloud/draco',
    'entry_points': {
        'console_scripts': [
            'dracoctl = draco:main'
        ]
    },
    'install_requires': [
        'argparse'
    ],
    'data_files': datafiles,
    'name': 'dracoctl',
    'include_package_data': True,
    'packages': find_packages(exclude="test"),
    'package_data': {'': ['*.sh']},
    'scripts': [],
    'url': 'https://github.intel.com/dinocloud/draco',
    'version': version
}

setup(**config)
