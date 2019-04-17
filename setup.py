#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='divio-dploi-deployments',
      version='0.2',
      description='Utilities for dploi style deplouments',
      author='Nephila',
      author_email='info@nephila.it',
      install_requires=[
          'fabric>=2,<3'
      ],
      packages=['divio_dploi_deployments',],
     )
