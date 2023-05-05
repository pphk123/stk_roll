from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in stk_roll/__init__.py
from stk_roll import __version__ as version

setup(
	name="stk_roll",
	version=version,
	description="stk roll",
	author="gami",
	author_email="g@g.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
