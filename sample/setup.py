import setuptools

with open("README.MD", "r") as fileheader:
    long_description  = fileheader.read()

setuptools.setup(
    name="sample",
    version="0.0.1",
    author="KrishnaMohan",
    author_email="krishnamohan.seelam@outlook.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=" ",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)