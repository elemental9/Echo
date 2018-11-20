# Import setuptools module
import setuptools

# Parse the readme markdown file
with open("../README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="Echo",
    version="0.0.1",
    author="elemental9",
    description=
    "A code os.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/elemental9/Echo",
    packages=setuptools.find_packages(),
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ),
)
