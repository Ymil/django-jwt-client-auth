#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# get version from __init__.py
from setuptools import find_packages
# from jwt_client_auth import __version__ as version

setup(
    name='django-jwt-client-auth',
    version="0.1.0",
    description='',
    long_description=open('README.md').read(),
    include_package_data=True,
    url='',
    packages=find_packages(),
    install_requires=[
        'django',
        'requests'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ]
)
