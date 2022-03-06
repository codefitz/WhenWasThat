import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="WhenWasThat",
    version="0.1.0",
    author="Wes Moskal-Fitzpatrick",
    author_email="wes@traversys.io",
    description="A small library for getting human readable time value.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codefitz/WhenWasThat",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
    install_requires=[
        'pandas',
    ]
)
