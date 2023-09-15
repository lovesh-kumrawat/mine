import setuptools


name = "mine"
version = "1.0.0"
description = "Personal custom supporting package"

with open("README.md", "r") as fh:
    readme = fh.read()

with open("LICENSE", "r") as fh:
    license = fh.read()


setuptools.setup(
    name=name,
    version=version,
    description=description,
    long_description=readme,
    license=license,
    author="Lovesh Kumrawat",
    author_email="kumrawat.lovesh@gmail.com",
    packages=setuptools.find_packages(),
    install_requires=[],
    url="https://github.com/lovesh-kumrawat/mine.git",
    keywords=[]
)
