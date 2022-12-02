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



class WafFirewallVersionDataAttributes(ModelNormal):
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
            'allowed_http_versions': (str,),  # noqa: E501
            'allowed_methods': (str,),  # noqa: E501
            'allowed_request_content_type': (str,),  # noqa: E501
            'allowed_request_content_type_charset': (str,),  # noqa: E501
            'arg_name_length': (int,),  # noqa: E501
            'arg_length': (int,),  # noqa: E501
            'combined_file_sizes': (int,),  # noqa: E501
            'comment': (str, none_type,),  # noqa: E501
            'critical_anomaly_score': (int,),  # noqa: E501
            'crs_validate_utf8_encoding': (bool,),  # noqa: E501
            'error_anomaly_score': (int,),  # noqa: E501
            'high_risk_country_codes': (str,),  # noqa: E501
            'http_violation_score_threshold': (int,),  # noqa: E501
            'inbound_anomaly_score_threshold': (int,),  # noqa: E501
            'lfi_score_threshold': (int,),  # noqa: E501
            'locked': (bool,),  # noqa: E501
            'max_file_size': (int,),  # noqa: E501
            'max_num_args': (int,),  # noqa: E501
            'notice_anomaly_score': (int,),  # noqa: E501
            'number': (int,),  # noqa: E501
            'paranoia_level': (int,),  # noqa: E501
            'php_injection_score_threshold': (int,),  # noqa: E501
            'rce_score_threshold': (int,),  # noqa: E501
            'restricted_extensions': (str,),  # noqa: E501
            'restricted_headers': (str,),  # noqa: E501
            'rfi_score_threshold': (int,),  # noqa: E501
            'session_fixation_score_threshold': (int,),  # noqa: E501
            'sql_injection_score_threshold': (int,),  # noqa: E501
            'total_arg_length': (int,),  # noqa: E501
            'warning_anomaly_score': (int,),  # noqa: E501
            'xss_score_threshold': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'allowed_http_versions': 'allowed_http_versions',  # noqa: E501
        'allowed_methods': 'allowed_methods',  # noqa: E501
        'allowed_request_content_type': 'allowed_request_content_type',  # noqa: E501
        'allowed_request_content_type_charset': 'allowed_request_content_type_charset',  # noqa: E501
        'arg_name_length': 'arg_name_length',  # noqa: E501
        'arg_length': 'arg_length',  # noqa: E501
        'combined_file_sizes': 'combined_file_sizes',  # noqa: E501
        'comment': 'comment',  # noqa: E501
        'critical_anomaly_score': 'critical_anomaly_score',  # noqa: E501
        'crs_validate_utf8_encoding': 'crs_validate_utf8_encoding',  # noqa: E501
        'error_anomaly_score': 'error_anomaly_score',  # noqa: E501
        'high_risk_country_codes': 'high_risk_country_codes',  # noqa: E501
        'http_violation_score_threshold': 'http_violation_score_threshold',  # noqa: E501
        'inbound_anomaly_score_threshold': 'inbound_anomaly_score_threshold',  # noqa: E501
        'lfi_score_threshold': 'lfi_score_threshold',  # noqa: E501
        'locked': 'locked',  # noqa: E501
        'max_file_size': 'max_file_size',  # noqa: E501
        'max_num_args': 'max_num_args',  # noqa: E501
        'notice_anomaly_score': 'notice_anomaly_score',  # noqa: E501
        'number': 'number',  # noqa: E501
        'paranoia_level': 'paranoia_level',  # noqa: E501
        'php_injection_score_threshold': 'php_injection_score_threshold',  # noqa: E501
        'rce_score_threshold': 'rce_score_threshold',  # noqa: E501
        'restricted_extensions': 'restricted_extensions',  # noqa: E501
        'restricted_headers': 'restricted_headers',  # noqa: E501
        'rfi_score_threshold': 'rfi_score_threshold',  # noqa: E501
        'session_fixation_score_threshold': 'session_fixation_score_threshold',  # noqa: E501
        'sql_injection_score_threshold': 'sql_injection_score_threshold',  # noqa: E501
        'total_arg_length': 'total_arg_length',  # noqa: E501
        'warning_anomaly_score': 'warning_anomaly_score',  # noqa: E501
        'xss_score_threshold': 'xss_score_threshold',  # noqa: E501
    }

    read_only_vars = {
        'number',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """WafFirewallVersionDataAttributes - a model defined in OpenAPI

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
            allowed_http_versions (str): Allowed HTTP versions.. [optional] if omitted the server will use the default value of "HTTP/1.0 HTTP/1.1 HTTP/2"  # noqa: E501
            allowed_methods (str): A space-separated list of HTTP method names.. [optional] if omitted the server will use the default value of "GET HEAD POST OPTIONS PUT PATCH DELETE"  # noqa: E501
            allowed_request_content_type (str): Allowed request content types.. [optional] if omitted the server will use the default value of "application/x-www-form-urlencoded|multipart/form-data|text/xml|application/xml|application/x-amf|application/json|text/plain"  # noqa: E501
            allowed_request_content_type_charset (str): Allowed request content type charset.. [optional] if omitted the server will use the default value of "utf-8|iso-8859-1|iso-8859-15|windows-1252"  # noqa: E501
            arg_name_length (int): The maximum allowed argument name length.. [optional] if omitted the server will use the default value of 100  # noqa: E501
            arg_length (int): The maximum allowed length of an argument.. [optional] if omitted the server will use the default value of 400  # noqa: E501
            combined_file_sizes (int): The maximum allowed size of all files (in bytes).. [optional] if omitted the server will use the default value of 10000000  # noqa: E501
            comment (str, none_type): A freeform descriptive note.. [optional]  # noqa: E501
            critical_anomaly_score (int): Score value to add for critical anomalies.. [optional] if omitted the server will use the default value of 6  # noqa: E501
            crs_validate_utf8_encoding (bool): CRS validate UTF8 encoding.. [optional]  # noqa: E501
            error_anomaly_score (int): Score value to add for error anomalies.. [optional] if omitted the server will use the default value of 5  # noqa: E501
            high_risk_country_codes (str): A space-separated list of country codes in ISO 3166-1 (two-letter) format.. [optional]  # noqa: E501
            http_violation_score_threshold (int): HTTP violation threshold.. [optional]  # noqa: E501
            inbound_anomaly_score_threshold (int): Inbound anomaly threshold.. [optional]  # noqa: E501
            lfi_score_threshold (int): Local file inclusion attack threshold.. [optional]  # noqa: E501
            locked (bool): Whether a specific firewall version is locked from being modified.. [optional] if omitted the server will use the default value of False  # noqa: E501
            max_file_size (int): The maximum allowed file size, in bytes.. [optional] if omitted the server will use the default value of 10000000  # noqa: E501
            max_num_args (int): The maximum number of arguments allowed.. [optional] if omitted the server will use the default value of 255  # noqa: E501
            notice_anomaly_score (int): Score value to add for notice anomalies.. [optional] if omitted the server will use the default value of 4  # noqa: E501
            number (int): [optional]  # noqa: E501
            paranoia_level (int): The configured paranoia level.. [optional] if omitted the server will use the default value of 1  # noqa: E501
            php_injection_score_threshold (int): PHP injection threshold.. [optional]  # noqa: E501
            rce_score_threshold (int): Remote code execution threshold.. [optional]  # noqa: E501
            restricted_extensions (str): A space-separated list of allowed file extensions.. [optional] if omitted the server will use the default value of ".asa/ .asax/ .ascx/ .axd/ .backup/ .bak/ .bat/ .cdx/ .cer/ .cfg/ .cmd/ .com/ .config/ .conf/ .cs/ .csproj/ .csr/ .dat/ .db/ .dbf/ .dll/ .dos/ .htr/ .htw/ .ida/ .idc/ .idq/ .inc/ .ini/ .key/ .licx/ .lnk/ .log/ .mdb/ .old/ .pass/ .pdb/ .pol/ .printer/ .pwd/ .resources/ .resx/ .sql/ .sys/ .vb/ .vbs/ .vbproj/ .vsdisco/ .webinfo/ .xsd/ .xsx"  # noqa: E501
            restricted_headers (str): A space-separated list of allowed header names.. [optional] if omitted the server will use the default value of "/proxy/ /lock-token/ /content-range/ /translate/ /if/"  # noqa: E501
            rfi_score_threshold (int): Remote file inclusion attack threshold.. [optional]  # noqa: E501
            session_fixation_score_threshold (int): Session fixation attack threshold.. [optional]  # noqa: E501
            sql_injection_score_threshold (int): SQL injection attack threshold.. [optional]  # noqa: E501
            total_arg_length (int): The maximum size of argument names and values.. [optional] if omitted the server will use the default value of 6400  # noqa: E501
            warning_anomaly_score (int): Score value to add for warning anomalies.. [optional]  # noqa: E501
            xss_score_threshold (int): XSS attack threshold.. [optional]  # noqa: E501
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
        """WafFirewallVersionDataAttributes - a model defined in OpenAPI

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
            allowed_http_versions (str): Allowed HTTP versions.. [optional] if omitted the server will use the default value of "HTTP/1.0 HTTP/1.1 HTTP/2"  # noqa: E501
            allowed_methods (str): A space-separated list of HTTP method names.. [optional] if omitted the server will use the default value of "GET HEAD POST OPTIONS PUT PATCH DELETE"  # noqa: E501
            allowed_request_content_type (str): Allowed request content types.. [optional] if omitted the server will use the default value of "application/x-www-form-urlencoded|multipart/form-data|text/xml|application/xml|application/x-amf|application/json|text/plain"  # noqa: E501
            allowed_request_content_type_charset (str): Allowed request content type charset.. [optional] if omitted the server will use the default value of "utf-8|iso-8859-1|iso-8859-15|windows-1252"  # noqa: E501
            arg_name_length (int): The maximum allowed argument name length.. [optional] if omitted the server will use the default value of 100  # noqa: E501
            arg_length (int): The maximum allowed length of an argument.. [optional] if omitted the server will use the default value of 400  # noqa: E501
            combined_file_sizes (int): The maximum allowed size of all files (in bytes).. [optional] if omitted the server will use the default value of 10000000  # noqa: E501
            comment (str, none_type): A freeform descriptive note.. [optional]  # noqa: E501
            critical_anomaly_score (int): Score value to add for critical anomalies.. [optional] if omitted the server will use the default value of 6  # noqa: E501
            crs_validate_utf8_encoding (bool): CRS validate UTF8 encoding.. [optional]  # noqa: E501
            error_anomaly_score (int): Score value to add for error anomalies.. [optional] if omitted the server will use the default value of 5  # noqa: E501
            high_risk_country_codes (str): A space-separated list of country codes in ISO 3166-1 (two-letter) format.. [optional]  # noqa: E501
            http_violation_score_threshold (int): HTTP violation threshold.. [optional]  # noqa: E501
            inbound_anomaly_score_threshold (int): Inbound anomaly threshold.. [optional]  # noqa: E501
            lfi_score_threshold (int): Local file inclusion attack threshold.. [optional]  # noqa: E501
            locked (bool): Whether a specific firewall version is locked from being modified.. [optional] if omitted the server will use the default value of False  # noqa: E501
            max_file_size (int): The maximum allowed file size, in bytes.. [optional] if omitted the server will use the default value of 10000000  # noqa: E501
            max_num_args (int): The maximum number of arguments allowed.. [optional] if omitted the server will use the default value of 255  # noqa: E501
            notice_anomaly_score (int): Score value to add for notice anomalies.. [optional] if omitted the server will use the default value of 4  # noqa: E501
            number (int): [optional]  # noqa: E501
            paranoia_level (int): The configured paranoia level.. [optional] if omitted the server will use the default value of 1  # noqa: E501
            php_injection_score_threshold (int): PHP injection threshold.. [optional]  # noqa: E501
            rce_score_threshold (int): Remote code execution threshold.. [optional]  # noqa: E501
            restricted_extensions (str): A space-separated list of allowed file extensions.. [optional] if omitted the server will use the default value of ".asa/ .asax/ .ascx/ .axd/ .backup/ .bak/ .bat/ .cdx/ .cer/ .cfg/ .cmd/ .com/ .config/ .conf/ .cs/ .csproj/ .csr/ .dat/ .db/ .dbf/ .dll/ .dos/ .htr/ .htw/ .ida/ .idc/ .idq/ .inc/ .ini/ .key/ .licx/ .lnk/ .log/ .mdb/ .old/ .pass/ .pdb/ .pol/ .printer/ .pwd/ .resources/ .resx/ .sql/ .sys/ .vb/ .vbs/ .vbproj/ .vsdisco/ .webinfo/ .xsd/ .xsx"  # noqa: E501
            restricted_headers (str): A space-separated list of allowed header names.. [optional] if omitted the server will use the default value of "/proxy/ /lock-token/ /content-range/ /translate/ /if/"  # noqa: E501
            rfi_score_threshold (int): Remote file inclusion attack threshold.. [optional]  # noqa: E501
            session_fixation_score_threshold (int): Session fixation attack threshold.. [optional]  # noqa: E501
            sql_injection_score_threshold (int): SQL injection attack threshold.. [optional]  # noqa: E501
            total_arg_length (int): The maximum size of argument names and values.. [optional] if omitted the server will use the default value of 6400  # noqa: E501
            warning_anomaly_score (int): Score value to add for warning anomalies.. [optional]  # noqa: E501
            xss_score_threshold (int): XSS attack threshold.. [optional]  # noqa: E501
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
