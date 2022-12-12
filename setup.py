from setuptools import setup

setup(
    name='psat-api-python',
    version='1.0.0',
    packages=['psat_api', 'psat_api.web', 'psat_api.reports'],
    install_requires=['requests'],
    url='https://github.com/pfptcommunity/psat-api-python',
    license='MIT',
    author='Ludvik Jerabek',
    author_email='',
    description='Proofpoint Security Awareness Training Python API Package'
)
