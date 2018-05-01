#!/usr/bin/env python

import os
import sys

from setuptools import find_packages
from distutils.core import setup, Extension
import distutils.command.install_data

f = open('version', 'r')
version = f.readline()[8:].strip()
f.close()

author = 'Chris Higgs, Stuart Hodgson'
author_email = 'cocotb@potentialventures.com'

install_requires = []
class cocotb_install_data(distutils.command.install_data.install_data):
    """need to change self.install_dir to the actual library dir"""
    def run(self):
      install_cmd = self.get_finalized_command('install')
      self.install_dir = getattr(install_cmd, 'install_lib')
      return distutils.command.install_data.install_data.run(self)

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join(path, filename))
    return paths

data_files  = [(os.path.join('cocotb', name), package_files(name))
              for name in ['makefiles', 'lib', 'include'] ]
data_files.append( (os.path.join('share/cocotb'), ['version']) )

setup(
    name='cocotb',
    version=version,
    description='**cocotb** is a coroutine based cosimulation library for writing VHDL and Verilog testbenches in Python.',
    url='https://github.com/potentialventures/cocotb',
    license='BSD',
    long_description='',
    author=author,
    maintainer=author,
    author_email=author_email,
    maintainer_email=author_email,
    install_requires=install_requires,
    packages=find_packages(),
    cmdclass={'install_data': cocotb_install_data},
    data_files=data_files,
    scripts=['bin/cocotb-path'],
    platforms='any'
)
