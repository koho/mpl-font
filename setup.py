from setuptools import setup, find_packages

setup(use_scm_version=True,
      packages=find_packages(),
      include_package_data=True,
      package_data={
        'mpl_font': ['fonts/**/*.?t?'],
      },
      license='BSD',
      )
