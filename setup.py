from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1",
    packages=find_packages(exclude=['tests*']),
    license="MIT",
    description="EDSA example python package",
    long_description=open('README.md').read(),
    install_requires=["numpy"],
    url="https://github.com/danny_stringz/top_n",
    author="Daniel Kwabena Tetteh",
    author_email="dtetteh995@gmail.com"
)