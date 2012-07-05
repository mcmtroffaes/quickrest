#!/usr/bin/env python

from distutils.core import setup

with open("README.rst", "rb") as readme_file:
    doclines = readme_file.read().split("\n")

with open("VERSION", "rb") as version_file:
    version = version_file.read().strip()

setup(
    name='quickrest',
    version=version,
    url='https://github.com/mcmtroffaes/quickrest',
    download_url='http://pypi.python.org/pypi/quickrest',
    license='GPL',
    author='Matthias C. M. Troffaes',
    author_email='matthias.troffaes@gmail.com',
    description=doclines[0],
    long_description="\n".join(doclines[2:]),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Topic :: Text Processing :: Markup',
    ],
    platforms='any',
    packages=['quickrest'],
    )
