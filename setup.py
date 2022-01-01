import sys
from setuptools import setup, find_packages

if sys.platform != "win32":
      raise Exception("ps3api only supports 32 bit windows.")

setup(name='ps3api',
      version='0.1',
      description='Python module for interacting with PS3 using CCAPI or TMAPI.',
      url='http://github.com/iMoD1998/PS3API',
      author='iMoD1998',
      author_email='imod1998@protonmail.com',
      license='MIT',
      packages=find_packages())