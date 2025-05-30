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
    from fastly.model.header import Header
    from fastly.model.service_id_and_version_string import ServiceIdAndVersionString
    from fastly.model.timestamps import Timestamps
    globals()['Header'] = Header
    globals()['ServiceIdAndVersionString'] = ServiceIdAndVersionString
    globals()['Timestamps'] = Timestamps


class HeaderResponse(ModelComposed):
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
            'SET': "set",
            'APPEND': "append",
            'DELETE': "delete",
            'REGEX': "regex",
            'REGEX_REPEAT': "regex_repeat",
        },
        ('type',): {
            'REQUEST': "request",
            'CACHE': "cache",
            'RESPONSE': "response",
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
            'action': (str,),  # noqa: E501
            'cache_condition': (str, none_type,),  # noqa: E501
            'dst': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'regex': (str, none_type,),  # noqa: E501
            'request_condition': (str, none_type,),  # noqa: E501
            'response_condition': (str, none_type,),  # noqa: E501
            'src': (str, none_type,),  # noqa: E501
            'substitution': (str, none_type,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'ignore_if_set': (str,),  # noqa: E501
            'priority': (str,),  # noqa: E501
            'service_id': (str,),  # noqa: E501
            'version': (str,),  # noqa: E501
            'created_at': (datetime, none_type,),  # noqa: E501
            'deleted_at': (datetime, none_type,),  # noqa: E501
            'updated_at': (datetime, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'action': 'action',  # noqa: E501
        'cache_condition': 'cache_condition',  # noqa: E501
        'dst': 'dst',  # noqa: E501
        'name': 'name',  # noqa: E501
        'regex': 'regex',  # noqa: E501
        'request_condition': 'request_condition',  # noqa: E501
        'response_condition': 'response_condition',  # noqa: E501
        'src': 'src',  # noqa: E501
        'substitution': 'substitution',  # noqa: E501
        'type': 'type',  # noqa: E501
        'ignore_if_set': 'ignore_if_set',  # noqa: E501
        'priority': 'priority',  # noqa: E501
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
        """HeaderResponse - a model defined in OpenAPI

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
            action (str): Accepts a string value.. [optional]  # noqa: E501
            cache_condition (str, none_type): Name of the cache condition controlling when this configuration applies.. [optional]  # noqa: E501
            dst (str): Header to set.. [optional]  # noqa: E501
            name (str): A handle to refer to this Header object.. [optional]  # noqa: E501
            regex (str, none_type): Regular expression to use. Only applies to `regex` and `regex_repeat` actions.. [optional]  # noqa: E501
            request_condition (str, none_type): Condition which, if met, will select this configuration during a request. Optional.. [optional]  # noqa: E501
            response_condition (str, none_type): Optional name of a response condition to apply.. [optional]  # noqa: E501
            src (str, none_type): Variable to be used as a source for the header content. Does not apply to `delete` action.. [optional]  # noqa: E501
            substitution (str, none_type): Value to substitute in place of regular expression. Only applies to `regex` and `regex_repeat` actions.. [optional]  # noqa: E501
            type (str): Accepts a string value.. [optional]  # noqa: E501
            ignore_if_set (str): Don't add the header if it is added already. Only applies to 'set' action. Numerical value (\"0\" = false, \"1\" = true). [optional]  # noqa: E501
            priority (str): Priority determines execution order. Lower numbers execute first.. [optional] if omitted the server will use the default value of "100"  # noqa: E501
            service_id (str): [optional]  # noqa: E501
            version (str): [optional]  # noqa: E501
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
        """HeaderResponse - a model defined in OpenAPI

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
            action (str): Accepts a string value.. [optional]  # noqa: E501
            cache_condition (str, none_type): Name of the cache condition controlling when this configuration applies.. [optional]  # noqa: E501
            dst (str): Header to set.. [optional]  # noqa: E501
            name (str): A handle to refer to this Header object.. [optional]  # noqa: E501
            regex (str, none_type): Regular expression to use. Only applies to `regex` and `regex_repeat` actions.. [optional]  # noqa: E501
            request_condition (str, none_type): Condition which, if met, will select this configuration during a request. Optional.. [optional]  # noqa: E501
            response_condition (str, none_type): Optional name of a response condition to apply.. [optional]  # noqa: E501
            src (str, none_type): Variable to be used as a source for the header content. Does not apply to `delete` action.. [optional]  # noqa: E501
            substitution (str, none_type): Value to substitute in place of regular expression. Only applies to `regex` and `regex_repeat` actions.. [optional]  # noqa: E501
            type (str): Accepts a string value.. [optional]  # noqa: E501
            ignore_if_set (str): Don't add the header if it is added already. Only applies to 'set' action. Numerical value (\"0\" = false, \"1\" = true). [optional]  # noqa: E501
            priority (str): Priority determines execution order. Lower numbers execute first.. [optional] if omitted the server will use the default value of "100"  # noqa: E501
            service_id (str): [optional]  # noqa: E501
            version (str): [optional]  # noqa: E501
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
              Header,
              ServiceIdAndVersionString,
              Timestamps,
          ],
          'oneOf': [
          ],
        }
