from setuptools import setup, find_packages

# Read the version from version.txt
with open('version.txt') as f:
    version = f.read().strip()

setup(
    name='calculator',
    version=version,  # Use the dynamically updated version
    packages=find_packages(),
    install_requires=[
        'pytest',
    ],
    description='Simple calculator package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    options={
        'sdist': {'formats': ['zip']}
    },
)
