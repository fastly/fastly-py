import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="fastly",
    version="0.0.2",
    author="Fastly",
    author_email="support@fastly.com",
    description="Fastly python API",
    keywords="fastly api",
    url="https://github.com/fastly/fastly-py",
    packages=find_packages(),
    long_description=read('README'),
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities"
    ],
    entry_points={
      'console_scripts': [
        'purge_service = fastly.scripts.purge_service:purge_service',
        'purge_key     = fastly.scripts.purge_key:purge_key',
        'purge_url     = fastly.scripts.purge_url:purge_url',
      ]
    },
)
