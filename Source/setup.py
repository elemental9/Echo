# Import setuptools module
import setuptools

# Setup module
setuptools.setup(
    version_format='{tag}',
    setup_requires=['setuptools-git-version'],
)
