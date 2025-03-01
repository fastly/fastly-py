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


def lazy_import():
    from fastly.model.log_property_service_id import LogPropertyServiceId
    globals()['LogPropertyServiceId'] = LogPropertyServiceId


class LogRecord(ModelNormal):
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
            'customer_id': (str,),  # noqa: E501
            'service_id': (LogPropertyServiceId,),  # noqa: E501
            'timestamp': (datetime,),  # noqa: E501
            'client_as_number': (int,),  # noqa: E501
            'client_region': (str,),  # noqa: E501
            'client_country_code': (str,),  # noqa: E501
            'client_os_name': (str,),  # noqa: E501
            'client_device_type': (str,),  # noqa: E501
            'client_browser_name': (str,),  # noqa: E501
            'client_browser_version': (str,),  # noqa: E501
            'fastly_pop': (str,),  # noqa: E501
            'origin_host': (str,),  # noqa: E501
            'request_protocol': (str,),  # noqa: E501
            'request_host': (str,),  # noqa: E501
            'request_path': (str,),  # noqa: E501
            'request_method': (str,),  # noqa: E501
            'response_bytes_body': (int,),  # noqa: E501
            'response_bytes_header': (int,),  # noqa: E501
            'response_content_length': (int,),  # noqa: E501
            'response_content_type': (str,),  # noqa: E501
            'response_reason': (str,),  # noqa: E501
            'response_state': (str,),  # noqa: E501
            'response_status': (int,),  # noqa: E501
            'response_time': (float,),  # noqa: E501
            'response_x_cache': (str,),  # noqa: E501
            'is_cache_hit': (bool,),  # noqa: E501
            'is_edge': (bool,),  # noqa: E501
            'is_shield': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'customer_id': 'customer_id',  # noqa: E501
        'service_id': 'service_id',  # noqa: E501
        'timestamp': 'timestamp',  # noqa: E501
        'client_as_number': 'client_as_number',  # noqa: E501
        'client_region': 'client_region',  # noqa: E501
        'client_country_code': 'client_country_code',  # noqa: E501
        'client_os_name': 'client_os_name',  # noqa: E501
        'client_device_type': 'client_device_type',  # noqa: E501
        'client_browser_name': 'client_browser_name',  # noqa: E501
        'client_browser_version': 'client_browser_version',  # noqa: E501
        'fastly_pop': 'fastly_pop',  # noqa: E501
        'origin_host': 'origin_host',  # noqa: E501
        'request_protocol': 'request_protocol',  # noqa: E501
        'request_host': 'request_host',  # noqa: E501
        'request_path': 'request_path',  # noqa: E501
        'request_method': 'request_method',  # noqa: E501
        'response_bytes_body': 'response_bytes_body',  # noqa: E501
        'response_bytes_header': 'response_bytes_header',  # noqa: E501
        'response_content_length': 'response_content_length',  # noqa: E501
        'response_content_type': 'response_content_type',  # noqa: E501
        'response_reason': 'response_reason',  # noqa: E501
        'response_state': 'response_state',  # noqa: E501
        'response_status': 'response_status',  # noqa: E501
        'response_time': 'response_time',  # noqa: E501
        'response_x_cache': 'response_x_cache',  # noqa: E501
        'is_cache_hit': 'is_cache_hit',  # noqa: E501
        'is_edge': 'is_edge',  # noqa: E501
        'is_shield': 'is_shield',  # noqa: E501
    }

    read_only_vars = {
        'customer_id',  # noqa: E501
        'client_as_number',  # noqa: E501
        'client_region',  # noqa: E501
        'client_country_code',  # noqa: E501
        'client_os_name',  # noqa: E501
        'client_device_type',  # noqa: E501
        'client_browser_name',  # noqa: E501
        'client_browser_version',  # noqa: E501
        'fastly_pop',  # noqa: E501
        'origin_host',  # noqa: E501
        'request_protocol',  # noqa: E501
        'request_host',  # noqa: E501
        'request_path',  # noqa: E501
        'request_method',  # noqa: E501
        'response_bytes_body',  # noqa: E501
        'response_bytes_header',  # noqa: E501
        'response_content_length',  # noqa: E501
        'response_content_type',  # noqa: E501
        'response_reason',  # noqa: E501
        'response_state',  # noqa: E501
        'response_status',  # noqa: E501
        'response_time',  # noqa: E501
        'response_x_cache',  # noqa: E501
        'is_cache_hit',  # noqa: E501
        'is_edge',  # noqa: E501
        'is_shield',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """LogRecord - a model defined in OpenAPI

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
            customer_id (str): The ID of the Fastly customer that owns the service.. [optional]  # noqa: E501
            service_id (LogPropertyServiceId): [optional]  # noqa: E501
            timestamp (datetime): Timestamp of the request in ISO 8601 format.. [optional]  # noqa: E501
            client_as_number (int): The autonomous system (AS) number of the client.. [optional]  # noqa: E501
            client_region (str): The client's country subdivision code as found in ISO 3166-2.. [optional]  # noqa: E501
            client_country_code (str): The two-letter ISO 3166-1 country code for the client.. [optional]  # noqa: E501
            client_os_name (str): The name of the operating system installed on the client device.. [optional]  # noqa: E501
            client_device_type (str): The type of the client's device.. [optional]  # noqa: E501
            client_browser_name (str): The name of the browser in use on the client device.. [optional]  # noqa: E501
            client_browser_version (str): The version of the browser in use on client device.. [optional]  # noqa: E501
            fastly_pop (str): The name of the Fastly POP that served this request.. [optional]  # noqa: E501
            origin_host (str): The name of the origin host that served this request.. [optional]  # noqa: E501
            request_protocol (str): HTTP protocol version in use for this request. For example, HTTP/1.1.. [optional]  # noqa: E501
            request_host (str): The name of the request host used for this request.. [optional]  # noqa: E501
            request_path (str): The URL path supplied for this request.. [optional]  # noqa: E501
            request_method (str): HTTP method sent by the client such as \"GET\" or \"POST\".. [optional]  # noqa: E501
            response_bytes_body (int): Body bytes sent to the client in the response.. [optional]  # noqa: E501
            response_bytes_header (int): Header bytes sent to the client in the response.. [optional]  # noqa: E501
            response_content_length (int): Total bytes sent to the client in the response.. [optional]  # noqa: E501
            response_content_type (str): The content type of the response sent to the client.. [optional]  # noqa: E501
            response_reason (str): The HTTP reason phrase returned for this request, if any.. [optional]  # noqa: E501
            response_state (str): The state of the request with optional suffixes describing special cases.. [optional]  # noqa: E501
            response_status (int): The HTTP response code returned for this request.. [optional]  # noqa: E501
            response_time (float): The time since the request started in seconds.. [optional]  # noqa: E501
            response_x_cache (str): Indicates whether the request was a HIT or a MISS.. [optional]  # noqa: E501
            is_cache_hit (bool): Indicates whether this request was fulfilled from cache.. [optional]  # noqa: E501
            is_edge (bool): Indicates whether the request was handled by a Fastly edge POP.. [optional]  # noqa: E501
            is_shield (bool): Indicates whether the request was handled by a Fastly shield POP.. [optional]  # noqa: E501
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
        """LogRecord - a model defined in OpenAPI

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
            customer_id (str): The ID of the Fastly customer that owns the service.. [optional]  # noqa: E501
            service_id (LogPropertyServiceId): [optional]  # noqa: E501
            timestamp (datetime): Timestamp of the request in ISO 8601 format.. [optional]  # noqa: E501
            client_as_number (int): The autonomous system (AS) number of the client.. [optional]  # noqa: E501
            client_region (str): The client's country subdivision code as found in ISO 3166-2.. [optional]  # noqa: E501
            client_country_code (str): The two-letter ISO 3166-1 country code for the client.. [optional]  # noqa: E501
            client_os_name (str): The name of the operating system installed on the client device.. [optional]  # noqa: E501
            client_device_type (str): The type of the client's device.. [optional]  # noqa: E501
            client_browser_name (str): The name of the browser in use on the client device.. [optional]  # noqa: E501
            client_browser_version (str): The version of the browser in use on client device.. [optional]  # noqa: E501
            fastly_pop (str): The name of the Fastly POP that served this request.. [optional]  # noqa: E501
            origin_host (str): The name of the origin host that served this request.. [optional]  # noqa: E501
            request_protocol (str): HTTP protocol version in use for this request. For example, HTTP/1.1.. [optional]  # noqa: E501
            request_host (str): The name of the request host used for this request.. [optional]  # noqa: E501
            request_path (str): The URL path supplied for this request.. [optional]  # noqa: E501
            request_method (str): HTTP method sent by the client such as \"GET\" or \"POST\".. [optional]  # noqa: E501
            response_bytes_body (int): Body bytes sent to the client in the response.. [optional]  # noqa: E501
            response_bytes_header (int): Header bytes sent to the client in the response.. [optional]  # noqa: E501
            response_content_length (int): Total bytes sent to the client in the response.. [optional]  # noqa: E501
            response_content_type (str): The content type of the response sent to the client.. [optional]  # noqa: E501
            response_reason (str): The HTTP reason phrase returned for this request, if any.. [optional]  # noqa: E501
            response_state (str): The state of the request with optional suffixes describing special cases.. [optional]  # noqa: E501
            response_status (int): The HTTP response code returned for this request.. [optional]  # noqa: E501
            response_time (float): The time since the request started in seconds.. [optional]  # noqa: E501
            response_x_cache (str): Indicates whether the request was a HIT or a MISS.. [optional]  # noqa: E501
            is_cache_hit (bool): Indicates whether this request was fulfilled from cache.. [optional]  # noqa: E501
            is_edge (bool): Indicates whether the request was handled by a Fastly edge POP.. [optional]  # noqa: E501
            is_shield (bool): Indicates whether the request was handled by a Fastly shield POP.. [optional]  # noqa: E501
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
