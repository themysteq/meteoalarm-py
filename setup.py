#!/usr/bin/env python

from setuptools import find_packages, setup

VERSION = "0.1.dev0"

install_requires = [
    "requests >= 2.29.0",
    "urllib3 < 2.0",
    "pydantic >= 1.10.8",
]
tests_require = []

dev_extras = tests_require + [
    "pytest",
    "pytest-cov",
    "pytest-vcr",
    "pytest-datafiles",
    "pylint",
    "black",
    "flake8",
    "isort",
    "check-manifest",
    "docutils",
    "urllib3<2.0",
]


setup(
    name="meteoalarm-py",
    version=VERSION,
    extras_require={"dev": dev_extras},
    tests_require=tests_require,
    packages=find_packages("src", exclude=["tests"]),
    install_requires=install_requires,
    package_dir={"": "src"},
    python_requires=">=3.7",
    url="https://github.com/themysteq/meteoalarm-py",
    author="themysteq",
    author_email="kurek.zxc@gmail.com",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
