# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from pkg_resources import resource_string
from setuptools import find_packages
from setuptools import setup


setup(
    name='canopener',
    version='0.1.5post1',
    author='David Selassie',
    author_email='selassid@gmail.com',
    packages=find_packages(exclude=['tests']),
    url='https://github.com/selassid/canopener',
    license=open('LICENSE.txt').read(),
    description=(
        'Python convenience function for opening compressed URLs and files.'
    ),
    keywords='open file s3 url bzip bz2 gzip gz',
    include_package_data=True,
    long_description=open('README.rst').read(),
    setup_requires=['setuptools'],
    install_requires=[
        'boto',
        'pystaticconfiguration',
    ],
)
