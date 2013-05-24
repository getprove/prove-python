import sys
from prove import __version__
from setuptools import setup, find_packages

# To install the prove-python library, open a Terminal shell, then run this
# file by typing:
#
# python setup.py install
#
# You need to have the setuptools module installed. Try reading the setuptools
# documentation: http://pypi.python.org/pypi/setuptools
REQUIRES = ["httplib2 >= 0.7", "six", "requests"]

if sys.version_info < (2, 6):
    REQUIRES.append('simplejson')
if sys.version_info >= (3,0):
    REQUIRES.append('unittest2py3k')
else:
    REQUIRES.append('unittest2')

setup(
    name = "prove",
    version = __version__,
    description = "Prove API client",
    author = "Nick Baugh",
    author_email = "niftylettuce@gmail.com",
    url = "https://github.com/getprove/prove-python",
    keywords = ["prove"],
    install_requires = REQUIRES,
    packages = find_packages(),
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Telephony",
        ],
    long_description = """\
    Python Prove Helper Library
    ----------------------------

    DESCRIPTION
    The Prove REST SDK simplifies the process of makes calls to the Prove REST.
    The Prove REST API lets to you initiate outgoing calls, list previous calls,
    and much more.  See https://github.com/getprove/prove-python for more information.

     LICENSE The Prove Python Helper Library is distributed under the MIT
    License """ )
