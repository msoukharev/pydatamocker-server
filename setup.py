import setuptools


with open("README.md", "rt", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="pydatamocker_server",
    version="0.2.0",
    author="Maxim Soukharev",
    author_email="maxim.soukharev@gmail.com",
    description="Pydatamocker flask server consumer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/msoukharev/pydatamocker-server",
    project_urls={
        "Bug Tracker": "https://github.com/msoukharev/pydatamocker-server/issues",
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Testing",
        "Topic :: Server",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10"
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where='.'),
    python_requires=">=3.10",
)
