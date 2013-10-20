#!/usr/bin/env python

import os
from setuptools import setup
from buster import _version


# get the requirements from the pip requirements file
requirements = []

with open("requirements.txt") as f:
    for l in f:
        l = l.strip()
        if l: requirements.append(l)

setup(name="buster",
            version=_version.__version__,
            description="Static site generator for Ghost and Github",
            long_description=open("README.md").read(),
            author="Akshit Khurana",
            author_email="axitkhurana@gmail.com",
            url="https://github.com/axitkhurana/buster",
            license="MIT",
            packages=["buster"],
            entry_points = { "console_scripts" : [ "buster = buster.buster:main"]},
            install_requires=requirements
           )

