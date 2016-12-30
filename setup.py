# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

__VERSION__ = '0.0.1'

entry_points = []

data = []

install_requires = []

with open('requirements.txt') as f:
    for r in f:
        install_requires.append(r)

setup(
    name="jsonql",
    version=__VERSION__,
    long_description=open('README.md').read(),
    author="MrKiven",
    author_email="kiven.mr@gmail.com",
    packages=find_packages(),
    package_data={"": ["LICENSE"], "jsonql": data},
    url="https://github.com/MrKiven/jsonql-py",
    entry_points={"console_scripts": entry_points},
    tests_require=[
        'pytest==2.5.2',
        'pytest-cov==1.8.1',
        'pytest-xdist==1.13.1',
        'mock==1.0.1',
    ],
    install_requires=install_requires,
    classifiers=[
        'Private :: Do Not Upload',
    ]
)
