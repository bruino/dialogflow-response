import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dialogflow-response",
    version="0.0.1",
    author="bruino",
    author_email="bruno.sarverry@outlook.com",
    description="Create webhook JSON responses for Dialogflow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bruino/dialogflow-response",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
    ],
    python_requires=">=3.6",
)