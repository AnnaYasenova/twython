#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__author__ = 'Ryan McGrath <ryan@venodesigns.net>'
__version__ = '3.7.0'

packages = [
    'twython',
    'twython.streaming'
]

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='twython',
    version=__version__,
    install_requires=['requests>=2.1.0', 'requests_oauthlib>=0.4.0'],
    author='Ryan McGrath',
    author_email='ryan@venodesigns.net',
    license=open('LICENSE').read(),
    url='https://github.com/ryanmcgrath/twython/tree/master',
    keywords='twitter search api tweet twython stream',
    description='Actively maintained, pure Python wrapper for the \
    Twitter API. Supports both normal and streaming Twitter APIs',
    long_description=open('README.rst').read() + '\n\n' +
        open('HISTORY.rst').read(),
    include_package_data=True,
    packages=packages,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Chat',
        'Topic :: Internet',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
