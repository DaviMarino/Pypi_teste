from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='pypi_teste',
    version='0.0.1',
    license='MIT License',
    author='Davi Marino',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='',
    keywords='Pypi',
    description=u'Pypi teste não oficial',
    packages=['Pypi_teste'])