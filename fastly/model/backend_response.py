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
    from fastly.model.backend import Backend
    from fastly.model.backend_response_all_of import BackendResponseAllOf
    from fastly.model.service_id_and_version import ServiceIdAndVersion
    from fastly.model.timestamps import Timestamps
    globals()['Backend'] = Backend
    globals()['BackendResponseAllOf'] = BackendResponseAllOf
    globals()['ServiceIdAndVersion'] = ServiceIdAndVersion
    globals()['Timestamps'] = Timestamps


class BackendResponse(ModelComposed):
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
            'address': (str,),  # noqa: E501
            'auto_loadbalance': (bool,),  # noqa: E501
            'between_bytes_timeout': (int,),  # noqa: E501
            'client_cert': (str, none_type,),  # noqa: E501
            'comment': (str, none_type,),  # noqa: E501
            'connect_timeout': (int,),  # noqa: E501
            'first_byte_timeout': (int,),  # noqa: E501
            'healthcheck': (str, none_type,),  # noqa: E501
            'hostname': (str, none_type,),  # noqa: E501
            'ipv4': (str, none_type,),  # noqa: E501
            'ipv6': (str, none_type,),  # noqa: E501
            'keepalive_time': (int, none_type,),  # noqa: E501
            'max_conn': (int,),  # noqa: E501
            'max_tls_version': (str, none_type,),  # noqa: E501
            'min_tls_version': (str, none_type,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'override_host': (str, none_type,),  # noqa: E501
            'port': (int,),  # noqa: E501
            'request_condition': (str,),  # noqa: E501
            'shield': (str, none_type,),  # noqa: E501
            'ssl_ca_cert': (str, none_type,),  # noqa: E501
            'ssl_cert_hostname': (str, none_type,),  # noqa: E501
            'ssl_check_cert': (bool,),  # noqa: E501
            'ssl_ciphers': (str, none_type,),  # noqa: E501
            'ssl_client_cert': (str, none_type,),  # noqa: E501
            'ssl_client_key': (str, none_type,),  # noqa: E501
            'ssl_hostname': (str, none_type,),  # noqa: E501
            'ssl_sni_hostname': (str, none_type,),  # noqa: E501
            'use_ssl': (bool,),  # noqa: E501
            'weight': (int,),  # noqa: E501
            'created_at': (datetime, none_type,),  # noqa: E501
            'deleted_at': (datetime, none_type,),  # noqa: E501
            'updated_at': (datetime, none_type,),  # noqa: E501
            'service_id': (str,),  # noqa: E501
            'version': (int,),  # noqa: E501
            'locked': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'address': 'address',  # noqa: E501
        'auto_loadbalance': 'auto_loadbalance',  # noqa: E501
        'between_bytes_timeout': 'between_bytes_timeout',  # noqa: E501
        'client_cert': 'client_cert',  # noqa: E501
        'comment': 'comment',  # noqa: E501
        'connect_timeout': 'connect_timeout',  # noqa: E501
        'first_byte_timeout': 'first_byte_timeout',  # noqa: E501
        'healthcheck': 'healthcheck',  # noqa: E501
        'hostname': 'hostname',  # noqa: E501
        'ipv4': 'ipv4',  # noqa: E501
        'ipv6': 'ipv6',  # noqa: E501
        'keepalive_time': 'keepalive_time',  # noqa: E501
        'max_conn': 'max_conn',  # noqa: E501
        'max_tls_version': 'max_tls_version',  # noqa: E501
        'min_tls_version': 'min_tls_version',  # noqa: E501
        'name': 'name',  # noqa: E501
        'override_host': 'override_host',  # noqa: E501
        'port': 'port',  # noqa: E501
        'request_condition': 'request_condition',  # noqa: E501
        'shield': 'shield',  # noqa: E501
        'ssl_ca_cert': 'ssl_ca_cert',  # noqa: E501
        'ssl_cert_hostname': 'ssl_cert_hostname',  # noqa: E501
        'ssl_check_cert': 'ssl_check_cert',  # noqa: E501
        'ssl_ciphers': 'ssl_ciphers',  # noqa: E501
        'ssl_client_cert': 'ssl_client_cert',  # noqa: E501
        'ssl_client_key': 'ssl_client_key',  # noqa: E501
        'ssl_hostname': 'ssl_hostname',  # noqa: E501
        'ssl_sni_hostname': 'ssl_sni_hostname',  # noqa: E501
        'use_ssl': 'use_ssl',  # noqa: E501
        'weight': 'weight',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'deleted_at': 'deleted_at',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'service_id': 'service_id',  # noqa: E501
        'version': 'version',  # noqa: E501
        'locked': 'locked',  # noqa: E501
    }

    read_only_vars = {
        'created_at',  # noqa: E501
        'deleted_at',  # noqa: E501
        'updated_at',  # noqa: E501
        'service_id',  # noqa: E501
        'version',  # noqa: E501
        'locked',  # noqa: E501
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """BackendResponse - a model defined in OpenAPI

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
            address (str): A hostname, IPv4, or IPv6 address for the backend. This is the preferred way to specify the location of your backend.. [optional]  # noqa: E501
            auto_loadbalance (bool): Whether or not this backend should be automatically load balanced. If true, all backends with this setting that don't have a `request_condition` will be selected based on their `weight`.. [optional]  # noqa: E501
            between_bytes_timeout (int): Maximum duration in milliseconds that Fastly will wait while receiving no data on a download from a backend. If exceeded, the response received so far will be considered complete and the fetch will end. May be set at runtime using `bereq.between_bytes_timeout`.. [optional]  # noqa: E501
            client_cert (str, none_type): Unused.. [optional]  # noqa: E501
            comment (str, none_type): A freeform descriptive note.. [optional]  # noqa: E501
            connect_timeout (int): Maximum duration in milliseconds to wait for a connection to this backend to be established. If exceeded, the connection is aborted and a synthethic `503` response will be presented instead. May be set at runtime using `bereq.connect_timeout`.. [optional]  # noqa: E501
            first_byte_timeout (int): Maximum duration in milliseconds to wait for the server response to begin after a TCP connection is established and the request has been sent. If exceeded, the connection is aborted and a synthethic `503` response will be presented instead. May be set at runtime using `bereq.first_byte_timeout`.. [optional]  # noqa: E501
            healthcheck (str, none_type): The name of the healthcheck to use with this backend.. [optional]  # noqa: E501
            hostname (str, none_type): The hostname of the backend. May be used as an alternative to `address` to set the backend location.. [optional]  # noqa: E501
            ipv4 (str, none_type): IPv4 address of the backend. May be used as an alternative to `address` to set the backend location.. [optional]  # noqa: E501
            ipv6 (str, none_type): IPv6 address of the backend. May be used as an alternative to `address` to set the backend location.. [optional]  # noqa: E501
            keepalive_time (int, none_type): How long to keep a persistent connection to the backend between requests.. [optional]  # noqa: E501
            max_conn (int): Maximum number of concurrent connections this backend will accept.. [optional]  # noqa: E501
            max_tls_version (str, none_type): Maximum allowed TLS version on SSL connections to this backend. If your backend server is not able to negotiate a connection meeting this constraint, a synthetic `503` error response will be generated.. [optional]  # noqa: E501
            min_tls_version (str, none_type): Minimum allowed TLS version on SSL connections to this backend. If your backend server is not able to negotiate a connection meeting this constraint, a synthetic `503` error response will be generated.. [optional]  # noqa: E501
            name (str): The name of the backend.. [optional]  # noqa: E501
            override_host (str, none_type): If set, will replace the client-supplied HTTP `Host` header on connections to this backend. Applied after VCL has been processed, so this setting will take precedence over changing `bereq.http.Host` in VCL.. [optional]  # noqa: E501
            port (int): Port on which the backend server is listening for connections from Fastly. Setting `port` to 80 or 443 will also set `use_ssl` automatically (to false and true respectively), unless explicitly overridden by setting `use_ssl` in the same request.. [optional]  # noqa: E501
            request_condition (str): Name of a Condition, which if satisfied, will select this backend during a request. If set, will override any `auto_loadbalance` setting. By default, the first backend added to a service is selected for all requests.. [optional]  # noqa: E501
            shield (str, none_type): Identifier of the POP to use as a [shield](https://docs.fastly.com/en/guides/shielding).. [optional]  # noqa: E501
            ssl_ca_cert (str, none_type): CA certificate attached to origin.. [optional]  # noqa: E501
            ssl_cert_hostname (str, none_type): Overrides `ssl_hostname`, but only for cert verification. Does not affect SNI at all.. [optional]  # noqa: E501
            ssl_check_cert (bool): Be strict on checking SSL certs.. [optional] if omitted the server will use the default value of True  # noqa: E501
            ssl_ciphers (str, none_type): List of [OpenSSL ciphers](https://www.openssl.org/docs/manmaster/man1/ciphers.html) to support for connections to this origin. If your backend server is not able to negotiate a connection meeting this constraint, a synthetic `503` error response will be generated.. [optional]  # noqa: E501
            ssl_client_cert (str, none_type): Client certificate attached to origin.. [optional]  # noqa: E501
            ssl_client_key (str, none_type): Client key attached to origin.. [optional]  # noqa: E501
            ssl_hostname (str, none_type): Use `ssl_cert_hostname` and `ssl_sni_hostname` to configure certificate validation.. [optional]  # noqa: E501
            ssl_sni_hostname (str, none_type): Overrides `ssl_hostname`, but only for SNI in the handshake. Does not affect cert validation at all.. [optional]  # noqa: E501
            use_ssl (bool): Whether or not to require TLS for connections to this backend.. [optional]  # noqa: E501
            weight (int): Weight used to load balance this backend against others. May be any positive integer. If `auto_loadbalance` is true, the chance of this backend being selected is equal to its own weight over the sum of all weights for backends that have `auto_loadbalance` set to true.. [optional]  # noqa: E501
            created_at (datetime, none_type): Date and time in ISO 8601 format.. [optional]  # noqa: E501
            deleted_at (datetime, none_type): Date and time in ISO 8601 format.. [optional]  # noqa: E501
            updated_at (datetime, none_type): Date and time in ISO 8601 format.. [optional]  # noqa: E501
            service_id (str): [optional]  # noqa: E501
            version (int): [optional]  # noqa: E501
            locked (bool): Indicates whether the version of the service this backend is attached to accepts edits.. [optional]  # noqa: E501
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
        """BackendResponse - a model defined in OpenAPI

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
            address (str): A hostname, IPv4, or IPv6 address for the backend. This is the preferred way to specify the location of your backend.. [optional]  # noqa: E501
            auto_loadbalance (bool): Whether or not this backend should be automatically load balanced. If true, all backends with this setting that don't have a `request_condition` will be selected based on their `weight`.. [optional]  # noqa: E501
            between_bytes_timeout (int): Maximum duration in milliseconds that Fastly will wait while receiving no data on a download from a backend. If exceeded, the response received so far will be considered complete and the fetch will end. May be set at runtime using `bereq.between_bytes_timeout`.. [optional]  # noqa: E501
            client_cert (str, none_type): Unused.. [optional]  # noqa: E501
            comment (str, none_type): A freeform descriptive note.. [optional]  # noqa: E501
            connect_timeout (int): Maximum duration in milliseconds to wait for a connection to this backend to be established. If exceeded, the connection is aborted and a synthethic `503` response will be presented instead. May be set at runtime using `bereq.connect_timeout`.. [optional]  # noqa: E501
            first_byte_timeout (int): Maximum duration in milliseconds to wait for the server response to begin after a TCP connection is established and the request has been sent. If exceeded, the connection is aborted and a synthethic `503` response will be presented instead. May be set at runtime using `bereq.first_byte_timeout`.. [optional]  # noqa: E501
            healthcheck (str, none_type): The name of the healthcheck to use with this backend.. [optional]  # noqa: E501
            hostname (str, none_type): The hostname of the backend. May be used as an alternative to `address` to set the backend location.. [optional]  # noqa: E501
            ipv4 (str, none_type): IPv4 address of the backend. May be used as an alternative to `address` to set the backend location.. [optional]  # noqa: E501
            ipv6 (str, none_type): IPv6 address of the backend. May be used as an alternative to `address` to set the backend location.. [optional]  # noqa: E501
            keepalive_time (int, none_type): How long to keep a persistent connection to the backend between requests.. [optional]  # noqa: E501
            max_conn (int): Maximum number of concurrent connections this backend will accept.. [optional]  # noqa: E501
            max_tls_version (str, none_type): Maximum allowed TLS version on SSL connections to this backend. If your backend server is not able to negotiate a connection meeting this constraint, a synthetic `503` error response will be generated.. [optional]  # noqa: E501
            min_tls_version (str, none_type): Minimum allowed TLS version on SSL connections to this backend. If your backend server is not able to negotiate a connection meeting this constraint, a synthetic `503` error response will be generated.. [optional]  # noqa: E501
            name (str): The name of the backend.. [optional]  # noqa: E501
            override_host (str, none_type): If set, will replace the client-supplied HTTP `Host` header on connections to this backend. Applied after VCL has been processed, so this setting will take precedence over changing `bereq.http.Host` in VCL.. [optional]  # noqa: E501
            port (int): Port on which the backend server is listening for connections from Fastly. Setting `port` to 80 or 443 will also set `use_ssl` automatically (to false and true respectively), unless explicitly overridden by setting `use_ssl` in the same request.. [optional]  # noqa: E501
            request_condition (str): Name of a Condition, which if satisfied, will select this backend during a request. If set, will override any `auto_loadbalance` setting. By default, the first backend added to a service is selected for all requests.. [optional]  # noqa: E501
            shield (str, none_type): Identifier of the POP to use as a [shield](https://docs.fastly.com/en/guides/shielding).. [optional]  # noqa: E501
            ssl_ca_cert (str, none_type): CA certificate attached to origin.. [optional]  # noqa: E501
            ssl_cert_hostname (str, none_type): Overrides `ssl_hostname`, but only for cert verification. Does not affect SNI at all.. [optional]  # noqa: E501
            ssl_check_cert (bool): Be strict on checking SSL certs.. [optional] if omitted the server will use the default value of True  # noqa: E501
            ssl_ciphers (str, none_type): List of [OpenSSL ciphers](https://www.openssl.org/docs/manmaster/man1/ciphers.html) to support for connections to this origin. If your backend server is not able to negotiate a connection meeting this constraint, a synthetic `503` error response will be generated.. [optional]  # noqa: E501
            ssl_client_cert (str, none_type): Client certificate attached to origin.. [optional]  # noqa: E501
            ssl_client_key (str, none_type): Client key attached to origin.. [optional]  # noqa: E501
            ssl_hostname (str, none_type): Use `ssl_cert_hostname` and `ssl_sni_hostname` to configure certificate validation.. [optional]  # noqa: E501
            ssl_sni_hostname (str, none_type): Overrides `ssl_hostname`, but only for SNI in the handshake. Does not affect cert validation at all.. [optional]  # noqa: E501
            use_ssl (bool): Whether or not to require TLS for connections to this backend.. [optional]  # noqa: E501
            weight (int): Weight used to load balance this backend against others. May be any positive integer. If `auto_loadbalance` is true, the chance of this backend being selected is equal to its own weight over the sum of all weights for backends that have `auto_loadbalance` set to true.. [optional]  # noqa: E501
            created_at (datetime, none_type): Date and time in ISO 8601 format.. [optional]  # noqa: E501
            deleted_at (datetime, none_type): Date and time in ISO 8601 format.. [optional]  # noqa: E501
            updated_at (datetime, none_type): Date and time in ISO 8601 format.. [optional]  # noqa: E501
            service_id (str): [optional]  # noqa: E501
            version (int): [optional]  # noqa: E501
            locked (bool): Indicates whether the version of the service this backend is attached to accepts edits.. [optional]  # noqa: E501
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
              Backend,
              BackendResponseAllOf,
              ServiceIdAndVersion,
              Timestamps,
          ],
          'oneOf': [
          ],
        }
