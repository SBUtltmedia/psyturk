from setuptools import setup

__version__ = '0.0.1'
__author__ = 'TLT Media Lab'

requirements = [
        "boto==2.46.1",
        "boto3==1.4.4",
        "botocore==1.5.38"
        ]

description = 'mturk setup with boto3 & boto3'
setup(
        name='psyturk',
        version=__version__,
        author=__author__,
        url='https://github.com/numaer/psyturk',
        description=description,
        install_requires=requirements
        )
