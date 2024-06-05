from setuptools import setup, find_packages

with open("README.md", "r") as r:
    desc = r.read()

setup(
    name="filewalker",
    version="1.0.1",
    author="5f0",
    url="https://github.com/5f0ne/filewalker",
    description="Searches hard drives/given path for files specified by file extension",
    classifiers=[
        "Operating System :: OS Independent ",
        "Programming Language :: Python :: 3 ",
        "License :: OSI Approved :: MIT License "
    ],
    license="MIT",
    long_description=desc,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where='src'),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "filewalker = filewalker.__main__:main"
        ]
    }
)
