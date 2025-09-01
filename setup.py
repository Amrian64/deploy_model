from setuptools import setup
from setuptools import find_packages

with open('requirements.txt') as f:
    content = f.readlines()
    requirements = [x.strip() for x in content if 'git+' not in x]

setup(
    name='estimator',
    version='0.0.0',
    packages=find_packages(),
    package_data={
      'pkg_estimator': ['data/*.pkl'],
    },
    install_requires=requirements

)
