from setuptools import setup
from setuptools import find_packages

setup(
    name='math_quiz',
    version='0.1.0',
    description= 'A pacakge for dsss_homework2.'
    author= 'Zeinab meivand',
    packages= ['math_quiz'],
    install_requires=[
        # List of some dependencies here
        'random>=1.2.0,<2.0.0'
    ],
)
