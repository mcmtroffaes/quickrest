#!/usr/bin/env python

from distutils.core import setup
from quickrest import __version__

setup(
    name='quickrest',
    version=__version__,
    description='Quick restructured text creator.',
    author='Matthias C. M. Troffaes',
    author_email='matthias.troffaes@gmail.com',
    packages=['quickrest'],
    )
