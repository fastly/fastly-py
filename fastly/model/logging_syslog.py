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
    from fastly.model.logging_address_and_port import LoggingAddressAndPort
    from fastly.model.logging_common import LoggingCommon
    from fastly.model.logging_message_type import LoggingMessageType
    from fastly.model.logging_syslog_all_of import LoggingSyslogAllOf
    from fastly.model.logging_tls_common import LoggingTlsCommon
    from fastly.model.logging_use_tls import LoggingUseTls
    globals()['LoggingAddressAndPort'] = LoggingAddressAndPort
    globals()['LoggingCommon'] = LoggingCommon
    globals()['LoggingMessageType'] = LoggingMessageType
    globals()['LoggingSyslogAllOf'] = LoggingSyslogAllOf
    globals()['LoggingTlsCommon'] = LoggingTlsCommon
    globals()['LoggingUseTls'] = LoggingUseTls


class LoggingSyslog(ModelComposed):
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
        ('placement',): {
            'None': None,
            'NONE': "none",
            'WAF_DEBUG': "waf_debug",
            'NULL': "null",
        },
        ('format_version',): {
            'v1': 1,
            'v2': 2,
        },
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
            'name': (str,),  # noqa: E501
            'placement': (str, none_type,),  # noqa: E501
            'format_version': (int,),  # noqa: E501
            'response_condition': (str, none_type,),  # noqa: E501
            'format': (str,),  # noqa: E501
            'tls_ca_cert': (str, none_type,),  # noqa: E501
            'tls_client_cert': (str, none_type,),  # noqa: E501
            'tls_client_key': (str, none_type,),  # noqa: E501
            'tls_hostname': (str, none_type,),  # noqa: E501
            'address': (str,),  # noqa: E501
            'port': (int,),  # noqa: E501
            'message_type': (LoggingMessageType,),  # noqa: E501
            'hostname': (str,),  # noqa: E501
            'ipv4': (str, none_type,),  # noqa: E501
            'token': (str, none_type,),  # noqa: E501
            'use_tls': (LoggingUseTls,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'name': 'name',  # noqa: E501
        'placement': 'placement',  # noqa: E501
        'format_version': 'format_version',  # noqa: E501
        'response_condition': 'response_condition',  # noqa: E501
        'format': 'format',  # noqa: E501
        'tls_ca_cert': 'tls_ca_cert',  # noqa: E501
        'tls_client_cert': 'tls_client_cert',  # noqa: E501
        'tls_client_key': 'tls_client_key',  # noqa: E501
        'tls_hostname': 'tls_hostname',  # noqa: E501
        'address': 'address',  # noqa: E501
        'port': 'port',  # noqa: E501
        'message_type': 'message_type',  # noqa: E501
        'hostname': 'hostname',  # noqa: E501
        'ipv4': 'ipv4',  # noqa: E501
        'token': 'token',  # noqa: E501
        'use_tls': 'use_tls',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """LoggingSyslog - a model defined in OpenAPI

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
            name (str): The name for the real-time logging configuration.. [optional]  # noqa: E501
            placement (str, none_type): Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`. . [optional]  # noqa: E501
            format_version (int): The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`. . [optional] if omitted the server will use the default value of 2  # noqa: E501
            response_condition (str, none_type): The name of an existing condition in the configured endpoint, or leave blank to always execute.. [optional]  # noqa: E501
            format (str): A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats).. [optional] if omitted the server will use the default value of "%h %l %u %t "%r" %&gt;s %b"  # noqa: E501
            tls_ca_cert (str, none_type): A secure certificate to authenticate a server with. Must be in PEM format.. [optional] if omitted the server will use the default value of "null"  # noqa: E501
            tls_client_cert (str, none_type): The client certificate used to make authenticated requests. Must be in PEM format.. [optional] if omitted the server will use the default value of "null"  # noqa: E501
            tls_client_key (str, none_type): The client private key used to make authenticated requests. Must be in PEM format.. [optional] if omitted the server will use the default value of "null"  # noqa: E501
            tls_hostname (str, none_type): The hostname to verify the server's certificate. This should be one of the Subject Alternative Name (SAN) fields for the certificate. Common Names (CN) are not supported.. [optional] if omitted the server will use the default value of "null"  # noqa: E501
            address (str): A hostname or IPv4 address.. [optional]  # noqa: E501
            port (int): The port number.. [optional] if omitted the server will use the default value of 514  # noqa: E501
            message_type (LoggingMessageType): [optional]  # noqa: E501
            hostname (str): The hostname used for the syslog endpoint.. [optional]  # noqa: E501
            ipv4 (str, none_type): The IPv4 address used for the syslog endpoint.. [optional]  # noqa: E501
            token (str, none_type): Whether to prepend each message with a specific token.. [optional] if omitted the server will use the default value of "null"  # noqa: E501
            use_tls (LoggingUseTls): [optional]  # noqa: E501
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
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
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """LoggingSyslog - a model defined in OpenAPI

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
            name (str): The name for the real-time logging configuration.. [optional]  # noqa: E501
            placement (str, none_type): Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`. . [optional]  # noqa: E501
            format_version (int): The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`. . [optional] if omitted the server will use the default value of 2  # noqa: E501
            response_condition (str, none_type): The name of an existing condition in the configured endpoint, or leave blank to always execute.. [optional]  # noqa: E501
            format (str): A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats).. [optional] if omitted the server will use the default value of "%h %l %u %t "%r" %&gt;s %b"  # noqa: E501
            tls_ca_cert (str, none_type): A secure certificate to authenticate a server with. Must be in PEM format.. [optional] if omitted the server will use the default value of "null"  # noqa: E501
            tls_client_cert (str, none_type): The client certificate used to make authenticated requests. Must be in PEM format.. [optional] if omitted the server will use the default value of "null"  # noqa: E501
            tls_client_key (str, none_type): The client private key used to make authenticated requests. Must be in PEM format.. [optional] if omitted the server will use the default value of "null"  # noqa: E501
            tls_hostname (str, none_type): The hostname to verify the server's certificate. This should be one of the Subject Alternative Name (SAN) fields for the certificate. Common Names (CN) are not supported.. [optional] if omitted the server will use the default value of "null"  # noqa: E501
            address (str): A hostname or IPv4 address.. [optional]  # noqa: E501
            port (int): The port number.. [optional] if omitted the server will use the default value of 514  # noqa: E501
            message_type (LoggingMessageType): [optional]  # noqa: E501
            hostname (str): The hostname used for the syslog endpoint.. [optional]  # noqa: E501
            ipv4 (str, none_type): The IPv4 address used for the syslog endpoint.. [optional]  # noqa: E501
            token (str, none_type): Whether to prepend each message with a specific token.. [optional] if omitted the server will use the default value of "null"  # noqa: E501
            use_tls (LoggingUseTls): [optional]  # noqa: E501
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
              LoggingAddressAndPort,
              LoggingCommon,
              LoggingSyslogAllOf,
              LoggingTlsCommon,
          ],
          'oneOf': [
          ],
        }
