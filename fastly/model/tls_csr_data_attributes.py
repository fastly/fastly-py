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



class TlsCsrDataAttributes(ModelNormal):
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
        ('key_type',): {
            'RSA2048': "RSA2048",
            'ECDSA256': "ECDSA256",
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
            'sans': ([str],),  # noqa: E501
            'common_name': (str,),  # noqa: E501
            'country': (str,),  # noqa: E501
            'state': (str,),  # noqa: E501
            'city': (str,),  # noqa: E501
            'postal_code': (str,),  # noqa: E501
            'street_address': (str,),  # noqa: E501
            'organization': (str,),  # noqa: E501
            'organizational_unit': (str,),  # noqa: E501
            'email': (str,),  # noqa: E501
            'key_type': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'sans': 'sans',  # noqa: E501
        'common_name': 'common_name',  # noqa: E501
        'country': 'country',  # noqa: E501
        'state': 'state',  # noqa: E501
        'city': 'city',  # noqa: E501
        'postal_code': 'postal_code',  # noqa: E501
        'street_address': 'street_address',  # noqa: E501
        'organization': 'organization',  # noqa: E501
        'organizational_unit': 'organizational_unit',  # noqa: E501
        'email': 'email',  # noqa: E501
        'key_type': 'key_type',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, sans, *args, **kwargs):  # noqa: E501
        """TlsCsrDataAttributes - a model defined in OpenAPI

        Args:
            sans ([str]): Subject Alternate Names - An array of one or more fully qualified domain names or public IP addresses to be secured by this certificate. Required.

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
            common_name (str): Common Name (CN) - The fully qualified domain name (FQDN) to be secured by this certificate. The common name should be one of the entries in the SANs parameter.. [optional]  # noqa: E501
            country (str): Country (C) - The two-letter ISO country code where the organization is located.. [optional]  # noqa: E501
            state (str): State (S) - The state, province, region, or county where the organization is located. This should not be abbreviated.. [optional]  # noqa: E501
            city (str): Locality (L) - The locality, city, town, or village where the organization is located.. [optional]  # noqa: E501
            postal_code (str): Postal Code - The postal code where the organization is located.. [optional]  # noqa: E501
            street_address (str): Street Address - The street address where the organization is located.. [optional]  # noqa: E501
            organization (str): Organization (O) - The legal name of the organization, including any suffixes. This should not be abbreviated.. [optional]  # noqa: E501
            organizational_unit (str): Organizational Unit (OU) - The internal division of the organization managing the certificate.. [optional]  # noqa: E501
            email (str): Email Address (EMAIL) - The organizational contact for this.. [optional]  # noqa: E501
            key_type (str): CSR Key Type.. [optional]  # noqa: E501
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

        self.sans = sans
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
    def __init__(self, sans, *args, **kwargs):  # noqa: E501
        """TlsCsrDataAttributes - a model defined in OpenAPI

        Args:
            sans ([str]): Subject Alternate Names - An array of one or more fully qualified domain names or public IP addresses to be secured by this certificate. Required.

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
            common_name (str): Common Name (CN) - The fully qualified domain name (FQDN) to be secured by this certificate. The common name should be one of the entries in the SANs parameter.. [optional]  # noqa: E501
            country (str): Country (C) - The two-letter ISO country code where the organization is located.. [optional]  # noqa: E501
            state (str): State (S) - The state, province, region, or county where the organization is located. This should not be abbreviated.. [optional]  # noqa: E501
            city (str): Locality (L) - The locality, city, town, or village where the organization is located.. [optional]  # noqa: E501
            postal_code (str): Postal Code - The postal code where the organization is located.. [optional]  # noqa: E501
            street_address (str): Street Address - The street address where the organization is located.. [optional]  # noqa: E501
            organization (str): Organization (O) - The legal name of the organization, including any suffixes. This should not be abbreviated.. [optional]  # noqa: E501
            organizational_unit (str): Organizational Unit (OU) - The internal division of the organization managing the certificate.. [optional]  # noqa: E501
            email (str): Email Address (EMAIL) - The organizational contact for this.. [optional]  # noqa: E501
            key_type (str): CSR Key Type.. [optional]  # noqa: E501
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

        self.sans = sans
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
