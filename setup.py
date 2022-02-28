#!/usr/bin/env python
from setuptools import setup

setup()

# import os
# import sys
#
# from setuptools import setup, find_packages
# from setuptools.command.test import test as TestCommand
#
# import bq_validator
#
#
# class PyTest(TestCommand):
#     def finalize_options(self):
#         TestCommand.finalize_options(self)
#         self.test_args = []
#         self.test_suite = True
#
#     def run_tests(self):
#         import pytest
#         errcode = pytest.main(self.test_args)
#         sys.exit(errcode)
#
#
# def parse_requirements(path: str):
#     """Parse requirements.txt
#
#     Args:
#         path (str): path to requirements.txt
#
#     Returns:
#         list: a list of python modules
#     """
#     with open(path, "r") as fp:
#         return [line.strip() for line in fp.readlines()]
#
#
# # Please maintain `./requirements/requirements.txt` directly.
# requirements_path = os.path.join(
#     os.path.dirname(__file__), "requirements", "requirements.txt")
# setup(
#     name='bq-validator',
#     packages=find_packages('bq_validator'),
#     version=bq_validator.__version__,
#     install_requires=parse_requirements(requirements_path),
#     entry_points={
#         "console_scripts": [
#             "bq-validator = bq_validator.cli:main",
#         ],
#     },
#     tests_require=['pytest'],
#     cmdclass={'test': PyTest}
# )
