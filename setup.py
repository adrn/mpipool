# coding: utf-8

from __future__ import division, print_function

import sys
try:
    from setuptools import setup
    setup
except ImportError:
    from distutils.core import setup
    setup

if sys.version_info[0] < 3:
    import __builtin__ as builtins
else:
    import builtins
builtins.__MPIPOOL_SETUP__ = True
import mpipool

setup(
    name="mpipool",
    version=mpipool.__version__,
    author="Adrian Price-Whelan",
    author_email="adrn@astro.columbia.edu",
    packages=["mpipool"],
    url="https://github.com/adrn/mpipool/",
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
