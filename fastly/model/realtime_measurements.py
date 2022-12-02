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



class RealtimeMeasurements(ModelNormal):
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
            'requests': (int,),  # noqa: E501
            'logging': (int,),  # noqa: E501
            'log': (int,),  # noqa: E501
            'resp_header_bytes': (int,),  # noqa: E501
            'header_size': (int,),  # noqa: E501
            'resp_body_bytes': (int,),  # noqa: E501
            'body_size': (int,),  # noqa: E501
            'hits': (int,),  # noqa: E501
            'miss': (int,),  # noqa: E501
            '_pass': (int,),  # noqa: E501
            'synth': (int,),  # noqa: E501
            'errors': (int,),  # noqa: E501
            'hits_time': (float,),  # noqa: E501
            'miss_time': (float,),  # noqa: E501
            'miss_histogram': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'compute_requests': (int,),  # noqa: E501
            'compute_execution_time_ms': (float,),  # noqa: E501
            'compute_ram_used': (int,),  # noqa: E501
            'compute_request_time_ms': (float,),  # noqa: E501
            'shield': (int,),  # noqa: E501
            'ipv6': (int,),  # noqa: E501
            'imgopto': (int,),  # noqa: E501
            'imgopto_shield': (int,),  # noqa: E501
            'imgopto_transforms': (int,),  # noqa: E501
            'otfp': (int,),  # noqa: E501
            'otfp_shield': (int,),  # noqa: E501
            'otfp_manifests': (int,),  # noqa: E501
            'video': (int,),  # noqa: E501
            'pci': (int,),  # noqa: E501
            'http2': (int,),  # noqa: E501
            'http3': (int,),  # noqa: E501
            'restarts': (int,),  # noqa: E501
            'req_header_bytes': (int,),  # noqa: E501
            'req_body_bytes': (int,),  # noqa: E501
            'bereq_header_bytes': (int,),  # noqa: E501
            'bereq_body_bytes': (int,),  # noqa: E501
            'waf_blocked': (int,),  # noqa: E501
            'waf_logged': (int,),  # noqa: E501
            'waf_passed': (int,),  # noqa: E501
            'attack_req_header_bytes': (int,),  # noqa: E501
            'attack_req_body_bytes': (int,),  # noqa: E501
            'attack_resp_synth_bytes': (int,),  # noqa: E501
            'attack_logged_req_header_bytes': (int,),  # noqa: E501
            'attack_logged_req_body_bytes': (int,),  # noqa: E501
            'attack_blocked_req_header_bytes': (int,),  # noqa: E501
            'attack_blocked_req_body_bytes': (int,),  # noqa: E501
            'attack_passed_req_header_bytes': (int,),  # noqa: E501
            'attack_passed_req_body_bytes': (int,),  # noqa: E501
            'shield_resp_header_bytes': (int,),  # noqa: E501
            'shield_resp_body_bytes': (int,),  # noqa: E501
            'otfp_resp_header_bytes': (int,),  # noqa: E501
            'otfp_resp_body_bytes': (int,),  # noqa: E501
            'otfp_shield_resp_header_bytes': (int,),  # noqa: E501
            'otfp_shield_resp_body_bytes': (int,),  # noqa: E501
            'otfp_shield_time': (float,),  # noqa: E501
            'otfp_deliver_time': (float,),  # noqa: E501
            'imgopto_resp_header_bytes': (int,),  # noqa: E501
            'imgopto_resp_body_bytes': (int,),  # noqa: E501
            'imgopto_shield_resp_header_bytes': (int,),  # noqa: E501
            'imgopto_shield_resp_body_bytes': (int,),  # noqa: E501
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
            'status_406': (int,),  # noqa: E501
            'status_416': (int,),  # noqa: E501
            'status_429': (int,),  # noqa: E501
            'status_500': (int,),  # noqa: E501
            'status_501': (int,),  # noqa: E501
            'status_502': (int,),  # noqa: E501
            'status_503': (int,),  # noqa: E501
            'status_504': (int,),  # noqa: E501
            'status_505': (int,),  # noqa: E501
            'uncacheable': (int,),  # noqa: E501
            'pass_time': (float,),  # noqa: E501
            'tls': (int,),  # noqa: E501
            'tls_v10': (int,),  # noqa: E501
            'tls_v11': (int,),  # noqa: E501
            'tls_v12': (int,),  # noqa: E501
            'tls_v13': (int,),  # noqa: E501
            'object_size_1k': (int,),  # noqa: E501
            'object_size_10k': (int,),  # noqa: E501
            'object_size_100k': (int,),  # noqa: E501
            'object_size_1m': (int,),  # noqa: E501
            'object_size_10m': (int,),  # noqa: E501
            'object_size_100m': (int,),  # noqa: E501
            'object_size_1g': (int,),  # noqa: E501
            'object_size_other': (int,),  # noqa: E501
            'recv_sub_time': (float,),  # noqa: E501
            'recv_sub_count': (int,),  # noqa: E501
            'hash_sub_time': (float,),  # noqa: E501
            'hash_sub_count': (int,),  # noqa: E501
            'miss_sub_time': (float,),  # noqa: E501
            'miss_sub_count': (int,),  # noqa: E501
            'fetch_sub_time': (float,),  # noqa: E501
            'fetch_sub_count': (int,),  # noqa: E501
            'pass_sub_time': (float,),  # noqa: E501
            'pass_sub_count': (int,),  # noqa: E501
            'pipe_sub_time': (float,),  # noqa: E501
            'pipe_sub_count': (int,),  # noqa: E501
            'deliver_sub_time': (float,),  # noqa: E501
            'deliver_sub_count': (int,),  # noqa: E501
            'error_sub_time': (float,),  # noqa: E501
            'error_sub_count': (int,),  # noqa: E501
            'hit_sub_time': (float,),  # noqa: E501
            'hit_sub_count': (int,),  # noqa: E501
            'prehash_sub_time': (float,),  # noqa: E501
            'prehash_sub_count': (int,),  # noqa: E501
            'predeliver_sub_time': (float,),  # noqa: E501
            'predeliver_sub_count': (int,),  # noqa: E501
            'hit_resp_body_bytes': (int,),  # noqa: E501
            'miss_resp_body_bytes': (int,),  # noqa: E501
            'pass_resp_body_bytes': (int,),  # noqa: E501
            'compute_req_header_bytes': (int,),  # noqa: E501
            'compute_req_body_bytes': (int,),  # noqa: E501
            'compute_resp_header_bytes': (int,),  # noqa: E501
            'compute_resp_body_bytes': (int,),  # noqa: E501
            'imgvideo': (int,),  # noqa: E501
            'imgvideo_frames': (int,),  # noqa: E501
            'imgvideo_resp_header_bytes': (int,),  # noqa: E501
            'imgvideo_resp_body_bytes': (int,),  # noqa: E501
            'imgvideo_shield': (int,),  # noqa: E501
            'imgvideo_shield_frames': (int,),  # noqa: E501
            'imgvideo_shield_resp_header_bytes': (int,),  # noqa: E501
            'imgvideo_shield_resp_body_bytes': (int,),  # noqa: E501
            'log_bytes': (int,),  # noqa: E501
            'edge_requests': (int,),  # noqa: E501
            'edge_resp_header_bytes': (int,),  # noqa: E501
            'edge_resp_body_bytes': (int,),  # noqa: E501
            'origin_revalidations': (int,),  # noqa: E501
            'origin_fetches': (int,),  # noqa: E501
            'origin_fetch_header_bytes': (int,),  # noqa: E501
            'origin_fetch_body_bytes': (int,),  # noqa: E501
            'origin_fetch_resp_header_bytes': (int,),  # noqa: E501
            'origin_fetch_resp_body_bytes': (int,),  # noqa: E501
            'shield_revalidations': (int,),  # noqa: E501
            'shield_fetches': (int,),  # noqa: E501
            'shield_fetch_header_bytes': (int,),  # noqa: E501
            'shield_fetch_body_bytes': (int,),  # noqa: E501
            'shield_fetch_resp_header_bytes': (int,),  # noqa: E501
            'shield_fetch_resp_body_bytes': (int,),  # noqa: E501
            'segblock_origin_fetches': (int,),  # noqa: E501
            'segblock_shield_fetches': (int,),  # noqa: E501
            'compute_resp_status_1xx': (int,),  # noqa: E501
            'compute_resp_status_2xx': (int,),  # noqa: E501
            'compute_resp_status_3xx': (int,),  # noqa: E501
            'compute_resp_status_4xx': (int,),  # noqa: E501
            'compute_resp_status_5xx': (int,),  # noqa: E501
            'edge_hit_requests': (int,),  # noqa: E501
            'edge_miss_requests': (int,),  # noqa: E501
            'compute_bereq_header_bytes': (int,),  # noqa: E501
            'compute_bereq_body_bytes': (int,),  # noqa: E501
            'compute_beresp_header_bytes': (int,),  # noqa: E501
            'compute_beresp_body_bytes': (int,),  # noqa: E501
            'origin_cache_fetches': (int,),  # noqa: E501
            'shield_cache_fetches': (int,),  # noqa: E501
            'compute_bereqs': (int,),  # noqa: E501
            'compute_bereq_errors': (int,),  # noqa: E501
            'compute_resource_limit_exceeded': (int,),  # noqa: E501
            'compute_heap_limit_exceeded': (int,),  # noqa: E501
            'compute_stack_limit_exceeded': (int,),  # noqa: E501
            'compute_globals_limit_exceeded': (int,),  # noqa: E501
            'compute_guest_errors': (int,),  # noqa: E501
            'compute_runtime_errors': (int,),  # noqa: E501
            'edge_hit_resp_body_bytes': (int,),  # noqa: E501
            'edge_hit_resp_header_bytes': (int,),  # noqa: E501
            'edge_miss_resp_body_bytes': (int,),  # noqa: E501
            'edge_miss_resp_header_bytes': (int,),  # noqa: E501
            'origin_cache_fetch_resp_body_bytes': (int,),  # noqa: E501
            'origin_cache_fetch_resp_header_bytes': (int,),  # noqa: E501
            'shield_hit_requests': (int,),  # noqa: E501
            'shield_miss_requests': (int,),  # noqa: E501
            'shield_hit_resp_header_bytes': (int,),  # noqa: E501
            'shield_hit_resp_body_bytes': (int,),  # noqa: E501
            'shield_miss_resp_header_bytes': (int,),  # noqa: E501
            'shield_miss_resp_body_bytes': (int,),  # noqa: E501
            'websocket_req_header_bytes': (int,),  # noqa: E501
            'websocket_req_body_bytes': (int,),  # noqa: E501
            'websocket_resp_header_bytes': (int,),  # noqa: E501
            'websocket_bereq_header_bytes': (int,),  # noqa: E501
            'websocket_bereq_body_bytes': (int,),  # noqa: E501
            'websocket_beresp_header_bytes': (int,),  # noqa: E501
            'websocket_beresp_body_bytes': (int,),  # noqa: E501
            'websocket_conn_time_ms': (int,),  # noqa: E501
            'websocket_resp_body_bytes': (int,),  # noqa: E501
            'fanout_recv_publishes': (int,),  # noqa: E501
            'fanout_send_publishes': (int,),  # noqa: E501
            'object_store_read_requests': (int,),  # noqa: E501
            'object_store_write_requests': (int,),  # noqa: E501
            'fanout_req_header_bytes': (int,),  # noqa: E501
            'fanout_req_body_bytes': (int,),  # noqa: E501
            'fanout_resp_header_bytes': (int,),  # noqa: E501
            'fanout_resp_body_bytes': (int,),  # noqa: E501
            'fanout_bereq_header_bytes': (int,),  # noqa: E501
            'fanout_bereq_body_bytes': (int,),  # noqa: E501
            'fanout_beresp_header_bytes': (int,),  # noqa: E501
            'fanout_beresp_body_bytes': (int,),  # noqa: E501
            'fanout_conn_time_ms': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'requests': 'requests',  # noqa: E501
        'logging': 'logging',  # noqa: E501
        'log': 'log',  # noqa: E501
        'resp_header_bytes': 'resp_header_bytes',  # noqa: E501
        'header_size': 'header_size',  # noqa: E501
        'resp_body_bytes': 'resp_body_bytes',  # noqa: E501
        'body_size': 'body_size',  # noqa: E501
        'hits': 'hits',  # noqa: E501
        'miss': 'miss',  # noqa: E501
        '_pass': 'pass',  # noqa: E501
        'synth': 'synth',  # noqa: E501
        'errors': 'errors',  # noqa: E501
        'hits_time': 'hits_time',  # noqa: E501
        'miss_time': 'miss_time',  # noqa: E501
        'miss_histogram': 'miss_histogram',  # noqa: E501
        'compute_requests': 'compute_requests',  # noqa: E501
        'compute_execution_time_ms': 'compute_execution_time_ms',  # noqa: E501
        'compute_ram_used': 'compute_ram_used',  # noqa: E501
        'compute_request_time_ms': 'compute_request_time_ms',  # noqa: E501
        'shield': 'shield',  # noqa: E501
        'ipv6': 'ipv6',  # noqa: E501
        'imgopto': 'imgopto',  # noqa: E501
        'imgopto_shield': 'imgopto_shield',  # noqa: E501
        'imgopto_transforms': 'imgopto_transforms',  # noqa: E501
        'otfp': 'otfp',  # noqa: E501
        'otfp_shield': 'otfp_shield',  # noqa: E501
        'otfp_manifests': 'otfp_manifests',  # noqa: E501
        'video': 'video',  # noqa: E501
        'pci': 'pci',  # noqa: E501
        'http2': 'http2',  # noqa: E501
        'http3': 'http3',  # noqa: E501
        'restarts': 'restarts',  # noqa: E501
        'req_header_bytes': 'req_header_bytes',  # noqa: E501
        'req_body_bytes': 'req_body_bytes',  # noqa: E501
        'bereq_header_bytes': 'bereq_header_bytes',  # noqa: E501
        'bereq_body_bytes': 'bereq_body_bytes',  # noqa: E501
        'waf_blocked': 'waf_blocked',  # noqa: E501
        'waf_logged': 'waf_logged',  # noqa: E501
        'waf_passed': 'waf_passed',  # noqa: E501
        'attack_req_header_bytes': 'attack_req_header_bytes',  # noqa: E501
        'attack_req_body_bytes': 'attack_req_body_bytes',  # noqa: E501
        'attack_resp_synth_bytes': 'attack_resp_synth_bytes',  # noqa: E501
        'attack_logged_req_header_bytes': 'attack_logged_req_header_bytes',  # noqa: E501
        'attack_logged_req_body_bytes': 'attack_logged_req_body_bytes',  # noqa: E501
        'attack_blocked_req_header_bytes': 'attack_blocked_req_header_bytes',  # noqa: E501
        'attack_blocked_req_body_bytes': 'attack_blocked_req_body_bytes',  # noqa: E501
        'attack_passed_req_header_bytes': 'attack_passed_req_header_bytes',  # noqa: E501
        'attack_passed_req_body_bytes': 'attack_passed_req_body_bytes',  # noqa: E501
        'shield_resp_header_bytes': 'shield_resp_header_bytes',  # noqa: E501
        'shield_resp_body_bytes': 'shield_resp_body_bytes',  # noqa: E501
        'otfp_resp_header_bytes': 'otfp_resp_header_bytes',  # noqa: E501
        'otfp_resp_body_bytes': 'otfp_resp_body_bytes',  # noqa: E501
        'otfp_shield_resp_header_bytes': 'otfp_shield_resp_header_bytes',  # noqa: E501
        'otfp_shield_resp_body_bytes': 'otfp_shield_resp_body_bytes',  # noqa: E501
        'otfp_shield_time': 'otfp_shield_time',  # noqa: E501
        'otfp_deliver_time': 'otfp_deliver_time',  # noqa: E501
        'imgopto_resp_header_bytes': 'imgopto_resp_header_bytes',  # noqa: E501
        'imgopto_resp_body_bytes': 'imgopto_resp_body_bytes',  # noqa: E501
        'imgopto_shield_resp_header_bytes': 'imgopto_shield_resp_header_bytes',  # noqa: E501
        'imgopto_shield_resp_body_bytes': 'imgopto_shield_resp_body_bytes',  # noqa: E501
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
        'status_406': 'status_406',  # noqa: E501
        'status_416': 'status_416',  # noqa: E501
        'status_429': 'status_429',  # noqa: E501
        'status_500': 'status_500',  # noqa: E501
        'status_501': 'status_501',  # noqa: E501
        'status_502': 'status_502',  # noqa: E501
        'status_503': 'status_503',  # noqa: E501
        'status_504': 'status_504',  # noqa: E501
        'status_505': 'status_505',  # noqa: E501
        'uncacheable': 'uncacheable',  # noqa: E501
        'pass_time': 'pass_time',  # noqa: E501
        'tls': 'tls',  # noqa: E501
        'tls_v10': 'tls_v10',  # noqa: E501
        'tls_v11': 'tls_v11',  # noqa: E501
        'tls_v12': 'tls_v12',  # noqa: E501
        'tls_v13': 'tls_v13',  # noqa: E501
        'object_size_1k': 'object_size_1k',  # noqa: E501
        'object_size_10k': 'object_size_10k',  # noqa: E501
        'object_size_100k': 'object_size_100k',  # noqa: E501
        'object_size_1m': 'object_size_1m',  # noqa: E501
        'object_size_10m': 'object_size_10m',  # noqa: E501
        'object_size_100m': 'object_size_100m',  # noqa: E501
        'object_size_1g': 'object_size_1g',  # noqa: E501
        'object_size_other': 'object_size_other',  # noqa: E501
        'recv_sub_time': 'recv_sub_time',  # noqa: E501
        'recv_sub_count': 'recv_sub_count',  # noqa: E501
        'hash_sub_time': 'hash_sub_time',  # noqa: E501
        'hash_sub_count': 'hash_sub_count',  # noqa: E501
        'miss_sub_time': 'miss_sub_time',  # noqa: E501
        'miss_sub_count': 'miss_sub_count',  # noqa: E501
        'fetch_sub_time': 'fetch_sub_time',  # noqa: E501
        'fetch_sub_count': 'fetch_sub_count',  # noqa: E501
        'pass_sub_time': 'pass_sub_time',  # noqa: E501
        'pass_sub_count': 'pass_sub_count',  # noqa: E501
        'pipe_sub_time': 'pipe_sub_time',  # noqa: E501
        'pipe_sub_count': 'pipe_sub_count',  # noqa: E501
        'deliver_sub_time': 'deliver_sub_time',  # noqa: E501
        'deliver_sub_count': 'deliver_sub_count',  # noqa: E501
        'error_sub_time': 'error_sub_time',  # noqa: E501
        'error_sub_count': 'error_sub_count',  # noqa: E501
        'hit_sub_time': 'hit_sub_time',  # noqa: E501
        'hit_sub_count': 'hit_sub_count',  # noqa: E501
        'prehash_sub_time': 'prehash_sub_time',  # noqa: E501
        'prehash_sub_count': 'prehash_sub_count',  # noqa: E501
        'predeliver_sub_time': 'predeliver_sub_time',  # noqa: E501
        'predeliver_sub_count': 'predeliver_sub_count',  # noqa: E501
        'hit_resp_body_bytes': 'hit_resp_body_bytes',  # noqa: E501
        'miss_resp_body_bytes': 'miss_resp_body_bytes',  # noqa: E501
        'pass_resp_body_bytes': 'pass_resp_body_bytes',  # noqa: E501
        'compute_req_header_bytes': 'compute_req_header_bytes',  # noqa: E501
        'compute_req_body_bytes': 'compute_req_body_bytes',  # noqa: E501
        'compute_resp_header_bytes': 'compute_resp_header_bytes',  # noqa: E501
        'compute_resp_body_bytes': 'compute_resp_body_bytes',  # noqa: E501
        'imgvideo': 'imgvideo',  # noqa: E501
        'imgvideo_frames': 'imgvideo_frames',  # noqa: E501
        'imgvideo_resp_header_bytes': 'imgvideo_resp_header_bytes',  # noqa: E501
        'imgvideo_resp_body_bytes': 'imgvideo_resp_body_bytes',  # noqa: E501
        'imgvideo_shield': 'imgvideo_shield',  # noqa: E501
        'imgvideo_shield_frames': 'imgvideo_shield_frames',  # noqa: E501
        'imgvideo_shield_resp_header_bytes': 'imgvideo_shield_resp_header_bytes',  # noqa: E501
        'imgvideo_shield_resp_body_bytes': 'imgvideo_shield_resp_body_bytes',  # noqa: E501
        'log_bytes': 'log_bytes',  # noqa: E501
        'edge_requests': 'edge_requests',  # noqa: E501
        'edge_resp_header_bytes': 'edge_resp_header_bytes',  # noqa: E501
        'edge_resp_body_bytes': 'edge_resp_body_bytes',  # noqa: E501
        'origin_revalidations': 'origin_revalidations',  # noqa: E501
        'origin_fetches': 'origin_fetches',  # noqa: E501
        'origin_fetch_header_bytes': 'origin_fetch_header_bytes',  # noqa: E501
        'origin_fetch_body_bytes': 'origin_fetch_body_bytes',  # noqa: E501
        'origin_fetch_resp_header_bytes': 'origin_fetch_resp_header_bytes',  # noqa: E501
        'origin_fetch_resp_body_bytes': 'origin_fetch_resp_body_bytes',  # noqa: E501
        'shield_revalidations': 'shield_revalidations',  # noqa: E501
        'shield_fetches': 'shield_fetches',  # noqa: E501
        'shield_fetch_header_bytes': 'shield_fetch_header_bytes',  # noqa: E501
        'shield_fetch_body_bytes': 'shield_fetch_body_bytes',  # noqa: E501
        'shield_fetch_resp_header_bytes': 'shield_fetch_resp_header_bytes',  # noqa: E501
        'shield_fetch_resp_body_bytes': 'shield_fetch_resp_body_bytes',  # noqa: E501
        'segblock_origin_fetches': 'segblock_origin_fetches',  # noqa: E501
        'segblock_shield_fetches': 'segblock_shield_fetches',  # noqa: E501
        'compute_resp_status_1xx': 'compute_resp_status_1xx',  # noqa: E501
        'compute_resp_status_2xx': 'compute_resp_status_2xx',  # noqa: E501
        'compute_resp_status_3xx': 'compute_resp_status_3xx',  # noqa: E501
        'compute_resp_status_4xx': 'compute_resp_status_4xx',  # noqa: E501
        'compute_resp_status_5xx': 'compute_resp_status_5xx',  # noqa: E501
        'edge_hit_requests': 'edge_hit_requests',  # noqa: E501
        'edge_miss_requests': 'edge_miss_requests',  # noqa: E501
        'compute_bereq_header_bytes': 'compute_bereq_header_bytes',  # noqa: E501
        'compute_bereq_body_bytes': 'compute_bereq_body_bytes',  # noqa: E501
        'compute_beresp_header_bytes': 'compute_beresp_header_bytes',  # noqa: E501
        'compute_beresp_body_bytes': 'compute_beresp_body_bytes',  # noqa: E501
        'origin_cache_fetches': 'origin_cache_fetches',  # noqa: E501
        'shield_cache_fetches': 'shield_cache_fetches',  # noqa: E501
        'compute_bereqs': 'compute_bereqs',  # noqa: E501
        'compute_bereq_errors': 'compute_bereq_errors',  # noqa: E501
        'compute_resource_limit_exceeded': 'compute_resource_limit_exceeded',  # noqa: E501
        'compute_heap_limit_exceeded': 'compute_heap_limit_exceeded',  # noqa: E501
        'compute_stack_limit_exceeded': 'compute_stack_limit_exceeded',  # noqa: E501
        'compute_globals_limit_exceeded': 'compute_globals_limit_exceeded',  # noqa: E501
        'compute_guest_errors': 'compute_guest_errors',  # noqa: E501
        'compute_runtime_errors': 'compute_runtime_errors',  # noqa: E501
        'edge_hit_resp_body_bytes': 'edge_hit_resp_body_bytes',  # noqa: E501
        'edge_hit_resp_header_bytes': 'edge_hit_resp_header_bytes',  # noqa: E501
        'edge_miss_resp_body_bytes': 'edge_miss_resp_body_bytes',  # noqa: E501
        'edge_miss_resp_header_bytes': 'edge_miss_resp_header_bytes',  # noqa: E501
        'origin_cache_fetch_resp_body_bytes': 'origin_cache_fetch_resp_body_bytes',  # noqa: E501
        'origin_cache_fetch_resp_header_bytes': 'origin_cache_fetch_resp_header_bytes',  # noqa: E501
        'shield_hit_requests': 'shield_hit_requests',  # noqa: E501
        'shield_miss_requests': 'shield_miss_requests',  # noqa: E501
        'shield_hit_resp_header_bytes': 'shield_hit_resp_header_bytes',  # noqa: E501
        'shield_hit_resp_body_bytes': 'shield_hit_resp_body_bytes',  # noqa: E501
        'shield_miss_resp_header_bytes': 'shield_miss_resp_header_bytes',  # noqa: E501
        'shield_miss_resp_body_bytes': 'shield_miss_resp_body_bytes',  # noqa: E501
        'websocket_req_header_bytes': 'websocket_req_header_bytes',  # noqa: E501
        'websocket_req_body_bytes': 'websocket_req_body_bytes',  # noqa: E501
        'websocket_resp_header_bytes': 'websocket_resp_header_bytes',  # noqa: E501
        'websocket_bereq_header_bytes': 'websocket_bereq_header_bytes',  # noqa: E501
        'websocket_bereq_body_bytes': 'websocket_bereq_body_bytes',  # noqa: E501
        'websocket_beresp_header_bytes': 'websocket_beresp_header_bytes',  # noqa: E501
        'websocket_beresp_body_bytes': 'websocket_beresp_body_bytes',  # noqa: E501
        'websocket_conn_time_ms': 'websocket_conn_time_ms',  # noqa: E501
        'websocket_resp_body_bytes': 'websocket_resp_body_bytes',  # noqa: E501
        'fanout_recv_publishes': 'fanout_recv_publishes',  # noqa: E501
        'fanout_send_publishes': 'fanout_send_publishes',  # noqa: E501
        'object_store_read_requests': 'object_store_read_requests',  # noqa: E501
        'object_store_write_requests': 'object_store_write_requests',  # noqa: E501
        'fanout_req_header_bytes': 'fanout_req_header_bytes',  # noqa: E501
        'fanout_req_body_bytes': 'fanout_req_body_bytes',  # noqa: E501
        'fanout_resp_header_bytes': 'fanout_resp_header_bytes',  # noqa: E501
        'fanout_resp_body_bytes': 'fanout_resp_body_bytes',  # noqa: E501
        'fanout_bereq_header_bytes': 'fanout_bereq_header_bytes',  # noqa: E501
        'fanout_bereq_body_bytes': 'fanout_bereq_body_bytes',  # noqa: E501
        'fanout_beresp_header_bytes': 'fanout_beresp_header_bytes',  # noqa: E501
        'fanout_beresp_body_bytes': 'fanout_beresp_body_bytes',  # noqa: E501
        'fanout_conn_time_ms': 'fanout_conn_time_ms',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """RealtimeMeasurements - a model defined in OpenAPI

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
            requests (int): Number of requests processed.. [optional]  # noqa: E501
            logging (int): Number of log lines sent (alias for `log`).. [optional]  # noqa: E501
            log (int): Number of log lines sent.. [optional]  # noqa: E501
            resp_header_bytes (int): Total header bytes delivered (edge_resp_header_bytes + shield_resp_header_bytes).. [optional]  # noqa: E501
            header_size (int): Total header bytes delivered (alias for resp_header_bytes).. [optional]  # noqa: E501
            resp_body_bytes (int): Total body bytes delivered (edge_resp_body_bytes + shield_resp_body_bytes).. [optional]  # noqa: E501
            body_size (int): Total body bytes delivered (alias for resp_body_bytes).. [optional]  # noqa: E501
            hits (int): Number of cache hits.. [optional]  # noqa: E501
            miss (int): Number of cache misses.. [optional]  # noqa: E501
            _pass (int): Number of requests that passed through the CDN without being cached.. [optional]  # noqa: E501
            synth (int): Number of requests that returned a synthetic response (i.e., response objects created with the `synthetic` VCL statement).. [optional]  # noqa: E501
            errors (int): Number of cache errors.. [optional]  # noqa: E501
            hits_time (float): Total amount of time spent processing cache hits (in seconds).. [optional]  # noqa: E501
            miss_time (float): Total amount of time spent processing cache misses (in seconds).. [optional]  # noqa: E501
            miss_histogram ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): A histogram. Each key represents the upper bound of a span of 10 milliseconds and the values represent the number of requests to origin during that 10ms period. Any origin request that takes more than 60 seconds to return will be in the 60000 bucket.. [optional]  # noqa: E501
            compute_requests (int): The total number of requests that were received for your service by Fastly.. [optional]  # noqa: E501
            compute_execution_time_ms (float): The amount of active CPU time used to process your requests (in milliseconds).. [optional]  # noqa: E501
            compute_ram_used (int): The amount of RAM used for your service by Fastly (in bytes).. [optional]  # noqa: E501
            compute_request_time_ms (float): The total, actual amount of time used to process your requests, including active CPU time (in milliseconds).. [optional]  # noqa: E501
            shield (int): Number of requests from edge to the shield POP.. [optional]  # noqa: E501
            ipv6 (int): Number of requests that were received over IPv6.. [optional]  # noqa: E501
            imgopto (int): Number of responses that came from the Fastly Image Optimizer service. If the service receives 10 requests for an image, this stat will be 10 regardless of how many times the image was transformed.. [optional]  # noqa: E501
            imgopto_shield (int): Number of responses that came from the Fastly Image Optimizer service via a shield.. [optional]  # noqa: E501
            imgopto_transforms (int): Number of transforms performed by the Fastly Image Optimizer service.. [optional]  # noqa: E501
            otfp (int): Number of responses that came from the Fastly On-the-Fly Packaging service for video-on-demand.. [optional]  # noqa: E501
            otfp_shield (int): Number of responses that came from the Fastly On-the-Fly Packaging service for video-on-demand via a shield.. [optional]  # noqa: E501
            otfp_manifests (int): Number of responses that were manifest files from the Fastly On-the-Fly Packaging service for video-on-demand.. [optional]  # noqa: E501
            video (int): Number of responses with the video segment or video manifest MIME type (i.e., application/x-mpegurl, application/vnd.apple.mpegurl, application/f4m, application/dash+xml, application/vnd.ms-sstr+xml, ideo/mp2t, audio/aac, video/f4f, video/x-flv, video/mp4, audio/mp4).. [optional]  # noqa: E501
            pci (int): Number of responses with the PCI flag turned on.. [optional]  # noqa: E501
            http2 (int): Number of requests received over HTTP/2.. [optional]  # noqa: E501
            http3 (int): Number of requests received over HTTP/3.. [optional]  # noqa: E501
            restarts (int): Number of restarts performed.. [optional]  # noqa: E501
            req_header_bytes (int): Total header bytes received.. [optional]  # noqa: E501
            req_body_bytes (int): Total body bytes received.. [optional]  # noqa: E501
            bereq_header_bytes (int): Total header bytes sent to origin.. [optional]  # noqa: E501
            bereq_body_bytes (int): Total body bytes sent to origin.. [optional]  # noqa: E501
            waf_blocked (int): Number of requests that triggered a WAF rule and were blocked.. [optional]  # noqa: E501
            waf_logged (int): Number of requests that triggered a WAF rule and were logged.. [optional]  # noqa: E501
            waf_passed (int): Number of requests that triggered a WAF rule and were passed.. [optional]  # noqa: E501
            attack_req_header_bytes (int): Total header bytes received from requests that triggered a WAF rule.. [optional]  # noqa: E501
            attack_req_body_bytes (int): Total body bytes received from requests that triggered a WAF rule.. [optional]  # noqa: E501
            attack_resp_synth_bytes (int): Total bytes delivered for requests that triggered a WAF rule and returned a synthetic response.. [optional]  # noqa: E501
            attack_logged_req_header_bytes (int): Total header bytes received from requests that triggered a WAF rule that was logged.. [optional]  # noqa: E501
            attack_logged_req_body_bytes (int): Total body bytes received from requests that triggered a WAF rule that was logged.. [optional]  # noqa: E501
            attack_blocked_req_header_bytes (int): Total header bytes received from requests that triggered a WAF rule that was blocked.. [optional]  # noqa: E501
            attack_blocked_req_body_bytes (int): Total body bytes received from requests that triggered a WAF rule that was blocked.. [optional]  # noqa: E501
            attack_passed_req_header_bytes (int): Total header bytes received from requests that triggered a WAF rule that was passed.. [optional]  # noqa: E501
            attack_passed_req_body_bytes (int): Total body bytes received from requests that triggered a WAF rule that was passed.. [optional]  # noqa: E501
            shield_resp_header_bytes (int): Total header bytes delivered via a shield.. [optional]  # noqa: E501
            shield_resp_body_bytes (int): Total body bytes delivered via a shield.. [optional]  # noqa: E501
            otfp_resp_header_bytes (int): Total header bytes delivered from the Fastly On-the-Fly Packaging service for video-on-demand.. [optional]  # noqa: E501
            otfp_resp_body_bytes (int): Total body bytes delivered from the Fastly On-the-Fly Packaging service for video-on-demand.. [optional]  # noqa: E501
            otfp_shield_resp_header_bytes (int): Total header bytes delivered via a shield for the Fastly On-the-Fly Packaging service for video-on-demand.. [optional]  # noqa: E501
            otfp_shield_resp_body_bytes (int): Total body bytes delivered via a shield for the Fastly On-the-Fly Packaging service for video-on-demand.. [optional]  # noqa: E501
            otfp_shield_time (float): Total amount of time spent delivering a response via a shield from the Fastly On-the-Fly Packaging service for video-on-demand (in seconds).. [optional]  # noqa: E501
            otfp_deliver_time (float): Total amount of time spent delivering a response from the Fastly On-the-Fly Packaging service for video-on-demand (in seconds).. [optional]  # noqa: E501
            imgopto_resp_header_bytes (int): Total header bytes delivered from the Fastly Image Optimizer service, including shield traffic.. [optional]  # noqa: E501
            imgopto_resp_body_bytes (int): Total body bytes delivered from the Fastly Image Optimizer service, including shield traffic.. [optional]  # noqa: E501
            imgopto_shield_resp_header_bytes (int): Total header bytes delivered via a shield from the Fastly Image Optimizer service.. [optional]  # noqa: E501
            imgopto_shield_resp_body_bytes (int): Total body bytes delivered via a shield from the Fastly Image Optimizer service.. [optional]  # noqa: E501
            status_1xx (int): Number of \"Informational\" category status codes delivered.. [optional]  # noqa: E501
            status_2xx (int): Number of \"Success\" status codes delivered.. [optional]  # noqa: E501
            status_3xx (int): Number of \"Redirection\" codes delivered.. [optional]  # noqa: E501
            status_4xx (int): Number of \"Client Error\" codes delivered.. [optional]  # noqa: E501
            status_5xx (int): Number of \"Server Error\" codes delivered.. [optional]  # noqa: E501
            status_200 (int): Number of responses sent with status code 200 (Success).. [optional]  # noqa: E501
            status_204 (int): Number of responses sent with status code 204 (No Content).. [optional]  # noqa: E501
            status_206 (int): Number of responses sent with status code 206 (Partial Content).. [optional]  # noqa: E501
            status_301 (int): Number of responses sent with status code 301 (Moved Permanently).. [optional]  # noqa: E501
            status_302 (int): Number of responses sent with status code 302 (Found).. [optional]  # noqa: E501
            status_304 (int): Number of responses sent with status code 304 (Not Modified).. [optional]  # noqa: E501
            status_400 (int): Number of responses sent with status code 400 (Bad Request).. [optional]  # noqa: E501
            status_401 (int): Number of responses sent with status code 401 (Unauthorized).. [optional]  # noqa: E501
            status_403 (int): Number of responses sent with status code 403 (Forbidden).. [optional]  # noqa: E501
            status_404 (int): Number of responses sent with status code 404 (Not Found).. [optional]  # noqa: E501
            status_406 (int): Number of responses sent with status code 406 (Not Acceptable).. [optional]  # noqa: E501
            status_416 (int): Number of responses sent with status code 416 (Range Not Satisfiable).. [optional]  # noqa: E501
            status_429 (int): Number of responses sent with status code 429 (Too Many Requests).. [optional]  # noqa: E501
            status_500 (int): Number of responses sent with status code 500 (Internal Server Error).. [optional]  # noqa: E501
            status_501 (int): Number of responses sent with status code 501 (Not Implemented).. [optional]  # noqa: E501
            status_502 (int): Number of responses sent with status code 502 (Bad Gateway).. [optional]  # noqa: E501
            status_503 (int): Number of responses sent with status code 503 (Service Unavailable).. [optional]  # noqa: E501
            status_504 (int): Number of responses sent with status code 504 (Gateway Timeout).. [optional]  # noqa: E501
            status_505 (int): Number of responses sent with status code 505 (HTTP Version Not Supported).. [optional]  # noqa: E501
            uncacheable (int): Number of requests that were designated uncachable.. [optional]  # noqa: E501
            pass_time (float): Total amount of time spent processing cache passes (in seconds).. [optional]  # noqa: E501
            tls (int): Number of requests that were received over TLS.. [optional]  # noqa: E501
            tls_v10 (int): Number of requests received over TLS 1.0.. [optional]  # noqa: E501
            tls_v11 (int): Number of requests received over TLS 1.1.. [optional]  # noqa: E501
            tls_v12 (int): Number of requests received over TLS 1.2.. [optional]  # noqa: E501
            tls_v13 (int): Number of requests received over TLS 1.3.. [optional]  # noqa: E501
            object_size_1k (int): Number of objects served that were under 1KB in size.. [optional]  # noqa: E501
            object_size_10k (int): Number of objects served that were between 1KB and 10KB in size.. [optional]  # noqa: E501
            object_size_100k (int): Number of objects served that were between 10KB and 100KB in size.. [optional]  # noqa: E501
            object_size_1m (int): Number of objects served that were between 100KB and 1MB in size.. [optional]  # noqa: E501
            object_size_10m (int): Number of objects served that were between 1MB and 10MB in size.. [optional]  # noqa: E501
            object_size_100m (int): Number of objects served that were between 10MB and 100MB in size.. [optional]  # noqa: E501
            object_size_1g (int): Number of objects served that were between 100MB and 1GB in size.. [optional]  # noqa: E501
            object_size_other (int): Number of objects served that were larger than 1GB in size.. [optional]  # noqa: E501
            recv_sub_time (float): Time spent inside the `vcl_recv` Varnish subroutine (in nanoseconds).. [optional]  # noqa: E501
            recv_sub_count (int): Number of executions of the `vcl_recv` Varnish subroutine.. [optional]  # noqa: E501
            hash_sub_time (float): Time spent inside the `vcl_hash` Varnish subroutine (in nanoseconds).. [optional]  # noqa: E501
            hash_sub_count (int): Number of executions of the `vcl_hash` Varnish subroutine.. [optional]  # noqa: E501
            miss_sub_time (float): Time spent inside the `vcl_miss` Varnish subroutine (in nanoseconds).. [optional]  # noqa: E501
            miss_sub_count (int): Number of executions of the `vcl_miss` Varnish subroutine.. [optional]  # noqa: E501
            fetch_sub_time (float): Time spent inside the `vcl_fetch` Varnish subroutine (in nanoseconds).. [optional]  # noqa: E501
            fetch_sub_count (int): Number of executions of the `vcl_fetch` Varnish subroutine.. [optional]  # noqa: E501
            pass_sub_time (float): Time spent inside the `vcl_pass` Varnish subroutine (in nanoseconds).. [optional]  # noqa: E501
            pass_sub_count (int): Number of executions of the `vcl_pass` Varnish subroutine.. [optional]  # noqa: E501
            pipe_sub_time (float): Time spent inside the `vcl_pipe` Varnish subroutine (in nanoseconds).. [optional]  # noqa: E501
            pipe_sub_count (int): Number of executions of the `vcl_pipe` Varnish subroutine.. [optional]  # noqa: E501
            deliver_sub_time (float): Time spent inside the `vcl_deliver` Varnish subroutine (in nanoseconds).. [optional]  # noqa: E501
            deliver_sub_count (int): Number of executions of the `vcl_deliver` Varnish subroutine.. [optional]  # noqa: E501
            error_sub_time (float): Time spent inside the `vcl_error` Varnish subroutine (in nanoseconds).. [optional]  # noqa: E501
            error_sub_count (int): Number of executions of the `vcl_error` Varnish subroutine.. [optional]  # noqa: E501
            hit_sub_time (float): Time spent inside the `vcl_hit` Varnish subroutine (in nanoseconds).. [optional]  # noqa: E501
            hit_sub_count (int): Number of executions of the `vcl_hit` Varnish subroutine.. [optional]  # noqa: E501
            prehash_sub_time (float): Time spent inside the `vcl_prehash` Varnish subroutine (in nanoseconds).. [optional]  # noqa: E501
            prehash_sub_count (int): Number of executions of the `vcl_prehash` Varnish subroutine.. [optional]  # noqa: E501
            predeliver_sub_time (float): Time spent inside the `vcl_predeliver` Varnish subroutine (in nanoseconds).. [optional]  # noqa: E501
            predeliver_sub_count (int): Number of executions of the `vcl_predeliver` Varnish subroutine.. [optional]  # noqa: E501
            hit_resp_body_bytes (int): Total body bytes delivered for cache hits.. [optional]  # noqa: E501
            miss_resp_body_bytes (int): Total body bytes delivered for cache misses.. [optional]  # noqa: E501
            pass_resp_body_bytes (int): Total body bytes delivered for cache passes.. [optional]  # noqa: E501
            compute_req_header_bytes (int): Total header bytes received by Compute@Edge.. [optional]  # noqa: E501
            compute_req_body_bytes (int): Total body bytes received by Compute@Edge.. [optional]  # noqa: E501
            compute_resp_header_bytes (int): Total header bytes sent from Compute@Edge to end user.. [optional]  # noqa: E501
            compute_resp_body_bytes (int): Total body bytes sent from Compute@Edge to end user.. [optional]  # noqa: E501
            imgvideo (int): Number of video responses that came from the Fastly Image Optimizer service.. [optional]  # noqa: E501
            imgvideo_frames (int): Number of video frames that came from the Fastly Image Optimizer service. A video frame is an individual image within a sequence of video.. [optional]  # noqa: E501
            imgvideo_resp_header_bytes (int): Total header bytes of video delivered from the Fastly Image Optimizer service.. [optional]  # noqa: E501
            imgvideo_resp_body_bytes (int): Total body bytes of video delivered from the Fastly Image Optimizer service.. [optional]  # noqa: E501
            imgvideo_shield (int): Number of video responses delivered via a shield that came from the Fastly Image Optimizer service.. [optional]  # noqa: E501
            imgvideo_shield_frames (int): Number of video frames delivered via a shield that came from the Fastly Image Optimizer service. A video frame is an individual image within a sequence of video.. [optional]  # noqa: E501
            imgvideo_shield_resp_header_bytes (int): Total header bytes of video delivered via a shield from the Fastly Image Optimizer service.. [optional]  # noqa: E501
            imgvideo_shield_resp_body_bytes (int): Total body bytes of video delivered via a shield from the Fastly Image Optimizer service.. [optional]  # noqa: E501
            log_bytes (int): Total log bytes sent.. [optional]  # noqa: E501
            edge_requests (int): Number of requests sent by end users to Fastly.. [optional]  # noqa: E501
            edge_resp_header_bytes (int): Total header bytes delivered from Fastly to the end user.. [optional]  # noqa: E501
            edge_resp_body_bytes (int): Total body bytes delivered from Fastly to the end user.. [optional]  # noqa: E501
            origin_revalidations (int): Number of responses received from origin with a `304` status code in response to an `If-Modified-Since` or `If-None-Match` request. Under regular scenarios, a revalidation will imply a cache hit. However, if using Fastly Image Optimizer or segmented caching this may result in a cache miss.. [optional]  # noqa: E501
            origin_fetches (int): Number of requests sent to origin.. [optional]  # noqa: E501
            origin_fetch_header_bytes (int): Total request header bytes sent to origin.. [optional]  # noqa: E501
            origin_fetch_body_bytes (int): Total request body bytes sent to origin.. [optional]  # noqa: E501
            origin_fetch_resp_header_bytes (int): Total header bytes received from origin.. [optional]  # noqa: E501
            origin_fetch_resp_body_bytes (int): Total body bytes received from origin.. [optional]  # noqa: E501
            shield_revalidations (int): Number of responses received from origin with a `304` status code, in response to an `If-Modified-Since` or `If-None-Match` request to a shield. Under regular scenarios, a revalidation will imply a cache hit. However, if using segmented caching this may result in a cache miss.. [optional]  # noqa: E501
            shield_fetches (int): Number of requests made from one Fastly POP to another, as part of shielding.. [optional]  # noqa: E501
            shield_fetch_header_bytes (int): Total request header bytes sent to a shield.. [optional]  # noqa: E501
            shield_fetch_body_bytes (int): Total request body bytes sent to a shield.. [optional]  # noqa: E501
            shield_fetch_resp_header_bytes (int): Total response header bytes sent from a shield to the edge.. [optional]  # noqa: E501
            shield_fetch_resp_body_bytes (int): Total response body bytes sent from a shield to the edge.. [optional]  # noqa: E501
            segblock_origin_fetches (int): Number of `Range` requests to origin for segments of resources when using segmented caching.. [optional]  # noqa: E501
            segblock_shield_fetches (int): Number of `Range` requests to a shield for segments of resources when using segmented caching.. [optional]  # noqa: E501
            compute_resp_status_1xx (int): Number of \"Informational\" category status codes delivered by Compute@Edge.. [optional]  # noqa: E501
            compute_resp_status_2xx (int): Number of \"Success\" category status codes delivered by Compute@Edge.. [optional]  # noqa: E501
            compute_resp_status_3xx (int): Number of \"Redirection\" category status codes delivered by Compute@Edge.. [optional]  # noqa: E501
            compute_resp_status_4xx (int): Number of \"Client Error\" category status codes delivered by Compute@Edge.. [optional]  # noqa: E501
            compute_resp_status_5xx (int): Number of \"Server Error\" category status codes delivered by Compute@Edge.. [optional]  # noqa: E501
            edge_hit_requests (int): Number of requests sent by end users to Fastly that resulted in a hit at the edge.. [optional]  # noqa: E501
            edge_miss_requests (int): Number of requests sent by end users to Fastly that resulted in a miss at the edge.. [optional]  # noqa: E501
            compute_bereq_header_bytes (int): Total header bytes sent to backends (origins) by Compute@Edge.. [optional]  # noqa: E501
            compute_bereq_body_bytes (int): Total body bytes sent to backends (origins) by Compute@Edge.. [optional]  # noqa: E501
            compute_beresp_header_bytes (int): Total header bytes received from backends (origins) by Compute@Edge.. [optional]  # noqa: E501
            compute_beresp_body_bytes (int): Total body bytes received from backends (origins) by Compute@Edge.. [optional]  # noqa: E501
            origin_cache_fetches (int): The total number of completed requests made to backends (origins) that returned cacheable content.. [optional]  # noqa: E501
            shield_cache_fetches (int): The total number of completed requests made to shields that returned cacheable content.. [optional]  # noqa: E501
            compute_bereqs (int): Number of backend requests started.. [optional]  # noqa: E501
            compute_bereq_errors (int): Number of backend request errors, including timeouts.. [optional]  # noqa: E501
            compute_resource_limit_exceeded (int): Number of times a guest exceeded its resource limit, includes heap, stack, globals, and code execution timeout.. [optional]  # noqa: E501
            compute_heap_limit_exceeded (int): Number of times a guest exceeded its heap limit.. [optional]  # noqa: E501
            compute_stack_limit_exceeded (int): Number of times a guest exceeded its stack limit.. [optional]  # noqa: E501
            compute_globals_limit_exceeded (int): Number of times a guest exceeded its globals limit.. [optional]  # noqa: E501
            compute_guest_errors (int): Number of times a service experienced a guest code error.. [optional]  # noqa: E501
            compute_runtime_errors (int): Number of times a service experienced a guest runtime error.. [optional]  # noqa: E501
            edge_hit_resp_body_bytes (int): Body bytes delivered for edge hits.. [optional]  # noqa: E501
            edge_hit_resp_header_bytes (int): Header bytes delivered for edge hits.. [optional]  # noqa: E501
            edge_miss_resp_body_bytes (int): Body bytes delivered for edge misses.. [optional]  # noqa: E501
            edge_miss_resp_header_bytes (int): Header bytes delivered for edge misses.. [optional]  # noqa: E501
            origin_cache_fetch_resp_body_bytes (int): Body bytes received from origin for cacheable content.. [optional]  # noqa: E501
            origin_cache_fetch_resp_header_bytes (int): Header bytes received from an origin for cacheable content.. [optional]  # noqa: E501
            shield_hit_requests (int): Number of requests that resulted in a hit at a shield.. [optional]  # noqa: E501
            shield_miss_requests (int): Number of requests that resulted in a miss at a shield.. [optional]  # noqa: E501
            shield_hit_resp_header_bytes (int): Header bytes delivered for shield hits.. [optional]  # noqa: E501
            shield_hit_resp_body_bytes (int): Body bytes delivered for shield hits.. [optional]  # noqa: E501
            shield_miss_resp_header_bytes (int): Header bytes delivered for shield misses.. [optional]  # noqa: E501
            shield_miss_resp_body_bytes (int): Body bytes delivered for shield misses.. [optional]  # noqa: E501
            websocket_req_header_bytes (int): Total header bytes received from end users over passthrough WebSocket connections.. [optional]  # noqa: E501
            websocket_req_body_bytes (int): Total message content bytes received from end users over passthrough WebSocket connections.. [optional]  # noqa: E501
            websocket_resp_header_bytes (int): Total header bytes sent to end users over passthrough WebSocket connections.. [optional]  # noqa: E501
            websocket_bereq_header_bytes (int): Total header bytes sent to backends over passthrough WebSocket connections.. [optional]  # noqa: E501
            websocket_bereq_body_bytes (int): Total message content bytes sent to backends over passthrough WebSocket connections.. [optional]  # noqa: E501
            websocket_beresp_header_bytes (int): Total header bytes received from backends over passthrough WebSocket connections.. [optional]  # noqa: E501
            websocket_beresp_body_bytes (int): Total message content bytes received from backends over passthrough WebSocket connections.. [optional]  # noqa: E501
            websocket_conn_time_ms (int): Total duration of passthrough WebSocket connections with end users.. [optional]  # noqa: E501
            websocket_resp_body_bytes (int): Total message content bytes sent to end users over passthrough WebSocket connections.. [optional]  # noqa: E501
            fanout_recv_publishes (int): Total published messages received from the publish API endpoint.. [optional]  # noqa: E501
            fanout_send_publishes (int): Total published messages sent to end users.. [optional]  # noqa: E501
            object_store_read_requests (int): The total number of reads received for the object store.. [optional]  # noqa: E501
            object_store_write_requests (int): The total number of writes received for the object store.. [optional]  # noqa: E501
            fanout_req_header_bytes (int): Total header bytes received from end users over Fanout connections.. [optional]  # noqa: E501
            fanout_req_body_bytes (int): Total body or message content bytes received from end users over Fanout connections.. [optional]  # noqa: E501
            fanout_resp_header_bytes (int): Total header bytes sent to end users over Fanout connections.. [optional]  # noqa: E501
            fanout_resp_body_bytes (int): Total body or message content bytes sent to end users over Fanout connections, excluding published message content.. [optional]  # noqa: E501
            fanout_bereq_header_bytes (int): Total header bytes sent to backends over Fanout connections.. [optional]  # noqa: E501
            fanout_bereq_body_bytes (int): Total body or message content bytes sent to backends over Fanout connections.. [optional]  # noqa: E501
            fanout_beresp_header_bytes (int): Total header bytes received from backends over Fanout connections.. [optional]  # noqa: E501
            fanout_beresp_body_bytes (int): Total body or message content bytes received from backends over Fanout connections.. [optional]  # noqa: E501
            fanout_conn_time_ms (int): Total duration of Fanout connections with end users.. [optional]  # noqa: E501
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
        """RealtimeMeasurements - a model defined in OpenAPI

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
            requests (int): Number of requests processed.. [optional]  # noqa: E501
            logging (int): Number of log lines sent (alias for `log`).. [optional]  # noqa: E501
            log (int): Number of log lines sent.. [optional]  # noqa: E501
            resp_header_bytes (int): Total header bytes delivered (edge_resp_header_bytes + shield_resp_header_bytes).. [optional]  # noqa: E501
            header_size (int): Total header bytes delivered (alias for resp_header_bytes).. [optional]  # noqa: E501
            resp_body_bytes (int): Total body bytes delivered (edge_resp_body_bytes + shield_resp_body_bytes).. [optional]  # noqa: E501
            body_size (int): Total body bytes delivered (alias for resp_body_bytes).. [optional]  # noqa: E501
            hits (int): Number of cache hits.. [optional]  # noqa: E501
            miss (int): Number of cache misses.. [optional]  # noqa: E501
            _pass (int): Number of requests that passed through the CDN without being cached.. [optional]  # noqa: E501
            synth (int): Number of requests that returned a synthetic response (i.e., response objects created with the `synthetic` VCL statement).. [optional]  # noqa: E501
            errors (int): Number of cache errors.. [optional]  # noqa: E501
            hits_time (float): Total amount of time spent processing cache hits (in seconds).. [optional]  # noqa: E501
            miss_time (float): Total amount of time spent processing cache misses (in seconds).. [optional]  # noqa: E501
            miss_histogram ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): A histogram. Each key represents the upper bound of a span of 10 milliseconds and the values represent the number of requests to origin during that 10ms period. Any origin request that takes more than 60 seconds to return will be in the 60000 bucket.. [optional]  # noqa: E501
            compute_requests (int): The total number of requests that were received for your service by Fastly.. [optional]  # noqa: E501
            compute_execution_time_ms (float): The amount of active CPU time used to process your requests (in milliseconds).. [optional]  # noqa: E501
            compute_ram_used (int): The amount of RAM used for your service by Fastly (in bytes).. [optional]  # noqa: E501
            compute_request_time_ms (float): The total, actual amount of time used to process your requests, including active CPU time (in milliseconds).. [optional]  # noqa: E501
            shield (int): Number of requests from edge to the shield POP.. [optional]  # noqa: E501
            ipv6 (int): Number of requests that were received over IPv6.. [optional]  # noqa: E501
            imgopto (int): Number of responses that came from the Fastly Image Optimizer service. If the service receives 10 requests for an image, this stat will be 10 regardless of how many times the image was transformed.. [optional]  # noqa: E501
            imgopto_shield (int): Number of responses that came from the Fastly Image Optimizer service via a shield.. [optional]  # noqa: E501
            imgopto_transforms (int): Number of transforms performed by the Fastly Image Optimizer service.. [optional]  # noqa: E501
            otfp (int): Number of responses that came from the Fastly On-the-Fly Packaging service for video-on-demand.. [optional]  # noqa: E501
            otfp_shield (int): Number of responses that came from the Fastly On-the-Fly Packaging service for video-on-demand via a shield.. [optional]  # noqa: E501
            otfp_manifests (int): Number of responses that were manifest files from the Fastly On-the-Fly Packaging service for video-on-demand.. [optional]  # noqa: E501
            video (int): Number of responses with the video segment or video manifest MIME type (i.e., application/x-mpegurl, application/vnd.apple.mpegurl, application/f4m, application/dash+xml, application/vnd.ms-sstr+xml, ideo/mp2t, audio/aac, video/f4f, video/x-flv, video/mp4, audio/mp4).. [optional]  # noqa: E501
            pci (int): Number of responses with the PCI flag turned on.. [optional]  # noqa: E501
            http2 (int): Number of requests received over HTTP/2.. [optional]  # noqa: E501
            http3 (int): Number of requests received over HTTP/3.. [optional]  # noqa: E501
            restarts (int): Number of restarts performed.. [optional]  # noqa: E501
            req_header_bytes (int): Total header bytes received.. [optional]  # noqa: E501
            req_body_bytes (int): Total body bytes received.. [optional]  # noqa: E501
            bereq_header_bytes (int): Total header bytes sent to origin.. [optional]  # noqa: E501
            bereq_body_bytes (int): Total body bytes sent to origin.. [optional]  # noqa: E501
            waf_blocked (int): Number of requests that triggered a WAF rule and were blocked.. [optional]  # noqa: E501
            waf_logged (int): Number of requests that triggered a WAF rule and were logged.. [optional]  # noqa: E501
            waf_passed (int): Number of requests that triggered a WAF rule and were passed.. [optional]  # noqa: E501
            attack_req_header_bytes (int): Total header bytes received from requests that triggered a WAF rule.. [optional]  # noqa: E501
            attack_req_body_bytes (int): Total body bytes received from requests that triggered a WAF rule.. [optional]  # noqa: E501
            attack_resp_synth_bytes (int): Total bytes delivered for requests that triggered a WAF rule and returned a synthetic response.. [optional]  # noqa: E501
            attack_logged_req_header_bytes (int): Total header bytes received from requests that triggered a WAF rule that was logged.. [optional]  # noqa: E501
            attack_logged_req_body_bytes (int): Total body bytes received from requests that triggered a WAF rule that was logged.. [optional]  # noqa: E501
            attack_blocked_req_header_bytes (int): Total header bytes received from requests that triggered a WAF rule that was blocked.. [optional]  # noqa: E501
            attack_blocked_req_body_bytes (int): Total body bytes received from requests that triggered a WAF rule that was blocked.. [optional]  # noqa: E501
            attack_passed_req_header_bytes (int): Total header bytes received from requests that triggered a WAF rule that was passed.. [optional]  # noqa: E501
            attack_passed_req_body_bytes (int): Total body bytes received from requests that triggered a WAF rule that was passed.. [optional]  # noqa: E501
            shield_resp_header_bytes (int): Total header bytes delivered via a shield.. [optional]  # noqa: E501
            shield_resp_body_bytes (int): Total body bytes delivered via a shield.. [optional]  # noqa: E501
            otfp_resp_header_bytes (int): Total header bytes delivered from the Fastly On-the-Fly Packaging service for video-on-demand.. [optional]  # noqa: E501
            otfp_resp_body_bytes (int): Total body bytes delivered from the Fastly On-the-Fly Packaging service for video-on-demand.. [optional]  # noqa: E501
            otfp_shield_resp_header_bytes (int): Total header bytes delivered via a shield for the Fastly On-the-Fly Packaging service for video-on-demand.. [optional]  # noqa: E501
            otfp_shield_resp_body_bytes (int): Total body bytes delivered via a shield for the Fastly On-the-Fly Packaging service for video-on-demand.. [optional]  # noqa: E501
            otfp_shield_time (float): Total amount of time spent delivering a response via a shield from the Fastly On-the-Fly Packaging service for video-on-demand (in seconds).. [optional]  # noqa: E501
            otfp_deliver_time (float): Total amount of time spent delivering a response from the Fastly On-the-Fly Packaging service for video-on-demand (in seconds).. [optional]  # noqa: E501
            imgopto_resp_header_bytes (int): Total header bytes delivered from the Fastly Image Optimizer service, including shield traffic.. [optional]  # noqa: E501
            imgopto_resp_body_bytes (int): Total body bytes delivered from the Fastly Image Optimizer service, including shield traffic.. [optional]  # noqa: E501
            imgopto_shield_resp_header_bytes (int): Total header bytes delivered via a shield from the Fastly Image Optimizer service.. [optional]  # noqa: E501
            imgopto_shield_resp_body_bytes (int): Total body bytes delivered via a shield from the Fastly Image Optimizer service.. [optional]  # noqa: E501
            status_1xx (int): Number of \"Informational\" category status codes delivered.. [optional]  # noqa: E501
            status_2xx (int): Number of \"Success\" status codes delivered.. [optional]  # noqa: E501
            status_3xx (int): Number of \"Redirection\" codes delivered.. [optional]  # noqa: E501
            status_4xx (int): Number of \"Client Error\" codes delivered.. [optional]  # noqa: E501
            status_5xx (int): Number of \"Server Error\" codes delivered.. [optional]  # noqa: E501
            status_200 (int): Number of responses sent with status code 200 (Success).. [optional]  # noqa: E501
            status_204 (int): Number of responses sent with status code 204 (No Content).. [optional]  # noqa: E501
            status_206 (int): Number of responses sent with status code 206 (Partial Content).. [optional]  # noqa: E501
            status_301 (int): Number of responses sent with status code 301 (Moved Permanently).. [optional]  # noqa: E501
            status_302 (int): Number of responses sent with status code 302 (Found).. [optional]  # noqa: E501
            status_304 (int): Number of responses sent with status code 304 (Not Modified).. [optional]  # noqa: E501
            status_400 (int): Number of responses sent with status code 400 (Bad Request).. [optional]  # noqa: E501
            status_401 (int): Number of responses sent with status code 401 (Unauthorized).. [optional]  # noqa: E501
            status_403 (int): Number of responses sent with status code 403 (Forbidden).. [optional]  # noqa: E501
            status_404 (int): Number of responses sent with status code 404 (Not Found).. [optional]  # noqa: E501
            status_406 (int): Number of responses sent with status code 406 (Not Acceptable).. [optional]  # noqa: E501
            status_416 (int): Number of responses sent with status code 416 (Range Not Satisfiable).. [optional]  # noqa: E501
            status_429 (int): Number of responses sent with status code 429 (Too Many Requests).. [optional]  # noqa: E501
            status_500 (int): Number of responses sent with status code 500 (Internal Server Error).. [optional]  # noqa: E501
            status_501 (int): Number of responses sent with status code 501 (Not Implemented).. [optional]  # noqa: E501
            status_502 (int): Number of responses sent with status code 502 (Bad Gateway).. [optional]  # noqa: E501
            status_503 (int): Number of responses sent with status code 503 (Service Unavailable).. [optional]  # noqa: E501
            status_504 (int): Number of responses sent with status code 504 (Gateway Timeout).. [optional]  # noqa: E501
            status_505 (int): Number of responses sent with status code 505 (HTTP Version Not Supported).. [optional]  # noqa: E501
            uncacheable (int): Number of requests that were designated uncachable.. [optional]  # noqa: E501
            pass_time (float): Total amount of time spent processing cache passes (in seconds).. [optional]  # noqa: E501
            tls (int): Number of requests that were received over TLS.. [optional]  # noqa: E501
            tls_v10 (int): Number of requests received over TLS 1.0.. [optional]  # noqa: E501
            tls_v11 (int): Number of requests received over TLS 1.1.. [optional]  # noqa: E501
            tls_v12 (int): Number of requests received over TLS 1.2.. [optional]  # noqa: E501
            tls_v13 (int): Number of requests received over TLS 1.3.. [optional]  # noqa: E501
            object_size_1k (int): Number of objects served that were under 1KB in size.. [optional]  # noqa: E501
            object_size_10k (int): Number of objects served that were between 1KB and 10KB in size.. [optional]  # noqa: E501
            object_size_100k (int): Number of objects served that were between 10KB and 100KB in size.. [optional]  # noqa: E501
            object_size_1m (int): Number of objects served that were between 100KB and 1MB in size.. [optional]  # noqa: E501
            object_size_10m (int): Number of objects served that were between 1MB and 10MB in size.. [optional]  # noqa: E501
            object_size_100m (int): Number of objects served that were between 10MB and 100MB in size.. [optional]  # noqa: E501
            object_size_1g (int): Number of objects served that were between 100MB and 1GB in size.. [optional]  # noqa: E501
            object_size_other (int): Number of objects served that were larger than 1GB in size.. [optional]  # noqa: E501
            recv_sub_time (float): Time spent inside the `vcl_recv` Varnish subroutine (in nanoseconds).. [optional]  # noqa: E501
            recv_sub_count (int): Number of executions of the `vcl_recv` Varnish subroutine.. [optional]  # noqa: E501
            hash_sub_time (float): Time spent inside the `vcl_hash` Varnish subroutine (in nanoseconds).. [optional]  # noqa: E501
            hash_sub_count (int): Number of executions of the `vcl_hash` Varnish subroutine.. [optional]  # noqa: E501
            miss_sub_time (float): Time spent inside the `vcl_miss` Varnish subroutine (in nanoseconds).. [optional]  # noqa: E501
            miss_sub_count (int): Number of executions of the `vcl_miss` Varnish subroutine.. [optional]  # noqa: E501
            fetch_sub_time (float): Time spent inside the `vcl_fetch` Varnish subroutine (in nanoseconds).. [optional]  # noqa: E501
            fetch_sub_count (int): Number of executions of the `vcl_fetch` Varnish subroutine.. [optional]  # noqa: E501
            pass_sub_time (float): Time spent inside the `vcl_pass` Varnish subroutine (in nanoseconds).. [optional]  # noqa: E501
            pass_sub_count (int): Number of executions of the `vcl_pass` Varnish subroutine.. [optional]  # noqa: E501
            pipe_sub_time (float): Time spent inside the `vcl_pipe` Varnish subroutine (in nanoseconds).. [optional]  # noqa: E501
            pipe_sub_count (int): Number of executions of the `vcl_pipe` Varnish subroutine.. [optional]  # noqa: E501
            deliver_sub_time (float): Time spent inside the `vcl_deliver` Varnish subroutine (in nanoseconds).. [optional]  # noqa: E501
            deliver_sub_count (int): Number of executions of the `vcl_deliver` Varnish subroutine.. [optional]  # noqa: E501
            error_sub_time (float): Time spent inside the `vcl_error` Varnish subroutine (in nanoseconds).. [optional]  # noqa: E501
            error_sub_count (int): Number of executions of the `vcl_error` Varnish subroutine.. [optional]  # noqa: E501
            hit_sub_time (float): Time spent inside the `vcl_hit` Varnish subroutine (in nanoseconds).. [optional]  # noqa: E501
            hit_sub_count (int): Number of executions of the `vcl_hit` Varnish subroutine.. [optional]  # noqa: E501
            prehash_sub_time (float): Time spent inside the `vcl_prehash` Varnish subroutine (in nanoseconds).. [optional]  # noqa: E501
            prehash_sub_count (int): Number of executions of the `vcl_prehash` Varnish subroutine.. [optional]  # noqa: E501
            predeliver_sub_time (float): Time spent inside the `vcl_predeliver` Varnish subroutine (in nanoseconds).. [optional]  # noqa: E501
            predeliver_sub_count (int): Number of executions of the `vcl_predeliver` Varnish subroutine.. [optional]  # noqa: E501
            hit_resp_body_bytes (int): Total body bytes delivered for cache hits.. [optional]  # noqa: E501
            miss_resp_body_bytes (int): Total body bytes delivered for cache misses.. [optional]  # noqa: E501
            pass_resp_body_bytes (int): Total body bytes delivered for cache passes.. [optional]  # noqa: E501
            compute_req_header_bytes (int): Total header bytes received by Compute@Edge.. [optional]  # noqa: E501
            compute_req_body_bytes (int): Total body bytes received by Compute@Edge.. [optional]  # noqa: E501
            compute_resp_header_bytes (int): Total header bytes sent from Compute@Edge to end user.. [optional]  # noqa: E501
            compute_resp_body_bytes (int): Total body bytes sent from Compute@Edge to end user.. [optional]  # noqa: E501
            imgvideo (int): Number of video responses that came from the Fastly Image Optimizer service.. [optional]  # noqa: E501
            imgvideo_frames (int): Number of video frames that came from the Fastly Image Optimizer service. A video frame is an individual image within a sequence of video.. [optional]  # noqa: E501
            imgvideo_resp_header_bytes (int): Total header bytes of video delivered from the Fastly Image Optimizer service.. [optional]  # noqa: E501
            imgvideo_resp_body_bytes (int): Total body bytes of video delivered from the Fastly Image Optimizer service.. [optional]  # noqa: E501
            imgvideo_shield (int): Number of video responses delivered via a shield that came from the Fastly Image Optimizer service.. [optional]  # noqa: E501
            imgvideo_shield_frames (int): Number of video frames delivered via a shield that came from the Fastly Image Optimizer service. A video frame is an individual image within a sequence of video.. [optional]  # noqa: E501
            imgvideo_shield_resp_header_bytes (int): Total header bytes of video delivered via a shield from the Fastly Image Optimizer service.. [optional]  # noqa: E501
            imgvideo_shield_resp_body_bytes (int): Total body bytes of video delivered via a shield from the Fastly Image Optimizer service.. [optional]  # noqa: E501
            log_bytes (int): Total log bytes sent.. [optional]  # noqa: E501
            edge_requests (int): Number of requests sent by end users to Fastly.. [optional]  # noqa: E501
            edge_resp_header_bytes (int): Total header bytes delivered from Fastly to the end user.. [optional]  # noqa: E501
            edge_resp_body_bytes (int): Total body bytes delivered from Fastly to the end user.. [optional]  # noqa: E501
            origin_revalidations (int): Number of responses received from origin with a `304` status code in response to an `If-Modified-Since` or `If-None-Match` request. Under regular scenarios, a revalidation will imply a cache hit. However, if using Fastly Image Optimizer or segmented caching this may result in a cache miss.. [optional]  # noqa: E501
            origin_fetches (int): Number of requests sent to origin.. [optional]  # noqa: E501
            origin_fetch_header_bytes (int): Total request header bytes sent to origin.. [optional]  # noqa: E501
            origin_fetch_body_bytes (int): Total request body bytes sent to origin.. [optional]  # noqa: E501
            origin_fetch_resp_header_bytes (int): Total header bytes received from origin.. [optional]  # noqa: E501
            origin_fetch_resp_body_bytes (int): Total body bytes received from origin.. [optional]  # noqa: E501
            shield_revalidations (int): Number of responses received from origin with a `304` status code, in response to an `If-Modified-Since` or `If-None-Match` request to a shield. Under regular scenarios, a revalidation will imply a cache hit. However, if using segmented caching this may result in a cache miss.. [optional]  # noqa: E501
            shield_fetches (int): Number of requests made from one Fastly POP to another, as part of shielding.. [optional]  # noqa: E501
            shield_fetch_header_bytes (int): Total request header bytes sent to a shield.. [optional]  # noqa: E501
            shield_fetch_body_bytes (int): Total request body bytes sent to a shield.. [optional]  # noqa: E501
            shield_fetch_resp_header_bytes (int): Total response header bytes sent from a shield to the edge.. [optional]  # noqa: E501
            shield_fetch_resp_body_bytes (int): Total response body bytes sent from a shield to the edge.. [optional]  # noqa: E501
            segblock_origin_fetches (int): Number of `Range` requests to origin for segments of resources when using segmented caching.. [optional]  # noqa: E501
            segblock_shield_fetches (int): Number of `Range` requests to a shield for segments of resources when using segmented caching.. [optional]  # noqa: E501
            compute_resp_status_1xx (int): Number of \"Informational\" category status codes delivered by Compute@Edge.. [optional]  # noqa: E501
            compute_resp_status_2xx (int): Number of \"Success\" category status codes delivered by Compute@Edge.. [optional]  # noqa: E501
            compute_resp_status_3xx (int): Number of \"Redirection\" category status codes delivered by Compute@Edge.. [optional]  # noqa: E501
            compute_resp_status_4xx (int): Number of \"Client Error\" category status codes delivered by Compute@Edge.. [optional]  # noqa: E501
            compute_resp_status_5xx (int): Number of \"Server Error\" category status codes delivered by Compute@Edge.. [optional]  # noqa: E501
            edge_hit_requests (int): Number of requests sent by end users to Fastly that resulted in a hit at the edge.. [optional]  # noqa: E501
            edge_miss_requests (int): Number of requests sent by end users to Fastly that resulted in a miss at the edge.. [optional]  # noqa: E501
            compute_bereq_header_bytes (int): Total header bytes sent to backends (origins) by Compute@Edge.. [optional]  # noqa: E501
            compute_bereq_body_bytes (int): Total body bytes sent to backends (origins) by Compute@Edge.. [optional]  # noqa: E501
            compute_beresp_header_bytes (int): Total header bytes received from backends (origins) by Compute@Edge.. [optional]  # noqa: E501
            compute_beresp_body_bytes (int): Total body bytes received from backends (origins) by Compute@Edge.. [optional]  # noqa: E501
            origin_cache_fetches (int): The total number of completed requests made to backends (origins) that returned cacheable content.. [optional]  # noqa: E501
            shield_cache_fetches (int): The total number of completed requests made to shields that returned cacheable content.. [optional]  # noqa: E501
            compute_bereqs (int): Number of backend requests started.. [optional]  # noqa: E501
            compute_bereq_errors (int): Number of backend request errors, including timeouts.. [optional]  # noqa: E501
            compute_resource_limit_exceeded (int): Number of times a guest exceeded its resource limit, includes heap, stack, globals, and code execution timeout.. [optional]  # noqa: E501
            compute_heap_limit_exceeded (int): Number of times a guest exceeded its heap limit.. [optional]  # noqa: E501
            compute_stack_limit_exceeded (int): Number of times a guest exceeded its stack limit.. [optional]  # noqa: E501
            compute_globals_limit_exceeded (int): Number of times a guest exceeded its globals limit.. [optional]  # noqa: E501
            compute_guest_errors (int): Number of times a service experienced a guest code error.. [optional]  # noqa: E501
            compute_runtime_errors (int): Number of times a service experienced a guest runtime error.. [optional]  # noqa: E501
            edge_hit_resp_body_bytes (int): Body bytes delivered for edge hits.. [optional]  # noqa: E501
            edge_hit_resp_header_bytes (int): Header bytes delivered for edge hits.. [optional]  # noqa: E501
            edge_miss_resp_body_bytes (int): Body bytes delivered for edge misses.. [optional]  # noqa: E501
            edge_miss_resp_header_bytes (int): Header bytes delivered for edge misses.. [optional]  # noqa: E501
            origin_cache_fetch_resp_body_bytes (int): Body bytes received from origin for cacheable content.. [optional]  # noqa: E501
            origin_cache_fetch_resp_header_bytes (int): Header bytes received from an origin for cacheable content.. [optional]  # noqa: E501
            shield_hit_requests (int): Number of requests that resulted in a hit at a shield.. [optional]  # noqa: E501
            shield_miss_requests (int): Number of requests that resulted in a miss at a shield.. [optional]  # noqa: E501
            shield_hit_resp_header_bytes (int): Header bytes delivered for shield hits.. [optional]  # noqa: E501
            shield_hit_resp_body_bytes (int): Body bytes delivered for shield hits.. [optional]  # noqa: E501
            shield_miss_resp_header_bytes (int): Header bytes delivered for shield misses.. [optional]  # noqa: E501
            shield_miss_resp_body_bytes (int): Body bytes delivered for shield misses.. [optional]  # noqa: E501
            websocket_req_header_bytes (int): Total header bytes received from end users over passthrough WebSocket connections.. [optional]  # noqa: E501
            websocket_req_body_bytes (int): Total message content bytes received from end users over passthrough WebSocket connections.. [optional]  # noqa: E501
            websocket_resp_header_bytes (int): Total header bytes sent to end users over passthrough WebSocket connections.. [optional]  # noqa: E501
            websocket_bereq_header_bytes (int): Total header bytes sent to backends over passthrough WebSocket connections.. [optional]  # noqa: E501
            websocket_bereq_body_bytes (int): Total message content bytes sent to backends over passthrough WebSocket connections.. [optional]  # noqa: E501
            websocket_beresp_header_bytes (int): Total header bytes received from backends over passthrough WebSocket connections.. [optional]  # noqa: E501
            websocket_beresp_body_bytes (int): Total message content bytes received from backends over passthrough WebSocket connections.. [optional]  # noqa: E501
            websocket_conn_time_ms (int): Total duration of passthrough WebSocket connections with end users.. [optional]  # noqa: E501
            websocket_resp_body_bytes (int): Total message content bytes sent to end users over passthrough WebSocket connections.. [optional]  # noqa: E501
            fanout_recv_publishes (int): Total published messages received from the publish API endpoint.. [optional]  # noqa: E501
            fanout_send_publishes (int): Total published messages sent to end users.. [optional]  # noqa: E501
            object_store_read_requests (int): The total number of reads received for the object store.. [optional]  # noqa: E501
            object_store_write_requests (int): The total number of writes received for the object store.. [optional]  # noqa: E501
            fanout_req_header_bytes (int): Total header bytes received from end users over Fanout connections.. [optional]  # noqa: E501
            fanout_req_body_bytes (int): Total body or message content bytes received from end users over Fanout connections.. [optional]  # noqa: E501
            fanout_resp_header_bytes (int): Total header bytes sent to end users over Fanout connections.. [optional]  # noqa: E501
            fanout_resp_body_bytes (int): Total body or message content bytes sent to end users over Fanout connections, excluding published message content.. [optional]  # noqa: E501
            fanout_bereq_header_bytes (int): Total header bytes sent to backends over Fanout connections.. [optional]  # noqa: E501
            fanout_bereq_body_bytes (int): Total body or message content bytes sent to backends over Fanout connections.. [optional]  # noqa: E501
            fanout_beresp_header_bytes (int): Total header bytes received from backends over Fanout connections.. [optional]  # noqa: E501
            fanout_beresp_body_bytes (int): Total body or message content bytes received from backends over Fanout connections.. [optional]  # noqa: E501
            fanout_conn_time_ms (int): Total duration of Fanout connections with end users.. [optional]  # noqa: E501
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
