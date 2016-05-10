## Fastly Python Client

fastly-py is available through `pip` as the [fastly](https://pypi.python.org/pypi/fastly) package

There are three simple scripts provided in `/bin` that can be used for various stand-alone purge operations.

### Usage

```python
import fastly
api = fastly.API()
api.authenticate_by_key('MYKEY')
api.purge_url('www.example.com', '/some/path')
```

### TODO:

Doc files
Docstrings
Config file

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

```
$ python setup.py register
```

Follow the prompts to create an account or login. The `register` command also ensures that your account has access to the fastly package on PyPi.

```
$ python setup.py sdist upload
```

Builds and uploads to PyPi. More info on this at the [python site](https://docs.python.org/2/distutils/packageindex.html).
You will need to be granted access to the fastly package in order to push.
