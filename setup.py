# setup.py
from setuptools import setup, find_packages

setup(
    name="tsrw",            
    version="1.0.0",       
    packages=find_packages(where="."),  
   
    entry_points={
        "console_scripts": [
            "tsrw = test_statistic_read_write.cli:main"
        ]
    },

    python_requires=">=3.7",
    install_requires=[],  
    author="Kirill Sedow",
    description="A tool that reads, analyses, and writes test case statistics."
)

