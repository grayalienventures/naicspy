from html.entities import name2codepoint
from setuptools import setup, find_packages


setup (
    name='naics',
    version='1.0',
    url='https://github.com/grayalienventures/naicspy',
    license='MIT',
    author='Gray Alien Ventures',
    author_email='info@intp.io',
    packages=find_packages(),
    classifiers=[
        "naics",
        "NAICS",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],        
    keywords=[
        "naics",
        "NAICS",
        "industry"
    ],  
    py_modules=["naics"],
    package_dir={'':'naics/src'},
    install_requires=[]
)