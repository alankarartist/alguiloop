from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="alguiloop",
    version="1.0.0",
    description="A Python package to use while and for loops without blocking the GUI. This is currently for Tkinter and PyQT.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/alankarartist/alguiloop",
    author="Alankar Singh",
    author_email="alankarartist@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["AlGUILoop"],
    include_package_data=True,
    install_requires=["PyQt5"],
)