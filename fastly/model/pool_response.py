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
    from fastly.model.pool_additional import PoolAdditional
    from fastly.model.pool_response_all_of import PoolResponseAllOf
    from fastly.model.pool_response_common import PoolResponseCommon
    from fastly.model.service_id_and_version_string import ServiceIdAndVersionString
    from fastly.model.timestamps import Timestamps
    from fastly.model.tls_common_response import TlsCommonResponse
    globals()['PoolAdditional'] = PoolAdditional
    globals()['PoolResponseAllOf'] = PoolResponseAllOf
    globals()['PoolResponseCommon'] = PoolResponseCommon
    globals()['ServiceIdAndVersionString'] = ServiceIdAndVersionString
    globals()['Timestamps'] = Timestamps
    globals()['TlsCommonResponse'] = TlsCommonResponse


class PoolResponse(ModelComposed):
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
        ('use_tls',): {
            'no_tls': "0",
            'use_tls': "1",
        },
        ('type',): {
            'RANDOM': "random",
            'HASH': "hash",
            'CLIENT': "client",
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
            'tls_ca_cert': (str, none_type,),  # noqa: E501
            'tls_client_cert': (str, none_type,),  # noqa: E501
            'tls_client_key': (str, none_type,),  # noqa: E501
            'tls_cert_hostname': (str, none_type,),  # noqa: E501
            'use_tls': (str,),  # noqa: E501
            'created_at': (datetime, none_type,),  # noqa: E501
            'deleted_at': (datetime, none_type,),  # noqa: E501
            'updated_at': (datetime, none_type,),  # noqa: E501
            'service_id': (str,),  # noqa: E501
            'version': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'shield': (str, none_type,),  # noqa: E501
            'request_condition': (str, none_type,),  # noqa: E501
            'tls_ciphers': (str, none_type,),  # noqa: E501
            'tls_sni_hostname': (str, none_type,),  # noqa: E501
            'min_tls_version': (int, none_type,),  # noqa: E501
            'max_tls_version': (int, none_type,),  # noqa: E501
            'healthcheck': (str, none_type,),  # noqa: E501
            'comment': (str, none_type,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'override_host': (str, none_type,),  # noqa: E501
            'between_bytes_timeout': (str,),  # noqa: E501
            'connect_timeout': (str,),  # noqa: E501
            'first_byte_timeout': (str,),  # noqa: E501
            'max_conn_default': (str,),  # noqa: E501
            'tls_check_cert': (str, none_type,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'quorum': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'tls_ca_cert': 'tls_ca_cert',  # noqa: E501
        'tls_client_cert': 'tls_client_cert',  # noqa: E501
        'tls_client_key': 'tls_client_key',  # noqa: E501
        'tls_cert_hostname': 'tls_cert_hostname',  # noqa: E501
        'use_tls': 'use_tls',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'deleted_at': 'deleted_at',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'service_id': 'service_id',  # noqa: E501
        'version': 'version',  # noqa: E501
        'name': 'name',  # noqa: E501
        'shield': 'shield',  # noqa: E501
        'request_condition': 'request_condition',  # noqa: E501
        'tls_ciphers': 'tls_ciphers',  # noqa: E501
        'tls_sni_hostname': 'tls_sni_hostname',  # noqa: E501
        'min_tls_version': 'min_tls_version',  # noqa: E501
        'max_tls_version': 'max_tls_version',  # noqa: E501
        'healthcheck': 'healthcheck',  # noqa: E501
        'comment': 'comment',  # noqa: E501
        'type': 'type',  # noqa: E501
        'override_host': 'override_host',  # noqa: E501
        'between_bytes_timeout': 'between_bytes_timeout',  # noqa: E501
        'connect_timeout': 'connect_timeout',  # noqa: E501
        'first_byte_timeout': 'first_byte_timeout',  # noqa: E501
        'max_conn_default': 'max_conn_default',  # noqa: E501
        'tls_check_cert': 'tls_check_cert',  # noqa: E501
        'id': 'id',  # noqa: E501
        'quorum': 'quorum',  # noqa: E501
    }

    read_only_vars = {
        'created_at',  # noqa: E501
        'deleted_at',  # noqa: E501
        'updated_at',  # noqa: E501
        'service_id',  # noqa: E501
        'version',  # noqa: E501
        'id',  # noqa: E501
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """PoolResponse - a model defined in OpenAPI

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
            tls_ca_cert (str, none_type): A secure certificate to authenticate a server with. Must be in PEM format.. [optional] if omitted the server will use the default value of "null"  # noqa: E501
            tls_client_cert (str, none_type): The client certificate used to make authenticated requests. Must be in PEM format.. [optional] if omitted the server will use the default value of "null"  # noqa: E501
            tls_client_key (str, none_type): The client private key used to make authenticated requests. Must be in PEM format.. [optional] if omitted the server will use the default value of "null"  # noqa: E501
            tls_cert_hostname (str, none_type): The hostname used to verify a server's certificate. It can either be the Common Name (CN) or a Subject Alternative Name (SAN).. [optional] if omitted the server will use the default value of "null"  # noqa: E501
            use_tls (str): Whether to use TLS.. [optional] if omitted the server will use the default value of "0"  # noqa: E501
            created_at (datetime, none_type): Date and time in ISO 8601 format.. [optional]  # noqa: E501
            deleted_at (datetime, none_type): Date and time in ISO 8601 format.. [optional]  # noqa: E501
            updated_at (datetime, none_type): Date and time in ISO 8601 format.. [optional]  # noqa: E501
            service_id (str): [optional]  # noqa: E501
            version (str): [optional]  # noqa: E501
            name (str): Name for the Pool.. [optional]  # noqa: E501
            shield (str, none_type): Selected POP to serve as a shield for the servers. Defaults to `null` meaning no origin shielding if not set. Refer to the [POPs API endpoint](/reference/api/utils/pops/) to get a list of available POPs used for shielding.. [optional] if omitted the server will use the default value of "null"  # noqa: E501
            request_condition (str, none_type): Condition which, if met, will select this configuration during a request. Optional.. [optional]  # noqa: E501
            tls_ciphers (str, none_type): List of OpenSSL ciphers (see the [openssl.org manpages](https://www.openssl.org/docs/man1.1.1/man1/ciphers.html) for details). Optional.. [optional]  # noqa: E501
            tls_sni_hostname (str, none_type): SNI hostname. Optional.. [optional]  # noqa: E501
            min_tls_version (int, none_type): Minimum allowed TLS version on connections to this server. Optional.. [optional]  # noqa: E501
            max_tls_version (int, none_type): Maximum allowed TLS version on connections to this server. Optional.. [optional]  # noqa: E501
            healthcheck (str, none_type): Name of the healthcheck to use with this pool. Can be empty and could be reused across multiple backend and pools.. [optional]  # noqa: E501
            comment (str, none_type): A freeform descriptive note.. [optional]  # noqa: E501
            type (str): What type of load balance group to use.. [optional]  # noqa: E501
            override_host (str, none_type): The hostname to [override the Host header](https://docs.fastly.com/en/guides/specifying-an-override-host). Defaults to `null` meaning no override of the Host header will occur. This setting can also be added to a Server definition. If the field is set on a Server definition it will override the Pool setting.. [optional] if omitted the server will use the default value of "null"  # noqa: E501
            between_bytes_timeout (str): Maximum duration in milliseconds that Fastly will wait while receiving no data on a download from a backend. If exceeded, the response received so far will be considered complete and the fetch will end. May be set at runtime using `bereq.between_bytes_timeout`.. [optional]  # noqa: E501
            connect_timeout (str): How long to wait for a timeout in milliseconds.. [optional]  # noqa: E501
            first_byte_timeout (str): How long to wait for the first byte in milliseconds.. [optional]  # noqa: E501
            max_conn_default (str): Maximum number of connections.. [optional] if omitted the server will use the default value of "200"  # noqa: E501
            tls_check_cert (str, none_type): Be strict on checking TLS certs.. [optional]  # noqa: E501
            id (str): [optional]  # noqa: E501
            quorum (str): Percentage of capacity (`0-100`) that needs to be operationally available for a pool to be considered up.. [optional] if omitted the server will use the default value of "75"  # noqa: E501
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
        """PoolResponse - a model defined in OpenAPI

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
            tls_ca_cert (str, none_type): A secure certificate to authenticate a server with. Must be in PEM format.. [optional] if omitted the server will use the default value of "null"  # noqa: E501
            tls_client_cert (str, none_type): The client certificate used to make authenticated requests. Must be in PEM format.. [optional] if omitted the server will use the default value of "null"  # noqa: E501
            tls_client_key (str, none_type): The client private key used to make authenticated requests. Must be in PEM format.. [optional] if omitted the server will use the default value of "null"  # noqa: E501
            tls_cert_hostname (str, none_type): The hostname used to verify a server's certificate. It can either be the Common Name (CN) or a Subject Alternative Name (SAN).. [optional] if omitted the server will use the default value of "null"  # noqa: E501
            use_tls (str): Whether to use TLS.. [optional] if omitted the server will use the default value of "0"  # noqa: E501
            created_at (datetime, none_type): Date and time in ISO 8601 format.. [optional]  # noqa: E501
            deleted_at (datetime, none_type): Date and time in ISO 8601 format.. [optional]  # noqa: E501
            updated_at (datetime, none_type): Date and time in ISO 8601 format.. [optional]  # noqa: E501
            service_id (str): [optional]  # noqa: E501
            version (str): [optional]  # noqa: E501
            name (str): Name for the Pool.. [optional]  # noqa: E501
            shield (str, none_type): Selected POP to serve as a shield for the servers. Defaults to `null` meaning no origin shielding if not set. Refer to the [POPs API endpoint](/reference/api/utils/pops/) to get a list of available POPs used for shielding.. [optional] if omitted the server will use the default value of "null"  # noqa: E501
            request_condition (str, none_type): Condition which, if met, will select this configuration during a request. Optional.. [optional]  # noqa: E501
            tls_ciphers (str, none_type): List of OpenSSL ciphers (see the [openssl.org manpages](https://www.openssl.org/docs/man1.1.1/man1/ciphers.html) for details). Optional.. [optional]  # noqa: E501
            tls_sni_hostname (str, none_type): SNI hostname. Optional.. [optional]  # noqa: E501
            min_tls_version (int, none_type): Minimum allowed TLS version on connections to this server. Optional.. [optional]  # noqa: E501
            max_tls_version (int, none_type): Maximum allowed TLS version on connections to this server. Optional.. [optional]  # noqa: E501
            healthcheck (str, none_type): Name of the healthcheck to use with this pool. Can be empty and could be reused across multiple backend and pools.. [optional]  # noqa: E501
            comment (str, none_type): A freeform descriptive note.. [optional]  # noqa: E501
            type (str): What type of load balance group to use.. [optional]  # noqa: E501
            override_host (str, none_type): The hostname to [override the Host header](https://docs.fastly.com/en/guides/specifying-an-override-host). Defaults to `null` meaning no override of the Host header will occur. This setting can also be added to a Server definition. If the field is set on a Server definition it will override the Pool setting.. [optional] if omitted the server will use the default value of "null"  # noqa: E501
            between_bytes_timeout (str): Maximum duration in milliseconds that Fastly will wait while receiving no data on a download from a backend. If exceeded, the response received so far will be considered complete and the fetch will end. May be set at runtime using `bereq.between_bytes_timeout`.. [optional]  # noqa: E501
            connect_timeout (str): How long to wait for a timeout in milliseconds.. [optional]  # noqa: E501
            first_byte_timeout (str): How long to wait for the first byte in milliseconds.. [optional]  # noqa: E501
            max_conn_default (str): Maximum number of connections.. [optional] if omitted the server will use the default value of "200"  # noqa: E501
            tls_check_cert (str, none_type): Be strict on checking TLS certs.. [optional]  # noqa: E501
            id (str): [optional]  # noqa: E501
            quorum (str): Percentage of capacity (`0-100`) that needs to be operationally available for a pool to be considered up.. [optional] if omitted the server will use the default value of "75"  # noqa: E501
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
              PoolAdditional,
              PoolResponseAllOf,
              PoolResponseCommon,
              ServiceIdAndVersionString,
              Timestamps,
              TlsCommonResponse,
          ],
          'oneOf': [
          ],
        }
