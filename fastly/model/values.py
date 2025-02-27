"""
    Fastly API

    Via the Fastly API you can perform any of the operations that are possible within the management console,  including creating services, domains, and backends, configuring rules or uploading your own application code, as well as account operations such as user administration and billing reports. The API is organized into collections of endpoints that allow manipulation of objects related to Fastly services and accounts. For the most accurate and up-to-date API reference content, visit our [Developer Hub](https://www.fastly.com/documentation/reference/api/)   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: oss@fastly.com
"""


import re  # noqa: F401
import sys  # noqa: F401

from fastly.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from fastly.exceptions import ApiAttributeError



class Values(ModelNormal):
    """NOTE: This class is auto generated.
    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'edge_requests': (int,),  # noqa: E501
            'edge_resp_header_bytes': (int,),  # noqa: E501
            'edge_resp_body_bytes': (int,),  # noqa: E501
            'status_1xx': (int,),  # noqa: E501
            'status_2xx': (int,),  # noqa: E501
            'status_3xx': (int,),  # noqa: E501
            'status_4xx': (int,),  # noqa: E501
            'status_5xx': (int,),  # noqa: E501
            'status_200': (int,),  # noqa: E501
            'status_204': (int,),  # noqa: E501
            'status_206': (int,),  # noqa: E501
            'status_301': (int,),  # noqa: E501
            'status_302': (int,),  # noqa: E501
            'status_304': (int,),  # noqa: E501
            'status_400': (int,),  # noqa: E501
            'status_401': (int,),  # noqa: E501
            'status_403': (int,),  # noqa: E501
            'status_404': (int,),  # noqa: E501
            'status_416': (int,),  # noqa: E501
            'status_429': (int,),  # noqa: E501
            'status_500': (int,),  # noqa: E501
            'status_501': (int,),  # noqa: E501
            'status_502': (int,),  # noqa: E501
            'status_503': (int,),  # noqa: E501
            'status_504': (int,),  # noqa: E501
            'status_505': (int,),  # noqa: E501
            'status_530': (int,),  # noqa: E501
            'requests': (int,),  # noqa: E501
            'resp_header_bytes': (int,),  # noqa: E501
            'resp_body_bytes': (int,),  # noqa: E501
            'bereq_header_bytes': (int,),  # noqa: E501
            'bereq_body_bytes': (int,),  # noqa: E501
            'edge_hit_requests': (int,),  # noqa: E501
            'edge_miss_requests': (int,),  # noqa: E501
            'origin_fetches': (int,),  # noqa: E501
            'origin_fetch_resp_header_bytes': (int,),  # noqa: E501
            'origin_fetch_resp_body_bytes': (int,),  # noqa: E501
            'bandwidth': (int,),  # noqa: E501
            'edge_hit_ratio': (float,),  # noqa: E501
            'origin_offload': (float,),  # noqa: E501
            'origin_status_200': (int,),  # noqa: E501
            'origin_status_204': (int,),  # noqa: E501
            'origin_status_206': (int,),  # noqa: E501
            'origin_status_301': (int,),  # noqa: E501
            'origin_status_302': (int,),  # noqa: E501
            'origin_status_304': (int,),  # noqa: E501
            'origin_status_400': (int,),  # noqa: E501
            'origin_status_401': (int,),  # noqa: E501
            'origin_status_403': (int,),  # noqa: E501
            'origin_status_404': (int,),  # noqa: E501
            'origin_status_416': (int,),  # noqa: E501
            'origin_status_429': (int,),  # noqa: E501
            'origin_status_500': (int,),  # noqa: E501
            'origin_status_501': (int,),  # noqa: E501
            'origin_status_502': (int,),  # noqa: E501
            'origin_status_503': (int,),  # noqa: E501
            'origin_status_504': (int,),  # noqa: E501
            'origin_status_505': (int,),  # noqa: E501
            'origin_status_530': (int,),  # noqa: E501
            'origin_status_1xx': (int,),  # noqa: E501
            'origin_status_2xx': (int,),  # noqa: E501
            'origin_status_3xx': (int,),  # noqa: E501
            'origin_status_4xx': (int,),  # noqa: E501
            'origin_status_5xx': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'edge_requests': 'edge_requests',  # noqa: E501
        'edge_resp_header_bytes': 'edge_resp_header_bytes',  # noqa: E501
        'edge_resp_body_bytes': 'edge_resp_body_bytes',  # noqa: E501
        'status_1xx': 'status_1xx',  # noqa: E501
        'status_2xx': 'status_2xx',  # noqa: E501
        'status_3xx': 'status_3xx',  # noqa: E501
        'status_4xx': 'status_4xx',  # noqa: E501
        'status_5xx': 'status_5xx',  # noqa: E501
        'status_200': 'status_200',  # noqa: E501
        'status_204': 'status_204',  # noqa: E501
        'status_206': 'status_206',  # noqa: E501
        'status_301': 'status_301',  # noqa: E501
        'status_302': 'status_302',  # noqa: E501
        'status_304': 'status_304',  # noqa: E501
        'status_400': 'status_400',  # noqa: E501
        'status_401': 'status_401',  # noqa: E501
        'status_403': 'status_403',  # noqa: E501
        'status_404': 'status_404',  # noqa: E501
        'status_416': 'status_416',  # noqa: E501
        'status_429': 'status_429',  # noqa: E501
        'status_500': 'status_500',  # noqa: E501
        'status_501': 'status_501',  # noqa: E501
        'status_502': 'status_502',  # noqa: E501
        'status_503': 'status_503',  # noqa: E501
        'status_504': 'status_504',  # noqa: E501
        'status_505': 'status_505',  # noqa: E501
        'status_530': 'status_530',  # noqa: E501
        'requests': 'requests',  # noqa: E501
        'resp_header_bytes': 'resp_header_bytes',  # noqa: E501
        'resp_body_bytes': 'resp_body_bytes',  # noqa: E501
        'bereq_header_bytes': 'bereq_header_bytes',  # noqa: E501
        'bereq_body_bytes': 'bereq_body_bytes',  # noqa: E501
        'edge_hit_requests': 'edge_hit_requests',  # noqa: E501
        'edge_miss_requests': 'edge_miss_requests',  # noqa: E501
        'origin_fetches': 'origin_fetches',  # noqa: E501
        'origin_fetch_resp_header_bytes': 'origin_fetch_resp_header_bytes',  # noqa: E501
        'origin_fetch_resp_body_bytes': 'origin_fetch_resp_body_bytes',  # noqa: E501
        'bandwidth': 'bandwidth',  # noqa: E501
        'edge_hit_ratio': 'edge_hit_ratio',  # noqa: E501
        'origin_offload': 'origin_offload',  # noqa: E501
        'origin_status_200': 'origin_status_200',  # noqa: E501
        'origin_status_204': 'origin_status_204',  # noqa: E501
        'origin_status_206': 'origin_status_206',  # noqa: E501
        'origin_status_301': 'origin_status_301',  # noqa: E501
        'origin_status_302': 'origin_status_302',  # noqa: E501
        'origin_status_304': 'origin_status_304',  # noqa: E501
        'origin_status_400': 'origin_status_400',  # noqa: E501
        'origin_status_401': 'origin_status_401',  # noqa: E501
        'origin_status_403': 'origin_status_403',  # noqa: E501
        'origin_status_404': 'origin_status_404',  # noqa: E501
        'origin_status_416': 'origin_status_416',  # noqa: E501
        'origin_status_429': 'origin_status_429',  # noqa: E501
        'origin_status_500': 'origin_status_500',  # noqa: E501
        'origin_status_501': 'origin_status_501',  # noqa: E501
        'origin_status_502': 'origin_status_502',  # noqa: E501
        'origin_status_503': 'origin_status_503',  # noqa: E501
        'origin_status_504': 'origin_status_504',  # noqa: E501
        'origin_status_505': 'origin_status_505',  # noqa: E501
        'origin_status_530': 'origin_status_530',  # noqa: E501
        'origin_status_1xx': 'origin_status_1xx',  # noqa: E501
        'origin_status_2xx': 'origin_status_2xx',  # noqa: E501
        'origin_status_3xx': 'origin_status_3xx',  # noqa: E501
        'origin_status_4xx': 'origin_status_4xx',  # noqa: E501
        'origin_status_5xx': 'origin_status_5xx',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Values - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            edge_requests (int): Number of requests sent by end users to Fastly.. [optional]  # noqa: E501
            edge_resp_header_bytes (int): Total header bytes delivered from Fastly to the end user.. [optional]  # noqa: E501
            edge_resp_body_bytes (int): Total body bytes delivered from Fastly to the end user.. [optional]  # noqa: E501
            status_1xx (int): Number of 1xx \"Informational\" category status codes delivered.. [optional]  # noqa: E501
            status_2xx (int): Number of 2xx \"Success\" status codes delivered.. [optional]  # noqa: E501
            status_3xx (int): Number of 3xx \"Redirection\" codes delivered.. [optional]  # noqa: E501
            status_4xx (int): Number of 4xx \"Client Error\" codes delivered.. [optional]  # noqa: E501
            status_5xx (int): Number of 5xx \"Server Error\" codes delivered.. [optional]  # noqa: E501
            status_200 (int): Number of responses delivered with status code 200 (Success).. [optional]  # noqa: E501
            status_204 (int): Number of responses delivered with status code 204 (No Content).. [optional]  # noqa: E501
            status_206 (int): Number of responses delivered with status code 206 (Partial Content).. [optional]  # noqa: E501
            status_301 (int): Number of responses delivered with status code 301 (Moved Permanently).. [optional]  # noqa: E501
            status_302 (int): Number of responses delivered with status code 302 (Found).. [optional]  # noqa: E501
            status_304 (int): Number of responses delivered with status code 304 (Not Modified).. [optional]  # noqa: E501
            status_400 (int): Number of responses delivered with status code 400 (Bad Request).. [optional]  # noqa: E501
            status_401 (int): Number of responses delivered with status code 401 (Unauthorized).. [optional]  # noqa: E501
            status_403 (int): Number of responses delivered with status code 403 (Forbidden).. [optional]  # noqa: E501
            status_404 (int): Number of responses delivered with status code 404 (Not Found).. [optional]  # noqa: E501
            status_416 (int): Number of responses delivered with status code 416 (Range Not Satisfiable).. [optional]  # noqa: E501
            status_429 (int): Number of responses delivered with status code 429 (Too Many Requests).. [optional]  # noqa: E501
            status_500 (int): Number of responses delivered with status code 500 (Internal Server Error).. [optional]  # noqa: E501
            status_501 (int): Number of responses delivered with status code 501 (Not Implemented).. [optional]  # noqa: E501
            status_502 (int): Number of responses delivered with status code 502 (Bad Gateway).. [optional]  # noqa: E501
            status_503 (int): Number of responses delivered with status code 503 (Service Unavailable).. [optional]  # noqa: E501
            status_504 (int): Number of responses delivered with status code 504 (Gateway Timeout).. [optional]  # noqa: E501
            status_505 (int): Number of responses delivered with status code 505 (HTTP Version Not Supported).. [optional]  # noqa: E501
            status_530 (int): Number of responses delivered with status code 530.. [optional]  # noqa: E501
            requests (int): Number of requests processed.. [optional]  # noqa: E501
            resp_header_bytes (int): Total header bytes delivered.. [optional]  # noqa: E501
            resp_body_bytes (int): Total body bytes delivered.. [optional]  # noqa: E501
            bereq_header_bytes (int): Total header bytes sent to origin.. [optional]  # noqa: E501
            bereq_body_bytes (int): Total body bytes sent to origin.. [optional]  # noqa: E501
            edge_hit_requests (int): Number of requests sent by end users to Fastly that resulted in a hit at the edge.. [optional]  # noqa: E501
            edge_miss_requests (int): Number of requests sent by end users to Fastly that resulted in a miss at the edge.. [optional]  # noqa: E501
            origin_fetches (int): Number of requests sent to origin.. [optional]  # noqa: E501
            origin_fetch_resp_header_bytes (int): Total header bytes received from origin.. [optional]  # noqa: E501
            origin_fetch_resp_body_bytes (int): Total body bytes received from origin.. [optional]  # noqa: E501
            bandwidth (int): Total bytes delivered (`resp_header_bytes` + `resp_body_bytes` + `bereq_header_bytes` + `bereq_body_bytes`).. [optional]  # noqa: E501
            edge_hit_ratio (float): Ratio of cache hits to cache misses at the edge, between 0 and 1 (`edge_hit_requests` / (`edge_hit_requests` + `edge_miss_requests`)).. [optional]  # noqa: E501
            origin_offload (float): Origin Offload measures the ratio of bytes served to end users that were cached by Fastly, over the bytes served to end users, between 0 and 1. ((`edge_resp_body_bytes` + `edge_resp_header_bytes`) - (`origin_fetch_resp_body_bytes` + `origin_fetch_resp_header_bytes`)) / (`edge_resp_body_bytes` + `edge_resp_header_bytes`). Previously, Origin Offload used a different formula. [Learn more](https://www.fastly.com/documentation/reference/changes/2024/06/add-origin_offload-metric).. [optional]  # noqa: E501
            origin_status_200 (int): Number of responses received from origin with status code 200 (Success).. [optional]  # noqa: E501
            origin_status_204 (int): Number of responses received from origin with status code 204 (No Content).. [optional]  # noqa: E501
            origin_status_206 (int): Number of responses received from origin with status code 206 (Partial Content).. [optional]  # noqa: E501
            origin_status_301 (int): Number of responses received from origin with status code 301 (Moved Permanently).. [optional]  # noqa: E501
            origin_status_302 (int): Number of responses received from origin with status code 302 (Found).. [optional]  # noqa: E501
            origin_status_304 (int): Number of responses received from origin with status code 304 (Not Modified).. [optional]  # noqa: E501
            origin_status_400 (int): Number of responses received from origin with status code 400 (Bad Request).. [optional]  # noqa: E501
            origin_status_401 (int): Number of responses received from origin with status code 401 (Unauthorized).. [optional]  # noqa: E501
            origin_status_403 (int): Number of responses received from origin with status code 403 (Forbidden).. [optional]  # noqa: E501
            origin_status_404 (int): Number of responses received from origin with status code 404 (Not Found).. [optional]  # noqa: E501
            origin_status_416 (int): Number of responses received from origin with status code 416 (Range Not Satisfiable).. [optional]  # noqa: E501
            origin_status_429 (int): Number of responses received from origin with status code 429 (Too Many Requests).. [optional]  # noqa: E501
            origin_status_500 (int): Number of responses received from origin with status code 500 (Internal Server Error).. [optional]  # noqa: E501
            origin_status_501 (int): Number of responses received from origin with status code 501 (Not Implemented).. [optional]  # noqa: E501
            origin_status_502 (int): Number of responses received from origin with status code 502 (Bad Gateway).. [optional]  # noqa: E501
            origin_status_503 (int): Number of responses received from origin with status code 503 (Service Unavailable).. [optional]  # noqa: E501
            origin_status_504 (int): Number of responses received from origin with status code 504 (Gateway Timeout).. [optional]  # noqa: E501
            origin_status_505 (int): Number of responses received from origin with status code 505 (HTTP Version Not Supported).. [optional]  # noqa: E501
            origin_status_530 (int): Number of responses received from origin with status code 530.. [optional]  # noqa: E501
            origin_status_1xx (int): Number of \"Informational\" category status codes received from origin.. [optional]  # noqa: E501
            origin_status_2xx (int): Number of \"Success\" status codes received from origin.. [optional]  # noqa: E501
            origin_status_3xx (int): Number of \"Redirection\" codes received from origin.. [optional]  # noqa: E501
            origin_status_4xx (int): Number of \"Client Error\" codes received from origin.. [optional]  # noqa: E501
            origin_status_5xx (int): Number of \"Server Error\" codes received from origin.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Values - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            edge_requests (int): Number of requests sent by end users to Fastly.. [optional]  # noqa: E501
            edge_resp_header_bytes (int): Total header bytes delivered from Fastly to the end user.. [optional]  # noqa: E501
            edge_resp_body_bytes (int): Total body bytes delivered from Fastly to the end user.. [optional]  # noqa: E501
            status_1xx (int): Number of 1xx \"Informational\" category status codes delivered.. [optional]  # noqa: E501
            status_2xx (int): Number of 2xx \"Success\" status codes delivered.. [optional]  # noqa: E501
            status_3xx (int): Number of 3xx \"Redirection\" codes delivered.. [optional]  # noqa: E501
            status_4xx (int): Number of 4xx \"Client Error\" codes delivered.. [optional]  # noqa: E501
            status_5xx (int): Number of 5xx \"Server Error\" codes delivered.. [optional]  # noqa: E501
            status_200 (int): Number of responses delivered with status code 200 (Success).. [optional]  # noqa: E501
            status_204 (int): Number of responses delivered with status code 204 (No Content).. [optional]  # noqa: E501
            status_206 (int): Number of responses delivered with status code 206 (Partial Content).. [optional]  # noqa: E501
            status_301 (int): Number of responses delivered with status code 301 (Moved Permanently).. [optional]  # noqa: E501
            status_302 (int): Number of responses delivered with status code 302 (Found).. [optional]  # noqa: E501
            status_304 (int): Number of responses delivered with status code 304 (Not Modified).. [optional]  # noqa: E501
            status_400 (int): Number of responses delivered with status code 400 (Bad Request).. [optional]  # noqa: E501
            status_401 (int): Number of responses delivered with status code 401 (Unauthorized).. [optional]  # noqa: E501
            status_403 (int): Number of responses delivered with status code 403 (Forbidden).. [optional]  # noqa: E501
            status_404 (int): Number of responses delivered with status code 404 (Not Found).. [optional]  # noqa: E501
            status_416 (int): Number of responses delivered with status code 416 (Range Not Satisfiable).. [optional]  # noqa: E501
            status_429 (int): Number of responses delivered with status code 429 (Too Many Requests).. [optional]  # noqa: E501
            status_500 (int): Number of responses delivered with status code 500 (Internal Server Error).. [optional]  # noqa: E501
            status_501 (int): Number of responses delivered with status code 501 (Not Implemented).. [optional]  # noqa: E501
            status_502 (int): Number of responses delivered with status code 502 (Bad Gateway).. [optional]  # noqa: E501
            status_503 (int): Number of responses delivered with status code 503 (Service Unavailable).. [optional]  # noqa: E501
            status_504 (int): Number of responses delivered with status code 504 (Gateway Timeout).. [optional]  # noqa: E501
            status_505 (int): Number of responses delivered with status code 505 (HTTP Version Not Supported).. [optional]  # noqa: E501
            status_530 (int): Number of responses delivered with status code 530.. [optional]  # noqa: E501
            requests (int): Number of requests processed.. [optional]  # noqa: E501
            resp_header_bytes (int): Total header bytes delivered.. [optional]  # noqa: E501
            resp_body_bytes (int): Total body bytes delivered.. [optional]  # noqa: E501
            bereq_header_bytes (int): Total header bytes sent to origin.. [optional]  # noqa: E501
            bereq_body_bytes (int): Total body bytes sent to origin.. [optional]  # noqa: E501
            edge_hit_requests (int): Number of requests sent by end users to Fastly that resulted in a hit at the edge.. [optional]  # noqa: E501
            edge_miss_requests (int): Number of requests sent by end users to Fastly that resulted in a miss at the edge.. [optional]  # noqa: E501
            origin_fetches (int): Number of requests sent to origin.. [optional]  # noqa: E501
            origin_fetch_resp_header_bytes (int): Total header bytes received from origin.. [optional]  # noqa: E501
            origin_fetch_resp_body_bytes (int): Total body bytes received from origin.. [optional]  # noqa: E501
            bandwidth (int): Total bytes delivered (`resp_header_bytes` + `resp_body_bytes` + `bereq_header_bytes` + `bereq_body_bytes`).. [optional]  # noqa: E501
            edge_hit_ratio (float): Ratio of cache hits to cache misses at the edge, between 0 and 1 (`edge_hit_requests` / (`edge_hit_requests` + `edge_miss_requests`)).. [optional]  # noqa: E501
            origin_offload (float): Origin Offload measures the ratio of bytes served to end users that were cached by Fastly, over the bytes served to end users, between 0 and 1. ((`edge_resp_body_bytes` + `edge_resp_header_bytes`) - (`origin_fetch_resp_body_bytes` + `origin_fetch_resp_header_bytes`)) / (`edge_resp_body_bytes` + `edge_resp_header_bytes`). Previously, Origin Offload used a different formula. [Learn more](https://www.fastly.com/documentation/reference/changes/2024/06/add-origin_offload-metric).. [optional]  # noqa: E501
            origin_status_200 (int): Number of responses received from origin with status code 200 (Success).. [optional]  # noqa: E501
            origin_status_204 (int): Number of responses received from origin with status code 204 (No Content).. [optional]  # noqa: E501
            origin_status_206 (int): Number of responses received from origin with status code 206 (Partial Content).. [optional]  # noqa: E501
            origin_status_301 (int): Number of responses received from origin with status code 301 (Moved Permanently).. [optional]  # noqa: E501
            origin_status_302 (int): Number of responses received from origin with status code 302 (Found).. [optional]  # noqa: E501
            origin_status_304 (int): Number of responses received from origin with status code 304 (Not Modified).. [optional]  # noqa: E501
            origin_status_400 (int): Number of responses received from origin with status code 400 (Bad Request).. [optional]  # noqa: E501
            origin_status_401 (int): Number of responses received from origin with status code 401 (Unauthorized).. [optional]  # noqa: E501
            origin_status_403 (int): Number of responses received from origin with status code 403 (Forbidden).. [optional]  # noqa: E501
            origin_status_404 (int): Number of responses received from origin with status code 404 (Not Found).. [optional]  # noqa: E501
            origin_status_416 (int): Number of responses received from origin with status code 416 (Range Not Satisfiable).. [optional]  # noqa: E501
            origin_status_429 (int): Number of responses received from origin with status code 429 (Too Many Requests).. [optional]  # noqa: E501
            origin_status_500 (int): Number of responses received from origin with status code 500 (Internal Server Error).. [optional]  # noqa: E501
            origin_status_501 (int): Number of responses received from origin with status code 501 (Not Implemented).. [optional]  # noqa: E501
            origin_status_502 (int): Number of responses received from origin with status code 502 (Bad Gateway).. [optional]  # noqa: E501
            origin_status_503 (int): Number of responses received from origin with status code 503 (Service Unavailable).. [optional]  # noqa: E501
            origin_status_504 (int): Number of responses received from origin with status code 504 (Gateway Timeout).. [optional]  # noqa: E501
            origin_status_505 (int): Number of responses received from origin with status code 505 (HTTP Version Not Supported).. [optional]  # noqa: E501
            origin_status_530 (int): Number of responses received from origin with status code 530.. [optional]  # noqa: E501
            origin_status_1xx (int): Number of \"Informational\" category status codes received from origin.. [optional]  # noqa: E501
            origin_status_2xx (int): Number of \"Success\" status codes received from origin.. [optional]  # noqa: E501
            origin_status_3xx (int): Number of \"Redirection\" codes received from origin.. [optional]  # noqa: E501
            origin_status_4xx (int): Number of \"Client Error\" codes received from origin.. [optional]  # noqa: E501
            origin_status_5xx (int): Number of \"Server Error\" codes received from origin.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
