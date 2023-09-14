from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in greentek/__init__.py
from greentek import __version__ as version

setup(
	name="greentek",
	version=version,
	description="Greentek",
	author="varsha chavan",
	author_email="varsha.r.chavan2020@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
