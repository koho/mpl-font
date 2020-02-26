import glob

from setuptools import setup, find_packages

setup(use_scm_version=True,
      packages=find_packages(),
      include_package_data=True,
      data_files=[('fonts', glob.glob('fonts/**/*', recursive=True))],
      license='BSD',
      )
