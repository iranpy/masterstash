import sys

try:
    from setuptools import setup, find_packages
except:
    from distutils.core import setup


base_dependencies = [
        'kombu',
        'marshmallow==3.0.0rc5',
        'requests',
        ]
setup(
      name="masterstash",
      description="lightweight log managemnet system",
      version="0.1",
      author="Ali Ebtehaj",
      author_email="debian1390@gmail.com",
      url="http://192.168.45.111/AI/masterstash",
      packages=find_packages(),
      install_requires=base_dependencies,
#      entry_points = {
#            'console_scripts': ['masterstash = masterstash.cli:base']
#      },
      classifiers=[
          'Programming Language :: Python :: 3',
      ]
      )
