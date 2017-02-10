#
# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.
#

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='codepoints',
    version='1.0',
    description='Converts code point sequences to and from Unicode strings',
    long_description=long_description,
    install_requires=['future'],
    url='https://github.com/bhamiltoncx/pycodepoints/',
    author='Ben Hamilton',
    author_email='bhamiltoncx@gmail.com',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Text Processing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='unicode utf16 surrogate pair bmp smp astral codepoint codeunit emoji maxunicode',
    py_modules=['codepoints'],
    test_suite='nose.collector',
    tests_require=['nose', 'nose-parameterized'],
    zip_safe=False,
)
