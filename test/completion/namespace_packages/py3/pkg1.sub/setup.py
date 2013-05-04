#!/usr/bin/env python
from distutils.core import setup
import os
import os.path as op


# Necessary because paths are modified by jedi tests. Will not affect tests
# since the setup is only run in a subprocess.
here = op.abspath(op.dirname(__file__))
os.chdir(here)


setup(name='pkg1.sub',
    packages=['pkg1.sub'],
)

