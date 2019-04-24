from setuptools import setup

setup(
    name="betterreads",
    description="Python 3 wrapper for Goodreads API",
    long_description=open("README.rst").read(),
    url="https://github.com/thejessleigh/betterreads",
    author="Jess Unrein",
    author_email="j.l.unrein@gmail.com",
    packages=["betterreads"],
    version="0.4.0",
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
)
