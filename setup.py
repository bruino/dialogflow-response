import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dialogflow-response",
    version="0.1.1",
    author="bruino",
    author_email="bruno.sarverry@outlook.com",
    description=" Create webhook responses for Dialogflow with this small library in python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bruino/dialogflow-response",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
