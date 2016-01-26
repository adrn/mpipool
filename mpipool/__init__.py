# -*- coding: utf-8 -*-

__version__ = "0.0.2.dev0"

try:
    __MPIPOOL_SETUP__
except NameError:
    __MPIPOOL_SETUP__ = False

if not __MPIPOOL_SETUP__:
    __all__ = ["MPIPool", "MPIPoolException"]
    from .core import MPIPool, MPIPoolException
