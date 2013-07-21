#!/usr/bin/env python

from setuptools import setup

setup(name="PyCitibike",
      version="0.0.1",
      description="A Python API wrapper for the Citibike API",
      author="John Bunting",
      author_email="codingjester@gmail.com",
      url="http://github.com/codingjester/pycitibike",
      license="MIT",
      packages=['pycitibike'],
      install_requires=["requests"]
)
