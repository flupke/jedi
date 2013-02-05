#!/usr/bin/env python
from setuptools import setup
import os
import os.path as op


# Necessary because paths are modified by jedi tests. Will not affect tests
# since the setup is only run in a subprocess.
here = op.abspath(op.dirname(__file__))
os.chdir(here)


setup(name='pkg1.sub',
    namespace_packages=['pkg1'],
    packages=['pkg1', 'pkg1.sub'],
)

