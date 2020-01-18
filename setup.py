# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
import os, sys, ast

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "version"), "r") as f:
    version = f.read().strip()

#hashcat_url = "https://hashcat.net/files/hashcat-5.1.0.7z"

with open(os.path.join(here, 'pypi.rst'), encoding='utf-8') as f:
    long_description = f.read()
#long_description = "See website for more info."

setup(
    name='hashcat-beta',
    version=version,
    description='Python pip installer for hashcat beta',
    long_description=long_description,
    url='https://github.com/bannsec/hashcat-beta',
    author='Michael Bann',
    author_email='self@bannsecurity.com',
    license='MIT',
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Environment :: Console'
    ],
    keywords='hashcat',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[],
    extras_require={
        'dev': ['ipython','twine','pytest','python-coveralls','coverage==4.5.4','pytest-cov','pytest-xdist','sphinxcontrib-napoleon', 'sphinx_rtd_theme','sphinx-autodoc-typehints'],
    },
    entry_points={
        'console_scripts': [
            'hashcat = hashcat.cli:main',
            'pp64 = hashcat.cli:pp',
            'pp = hashcat.cli:pp',
            'cap2hccapx = hashcat.cli:cap2hccapx',
            'kwp = hashcat.cli:kwp',
        ],
    },
    include_package_data = True,
)

