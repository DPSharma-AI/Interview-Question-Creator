from setuptools import find_packages,setup

setup(
    name = "Generative AI Project",
    version = "0.0.0",
    author="DP Sharma",
    author_email="dps158@gmail.com",
    packages = find_packages(), # It will find the scr automatically which consists of __init__.py
    install_requires = [] # it automatically take care of requirements.txt based packages
)