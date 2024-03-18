from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-merger-rgb",
    version="0.1.0",
    author=" G. Alves",
    author_email="your.email@example.com",
    description="A simple utility to merge two images using RGB parameters",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="[1](https://github.com/yourusername/image-merger-rgb)",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.6',
)
