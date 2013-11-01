from setuptools import setup, find_packages
setup(
    name="lssh",
    version="0.0.1",
    description="LightySSH",
    author="Lhfcws Wu",
    url="http://www.github.com/Lhfcws/lssh",
    license="LGPL",
    packages= find_packages(),
    scripts=["scripts/lssh.py"],
    )
