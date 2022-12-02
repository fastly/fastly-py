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
    from fastly.model.request_settings import RequestSettings
    from fastly.model.service_id_and_version import ServiceIdAndVersion
    from fastly.model.timestamps import Timestamps
    globals()['RequestSettings'] = RequestSettings
    globals()['ServiceIdAndVersion'] = ServiceIdAndVersion
    globals()['Timestamps'] = Timestamps


class RequestSettingsResponse(ModelComposed):
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
        ('action',): {
            'None': None,
            'LOOKUP': "lookup",
            'PASS': "pass",
        },
        ('xff',): {
            'CLEAR': "clear",
            'LEAVE': "leave",
            'APPEND': "append",
            'APPEND_ALL': "append_all",
            'OVERWRITE': "overwrite",
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
            'action': (str, none_type,),  # noqa: E501
            'bypass_busy_wait': (int,),  # noqa: E501
            'default_host': (str, none_type,),  # noqa: E501
            'force_miss': (int,),  # noqa: E501
            'force_ssl': (int,),  # noqa: E501
            'geo_headers': (int,),  # noqa: E501
            'hash_keys': (str, none_type,),  # noqa: E501
            'max_stale_age': (int,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'request_condition': (str, none_type,),  # noqa: E501
            'timer_support': (int,),  # noqa: E501
            'xff': (str,),  # noqa: E501
            'service_id': (str,),  # noqa: E501
            'version': (int,),  # noqa: E501
            'created_at': (datetime, none_type,),  # noqa: E501
            'deleted_at': (datetime, none_type,),  # noqa: E501
            'updated_at': (datetime, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'action': 'action',  # noqa: E501
        'bypass_busy_wait': 'bypass_busy_wait',  # noqa: E501
        'default_host': 'default_host',  # noqa: E501
        'force_miss': 'force_miss',  # noqa: E501
        'force_ssl': 'force_ssl',  # noqa: E501
        'geo_headers': 'geo_headers',  # noqa: E501
        'hash_keys': 'hash_keys',  # noqa: E501
        'max_stale_age': 'max_stale_age',  # noqa: E501
        'name': 'name',  # noqa: E501
        'request_condition': 'request_condition',  # noqa: E501
        'timer_support': 'timer_support',  # noqa: E501
        'xff': 'xff',  # noqa: E501
        'service_id': 'service_id',  # noqa: E501
        'version': 'version',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'deleted_at': 'deleted_at',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
    }

    read_only_vars = {
        'service_id',  # noqa: E501
        'version',  # noqa: E501
        'created_at',  # noqa: E501
        'deleted_at',  # noqa: E501
        'updated_at',  # noqa: E501
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """RequestSettingsResponse - a model defined in OpenAPI

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
            action (str, none_type): Allows you to terminate request handling and immediately perform an action.. [optional]  # noqa: E501
            bypass_busy_wait (int): Disable collapsed forwarding, so you don't wait for other objects to origin.. [optional]  # noqa: E501
            default_host (str, none_type): Sets the host header.. [optional]  # noqa: E501
            force_miss (int): Allows you to force a cache miss for the request. Replaces the item in the cache if the content is cacheable.. [optional]  # noqa: E501
            force_ssl (int): Forces the request use SSL (redirects a non-SSL to SSL).. [optional]  # noqa: E501
            geo_headers (int): Injects Fastly-Geo-Country, Fastly-Geo-City, and Fastly-Geo-Region into the request headers.. [optional]  # noqa: E501
            hash_keys (str, none_type): Comma separated list of varnish request object fields that should be in the hash key.. [optional]  # noqa: E501
            max_stale_age (int): How old an object is allowed to be to serve stale-if-error or stale-while-revalidate.. [optional]  # noqa: E501
            name (str): Name for the request settings.. [optional]  # noqa: E501
            request_condition (str, none_type): Condition which, if met, will select this configuration during a request. Optional.. [optional]  # noqa: E501
            timer_support (int): Injects the X-Timer info into the request for viewing origin fetch durations.. [optional]  # noqa: E501
            xff (str): Short for X-Forwarded-For.. [optional]  # noqa: E501
            service_id (str): [optional]  # noqa: E501
            version (int): [optional]  # noqa: E501
            created_at (datetime, none_type): Date and time in ISO 8601 format.. [optional]  # noqa: E501
            deleted_at (datetime, none_type): Date and time in ISO 8601 format.. [optional]  # noqa: E501
            updated_at (datetime, none_type): Date and time in ISO 8601 format.. [optional]  # noqa: E501
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
        """RequestSettingsResponse - a model defined in OpenAPI

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
            action (str, none_type): Allows you to terminate request handling and immediately perform an action.. [optional]  # noqa: E501
            bypass_busy_wait (int): Disable collapsed forwarding, so you don't wait for other objects to origin.. [optional]  # noqa: E501
            default_host (str, none_type): Sets the host header.. [optional]  # noqa: E501
            force_miss (int): Allows you to force a cache miss for the request. Replaces the item in the cache if the content is cacheable.. [optional]  # noqa: E501
            force_ssl (int): Forces the request use SSL (redirects a non-SSL to SSL).. [optional]  # noqa: E501
            geo_headers (int): Injects Fastly-Geo-Country, Fastly-Geo-City, and Fastly-Geo-Region into the request headers.. [optional]  # noqa: E501
            hash_keys (str, none_type): Comma separated list of varnish request object fields that should be in the hash key.. [optional]  # noqa: E501
            max_stale_age (int): How old an object is allowed to be to serve stale-if-error or stale-while-revalidate.. [optional]  # noqa: E501
            name (str): Name for the request settings.. [optional]  # noqa: E501
            request_condition (str, none_type): Condition which, if met, will select this configuration during a request. Optional.. [optional]  # noqa: E501
            timer_support (int): Injects the X-Timer info into the request for viewing origin fetch durations.. [optional]  # noqa: E501
            xff (str): Short for X-Forwarded-For.. [optional]  # noqa: E501
            service_id (str): [optional]  # noqa: E501
            version (int): [optional]  # noqa: E501
            created_at (datetime, none_type): Date and time in ISO 8601 format.. [optional]  # noqa: E501
            deleted_at (datetime, none_type): Date and time in ISO 8601 format.. [optional]  # noqa: E501
            updated_at (datetime, none_type): Date and time in ISO 8601 format.. [optional]  # noqa: E501
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
              RequestSettings,
              ServiceIdAndVersion,
              Timestamps,
          ],
          'oneOf': [
          ],
        }
