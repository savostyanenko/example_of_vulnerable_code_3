from setuptools import setup, find_packages

setup(
    name="example_of_vulnerable_code_3",
    version="1.0.1",
    author="Kostiantyn Savostianenko",
    description="Example vulnerable Python project for SBOM and Cosign demo",
    packages=find_packages(),
    install_requires=[
        "requests",
        "PyMySQL",
        "opencv-python-headless",
        "Django",
        "bleach",
    ],
)
