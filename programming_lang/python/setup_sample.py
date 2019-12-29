# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

version = {}
with open(path.join(here, '<placeholder>/__about__.py'), encoding='utf-8') as f:
    exec(f.read(), version)

requires = [
]

test_requires = [
    'pytest',
    'pytest-mock',
]

dev_requires = test_requires + [
    'wheel',
    'bpython',
    'pytest',
    'flake8',
    'autopep8',
    'pylint'
]

setup(
    name='<placeholder>',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # http://packaging.python.org/en/latest/tutorial.html#version
    version=version['__version__'],

    description='<placeholder>',
    long_description=long_description,
    long_description_content_type='text/x-rst',

    # The project's main homepage.
    url='',

    # Author details
    author='Gatsby Lee',

    # Choose your license
    license='GPL-3.0',

    # See https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[

        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
    ],
    # What does your project relate to?
    keywords='<placeholder>',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(
        exclude=['contrib', 'docs', 'tests*', 'playground*']),

    # List run-time dependencies here.  These will be installed by pip when your
    # project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/technical.html#install-requires-vs-requirements-files
    python_requires=">=3.6",
    install_requires=requires,
    extras_require={
        'dev': dev_requires,
        'test': test_requires,
    },
)
