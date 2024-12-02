from setuptools import setup, find_packages

setup(
    name='calculator',
    version='1.0.6',  # Incremented version
    packages=find_packages(),
    install_requires=[
        'pytest',
    ],
    description='A calculator package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
