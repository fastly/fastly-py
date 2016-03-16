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
