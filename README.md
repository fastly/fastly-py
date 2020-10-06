## Fastly Python Client

fastly-py is available through `pip` as the [fastly](https://pypi.python.org/pypi/fastly) package

There are three simple scripts provided in `/bin` that can be used for various stand-alone purge operations.

### A Note About Authentication

Authenticating with an API Token is shown in the example below. For more information on API Tokens, please see [Fastly's API Token documentation](https://developer.fastly.com/reference/api/auth/). For more information about authenticating to our API, please see our [Authentication section](https://developer.fastly.com/reference/api/#authentication).


### Usage

```python
import fastly
api = fastly.API()
api.authenticate_by_key('MYKEY')
api.purge_url('www.example.com', '/some/path')
```

### TODO:

Doc files<br>
Docstrings<br>
Config file<br>

### Running Tests

```
$ python -m test.api_test
```

#### Set up environment configuration
We use Python's [os](https://docs.python.org/2/library/os.html) and a `.env` file to manage environment variables in development and test environments. See the list of required environment variables in the `.env.example` file in the root directory.

To optionally set values for testing, make a copy of `.env.example` and name it `.env`.

```bash
cp .env.example .env

# Note:
# If using direnv, you can just use it as a `.envrc` file and not have to `source` it manually.

# Using your favorite editor, update the values of the environment variables in `.env` and then

source .env
```

### Distributing a package

Create a `.pypirc` file:

```
$ cat > .pypirc
[distutils]
index-servers =
    pypi

[pypi]
repository: https://upload.python.org/legacy/
```

Install twine:

```
$ python3 -m pip install --user --upgrade twine
```

Create a build:
```
$ python3 setup.py sdist bdist_wheel
```

Use twine to publish to Pypi:

```
$ twine upload dist/* 
Uploading distributions to https://upload.pypi.org/legacy/
Enter your username: [YOUR_USERNAME]
Enter your password:
Uploading fastly-0.2.3-py3-none-any.whl
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 13.2k/13.2k [00:02<00:00, 6.40kB/s]
Uploading fastly-0.1.3-py2.7.egg
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 17.8k/17.8k [00:01<00:00, 12.8kB/s]
Uploading fastly-0.1.3-py3.6.egg
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 18.3k/18.3k [00:01<00:00, 14.2kB/s]
Uploading fastly-0.2.3.tar.gz
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 9.25k/9.25k [00:01<00:00, 9.09kB/s]
```

Builds and uploads to PyPi. More info on this at the [python
site](https://packaging.python.org/tutorials/packaging-projects/). You will
need to be granted access to the fastly package in order to push.
