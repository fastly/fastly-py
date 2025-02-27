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



class OriginInspectorMeasurements(ModelNormal):
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
            'responses': (int,),  # noqa: E501
            'resp_header_bytes': (int,),  # noqa: E501
            'resp_body_bytes': (int,),  # noqa: E501
            'status_1xx': (int,),  # noqa: E501
            'status_2xx': (int,),  # noqa: E501
            'status_3xx': (int,),  # noqa: E501
            'status_4xx': (int,),  # noqa: E501
            'status_5xx': (int,),  # noqa: E501
            'status_200': (int,),  # noqa: E501
            'status_204': (int,),  # noqa: E501
            'status_206': (int,),  # noqa: E501
            'status_301': (int,),  # noqa: E501
            'status_302': (int,),  # noqa: E501
            'status_304': (int,),  # noqa: E501
            'status_400': (int,),  # noqa: E501
            'status_401': (int,),  # noqa: E501
            'status_403': (int,),  # noqa: E501
            'status_404': (int,),  # noqa: E501
            'status_416': (int,),  # noqa: E501
            'status_429': (int,),  # noqa: E501
            'status_500': (int,),  # noqa: E501
            'status_501': (int,),  # noqa: E501
            'status_502': (int,),  # noqa: E501
            'status_503': (int,),  # noqa: E501
            'status_504': (int,),  # noqa: E501
            'status_505': (int,),  # noqa: E501
            'status_530': (int,),  # noqa: E501
            'latency_0_to_1ms': (int,),  # noqa: E501
            'latency_1_to_5ms': (int,),  # noqa: E501
            'latency_5_to_10ms': (int,),  # noqa: E501
            'latency_10_to_50ms': (int,),  # noqa: E501
            'latency_50_to_100ms': (int,),  # noqa: E501
            'latency_100_to_250ms': (int,),  # noqa: E501
            'latency_250_to_500ms': (int,),  # noqa: E501
            'latency_500_to_1000ms': (int,),  # noqa: E501
            'latency_1000_to_5000ms': (int,),  # noqa: E501
            'latency_5000_to_10000ms': (int,),  # noqa: E501
            'latency_10000_to_60000ms': (int,),  # noqa: E501
            'latency_60000ms': (int,),  # noqa: E501
            'waf_responses': (int,),  # noqa: E501
            'waf_resp_header_bytes': (int,),  # noqa: E501
            'waf_resp_body_bytes': (int,),  # noqa: E501
            'waf_status_1xx': (int,),  # noqa: E501
            'waf_status_2xx': (int,),  # noqa: E501
            'waf_status_3xx': (int,),  # noqa: E501
            'waf_status_4xx': (int,),  # noqa: E501
            'waf_status_5xx': (int,),  # noqa: E501
            'waf_status_200': (int,),  # noqa: E501
            'waf_status_204': (int,),  # noqa: E501
            'waf_status_206': (int,),  # noqa: E501
            'waf_status_301': (int,),  # noqa: E501
            'waf_status_302': (int,),  # noqa: E501
            'waf_status_304': (int,),  # noqa: E501
            'waf_status_400': (int,),  # noqa: E501
            'waf_status_401': (int,),  # noqa: E501
            'waf_status_403': (int,),  # noqa: E501
            'waf_status_404': (int,),  # noqa: E501
            'waf_status_416': (int,),  # noqa: E501
            'waf_status_429': (int,),  # noqa: E501
            'waf_status_500': (int,),  # noqa: E501
            'waf_status_501': (int,),  # noqa: E501
            'waf_status_502': (int,),  # noqa: E501
            'waf_status_503': (int,),  # noqa: E501
            'waf_status_504': (int,),  # noqa: E501
            'waf_status_505': (int,),  # noqa: E501
            'waf_status_530': (int,),  # noqa: E501
            'waf_latency_0_to_1ms': (int,),  # noqa: E501
            'waf_latency_1_to_5ms': (int,),  # noqa: E501
            'waf_latency_5_to_10ms': (int,),  # noqa: E501
            'waf_latency_10_to_50ms': (int,),  # noqa: E501
            'waf_latency_50_to_100ms': (int,),  # noqa: E501
            'waf_latency_100_to_250ms': (int,),  # noqa: E501
            'waf_latency_250_to_500ms': (int,),  # noqa: E501
            'waf_latency_500_to_1000ms': (int,),  # noqa: E501
            'waf_latency_1000_to_5000ms': (int,),  # noqa: E501
            'waf_latency_5000_to_10000ms': (int,),  # noqa: E501
            'waf_latency_10000_to_60000ms': (int,),  # noqa: E501
            'waf_latency_60000ms': (int,),  # noqa: E501
            'compute_responses': (int,),  # noqa: E501
            'compute_resp_header_bytes': (int,),  # noqa: E501
            'compute_resp_body_bytes': (int,),  # noqa: E501
            'compute_status_1xx': (int,),  # noqa: E501
            'compute_status_2xx': (int,),  # noqa: E501
            'compute_status_3xx': (int,),  # noqa: E501
            'compute_status_4xx': (int,),  # noqa: E501
            'compute_status_5xx': (int,),  # noqa: E501
            'compute_status_200': (int,),  # noqa: E501
            'compute_status_204': (int,),  # noqa: E501
            'compute_status_206': (int,),  # noqa: E501
            'compute_status_301': (int,),  # noqa: E501
            'compute_status_302': (int,),  # noqa: E501
            'compute_status_304': (int,),  # noqa: E501
            'compute_status_400': (int,),  # noqa: E501
            'compute_status_401': (int,),  # noqa: E501
            'compute_status_403': (int,),  # noqa: E501
            'compute_status_404': (int,),  # noqa: E501
            'compute_status_416': (int,),  # noqa: E501
            'compute_status_429': (int,),  # noqa: E501
            'compute_status_500': (int,),  # noqa: E501
            'compute_status_501': (int,),  # noqa: E501
            'compute_status_502': (int,),  # noqa: E501
            'compute_status_503': (int,),  # noqa: E501
            'compute_status_504': (int,),  # noqa: E501
            'compute_status_505': (int,),  # noqa: E501
            'compute_status_530': (int,),  # noqa: E501
            'compute_latency_0_to_1ms': (int,),  # noqa: E501
            'compute_latency_1_to_5ms': (int,),  # noqa: E501
            'compute_latency_5_to_10ms': (int,),  # noqa: E501
            'compute_latency_10_to_50ms': (int,),  # noqa: E501
            'compute_latency_50_to_100ms': (int,),  # noqa: E501
            'compute_latency_100_to_250ms': (int,),  # noqa: E501
            'compute_latency_250_to_500ms': (int,),  # noqa: E501
            'compute_latency_500_to_1000ms': (int,),  # noqa: E501
            'compute_latency_1000_to_5000ms': (int,),  # noqa: E501
            'compute_latency_5000_to_10000ms': (int,),  # noqa: E501
            'compute_latency_10000_to_60000ms': (int,),  # noqa: E501
            'compute_latency_60000ms': (int,),  # noqa: E501
            'all_responses': (int,),  # noqa: E501
            'all_resp_header_bytes': (int,),  # noqa: E501
            'all_resp_body_bytes': (int,),  # noqa: E501
            'all_status_1xx': (int,),  # noqa: E501
            'all_status_2xx': (int,),  # noqa: E501
            'all_status_3xx': (int,),  # noqa: E501
            'all_status_4xx': (int,),  # noqa: E501
            'all_status_5xx': (int,),  # noqa: E501
            'all_status_200': (int,),  # noqa: E501
            'all_status_204': (int,),  # noqa: E501
            'all_status_206': (int,),  # noqa: E501
            'all_status_301': (int,),  # noqa: E501
            'all_status_302': (int,),  # noqa: E501
            'all_status_304': (int,),  # noqa: E501
            'all_status_400': (int,),  # noqa: E501
            'all_status_401': (int,),  # noqa: E501
            'all_status_403': (int,),  # noqa: E501
            'all_status_404': (int,),  # noqa: E501
            'all_status_416': (int,),  # noqa: E501
            'all_status_429': (int,),  # noqa: E501
            'all_status_500': (int,),  # noqa: E501
            'all_status_501': (int,),  # noqa: E501
            'all_status_502': (int,),  # noqa: E501
            'all_status_503': (int,),  # noqa: E501
            'all_status_504': (int,),  # noqa: E501
            'all_status_505': (int,),  # noqa: E501
            'all_status_530': (int,),  # noqa: E501
            'all_latency_0_to_1ms': (int,),  # noqa: E501
            'all_latency_1_to_5ms': (int,),  # noqa: E501
            'all_latency_5_to_10ms': (int,),  # noqa: E501
            'all_latency_10_to_50ms': (int,),  # noqa: E501
            'all_latency_50_to_100ms': (int,),  # noqa: E501
            'all_latency_100_to_250ms': (int,),  # noqa: E501
            'all_latency_250_to_500ms': (int,),  # noqa: E501
            'all_latency_500_to_1000ms': (int,),  # noqa: E501
            'all_latency_1000_to_5000ms': (int,),  # noqa: E501
            'all_latency_5000_to_10000ms': (int,),  # noqa: E501
            'all_latency_10000_to_60000ms': (int,),  # noqa: E501
            'all_latency_60000ms': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'responses': 'responses',  # noqa: E501
        'resp_header_bytes': 'resp_header_bytes',  # noqa: E501
        'resp_body_bytes': 'resp_body_bytes',  # noqa: E501
        'status_1xx': 'status_1xx',  # noqa: E501
        'status_2xx': 'status_2xx',  # noqa: E501
        'status_3xx': 'status_3xx',  # noqa: E501
        'status_4xx': 'status_4xx',  # noqa: E501
        'status_5xx': 'status_5xx',  # noqa: E501
        'status_200': 'status_200',  # noqa: E501
        'status_204': 'status_204',  # noqa: E501
        'status_206': 'status_206',  # noqa: E501
        'status_301': 'status_301',  # noqa: E501
        'status_302': 'status_302',  # noqa: E501
        'status_304': 'status_304',  # noqa: E501
        'status_400': 'status_400',  # noqa: E501
        'status_401': 'status_401',  # noqa: E501
        'status_403': 'status_403',  # noqa: E501
        'status_404': 'status_404',  # noqa: E501
        'status_416': 'status_416',  # noqa: E501
        'status_429': 'status_429',  # noqa: E501
        'status_500': 'status_500',  # noqa: E501
        'status_501': 'status_501',  # noqa: E501
        'status_502': 'status_502',  # noqa: E501
        'status_503': 'status_503',  # noqa: E501
        'status_504': 'status_504',  # noqa: E501
        'status_505': 'status_505',  # noqa: E501
        'status_530': 'status_530',  # noqa: E501
        'latency_0_to_1ms': 'latency_0_to_1ms',  # noqa: E501
        'latency_1_to_5ms': 'latency_1_to_5ms',  # noqa: E501
        'latency_5_to_10ms': 'latency_5_to_10ms',  # noqa: E501
        'latency_10_to_50ms': 'latency_10_to_50ms',  # noqa: E501
        'latency_50_to_100ms': 'latency_50_to_100ms',  # noqa: E501
        'latency_100_to_250ms': 'latency_100_to_250ms',  # noqa: E501
        'latency_250_to_500ms': 'latency_250_to_500ms',  # noqa: E501
        'latency_500_to_1000ms': 'latency_500_to_1000ms',  # noqa: E501
        'latency_1000_to_5000ms': 'latency_1000_to_5000ms',  # noqa: E501
        'latency_5000_to_10000ms': 'latency_5000_to_10000ms',  # noqa: E501
        'latency_10000_to_60000ms': 'latency_10000_to_60000ms',  # noqa: E501
        'latency_60000ms': 'latency_60000ms',  # noqa: E501
        'waf_responses': 'waf_responses',  # noqa: E501
        'waf_resp_header_bytes': 'waf_resp_header_bytes',  # noqa: E501
        'waf_resp_body_bytes': 'waf_resp_body_bytes',  # noqa: E501
        'waf_status_1xx': 'waf_status_1xx',  # noqa: E501
        'waf_status_2xx': 'waf_status_2xx',  # noqa: E501
        'waf_status_3xx': 'waf_status_3xx',  # noqa: E501
        'waf_status_4xx': 'waf_status_4xx',  # noqa: E501
        'waf_status_5xx': 'waf_status_5xx',  # noqa: E501
        'waf_status_200': 'waf_status_200',  # noqa: E501
        'waf_status_204': 'waf_status_204',  # noqa: E501
        'waf_status_206': 'waf_status_206',  # noqa: E501
        'waf_status_301': 'waf_status_301',  # noqa: E501
        'waf_status_302': 'waf_status_302',  # noqa: E501
        'waf_status_304': 'waf_status_304',  # noqa: E501
        'waf_status_400': 'waf_status_400',  # noqa: E501
        'waf_status_401': 'waf_status_401',  # noqa: E501
        'waf_status_403': 'waf_status_403',  # noqa: E501
        'waf_status_404': 'waf_status_404',  # noqa: E501
        'waf_status_416': 'waf_status_416',  # noqa: E501
        'waf_status_429': 'waf_status_429',  # noqa: E501
        'waf_status_500': 'waf_status_500',  # noqa: E501
        'waf_status_501': 'waf_status_501',  # noqa: E501
        'waf_status_502': 'waf_status_502',  # noqa: E501
        'waf_status_503': 'waf_status_503',  # noqa: E501
        'waf_status_504': 'waf_status_504',  # noqa: E501
        'waf_status_505': 'waf_status_505',  # noqa: E501
        'waf_status_530': 'waf_status_530',  # noqa: E501
        'waf_latency_0_to_1ms': 'waf_latency_0_to_1ms',  # noqa: E501
        'waf_latency_1_to_5ms': 'waf_latency_1_to_5ms',  # noqa: E501
        'waf_latency_5_to_10ms': 'waf_latency_5_to_10ms',  # noqa: E501
        'waf_latency_10_to_50ms': 'waf_latency_10_to_50ms',  # noqa: E501
        'waf_latency_50_to_100ms': 'waf_latency_50_to_100ms',  # noqa: E501
        'waf_latency_100_to_250ms': 'waf_latency_100_to_250ms',  # noqa: E501
        'waf_latency_250_to_500ms': 'waf_latency_250_to_500ms',  # noqa: E501
        'waf_latency_500_to_1000ms': 'waf_latency_500_to_1000ms',  # noqa: E501
        'waf_latency_1000_to_5000ms': 'waf_latency_1000_to_5000ms',  # noqa: E501
        'waf_latency_5000_to_10000ms': 'waf_latency_5000_to_10000ms',  # noqa: E501
        'waf_latency_10000_to_60000ms': 'waf_latency_10000_to_60000ms',  # noqa: E501
        'waf_latency_60000ms': 'waf_latency_60000ms',  # noqa: E501
        'compute_responses': 'compute_responses',  # noqa: E501
        'compute_resp_header_bytes': 'compute_resp_header_bytes',  # noqa: E501
        'compute_resp_body_bytes': 'compute_resp_body_bytes',  # noqa: E501
        'compute_status_1xx': 'compute_status_1xx',  # noqa: E501
        'compute_status_2xx': 'compute_status_2xx',  # noqa: E501
        'compute_status_3xx': 'compute_status_3xx',  # noqa: E501
        'compute_status_4xx': 'compute_status_4xx',  # noqa: E501
        'compute_status_5xx': 'compute_status_5xx',  # noqa: E501
        'compute_status_200': 'compute_status_200',  # noqa: E501
        'compute_status_204': 'compute_status_204',  # noqa: E501
        'compute_status_206': 'compute_status_206',  # noqa: E501
        'compute_status_301': 'compute_status_301',  # noqa: E501
        'compute_status_302': 'compute_status_302',  # noqa: E501
        'compute_status_304': 'compute_status_304',  # noqa: E501
        'compute_status_400': 'compute_status_400',  # noqa: E501
        'compute_status_401': 'compute_status_401',  # noqa: E501
        'compute_status_403': 'compute_status_403',  # noqa: E501
        'compute_status_404': 'compute_status_404',  # noqa: E501
        'compute_status_416': 'compute_status_416',  # noqa: E501
        'compute_status_429': 'compute_status_429',  # noqa: E501
        'compute_status_500': 'compute_status_500',  # noqa: E501
        'compute_status_501': 'compute_status_501',  # noqa: E501
        'compute_status_502': 'compute_status_502',  # noqa: E501
        'compute_status_503': 'compute_status_503',  # noqa: E501
        'compute_status_504': 'compute_status_504',  # noqa: E501
        'compute_status_505': 'compute_status_505',  # noqa: E501
        'compute_status_530': 'compute_status_530',  # noqa: E501
        'compute_latency_0_to_1ms': 'compute_latency_0_to_1ms',  # noqa: E501
        'compute_latency_1_to_5ms': 'compute_latency_1_to_5ms',  # noqa: E501
        'compute_latency_5_to_10ms': 'compute_latency_5_to_10ms',  # noqa: E501
        'compute_latency_10_to_50ms': 'compute_latency_10_to_50ms',  # noqa: E501
        'compute_latency_50_to_100ms': 'compute_latency_50_to_100ms',  # noqa: E501
        'compute_latency_100_to_250ms': 'compute_latency_100_to_250ms',  # noqa: E501
        'compute_latency_250_to_500ms': 'compute_latency_250_to_500ms',  # noqa: E501
        'compute_latency_500_to_1000ms': 'compute_latency_500_to_1000ms',  # noqa: E501
        'compute_latency_1000_to_5000ms': 'compute_latency_1000_to_5000ms',  # noqa: E501
        'compute_latency_5000_to_10000ms': 'compute_latency_5000_to_10000ms',  # noqa: E501
        'compute_latency_10000_to_60000ms': 'compute_latency_10000_to_60000ms',  # noqa: E501
        'compute_latency_60000ms': 'compute_latency_60000ms',  # noqa: E501
        'all_responses': 'all_responses',  # noqa: E501
        'all_resp_header_bytes': 'all_resp_header_bytes',  # noqa: E501
        'all_resp_body_bytes': 'all_resp_body_bytes',  # noqa: E501
        'all_status_1xx': 'all_status_1xx',  # noqa: E501
        'all_status_2xx': 'all_status_2xx',  # noqa: E501
        'all_status_3xx': 'all_status_3xx',  # noqa: E501
        'all_status_4xx': 'all_status_4xx',  # noqa: E501
        'all_status_5xx': 'all_status_5xx',  # noqa: E501
        'all_status_200': 'all_status_200',  # noqa: E501
        'all_status_204': 'all_status_204',  # noqa: E501
        'all_status_206': 'all_status_206',  # noqa: E501
        'all_status_301': 'all_status_301',  # noqa: E501
        'all_status_302': 'all_status_302',  # noqa: E501
        'all_status_304': 'all_status_304',  # noqa: E501
        'all_status_400': 'all_status_400',  # noqa: E501
        'all_status_401': 'all_status_401',  # noqa: E501
        'all_status_403': 'all_status_403',  # noqa: E501
        'all_status_404': 'all_status_404',  # noqa: E501
        'all_status_416': 'all_status_416',  # noqa: E501
        'all_status_429': 'all_status_429',  # noqa: E501
        'all_status_500': 'all_status_500',  # noqa: E501
        'all_status_501': 'all_status_501',  # noqa: E501
        'all_status_502': 'all_status_502',  # noqa: E501
        'all_status_503': 'all_status_503',  # noqa: E501
        'all_status_504': 'all_status_504',  # noqa: E501
        'all_status_505': 'all_status_505',  # noqa: E501
        'all_status_530': 'all_status_530',  # noqa: E501
        'all_latency_0_to_1ms': 'all_latency_0_to_1ms',  # noqa: E501
        'all_latency_1_to_5ms': 'all_latency_1_to_5ms',  # noqa: E501
        'all_latency_5_to_10ms': 'all_latency_5_to_10ms',  # noqa: E501
        'all_latency_10_to_50ms': 'all_latency_10_to_50ms',  # noqa: E501
        'all_latency_50_to_100ms': 'all_latency_50_to_100ms',  # noqa: E501
        'all_latency_100_to_250ms': 'all_latency_100_to_250ms',  # noqa: E501
        'all_latency_250_to_500ms': 'all_latency_250_to_500ms',  # noqa: E501
        'all_latency_500_to_1000ms': 'all_latency_500_to_1000ms',  # noqa: E501
        'all_latency_1000_to_5000ms': 'all_latency_1000_to_5000ms',  # noqa: E501
        'all_latency_5000_to_10000ms': 'all_latency_5000_to_10000ms',  # noqa: E501
        'all_latency_10000_to_60000ms': 'all_latency_10000_to_60000ms',  # noqa: E501
        'all_latency_60000ms': 'all_latency_60000ms',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """OriginInspectorMeasurements - a model defined in OpenAPI

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
            responses (int): Number of responses from origin.. [optional]  # noqa: E501
            resp_header_bytes (int): Number of header bytes from origin.. [optional]  # noqa: E501
            resp_body_bytes (int): Number of body bytes from origin.. [optional]  # noqa: E501
            status_1xx (int): Number of 1xx \"Informational\" status codes delivered from origin.. [optional]  # noqa: E501
            status_2xx (int): Number of 2xx \"Success\" status codes delivered from origin.. [optional]  # noqa: E501
            status_3xx (int): Number of 3xx \"Redirection\" codes delivered from origin.. [optional]  # noqa: E501
            status_4xx (int): Number of 4xx \"Client Error\" codes delivered from origin.. [optional]  # noqa: E501
            status_5xx (int): Number of 5xx \"Server Error\" codes delivered from origin.. [optional]  # noqa: E501
            status_200 (int): Number of responses received with status code 200 (Success) from origin.. [optional]  # noqa: E501
            status_204 (int): Number of responses received with status code 204 (No Content) from origin.. [optional]  # noqa: E501
            status_206 (int): Number of responses received with status code 206 (Partial Content) from origin.. [optional]  # noqa: E501
            status_301 (int): Number of responses received with status code 301 (Moved Permanently) from origin.. [optional]  # noqa: E501
            status_302 (int): Number of responses received with status code 302 (Found) from origin.. [optional]  # noqa: E501
            status_304 (int): Number of responses received with status code 304 (Not Modified) from origin.. [optional]  # noqa: E501
            status_400 (int): Number of responses received with status code 400 (Bad Request) from origin.. [optional]  # noqa: E501
            status_401 (int): Number of responses received with status code 401 (Unauthorized) from origin.. [optional]  # noqa: E501
            status_403 (int): Number of responses received with status code 403 (Forbidden) from origin.. [optional]  # noqa: E501
            status_404 (int): Number of responses received with status code 404 (Not Found) from origin.. [optional]  # noqa: E501
            status_416 (int): Number of responses received with status code 416 (Range Not Satisfiable) from origin.. [optional]  # noqa: E501
            status_429 (int): Number of responses received with status code 429 (Too Many Requests) from origin.. [optional]  # noqa: E501
            status_500 (int): Number of responses received with status code 500 (Internal Server Error) from origin.. [optional]  # noqa: E501
            status_501 (int): Number of responses received with status code 501 (Not Implemented) from origin.. [optional]  # noqa: E501
            status_502 (int): Number of responses received with status code 502 (Bad Gateway) from origin.. [optional]  # noqa: E501
            status_503 (int): Number of responses received with status code 503 (Service Unavailable) from origin.. [optional]  # noqa: E501
            status_504 (int): Number of responses received with status code 504 (Gateway Timeout) from origin.. [optional]  # noqa: E501
            status_505 (int): Number of responses received with status code 505 (HTTP Version Not Supported) from origin.. [optional]  # noqa: E501
            status_530 (int): Number of responses received from origin with status code 530.. [optional]  # noqa: E501
            latency_0_to_1ms (int): Number of responses from origin with latency between 0 and 1 millisecond.. [optional]  # noqa: E501
            latency_1_to_5ms (int): Number of responses from origin with latency between 1 and 5 milliseconds.. [optional]  # noqa: E501
            latency_5_to_10ms (int): Number of responses from origin with latency between 5 and 10 milliseconds.. [optional]  # noqa: E501
            latency_10_to_50ms (int): Number of responses from origin with latency between 10 and 50 milliseconds.. [optional]  # noqa: E501
            latency_50_to_100ms (int): Number of responses from origin with latency between 50 and 100 milliseconds.. [optional]  # noqa: E501
            latency_100_to_250ms (int): Number of responses from origin with latency between 100 and 250 milliseconds.. [optional]  # noqa: E501
            latency_250_to_500ms (int): Number of responses from origin with latency between 250 and 500 milliseconds.. [optional]  # noqa: E501
            latency_500_to_1000ms (int): Number of responses from origin with latency between 500 and 1,000 milliseconds.. [optional]  # noqa: E501
            latency_1000_to_5000ms (int): Number of responses from origin with latency between 1,000 and 5,000 milliseconds.. [optional]  # noqa: E501
            latency_5000_to_10000ms (int): Number of responses from origin with latency between 5,000 and 10,000 milliseconds.. [optional]  # noqa: E501
            latency_10000_to_60000ms (int): Number of responses from origin with latency between 10,000 and 60,000 milliseconds.. [optional]  # noqa: E501
            latency_60000ms (int): Number of responses from origin with latency of 60,000 milliseconds and above.. [optional]  # noqa: E501
            waf_responses (int): Number of responses received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_resp_header_bytes (int): Number of header bytes received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_resp_body_bytes (int): Number of body bytes received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_1xx (int): Number of 1xx \"Informational\" status codes received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_2xx (int): Number of 2xx \"Success\" status codes received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_3xx (int): Number of 3xx \"Redirection\" codes received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_4xx (int): Number of 4xx \"Client Error\" codes received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_5xx (int): Number of 5xx \"Server Error\" codes received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_200 (int): Number of responses received with status code 200 (Success) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_204 (int): Number of responses received with status code 204 (No Content) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_206 (int): Number of responses received with status code 206 (Partial Content) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_301 (int): Number of responses received with status code 301 (Moved Permanently) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_302 (int): Number of responses received with status code 302 (Found) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_304 (int): Number of responses received with status code 304 (Not Modified) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_400 (int): Number of responses received with status code 400 (Bad Request) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_401 (int): Number of responses received with status code 401 (Unauthorized) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_403 (int): Number of responses received with status code 403 (Forbidden) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_404 (int): Number of responses received with status code 404 (Not Found) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_416 (int): Number of responses received with status code 416 (Range Not Satisfiable) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_429 (int): Number of responses received with status code 429 (Too Many Requests) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_500 (int): Number of responses received with status code 500 (Internal Server Error) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_501 (int): Number of responses received with status code 501 (Not Implemented) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_502 (int): Number of responses received with status code 502 (Bad Gateway) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_503 (int): Number of responses received with status code 503 (Service Unavailable) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_504 (int): Number of responses received with status code 504 (Gateway Timeout) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_505 (int): Number of responses received with status code 505 (HTTP Version Not Supported) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_530 (int): Number of responses received with status code 530 received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_latency_0_to_1ms (int): Number of responses with latency between 0 and 1 millisecond received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_latency_1_to_5ms (int): Number of responses with latency between 1 and 5 milliseconds received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_latency_5_to_10ms (int): Number of responses with latency between 5 and 10 milliseconds received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_latency_10_to_50ms (int): Number of responses with latency between 10 and 50 milliseconds received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_latency_50_to_100ms (int): Number of responses with latency between 50 and 100 milliseconds received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_latency_100_to_250ms (int): Number of responses with latency between 100 and 250 milliseconds received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_latency_250_to_500ms (int): Number of responses with latency between 250 and 500 milliseconds received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_latency_500_to_1000ms (int): Number of responses with latency between 500 and 1,000 milliseconds received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_latency_1000_to_5000ms (int): Number of responses with latency between 1,000 and 5,000 milliseconds received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_latency_5000_to_10000ms (int): Number of responses with latency between 5,000 and 10,000 milliseconds received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_latency_10000_to_60000ms (int): Number of responses with latency between 10,000 and 60,000 milliseconds received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_latency_60000ms (int): Number of responses with latency of 60,000 milliseconds and above received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            compute_responses (int): Number of responses for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_resp_header_bytes (int): Number of header bytes for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_resp_body_bytes (int): Number of body bytes for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_1xx (int): Number of 1xx \"Informational\" status codes for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_2xx (int): Number of 2xx \"Success\" status codes for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_3xx (int): Number of 3xx \"Redirection\" codes for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_4xx (int): Number of 4xx \"Client Error\" codes for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_5xx (int): Number of 5xx \"Server Error\" codes for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_200 (int): Number of responses received with status code 200 (Success) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_204 (int): Number of responses received with status code 204 (No Content) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_206 (int): Number of responses received with status code 206 (Partial Content) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_301 (int): Number of responses received with status code 301 (Moved Permanently) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_302 (int): Number of responses received with status code 302 (Found) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_304 (int): Number of responses received with status code 304 (Not Modified) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_400 (int): Number of responses received with status code 400 (Bad Request) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_401 (int): Number of responses received with status code 401 (Unauthorized) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_403 (int): Number of responses received with status code 403 (Forbidden) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_404 (int): Number of responses received with status code 404 (Not Found) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_416 (int): Number of responses received with status code 416 (Range Not Satisfiable) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_429 (int): Number of responses received with status code 429 (Too Many Requests) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_500 (int): Number of responses received with status code 500 (Internal Server Error) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_501 (int): Number of responses received with status code 501 (Not Implemented) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_502 (int): Number of responses received with status code 502 (Bad Gateway) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_503 (int): Number of responses received with status code 503 (Service Unavailable) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_504 (int): Number of responses received with status code 504 (Gateway Timeout) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_505 (int): Number of responses received with status code 505 (HTTP Version Not Supported) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_530 (int): Number of responses received with status code 530 for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_latency_0_to_1ms (int): Number of responses with latency between 0 and 1 millisecond for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_latency_1_to_5ms (int): Number of responses with latency between 1 and 5 milliseconds for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_latency_5_to_10ms (int): Number of responses with latency between 5 and 10 milliseconds for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_latency_10_to_50ms (int): Number of responses with latency between 10 and 50 milliseconds for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_latency_50_to_100ms (int): Number of responses with latency between 50 and 100 milliseconds for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_latency_100_to_250ms (int): Number of responses with latency between 100 and 250 milliseconds for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_latency_250_to_500ms (int): Number of responses with latency between 250 and 500 milliseconds for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_latency_500_to_1000ms (int): Number of responses with latency between 500 and 1,000 milliseconds for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_latency_1000_to_5000ms (int): Number of responses with latency between 1,000 and 5,000 milliseconds for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_latency_5000_to_10000ms (int): Number of responses with latency between 5,000 and 10,000 milliseconds for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_latency_10000_to_60000ms (int): Number of responses with latency between 10,000 and 60,000 milliseconds for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_latency_60000ms (int): Number of responses with latency of 60,000 milliseconds and above for origin received by the Compute platform.. [optional]  # noqa: E501
            all_responses (int): Number of responses received for origin requests made by all sources.. [optional]  # noqa: E501
            all_resp_header_bytes (int): Number of header bytes received for origin requests made by all sources.. [optional]  # noqa: E501
            all_resp_body_bytes (int): Number of body bytes received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_1xx (int): Number of 1xx \"Informational\" category status codes delivered received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_2xx (int): Number of 2xx \"Success\" status codes received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_3xx (int): Number of 3xx \"Redirection\" codes received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_4xx (int): Number of 4xx \"Client Error\" codes received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_5xx (int): Number of 5xx \"Server Error\" codes received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_200 (int): Number of responses received with status code 200 (Success) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_204 (int): Number of responses received with status code 204 (No Content) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_206 (int): Number of responses received with status code 206 (Partial Content) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_301 (int): Number of responses received with status code 301 (Moved Permanently) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_302 (int): Number of responses received with status code 302 (Found) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_304 (int): Number of responses received with status code 304 (Not Modified) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_400 (int): Number of responses received with status code 400 (Bad Request) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_401 (int): Number of responses received with status code 401 (Unauthorized) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_403 (int): Number of responses received with status code 403 (Forbidden) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_404 (int): Number of responses received with status code 404 (Not Found) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_416 (int): Number of responses received with status code 416 (Range Not Satisfiable) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_429 (int): Number of responses received with status code 429 (Too Many Requests) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_500 (int): Number of responses received with status code 500 (Internal Server Error) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_501 (int): Number of responses received with status code 501 (Not Implemented) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_502 (int): Number of responses received with status code 502 (Bad Gateway) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_503 (int): Number of responses received with status code 503 (Service Unavailable) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_504 (int): Number of responses received with status code 504 (Gateway Timeout) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_505 (int): Number of responses received with status code 505 (HTTP Version Not Supported) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_530 (int): Number of responses received with status code 530 received for origin requests made by all sources.. [optional]  # noqa: E501
            all_latency_0_to_1ms (int): Number of responses with latency between 0 and 1 millisecond received for origin requests made by all sources.. [optional]  # noqa: E501
            all_latency_1_to_5ms (int): Number of responses with latency between 1 and 5 milliseconds received for origin requests made by all sources.. [optional]  # noqa: E501
            all_latency_5_to_10ms (int): Number of responses with latency between 5 and 10 milliseconds received for origin requests made by all sources.. [optional]  # noqa: E501
            all_latency_10_to_50ms (int): Number of responses with latency between 10 and 50 milliseconds received for origin requests made by all sources.. [optional]  # noqa: E501
            all_latency_50_to_100ms (int): Number of responses with latency between 50 and 100 milliseconds received for origin requests made by all sources.. [optional]  # noqa: E501
            all_latency_100_to_250ms (int): Number of responses with latency between 100 and 250 milliseconds received for origin requests made by all sources.. [optional]  # noqa: E501
            all_latency_250_to_500ms (int): Number of responses with latency between 250 and 500 milliseconds received for origin requests made by all sources.. [optional]  # noqa: E501
            all_latency_500_to_1000ms (int): Number of responses with latency between 500 and 1,000 milliseconds received for origin requests made by all sources.. [optional]  # noqa: E501
            all_latency_1000_to_5000ms (int): Number of responses with latency between 1,000 and 5,000 milliseconds received for origin requests made by all sources.. [optional]  # noqa: E501
            all_latency_5000_to_10000ms (int): Number of responses with latency between 5,000 and 10,000 milliseconds received for origin requests made by all sources.. [optional]  # noqa: E501
            all_latency_10000_to_60000ms (int): Number of responses with latency between 10,000 and 60,000 milliseconds received for origin requests made by all sources.. [optional]  # noqa: E501
            all_latency_60000ms (int): Number of responses with latency of 60,000 milliseconds and above received for origin requests made by all sources.. [optional]  # noqa: E501
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
        """OriginInspectorMeasurements - a model defined in OpenAPI

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
            responses (int): Number of responses from origin.. [optional]  # noqa: E501
            resp_header_bytes (int): Number of header bytes from origin.. [optional]  # noqa: E501
            resp_body_bytes (int): Number of body bytes from origin.. [optional]  # noqa: E501
            status_1xx (int): Number of 1xx \"Informational\" status codes delivered from origin.. [optional]  # noqa: E501
            status_2xx (int): Number of 2xx \"Success\" status codes delivered from origin.. [optional]  # noqa: E501
            status_3xx (int): Number of 3xx \"Redirection\" codes delivered from origin.. [optional]  # noqa: E501
            status_4xx (int): Number of 4xx \"Client Error\" codes delivered from origin.. [optional]  # noqa: E501
            status_5xx (int): Number of 5xx \"Server Error\" codes delivered from origin.. [optional]  # noqa: E501
            status_200 (int): Number of responses received with status code 200 (Success) from origin.. [optional]  # noqa: E501
            status_204 (int): Number of responses received with status code 204 (No Content) from origin.. [optional]  # noqa: E501
            status_206 (int): Number of responses received with status code 206 (Partial Content) from origin.. [optional]  # noqa: E501
            status_301 (int): Number of responses received with status code 301 (Moved Permanently) from origin.. [optional]  # noqa: E501
            status_302 (int): Number of responses received with status code 302 (Found) from origin.. [optional]  # noqa: E501
            status_304 (int): Number of responses received with status code 304 (Not Modified) from origin.. [optional]  # noqa: E501
            status_400 (int): Number of responses received with status code 400 (Bad Request) from origin.. [optional]  # noqa: E501
            status_401 (int): Number of responses received with status code 401 (Unauthorized) from origin.. [optional]  # noqa: E501
            status_403 (int): Number of responses received with status code 403 (Forbidden) from origin.. [optional]  # noqa: E501
            status_404 (int): Number of responses received with status code 404 (Not Found) from origin.. [optional]  # noqa: E501
            status_416 (int): Number of responses received with status code 416 (Range Not Satisfiable) from origin.. [optional]  # noqa: E501
            status_429 (int): Number of responses received with status code 429 (Too Many Requests) from origin.. [optional]  # noqa: E501
            status_500 (int): Number of responses received with status code 500 (Internal Server Error) from origin.. [optional]  # noqa: E501
            status_501 (int): Number of responses received with status code 501 (Not Implemented) from origin.. [optional]  # noqa: E501
            status_502 (int): Number of responses received with status code 502 (Bad Gateway) from origin.. [optional]  # noqa: E501
            status_503 (int): Number of responses received with status code 503 (Service Unavailable) from origin.. [optional]  # noqa: E501
            status_504 (int): Number of responses received with status code 504 (Gateway Timeout) from origin.. [optional]  # noqa: E501
            status_505 (int): Number of responses received with status code 505 (HTTP Version Not Supported) from origin.. [optional]  # noqa: E501
            status_530 (int): Number of responses received from origin with status code 530.. [optional]  # noqa: E501
            latency_0_to_1ms (int): Number of responses from origin with latency between 0 and 1 millisecond.. [optional]  # noqa: E501
            latency_1_to_5ms (int): Number of responses from origin with latency between 1 and 5 milliseconds.. [optional]  # noqa: E501
            latency_5_to_10ms (int): Number of responses from origin with latency between 5 and 10 milliseconds.. [optional]  # noqa: E501
            latency_10_to_50ms (int): Number of responses from origin with latency between 10 and 50 milliseconds.. [optional]  # noqa: E501
            latency_50_to_100ms (int): Number of responses from origin with latency between 50 and 100 milliseconds.. [optional]  # noqa: E501
            latency_100_to_250ms (int): Number of responses from origin with latency between 100 and 250 milliseconds.. [optional]  # noqa: E501
            latency_250_to_500ms (int): Number of responses from origin with latency between 250 and 500 milliseconds.. [optional]  # noqa: E501
            latency_500_to_1000ms (int): Number of responses from origin with latency between 500 and 1,000 milliseconds.. [optional]  # noqa: E501
            latency_1000_to_5000ms (int): Number of responses from origin with latency between 1,000 and 5,000 milliseconds.. [optional]  # noqa: E501
            latency_5000_to_10000ms (int): Number of responses from origin with latency between 5,000 and 10,000 milliseconds.. [optional]  # noqa: E501
            latency_10000_to_60000ms (int): Number of responses from origin with latency between 10,000 and 60,000 milliseconds.. [optional]  # noqa: E501
            latency_60000ms (int): Number of responses from origin with latency of 60,000 milliseconds and above.. [optional]  # noqa: E501
            waf_responses (int): Number of responses received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_resp_header_bytes (int): Number of header bytes received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_resp_body_bytes (int): Number of body bytes received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_1xx (int): Number of 1xx \"Informational\" status codes received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_2xx (int): Number of 2xx \"Success\" status codes received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_3xx (int): Number of 3xx \"Redirection\" codes received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_4xx (int): Number of 4xx \"Client Error\" codes received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_5xx (int): Number of 5xx \"Server Error\" codes received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_200 (int): Number of responses received with status code 200 (Success) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_204 (int): Number of responses received with status code 204 (No Content) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_206 (int): Number of responses received with status code 206 (Partial Content) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_301 (int): Number of responses received with status code 301 (Moved Permanently) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_302 (int): Number of responses received with status code 302 (Found) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_304 (int): Number of responses received with status code 304 (Not Modified) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_400 (int): Number of responses received with status code 400 (Bad Request) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_401 (int): Number of responses received with status code 401 (Unauthorized) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_403 (int): Number of responses received with status code 403 (Forbidden) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_404 (int): Number of responses received with status code 404 (Not Found) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_416 (int): Number of responses received with status code 416 (Range Not Satisfiable) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_429 (int): Number of responses received with status code 429 (Too Many Requests) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_500 (int): Number of responses received with status code 500 (Internal Server Error) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_501 (int): Number of responses received with status code 501 (Not Implemented) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_502 (int): Number of responses received with status code 502 (Bad Gateway) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_503 (int): Number of responses received with status code 503 (Service Unavailable) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_504 (int): Number of responses received with status code 504 (Gateway Timeout) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_505 (int): Number of responses received with status code 505 (HTTP Version Not Supported) received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_status_530 (int): Number of responses received with status code 530 received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_latency_0_to_1ms (int): Number of responses with latency between 0 and 1 millisecond received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_latency_1_to_5ms (int): Number of responses with latency between 1 and 5 milliseconds received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_latency_5_to_10ms (int): Number of responses with latency between 5 and 10 milliseconds received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_latency_10_to_50ms (int): Number of responses with latency between 10 and 50 milliseconds received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_latency_50_to_100ms (int): Number of responses with latency between 50 and 100 milliseconds received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_latency_100_to_250ms (int): Number of responses with latency between 100 and 250 milliseconds received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_latency_250_to_500ms (int): Number of responses with latency between 250 and 500 milliseconds received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_latency_500_to_1000ms (int): Number of responses with latency between 500 and 1,000 milliseconds received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_latency_1000_to_5000ms (int): Number of responses with latency between 1,000 and 5,000 milliseconds received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_latency_5000_to_10000ms (int): Number of responses with latency between 5,000 and 10,000 milliseconds received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_latency_10000_to_60000ms (int): Number of responses with latency between 10,000 and 60,000 milliseconds received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            waf_latency_60000ms (int): Number of responses with latency of 60,000 milliseconds and above received for origin requests made by the Fastly WAF.. [optional]  # noqa: E501
            compute_responses (int): Number of responses for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_resp_header_bytes (int): Number of header bytes for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_resp_body_bytes (int): Number of body bytes for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_1xx (int): Number of 1xx \"Informational\" status codes for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_2xx (int): Number of 2xx \"Success\" status codes for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_3xx (int): Number of 3xx \"Redirection\" codes for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_4xx (int): Number of 4xx \"Client Error\" codes for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_5xx (int): Number of 5xx \"Server Error\" codes for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_200 (int): Number of responses received with status code 200 (Success) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_204 (int): Number of responses received with status code 204 (No Content) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_206 (int): Number of responses received with status code 206 (Partial Content) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_301 (int): Number of responses received with status code 301 (Moved Permanently) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_302 (int): Number of responses received with status code 302 (Found) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_304 (int): Number of responses received with status code 304 (Not Modified) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_400 (int): Number of responses received with status code 400 (Bad Request) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_401 (int): Number of responses received with status code 401 (Unauthorized) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_403 (int): Number of responses received with status code 403 (Forbidden) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_404 (int): Number of responses received with status code 404 (Not Found) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_416 (int): Number of responses received with status code 416 (Range Not Satisfiable) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_429 (int): Number of responses received with status code 429 (Too Many Requests) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_500 (int): Number of responses received with status code 500 (Internal Server Error) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_501 (int): Number of responses received with status code 501 (Not Implemented) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_502 (int): Number of responses received with status code 502 (Bad Gateway) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_503 (int): Number of responses received with status code 503 (Service Unavailable) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_504 (int): Number of responses received with status code 504 (Gateway Timeout) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_505 (int): Number of responses received with status code 505 (HTTP Version Not Supported) for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_status_530 (int): Number of responses received with status code 530 for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_latency_0_to_1ms (int): Number of responses with latency between 0 and 1 millisecond for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_latency_1_to_5ms (int): Number of responses with latency between 1 and 5 milliseconds for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_latency_5_to_10ms (int): Number of responses with latency between 5 and 10 milliseconds for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_latency_10_to_50ms (int): Number of responses with latency between 10 and 50 milliseconds for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_latency_50_to_100ms (int): Number of responses with latency between 50 and 100 milliseconds for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_latency_100_to_250ms (int): Number of responses with latency between 100 and 250 milliseconds for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_latency_250_to_500ms (int): Number of responses with latency between 250 and 500 milliseconds for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_latency_500_to_1000ms (int): Number of responses with latency between 500 and 1,000 milliseconds for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_latency_1000_to_5000ms (int): Number of responses with latency between 1,000 and 5,000 milliseconds for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_latency_5000_to_10000ms (int): Number of responses with latency between 5,000 and 10,000 milliseconds for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_latency_10000_to_60000ms (int): Number of responses with latency between 10,000 and 60,000 milliseconds for origin received by the Compute platform.. [optional]  # noqa: E501
            compute_latency_60000ms (int): Number of responses with latency of 60,000 milliseconds and above for origin received by the Compute platform.. [optional]  # noqa: E501
            all_responses (int): Number of responses received for origin requests made by all sources.. [optional]  # noqa: E501
            all_resp_header_bytes (int): Number of header bytes received for origin requests made by all sources.. [optional]  # noqa: E501
            all_resp_body_bytes (int): Number of body bytes received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_1xx (int): Number of 1xx \"Informational\" category status codes delivered received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_2xx (int): Number of 2xx \"Success\" status codes received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_3xx (int): Number of 3xx \"Redirection\" codes received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_4xx (int): Number of 4xx \"Client Error\" codes received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_5xx (int): Number of 5xx \"Server Error\" codes received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_200 (int): Number of responses received with status code 200 (Success) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_204 (int): Number of responses received with status code 204 (No Content) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_206 (int): Number of responses received with status code 206 (Partial Content) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_301 (int): Number of responses received with status code 301 (Moved Permanently) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_302 (int): Number of responses received with status code 302 (Found) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_304 (int): Number of responses received with status code 304 (Not Modified) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_400 (int): Number of responses received with status code 400 (Bad Request) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_401 (int): Number of responses received with status code 401 (Unauthorized) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_403 (int): Number of responses received with status code 403 (Forbidden) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_404 (int): Number of responses received with status code 404 (Not Found) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_416 (int): Number of responses received with status code 416 (Range Not Satisfiable) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_429 (int): Number of responses received with status code 429 (Too Many Requests) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_500 (int): Number of responses received with status code 500 (Internal Server Error) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_501 (int): Number of responses received with status code 501 (Not Implemented) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_502 (int): Number of responses received with status code 502 (Bad Gateway) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_503 (int): Number of responses received with status code 503 (Service Unavailable) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_504 (int): Number of responses received with status code 504 (Gateway Timeout) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_505 (int): Number of responses received with status code 505 (HTTP Version Not Supported) received for origin requests made by all sources.. [optional]  # noqa: E501
            all_status_530 (int): Number of responses received with status code 530 received for origin requests made by all sources.. [optional]  # noqa: E501
            all_latency_0_to_1ms (int): Number of responses with latency between 0 and 1 millisecond received for origin requests made by all sources.. [optional]  # noqa: E501
            all_latency_1_to_5ms (int): Number of responses with latency between 1 and 5 milliseconds received for origin requests made by all sources.. [optional]  # noqa: E501
            all_latency_5_to_10ms (int): Number of responses with latency between 5 and 10 milliseconds received for origin requests made by all sources.. [optional]  # noqa: E501
            all_latency_10_to_50ms (int): Number of responses with latency between 10 and 50 milliseconds received for origin requests made by all sources.. [optional]  # noqa: E501
            all_latency_50_to_100ms (int): Number of responses with latency between 50 and 100 milliseconds received for origin requests made by all sources.. [optional]  # noqa: E501
            all_latency_100_to_250ms (int): Number of responses with latency between 100 and 250 milliseconds received for origin requests made by all sources.. [optional]  # noqa: E501
            all_latency_250_to_500ms (int): Number of responses with latency between 250 and 500 milliseconds received for origin requests made by all sources.. [optional]  # noqa: E501
            all_latency_500_to_1000ms (int): Number of responses with latency between 500 and 1,000 milliseconds received for origin requests made by all sources.. [optional]  # noqa: E501
            all_latency_1000_to_5000ms (int): Number of responses with latency between 1,000 and 5,000 milliseconds received for origin requests made by all sources.. [optional]  # noqa: E501
            all_latency_5000_to_10000ms (int): Number of responses with latency between 5,000 and 10,000 milliseconds received for origin requests made by all sources.. [optional]  # noqa: E501
            all_latency_10000_to_60000ms (int): Number of responses with latency between 10,000 and 60,000 milliseconds received for origin requests made by all sources.. [optional]  # noqa: E501
            all_latency_60000ms (int): Number of responses with latency of 60,000 milliseconds and above received for origin requests made by all sources.. [optional]  # noqa: E501
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
