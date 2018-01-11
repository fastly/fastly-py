from setuptools import setup
version = {}
with open('fastly/_version.py') as fp:
    exec(fp.read(), version)

setup(
    name="fastly",
    version=version['__version__'],
    author="Fastly",
    author_email="support@fastly.com",
    description="Fastly python API",
    keywords="fastly api",
    url="https://github.com/fastly/fastly-py",
    packages=['fastly'],
    long_description=open('README.md').read(),
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities"
    ],
    scripts=[
        "bin/purge_service",
        "bin/purge_key",
        "bin/purge_url"
    ]
)
