from html.entities import name2codepoint
from setuptools import setup, find_packages


setup (
    name='naics',
    version='1.0',
    # url='https://github.com/naics.git',
    license='MIT',
    author='Gray Alien Ventures',
    author_email='info@intp.io',
    packages=find_packages(),
    # classifiers=[
    #     "Programming Language :: Python :: 3",
    #     "License :: OSI Approved :: MIT License",
    #     "Operating System :: OS Independent",
    # ],                                      # Information to filter the project on PyPi website
    py_modules=["naics"],             # Name of the python package
    package_dir={'':'naics/src'},     # Directory of the source code of the package
    install_requires=[]                     # Install other dependencies if any
)