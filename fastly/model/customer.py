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



class Customer(ModelNormal):
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
        ('billing_network_type',): {
            'PUBLIC': "public",
            'PRIVATE': "private",
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
            'billing_contact_id': (str, none_type,),  # noqa: E501
            'billing_network_type': (str,),  # noqa: E501
            'billing_ref': (str, none_type,),  # noqa: E501
            'can_configure_wordpress': (bool, none_type,),  # noqa: E501
            'can_reset_passwords': (bool,),  # noqa: E501
            'can_upload_vcl': (bool,),  # noqa: E501
            'force_2fa': (bool,),  # noqa: E501
            'force_sso': (bool,),  # noqa: E501
            'has_account_panel': (bool,),  # noqa: E501
            'has_improved_events': (bool,),  # noqa: E501
            'has_improved_ssl_config': (bool,),  # noqa: E501
            'has_openstack_logging': (bool,),  # noqa: E501
            'has_pci': (bool,),  # noqa: E501
            'has_pci_passwords': (bool,),  # noqa: E501
            'ip_whitelist': (str,),  # noqa: E501
            'legal_contact_id': (str, none_type,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'owner_id': (str,),  # noqa: E501
            'phone_number': (str,),  # noqa: E501
            'postal_address': (str, none_type,),  # noqa: E501
            'pricing_plan': (str,),  # noqa: E501
            'pricing_plan_id': (str,),  # noqa: E501
            'security_contact_id': (str, none_type,),  # noqa: E501
            'technical_contact_id': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'billing_contact_id': 'billing_contact_id',  # noqa: E501
        'billing_network_type': 'billing_network_type',  # noqa: E501
        'billing_ref': 'billing_ref',  # noqa: E501
        'can_configure_wordpress': 'can_configure_wordpress',  # noqa: E501
        'can_reset_passwords': 'can_reset_passwords',  # noqa: E501
        'can_upload_vcl': 'can_upload_vcl',  # noqa: E501
        'force_2fa': 'force_2fa',  # noqa: E501
        'force_sso': 'force_sso',  # noqa: E501
        'has_account_panel': 'has_account_panel',  # noqa: E501
        'has_improved_events': 'has_improved_events',  # noqa: E501
        'has_improved_ssl_config': 'has_improved_ssl_config',  # noqa: E501
        'has_openstack_logging': 'has_openstack_logging',  # noqa: E501
        'has_pci': 'has_pci',  # noqa: E501
        'has_pci_passwords': 'has_pci_passwords',  # noqa: E501
        'ip_whitelist': 'ip_whitelist',  # noqa: E501
        'legal_contact_id': 'legal_contact_id',  # noqa: E501
        'name': 'name',  # noqa: E501
        'owner_id': 'owner_id',  # noqa: E501
        'phone_number': 'phone_number',  # noqa: E501
        'postal_address': 'postal_address',  # noqa: E501
        'pricing_plan': 'pricing_plan',  # noqa: E501
        'pricing_plan_id': 'pricing_plan_id',  # noqa: E501
        'security_contact_id': 'security_contact_id',  # noqa: E501
        'technical_contact_id': 'technical_contact_id',  # noqa: E501
    }

    read_only_vars = {
        'can_configure_wordpress',  # noqa: E501
        'can_reset_passwords',  # noqa: E501
        'can_upload_vcl',  # noqa: E501
        'has_improved_ssl_config',  # noqa: E501
        'has_pci_passwords',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Customer - a model defined in OpenAPI

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
            billing_contact_id (str, none_type): The alphanumeric string representing the primary billing contact.. [optional]  # noqa: E501
            billing_network_type (str): Customer's current network revenue type.. [optional]  # noqa: E501
            billing_ref (str, none_type): Used for adding purchased orders to customer's account.. [optional]  # noqa: E501
            can_configure_wordpress (bool, none_type): Whether this customer can view or edit wordpress.. [optional]  # noqa: E501
            can_reset_passwords (bool): Whether this customer can reset passwords.. [optional]  # noqa: E501
            can_upload_vcl (bool): Whether this customer can upload VCL.. [optional]  # noqa: E501
            force_2fa (bool): Specifies whether 2FA is forced or not forced on the customer account. Logs out non-2FA users once 2FA is force enabled.. [optional]  # noqa: E501
            force_sso (bool): Specifies whether SSO is forced or not forced on the customer account.. [optional]  # noqa: E501
            has_account_panel (bool): Specifies whether the account has access or does not have access to the account panel.. [optional]  # noqa: E501
            has_improved_events (bool): Specifies whether the account has access or does not have access to the improved events.. [optional]  # noqa: E501
            has_improved_ssl_config (bool): Whether this customer can view or edit the SSL config.. [optional]  # noqa: E501
            has_openstack_logging (bool): Specifies whether the account has enabled or not enabled openstack logging.. [optional]  # noqa: E501
            has_pci (bool): Specifies whether the account can edit PCI for a service.. [optional]  # noqa: E501
            has_pci_passwords (bool): Specifies whether PCI passwords are required for the account.. [optional]  # noqa: E501
            ip_whitelist (str): The range of IP addresses authorized to access the customer account.. [optional]  # noqa: E501
            legal_contact_id (str, none_type): The alphanumeric string identifying the account's legal contact.. [optional]  # noqa: E501
            name (str): The name of the customer, generally the company name.. [optional]  # noqa: E501
            owner_id (str): The alphanumeric string identifying the account owner.. [optional]  # noqa: E501
            phone_number (str): The phone number associated with the account.. [optional]  # noqa: E501
            postal_address (str, none_type): The postal address associated with the account.. [optional]  # noqa: E501
            pricing_plan (str): The pricing plan this customer is under.. [optional]  # noqa: E501
            pricing_plan_id (str): The alphanumeric string identifying the pricing plan.. [optional]  # noqa: E501
            security_contact_id (str, none_type): The alphanumeric string identifying the account's security contact.. [optional]  # noqa: E501
            technical_contact_id (str, none_type): The alphanumeric string identifying the account's technical contact.. [optional]  # noqa: E501
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
        """Customer - a model defined in OpenAPI

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
            billing_contact_id (str, none_type): The alphanumeric string representing the primary billing contact.. [optional]  # noqa: E501
            billing_network_type (str): Customer's current network revenue type.. [optional]  # noqa: E501
            billing_ref (str, none_type): Used for adding purchased orders to customer's account.. [optional]  # noqa: E501
            can_configure_wordpress (bool, none_type): Whether this customer can view or edit wordpress.. [optional]  # noqa: E501
            can_reset_passwords (bool): Whether this customer can reset passwords.. [optional]  # noqa: E501
            can_upload_vcl (bool): Whether this customer can upload VCL.. [optional]  # noqa: E501
            force_2fa (bool): Specifies whether 2FA is forced or not forced on the customer account. Logs out non-2FA users once 2FA is force enabled.. [optional]  # noqa: E501
            force_sso (bool): Specifies whether SSO is forced or not forced on the customer account.. [optional]  # noqa: E501
            has_account_panel (bool): Specifies whether the account has access or does not have access to the account panel.. [optional]  # noqa: E501
            has_improved_events (bool): Specifies whether the account has access or does not have access to the improved events.. [optional]  # noqa: E501
            has_improved_ssl_config (bool): Whether this customer can view or edit the SSL config.. [optional]  # noqa: E501
            has_openstack_logging (bool): Specifies whether the account has enabled or not enabled openstack logging.. [optional]  # noqa: E501
            has_pci (bool): Specifies whether the account can edit PCI for a service.. [optional]  # noqa: E501
            has_pci_passwords (bool): Specifies whether PCI passwords are required for the account.. [optional]  # noqa: E501
            ip_whitelist (str): The range of IP addresses authorized to access the customer account.. [optional]  # noqa: E501
            legal_contact_id (str, none_type): The alphanumeric string identifying the account's legal contact.. [optional]  # noqa: E501
            name (str): The name of the customer, generally the company name.. [optional]  # noqa: E501
            owner_id (str): The alphanumeric string identifying the account owner.. [optional]  # noqa: E501
            phone_number (str): The phone number associated with the account.. [optional]  # noqa: E501
            postal_address (str, none_type): The postal address associated with the account.. [optional]  # noqa: E501
            pricing_plan (str): The pricing plan this customer is under.. [optional]  # noqa: E501
            pricing_plan_id (str): The alphanumeric string identifying the pricing plan.. [optional]  # noqa: E501
            security_contact_id (str, none_type): The alphanumeric string identifying the account's security contact.. [optional]  # noqa: E501
            technical_contact_id (str, none_type): The alphanumeric string identifying the account's technical contact.. [optional]  # noqa: E501
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
