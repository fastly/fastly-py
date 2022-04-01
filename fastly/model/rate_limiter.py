"""
    Fastly API

    Via the Fastly API you can perform any of the operations that are possible within the management console,  including creating services, domains, and backends, configuring rules or uploading your own application code, as well as account operations such as user administration and billing reports. The API is organized into collections of endpoints that allow manipulation of objects related to Fastly services and accounts. For the most accurate and up-to-date API reference content, visit our [Developer Hub](https://developer.fastly.com/reference/api/)   # noqa: E501

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


def lazy_import():
    from fastly.model.rate_limiter_response1 import RateLimiterResponse1
    globals()['RateLimiterResponse1'] = RateLimiterResponse1


class RateLimiter(ModelNormal):
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
        ('http_methods',): {
            'HEAD': "HEAD",
            'OPTIONS': "OPTIONS",
            'GET': "GET",
            'POST': "POST",
            'PUT': "PUT",
            'PATCH': "PATCH",
            'DELETE': "DELETE",
            'TRACE': "TRACE",
        },
        ('window_size',): {
            'one_second': 1,
            'ten_seconds': 10,
            'one_minute': 60,
        },
        ('action',): {
            'RESPONSE': "response",
            'RESPONSE_OBJECT': "response_object",
            'LOG_ONLY': "log_only",
        },
        ('logger_type',): {
            'AZUREBLOB': "azureblob",
            'BIGQUERY': "bigquery",
            'CLOUDFILES': "cloudfiles",
            'DATADOG': "datadog",
            'DIGITALOCEAN': "digitalocean",
            'ELASTICSEARCH': "elasticsearch",
            'FTP': "ftp",
            'GCS': "gcs",
            'GOOGLEANALYTICS': "googleanalytics",
            'HEROKU': "heroku",
            'HONEYCOMB': "honeycomb",
            'HTTP': "http",
            'HTTPS': "https",
            'KAFKA': "kafka",
            'KINESIS': "kinesis",
            'LOGENTRIES': "logentries",
            'LOGGLY': "loggly",
            'LOGSHUTTLE': "logshuttle",
            'NEWRELIC': "newrelic",
            'OPENSTACK': "openstack",
            'PAPERTRAIL': "papertrail",
            'PUBSUB': "pubsub",
            'S3': "s3",
            'SCALYR': "scalyr",
            'SFTP': "sftp",
            'SPLUNK': "splunk",
            'STACKDRIVER': "stackdriver",
            'SUMOLOGIC': "sumologic",
            'SYSLOG': "syslog",
        },
    }

    validations = {
        ('name',): {
            'max_length': 255,
            'min_length': 1,
        },
        ('uri_dictionary_name',): {
            'max_length': 255,
            'min_length': 1,
        },
        ('http_methods',): {
            'min_items': 1,
        },
        ('rps_limit',): {
            'inclusive_maximum': 10000,
            'inclusive_minimum': 10,
        },
        ('client_key',): {
            'min_items': 1,
        },
        ('penalty_box_duration',): {
            'inclusive_maximum': 60,
            'inclusive_minimum': 1,
        },
        ('action',): {
            'min_length': 1,
        },
        ('response_object_name',): {
            'max_length': 255,
            'min_length': 1,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
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
        lazy_import()
        return {
            'name': (str,),  # noqa: E501
            'uri_dictionary_name': (str, none_type,),  # noqa: E501
            'http_methods': ([str],),  # noqa: E501
            'rps_limit': (int,),  # noqa: E501
            'window_size': (int,),  # noqa: E501
            'client_key': ([str],),  # noqa: E501
            'penalty_box_duration': (int,),  # noqa: E501
            'action': (str,),  # noqa: E501
            'response': (RateLimiterResponse1,),  # noqa: E501
            'response_object_name': (str, none_type,),  # noqa: E501
            'logger_type': (str,),  # noqa: E501
            'feature_revision': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'name': 'name',  # noqa: E501
        'uri_dictionary_name': 'uri_dictionary_name',  # noqa: E501
        'http_methods': 'http_methods',  # noqa: E501
        'rps_limit': 'rps_limit',  # noqa: E501
        'window_size': 'window_size',  # noqa: E501
        'client_key': 'client_key',  # noqa: E501
        'penalty_box_duration': 'penalty_box_duration',  # noqa: E501
        'action': 'action',  # noqa: E501
        'response': 'response',  # noqa: E501
        'response_object_name': 'response_object_name',  # noqa: E501
        'logger_type': 'logger_type',  # noqa: E501
        'feature_revision': 'feature_revision',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """RateLimiter - a model defined in OpenAPI

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
            name (str): A human readable name for the rate limiting rule.. [optional]  # noqa: E501
            uri_dictionary_name (str, none_type): The name of an Edge Dictionary containing URIs as keys. If not defined or `null`, all origin URIs will be rate limited.. [optional]  # noqa: E501
            http_methods ([str]): Array of HTTP methods to apply rate limiting to.. [optional]  # noqa: E501
            rps_limit (int): Upper limit of requests per second allowed by the rate limiter.. [optional]  # noqa: E501
            window_size (int): Number of seconds during which the RPS limit must be exceeded in order to trigger a violation.. [optional]  # noqa: E501
            client_key ([str]): Array of VCL variables used to generate a counter key to identify a client. Example variables include `req.http.Fastly-Client-IP`, `req.http.User-Agent`, or a custom header like `req.http.API-Key`.. [optional]  # noqa: E501
            penalty_box_duration (int): Length of time in minutes that the rate limiter is in effect after the initial violation is detected.. [optional]  # noqa: E501
            action (str): The action to take when a rate limiter violation is detected.. [optional]  # noqa: E501
            response (RateLimiterResponse1): [optional]  # noqa: E501
            response_object_name (str, none_type): Name of existing response object. Required if `action` is `response_object`. Note that the rate limiter response is only updated to reflect the response object content when saving the rate limiter configuration.. [optional]  # noqa: E501
            logger_type (str): Name of the type of logging endpoint to be used when action is `log_only`. The logging endpoint type is used to determine the appropriate log format to use when emitting log entries.. [optional]  # noqa: E501
            feature_revision (int): Revision number of the rate limiting feature implementation. Defaults to the most recent revision.. [optional]  # noqa: E501
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
        """RateLimiter - a model defined in OpenAPI

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
            name (str): A human readable name for the rate limiting rule.. [optional]  # noqa: E501
            uri_dictionary_name (str, none_type): The name of an Edge Dictionary containing URIs as keys. If not defined or `null`, all origin URIs will be rate limited.. [optional]  # noqa: E501
            http_methods ([str]): Array of HTTP methods to apply rate limiting to.. [optional]  # noqa: E501
            rps_limit (int): Upper limit of requests per second allowed by the rate limiter.. [optional]  # noqa: E501
            window_size (int): Number of seconds during which the RPS limit must be exceeded in order to trigger a violation.. [optional]  # noqa: E501
            client_key ([str]): Array of VCL variables used to generate a counter key to identify a client. Example variables include `req.http.Fastly-Client-IP`, `req.http.User-Agent`, or a custom header like `req.http.API-Key`.. [optional]  # noqa: E501
            penalty_box_duration (int): Length of time in minutes that the rate limiter is in effect after the initial violation is detected.. [optional]  # noqa: E501
            action (str): The action to take when a rate limiter violation is detected.. [optional]  # noqa: E501
            response (RateLimiterResponse1): [optional]  # noqa: E501
            response_object_name (str, none_type): Name of existing response object. Required if `action` is `response_object`. Note that the rate limiter response is only updated to reflect the response object content when saving the rate limiter configuration.. [optional]  # noqa: E501
            logger_type (str): Name of the type of logging endpoint to be used when action is `log_only`. The logging endpoint type is used to determine the appropriate log format to use when emitting log entries.. [optional]  # noqa: E501
            feature_revision (int): Revision number of the rate limiting feature implementation. Defaults to the most recent revision.. [optional]  # noqa: E501
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
