from os import path

from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="betterreads",
    description="Python 3 wrapper for Goodreads API",
    long_description=long_description,
    url="https://github.com/thejessleigh/betterreads",
    author="Jess Unrein",
    author_email="j.l.unrein@gmail.com",
    packages=["betterreads"],
    version="0.4.1",
    install_requires=["nose", "xmltodict", "requests", "rauth"],
    license="MIT",
    keywords="goodreads API",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    long_description_content_type="text/markdown",
)
