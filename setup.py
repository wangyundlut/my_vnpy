# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    packages=find_packages(),
    package_data={'': ['*.json', '*.md', '*.ico',
                       '*.h', '*.cpp', '*.bash', '*.txt',
                       '*.dll', '*.lib', '*.so', '*.pyd',
                       '*.dat', '*.ini', '*.pfx', '*.scc', '*.crt', '*.key']},
    extras_require={'tq': ["tornado>=4.5.1", "sortedcontainers>=1.5.7"]})
