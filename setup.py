import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.partdir)))

setup(
    name = 'facerec',
    version = '0.1',
    packages = ['facerec'],
    include_package_data = True,
    license = 'Apache V2',
    description = 'Facial recognition python library',
    long_description = README,
    url = 'http://hyperlayer.io',
    author = 'Dan Lipert',
    author_email = 'dan@hyperlayer.io',
    classifiers =['Intended Audience :: Developers',
                  'License :: OSI Approved :: Apache Software License',
                  'Operating System :: OS Independent',
                  'Programming Language :: Python',
                  'Programming Language :: Python :: 2.6',
                  'Programming Language :: Python :: 2.7',
                  ]
)
