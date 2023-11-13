from setuptools import setup
from setuptools import find_packages

setup(
    name='math_quiz',
    version='0.1',
    #author_email= "zeinab.meivand@fau.de",
    packages=find_packages(),
    install_requires=[
        # List of some dependencies here
        'random'
    ],
)
