from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="alguiloop",
    version="1.0.5",
    description="A python package which allows to use while and for loops without obstructing the GUI. This is currently for tkinter, PyQt5, PyQt6, wxPython, PyForms-GUI and PySide2.",
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
    install_requires=["PyQt5","PyQt6","wxPython","PySide2"],
)