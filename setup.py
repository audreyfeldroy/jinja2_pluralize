#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'jinja2>=2.4',
    'inflect>=0.2.4',
]

setup(
    name='jinja2_pluralize',
    version='0.3.0',
    description="Jinja2 pluralize filters.",
    long_description=readme + '\n\n' + history,
    author='Audrey Roy Greenfeld',
    author_email='aroy@alum.mit.edu',
    url='https://github.com/audreyr/jinja2_pluralize',
    packages=[
        'jinja2_pluralize',
    ],
    package_dir={'jinja2_pluralize': 'jinja2_pluralize'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='Jinja2, filter, pluralize, Django, inflect',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
)