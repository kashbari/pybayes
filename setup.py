from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="PyBayes",
    version="0.0.1",
    author="Kashif Bari",
    author_email="kashbari@gmail.com",
    description="Bayesian Filtering",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/kashbari/pybayes",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
    ],
)