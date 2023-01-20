# flake8: noqa

"""
    Fastly API

    Via the Fastly API you can perform any of the operations that are possible within the management console,  including creating services, domains, and backends, configuring rules or uploading your own application code, as well as account operations such as user administration and billing reports. The API is organized into collections of endpoints that allow manipulation of objects related to Fastly services and accounts. For the most accurate and up-to-date API reference content, visit our [Developer Hub](https://developer.fastly.com/reference/api/)   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: oss@fastly.com
"""


__version__ = "v1.1.0"

# import ApiClient
from fastly.api_client import ApiClient

# import Configuration
from fastly.configuration import Configuration

# import exceptions
from fastly.exceptions import OpenApiException
from fastly.exceptions import ApiAttributeError
from fastly.exceptions import ApiTypeError
from fastly.exceptions import ApiValueError
from fastly.exceptions import ApiKeyError
from fastly.exceptions import ApiException
