#!/usr/bin/env python
from setuptools import find_packages, setup

version = '0.0.1'

setup(
    name='experimental',
    version=version,
    packages=find_packages(exclude=['tests']),
    description='Infra portal for Uber',
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'experimental = experimental.main'
        ],
    },
)