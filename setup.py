from setuptools import setup
exec(open('fastly/_version.py').read())

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="fastly",
    version=__version__,  # pylint: disable=undefined-variable
    author="Fastly",
    author_email="support@fastly.com",
    description="Fastly python API",
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities"
    ],
    keywords="fastly api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['fastly'],
    install_requires=[
        'six',
    ],
    scripts=[
        "bin/purge_service",
        "bin/purge_key",
        "bin/purge_url",
        "bin/fastly"
    ],
    url="https://github.com/fastly/fastly-py",
)
