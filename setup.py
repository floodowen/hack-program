#!/usr/bin/env python

"""
Install dice package. To install locally use:
'pip install -e .'
"""

from setuptools import setup

setup(
    name="dice",
    version="0.0.1",
    author="Owen Flood",
    author_email="owen.flood@columbia.edu",
    description="A package for rolling dice",
    packages=[],
    classifiers=["Programming Language :: Python :: 3"],
    entry_points={
        "console_scripts": ["roll = dice.__main__:main"],
    },
)
