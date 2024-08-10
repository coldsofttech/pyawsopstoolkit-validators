from setuptools import setup, find_packages

import pyawsopstoolkit_validators

setup(
    name=pyawsopstoolkit_validators.__name__,
    version=pyawsopstoolkit_validators.__version__,
    packages=find_packages(),
    url='https://github.com/coldsofttech/pyawsopstoolkit-validators.git',
    license='MIT',
    author='coldsofttech',
    description=pyawsopstoolkit_validators.__description__,
    requires_python=">=3.10",
    install_requires=[
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords=[
        "aws", "toolkit", "operations", "tools", "development", "python", "validation", "utilities",
        "amazon-web-services"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12"
    ]
)
