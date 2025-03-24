from setuptools import setup, find_packages

setup(
    name="PHTrans",  
    version="0.1.0",  
    author="Zejing Wang",  
    author_email="wangzej@oregonstate.edu", 
    description="The package computes persistent homology transform of a point cloud.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/zejingwa/PHTrans",  
    packages=find_packages(), 
    install_requires=[
        "numpy",
        "scikit-learn",
        "gudhi",
        "matplotlib",
        "sklearn.preprocessing",
    ],  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"
)
