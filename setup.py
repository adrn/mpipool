# coding: utf-8

from __future__ import division, print_function

# Standard library
try:
    from setuptools import setup
    setup
except ImportError:
    from distutils.core import setup
    setup


setup(
    name="mpipool",
    version="0.0.1",
    author="Daniel Foreman-Mackey",
    author_email="danfm@nyu.edu",
    packages=["mpipool"],
    url="https://github.com/dfm/mpipool/",
    license="MIT",
    description="MPI pool",
    package_data={"": ["LICENSE", "AUTHORS"]},
    include_package_data=True,
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
)
