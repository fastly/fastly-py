"""
    Fastly API

    Via the Fastly API you can perform any of the operations that are possible within the management console,  including creating services, domains, and backends, configuring rules or uploading your own application code, as well as account operations such as user administration and billing reports. The API is organized into collections of endpoints that allow manipulation of objects related to Fastly services and accounts. For the most accurate and up-to-date API reference content, visit our [Developer Hub](https://www.fastly.com/documentation/reference/api/)   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: oss@fastly.com
"""


import re  # noqa: F401
import sys  # noqa: F401

from fastly.api_client import ApiClient, Endpoint as _Endpoint
from fastly.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from fastly.model.network_protect_conflict import NetworkProtectConflict
from fastly.model.network_protect_endpoint_create import NetworkProtectEndpointCreate
from fastly.model.network_protect_endpoint_response import NetworkProtectEndpointResponse
from fastly.model.network_protect_endpoint_update import NetworkProtectEndpointUpdate
from fastly.model.network_protect_endpoints_response import NetworkProtectEndpointsResponse
from fastly.model.network_protect_invalid_request import NetworkProtectInvalidRequest
from fastly.model.network_protect_network_create import NetworkProtectNetworkCreate
from fastly.model.network_protect_network_response import NetworkProtectNetworkResponse
from fastly.model.network_protect_network_update import NetworkProtectNetworkUpdate
from fastly.model.network_protect_networks_response import NetworkProtectNetworksResponse
from fastly.model.network_protect_prefix_list_create import NetworkProtectPrefixListCreate
from fastly.model.network_protect_prefix_list_response import NetworkProtectPrefixListResponse
from fastly.model.network_protect_prefix_list_update import NetworkProtectPrefixListUpdate
from fastly.model.network_protect_prefix_lists_response import NetworkProtectPrefixListsResponse
from fastly.model.network_protect_rule_set_create import NetworkProtectRuleSetCreate
from fastly.model.network_protect_rule_set_response import NetworkProtectRuleSetResponse
from fastly.model.network_protect_rule_set_update import NetworkProtectRuleSetUpdate
from fastly.model.network_protect_rule_sets_response import NetworkProtectRuleSetsResponse


class NetworkProtectApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_network_protect_endpoint_endpoint = _Endpoint(
            settings={
                'response_type': (NetworkProtectEndpointResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/network-protect/v1/endpoints',
                'operation_id': 'create_network_protect_endpoint',
                'http_method': 'POST',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'network_protect_endpoint_create',
                ],
                'required': [
                    'network_protect_endpoint_create',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'network_protect_endpoint_create':
                        (NetworkProtectEndpointCreate,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'network_protect_endpoint_create': 'body',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/problem+json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.create_network_protect_network_endpoint = _Endpoint(
            settings={
                'response_type': (NetworkProtectNetworkResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/network-protect/v1/networks',
                'operation_id': 'create_network_protect_network',
                'http_method': 'POST',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'network_protect_network_create',
                ],
                'required': [
                    'network_protect_network_create',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'network_protect_network_create':
                        (NetworkProtectNetworkCreate,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'network_protect_network_create': 'body',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/problem+json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.create_network_protect_prefix_list_endpoint = _Endpoint(
            settings={
                'response_type': (NetworkProtectPrefixListResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/network-protect/v1/prefix-lists',
                'operation_id': 'create_network_protect_prefix_list',
                'http_method': 'POST',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'network_protect_prefix_list_create',
                ],
                'required': [
                    'network_protect_prefix_list_create',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'network_protect_prefix_list_create':
                        (NetworkProtectPrefixListCreate,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'network_protect_prefix_list_create': 'body',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/problem+json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.create_network_protect_rule_set_endpoint = _Endpoint(
            settings={
                'response_type': (NetworkProtectRuleSetResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/network-protect/v1/rule-sets',
                'operation_id': 'create_network_protect_rule_set',
                'http_method': 'POST',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'network_protect_rule_set_create',
                ],
                'required': [
                    'network_protect_rule_set_create',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'network_protect_rule_set_create':
                        (NetworkProtectRuleSetCreate,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'network_protect_rule_set_create': 'body',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/problem+json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.delete_network_protect_endpoint_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'token'
                ],
                'endpoint_path': '/network-protect/v1/endpoints/{endpoint_id}',
                'operation_id': 'delete_network_protect_endpoint',
                'http_method': 'DELETE',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'endpoint_id',
                ],
                'required': [
                    'endpoint_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'endpoint_id',
                ]
            },
            root_map={
                'validations': {
                    ('endpoint_id',): {

                        'regex': {
                            'pattern': r'^[A-Za-z0-9]{19,22}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'endpoint_id':
                        (str,),
                },
                'attribute_map': {
                    'endpoint_id': 'endpoint_id',
                },
                'location_map': {
                    'endpoint_id': 'path',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/problem+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.delete_network_protect_network_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'token'
                ],
                'endpoint_path': '/network-protect/v1/networks/{network_id}',
                'operation_id': 'delete_network_protect_network',
                'http_method': 'DELETE',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'network_id',
                ],
                'required': [
                    'network_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'network_id',
                ]
            },
            root_map={
                'validations': {
                    ('network_id',): {

                        'regex': {
                            'pattern': r'^[A-Za-z0-9]{19,22}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'network_id':
                        (str,),
                },
                'attribute_map': {
                    'network_id': 'network_id',
                },
                'location_map': {
                    'network_id': 'path',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/problem+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.delete_network_protect_prefix_list_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'token'
                ],
                'endpoint_path': '/network-protect/v1/prefix-lists/{prefix_list_id}',
                'operation_id': 'delete_network_protect_prefix_list',
                'http_method': 'DELETE',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'prefix_list_id',
                ],
                'required': [
                    'prefix_list_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'prefix_list_id',
                ]
            },
            root_map={
                'validations': {
                    ('prefix_list_id',): {

                        'regex': {
                            'pattern': r'^[A-Za-z0-9]{19,22}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'prefix_list_id':
                        (str,),
                },
                'attribute_map': {
                    'prefix_list_id': 'prefix_list_id',
                },
                'location_map': {
                    'prefix_list_id': 'path',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/problem+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.delete_network_protect_rule_set_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'token'
                ],
                'endpoint_path': '/network-protect/v1/rule-sets/{rule_set_id}',
                'operation_id': 'delete_network_protect_rule_set',
                'http_method': 'DELETE',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'rule_set_id',
                ],
                'required': [
                    'rule_set_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'rule_set_id',
                ]
            },
            root_map={
                'validations': {
                    ('rule_set_id',): {

                        'regex': {
                            'pattern': r'^[A-Za-z0-9]{19,22}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'rule_set_id':
                        (str,),
                },
                'attribute_map': {
                    'rule_set_id': 'rule_set_id',
                },
                'location_map': {
                    'rule_set_id': 'path',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/problem+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_network_protect_endpoint_endpoint = _Endpoint(
            settings={
                'response_type': (NetworkProtectEndpointResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/network-protect/v1/endpoints/{endpoint_id}',
                'operation_id': 'get_network_protect_endpoint',
                'http_method': 'GET',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'endpoint_id',
                ],
                'required': [
                    'endpoint_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'endpoint_id',
                ]
            },
            root_map={
                'validations': {
                    ('endpoint_id',): {

                        'regex': {
                            'pattern': r'^[A-Za-z0-9]{19,22}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'endpoint_id':
                        (str,),
                },
                'attribute_map': {
                    'endpoint_id': 'endpoint_id',
                },
                'location_map': {
                    'endpoint_id': 'path',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/problem+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_network_protect_network_endpoint = _Endpoint(
            settings={
                'response_type': (NetworkProtectNetworkResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/network-protect/v1/networks/{network_id}',
                'operation_id': 'get_network_protect_network',
                'http_method': 'GET',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'network_id',
                ],
                'required': [
                    'network_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'network_id',
                ]
            },
            root_map={
                'validations': {
                    ('network_id',): {

                        'regex': {
                            'pattern': r'^[A-Za-z0-9]{19,22}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'network_id':
                        (str,),
                },
                'attribute_map': {
                    'network_id': 'network_id',
                },
                'location_map': {
                    'network_id': 'path',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/problem+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_network_protect_prefix_list_endpoint = _Endpoint(
            settings={
                'response_type': (NetworkProtectPrefixListResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/network-protect/v1/prefix-lists/{prefix_list_id}',
                'operation_id': 'get_network_protect_prefix_list',
                'http_method': 'GET',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'prefix_list_id',
                ],
                'required': [
                    'prefix_list_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'prefix_list_id',
                ]
            },
            root_map={
                'validations': {
                    ('prefix_list_id',): {

                        'regex': {
                            'pattern': r'^[A-Za-z0-9]{19,22}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'prefix_list_id':
                        (str,),
                },
                'attribute_map': {
                    'prefix_list_id': 'prefix_list_id',
                },
                'location_map': {
                    'prefix_list_id': 'path',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/problem+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_network_protect_rule_set_endpoint = _Endpoint(
            settings={
                'response_type': (NetworkProtectRuleSetResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/network-protect/v1/rule-sets/{rule_set_id}',
                'operation_id': 'get_network_protect_rule_set',
                'http_method': 'GET',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'rule_set_id',
                ],
                'required': [
                    'rule_set_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'rule_set_id',
                ]
            },
            root_map={
                'validations': {
                    ('rule_set_id',): {

                        'regex': {
                            'pattern': r'^[A-Za-z0-9]{19,22}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'rule_set_id':
                        (str,),
                },
                'attribute_map': {
                    'rule_set_id': 'rule_set_id',
                },
                'location_map': {
                    'rule_set_id': 'path',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/problem+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_network_protect_endpoints_endpoint = _Endpoint(
            settings={
                'response_type': (NetworkProtectEndpointsResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/network-protect/v1/endpoints',
                'operation_id': 'list_network_protect_endpoints',
                'http_method': 'GET',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'limit',
                    'cursor',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'limit',
                ]
            },
            root_map={
                'validations': {
                    ('limit',): {

                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'limit':
                        (int,),
                    'cursor':
                        (str,),
                },
                'attribute_map': {
                    'limit': 'limit',
                    'cursor': 'cursor',
                },
                'location_map': {
                    'limit': 'query',
                    'cursor': 'query',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/problem+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_network_protect_networks_endpoint = _Endpoint(
            settings={
                'response_type': (NetworkProtectNetworksResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/network-protect/v1/networks',
                'operation_id': 'list_network_protect_networks',
                'http_method': 'GET',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'limit',
                    'cursor',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'limit',
                ]
            },
            root_map={
                'validations': {
                    ('limit',): {

                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'limit':
                        (int,),
                    'cursor':
                        (str,),
                },
                'attribute_map': {
                    'limit': 'limit',
                    'cursor': 'cursor',
                },
                'location_map': {
                    'limit': 'query',
                    'cursor': 'query',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/problem+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_network_protect_prefix_lists_endpoint = _Endpoint(
            settings={
                'response_type': (NetworkProtectPrefixListsResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/network-protect/v1/prefix-lists',
                'operation_id': 'list_network_protect_prefix_lists',
                'http_method': 'GET',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'limit',
                    'cursor',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'limit',
                ]
            },
            root_map={
                'validations': {
                    ('limit',): {

                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'limit':
                        (int,),
                    'cursor':
                        (str,),
                },
                'attribute_map': {
                    'limit': 'limit',
                    'cursor': 'cursor',
                },
                'location_map': {
                    'limit': 'query',
                    'cursor': 'query',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/problem+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_network_protect_rule_sets_endpoint = _Endpoint(
            settings={
                'response_type': (NetworkProtectRuleSetsResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/network-protect/v1/rule-sets',
                'operation_id': 'list_network_protect_rule_sets',
                'http_method': 'GET',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'limit',
                    'cursor',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'limit',
                ]
            },
            root_map={
                'validations': {
                    ('limit',): {

                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'limit':
                        (int,),
                    'cursor':
                        (str,),
                },
                'attribute_map': {
                    'limit': 'limit',
                    'cursor': 'cursor',
                },
                'location_map': {
                    'limit': 'query',
                    'cursor': 'query',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/problem+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.update_network_protect_endpoint_endpoint = _Endpoint(
            settings={
                'response_type': (NetworkProtectEndpointResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/network-protect/v1/endpoints/{endpoint_id}',
                'operation_id': 'update_network_protect_endpoint',
                'http_method': 'PATCH',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'endpoint_id',
                    'network_protect_endpoint_update',
                ],
                'required': [
                    'endpoint_id',
                    'network_protect_endpoint_update',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'endpoint_id',
                ]
            },
            root_map={
                'validations': {
                    ('endpoint_id',): {

                        'regex': {
                            'pattern': r'^[A-Za-z0-9]{19,22}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'endpoint_id':
                        (str,),
                    'network_protect_endpoint_update':
                        (NetworkProtectEndpointUpdate,),
                },
                'attribute_map': {
                    'endpoint_id': 'endpoint_id',
                },
                'location_map': {
                    'endpoint_id': 'path',
                    'network_protect_endpoint_update': 'body',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/problem+json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.update_network_protect_network_endpoint = _Endpoint(
            settings={
                'response_type': (NetworkProtectNetworkResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/network-protect/v1/networks/{network_id}',
                'operation_id': 'update_network_protect_network',
                'http_method': 'PATCH',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'network_id',
                    'network_protect_network_update',
                ],
                'required': [
                    'network_id',
                    'network_protect_network_update',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'network_id',
                ]
            },
            root_map={
                'validations': {
                    ('network_id',): {

                        'regex': {
                            'pattern': r'^[A-Za-z0-9]{19,22}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'network_id':
                        (str,),
                    'network_protect_network_update':
                        (NetworkProtectNetworkUpdate,),
                },
                'attribute_map': {
                    'network_id': 'network_id',
                },
                'location_map': {
                    'network_id': 'path',
                    'network_protect_network_update': 'body',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/problem+json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.update_network_protect_prefix_list_endpoint = _Endpoint(
            settings={
                'response_type': (NetworkProtectPrefixListResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/network-protect/v1/prefix-lists/{prefix_list_id}',
                'operation_id': 'update_network_protect_prefix_list',
                'http_method': 'PATCH',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'prefix_list_id',
                    'network_protect_prefix_list_update',
                ],
                'required': [
                    'prefix_list_id',
                    'network_protect_prefix_list_update',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'prefix_list_id',
                ]
            },
            root_map={
                'validations': {
                    ('prefix_list_id',): {

                        'regex': {
                            'pattern': r'^[A-Za-z0-9]{19,22}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'prefix_list_id':
                        (str,),
                    'network_protect_prefix_list_update':
                        (NetworkProtectPrefixListUpdate,),
                },
                'attribute_map': {
                    'prefix_list_id': 'prefix_list_id',
                },
                'location_map': {
                    'prefix_list_id': 'path',
                    'network_protect_prefix_list_update': 'body',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/problem+json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.update_network_protect_rule_set_endpoint = _Endpoint(
            settings={
                'response_type': (NetworkProtectRuleSetResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/network-protect/v1/rule-sets/{rule_set_id}',
                'operation_id': 'update_network_protect_rule_set',
                'http_method': 'PATCH',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'rule_set_id',
                    'network_protect_rule_set_update',
                ],
                'required': [
                    'rule_set_id',
                    'network_protect_rule_set_update',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'rule_set_id',
                ]
            },
            root_map={
                'validations': {
                    ('rule_set_id',): {

                        'regex': {
                            'pattern': r'^[A-Za-z0-9]{19,22}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'rule_set_id':
                        (str,),
                    'network_protect_rule_set_update':
                        (NetworkProtectRuleSetUpdate,),
                },
                'attribute_map': {
                    'rule_set_id': 'rule_set_id',
                },
                'location_map': {
                    'rule_set_id': 'path',
                    'network_protect_rule_set_update': 'body',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/problem+json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def create_network_protect_endpoint(
        self,
        network_protect_endpoint_create,
        **kwargs
    ):
        """Create a Network Protect endpoint  # noqa: E501

        Creates a GRE delivery destination. A new endpoint is not attached to a network until it is added to an endpoint policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_network_protect_endpoint(network_protect_endpoint_create, async_req=True)
        >>> result = thread.get()

        Args:
            network_protect_endpoint_create (NetworkProtectEndpointCreate):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            NetworkProtectEndpointResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['network_protect_endpoint_create'] = \
            network_protect_endpoint_create
        return self.create_network_protect_endpoint_endpoint.call_with_http_info(**kwargs)

    def create_network_protect_network(
        self,
        network_protect_network_create,
        **kwargs
    ):
        """Create a Network Protect network  # noqa: E501

        Registers customer-owned IP space for protection. The network starts with advertisement disabled and Fastly does not announce its prefix. Turn advertisement on after LOA and ROA authorization are ready. The create request cannot include advertise; sending it returns a `400 Bad Request` error.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_network_protect_network(network_protect_network_create, async_req=True)
        >>> result = thread.get()

        Args:
            network_protect_network_create (NetworkProtectNetworkCreate):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            NetworkProtectNetworkResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['network_protect_network_create'] = \
            network_protect_network_create
        return self.create_network_protect_network_endpoint.call_with_http_info(**kwargs)

    def create_network_protect_prefix_list(
        self,
        network_protect_prefix_list_create,
        **kwargs
    ):
        """Create a Network Protect prefix list  # noqa: E501

        Creates a typed list of addresses that rules can reference. The family is required and cannot be changed. The addresses list may remain empty.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_network_protect_prefix_list(network_protect_prefix_list_create, async_req=True)
        >>> result = thread.get()

        Args:
            network_protect_prefix_list_create (NetworkProtectPrefixListCreate):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            NetworkProtectPrefixListResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['network_protect_prefix_list_create'] = \
            network_protect_prefix_list_create
        return self.create_network_protect_prefix_list_endpoint.call_with_http_info(**kwargs)

    def create_network_protect_rule_set(
        self,
        network_protect_rule_set_create,
        **kwargs
    ):
        """Create a Network Protect rule set  # noqa: E501

        Creates an ordered rule set and stores its filtering intent. A rule set has at most 64 rules and uses the default action when no rule matches. Custom attachment and detachment are restricted in this release.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_network_protect_rule_set(network_protect_rule_set_create, async_req=True)
        >>> result = thread.get()

        Args:
            network_protect_rule_set_create (NetworkProtectRuleSetCreate):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            NetworkProtectRuleSetResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['network_protect_rule_set_create'] = \
            network_protect_rule_set_create
        return self.create_network_protect_rule_set_endpoint.call_with_http_info(**kwargs)

    def delete_network_protect_endpoint(
        self,
        endpoint_id,
        **kwargs
    ):
        """Delete a Network Protect endpoint  # noqa: E501

        Deletes an endpoint. The endpoint must first be removed from every network policy; active references return a `409 Conflict` error.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_network_protect_endpoint(endpoint_id, async_req=True)
        >>> result = thread.get()

        Args:
            endpoint_id (str): Unique identifier of the Network Protect endpoint.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['endpoint_id'] = \
            endpoint_id
        return self.delete_network_protect_endpoint_endpoint.call_with_http_info(**kwargs)

    def delete_network_protect_network(
        self,
        network_id,
        **kwargs
    ):
        """Delete a Network Protect network  # noqa: E501

        Deletes a network and stops its advertisement and filtering. Endpoints and rule sets used by the network are not deleted.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_network_protect_network(network_id, async_req=True)
        >>> result = thread.get()

        Args:
            network_id (str): Unique identifier of the Network Protect network.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['network_id'] = \
            network_id
        return self.delete_network_protect_network_endpoint.call_with_http_info(**kwargs)

    def delete_network_protect_prefix_list(
        self,
        prefix_list_id,
        **kwargs
    ):
        """Delete a Network Protect prefix list  # noqa: E501

        Deletes a prefix list. Active rule references must be removed first; referenced lists return a `409 Conflict` error. Unknown and foreign IDs are indistinguishable and return a `404 Not Found` error.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_network_protect_prefix_list(prefix_list_id, async_req=True)
        >>> result = thread.get()

        Args:
            prefix_list_id (str): Unique identifier of the Network Protect prefix list.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['prefix_list_id'] = \
            prefix_list_id
        return self.delete_network_protect_prefix_list_endpoint.call_with_http_info(**kwargs)

    def delete_network_protect_rule_set(
        self,
        rule_set_id,
        **kwargs
    ):
        """Delete a Network Protect rule set  # noqa: E501

        Deletes a rule set. Attached rule sets cannot be deleted and return a `409 Conflict` error until their references are removed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_network_protect_rule_set(rule_set_id, async_req=True)
        >>> result = thread.get()

        Args:
            rule_set_id (str): Unique identifier of the Network Protect rule set.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['rule_set_id'] = \
            rule_set_id
        return self.delete_network_protect_rule_set_endpoint.call_with_http_info(**kwargs)

    def get_network_protect_endpoint(
        self,
        endpoint_id,
        **kwargs
    ):
        """Get a Network Protect endpoint  # noqa: E501

        Retrieves a single endpoint by its identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_network_protect_endpoint(endpoint_id, async_req=True)
        >>> result = thread.get()

        Args:
            endpoint_id (str): Unique identifier of the Network Protect endpoint.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            NetworkProtectEndpointResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['endpoint_id'] = \
            endpoint_id
        return self.get_network_protect_endpoint_endpoint.call_with_http_info(**kwargs)

    def get_network_protect_network(
        self,
        network_id,
        **kwargs
    ):
        """Get a Network Protect network  # noqa: E501

        Retrieves a single network by its identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_network_protect_network(network_id, async_req=True)
        >>> result = thread.get()

        Args:
            network_id (str): Unique identifier of the Network Protect network.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            NetworkProtectNetworkResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['network_id'] = \
            network_id
        return self.get_network_protect_network_endpoint.call_with_http_info(**kwargs)

    def get_network_protect_prefix_list(
        self,
        prefix_list_id,
        **kwargs
    ):
        """Get a Network Protect prefix list  # noqa: E501

        Retrieves a single prefix list by its identifier. Unknown and foreign IDs are indistinguishable and return a `404 Not Found` error.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_network_protect_prefix_list(prefix_list_id, async_req=True)
        >>> result = thread.get()

        Args:
            prefix_list_id (str): Unique identifier of the Network Protect prefix list.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            NetworkProtectPrefixListResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['prefix_list_id'] = \
            prefix_list_id
        return self.get_network_protect_prefix_list_endpoint.call_with_http_info(**kwargs)

    def get_network_protect_rule_set(
        self,
        rule_set_id,
        **kwargs
    ):
        """Get a Network Protect rule set  # noqa: E501

        Retrieves a single rule set with rules in evaluation order.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_network_protect_rule_set(rule_set_id, async_req=True)
        >>> result = thread.get()

        Args:
            rule_set_id (str): Unique identifier of the Network Protect rule set.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            NetworkProtectRuleSetResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['rule_set_id'] = \
            rule_set_id
        return self.get_network_protect_rule_set_endpoint.call_with_http_info(**kwargs)

    def list_network_protect_endpoints(
        self,
        **kwargs
    ):
        """List Network Protect endpoints  # noqa: E501

        Lists the customer's GRE delivery endpoints in ascending ID order. The response is cursor-paginated and includes the effective page limit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_network_protect_endpoints(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            limit (int): Maximum resources to return. Defaults to 100. Positive values above 1000 are accepted and clamped to 1000; the effective value is reported in meta.limit. Zero, negative, and non-integer values return a `400 Bad Request` error.. [optional] if omitted the server will use the default value of 100
            cursor (str): Continuation value from a previous response's meta.next_cursor. Omit this parameter to request the first page.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            NetworkProtectEndpointsResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.list_network_protect_endpoints_endpoint.call_with_http_info(**kwargs)

    def list_network_protect_networks(
        self,
        **kwargs
    ):
        """List Network Protect networks  # noqa: E501

        Lists the customer's networks in ascending ID order. The response is cursor-paginated and includes the effective page limit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_network_protect_networks(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            limit (int): Maximum resources to return. Defaults to 100. Positive values above 1000 are accepted and clamped to 1000; the effective value is reported in meta.limit. Zero, negative, and non-integer values return a `400 Bad Request` error.. [optional] if omitted the server will use the default value of 100
            cursor (str): Continuation value from a previous response's meta.next_cursor. Omit this parameter to request the first page.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            NetworkProtectNetworksResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.list_network_protect_networks_endpoint.call_with_http_info(**kwargs)

    def list_network_protect_prefix_lists(
        self,
        **kwargs
    ):
        """List Network Protect prefix lists  # noqa: E501

        Lists prefix lists in ascending ID order. Positive limits above 1000 are accepted and clamped to 1000. Invalid limits return a `400 Bad Request` error.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_network_protect_prefix_lists(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            limit (int): Maximum resources to return. Defaults to 100. Positive values above 1000 are accepted and clamped to 1000; the effective value is reported in meta.limit. Zero, negative, and non-integer values return a `400 Bad Request` error.. [optional] if omitted the server will use the default value of 100
            cursor (str): Continuation value from a previous response's meta.next_cursor. Omit this parameter to request the first page.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            NetworkProtectPrefixListsResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.list_network_protect_prefix_lists_endpoint.call_with_http_info(**kwargs)

    def list_network_protect_rule_sets(
        self,
        **kwargs
    ):
        """List Network Protect rule sets  # noqa: E501

        Lists rule sets in ascending ID order. Positive limits above 1000 are accepted and clamped to 1000; invalid limits return a `400 Bad Request` error.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_network_protect_rule_sets(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            limit (int): Maximum resources to return. Defaults to 100. Positive values above 1000 are accepted and clamped to 1000; the effective value is reported in meta.limit. Zero, negative, and non-integer values return a `400 Bad Request` error.. [optional] if omitted the server will use the default value of 100
            cursor (str): Continuation value from a previous response's meta.next_cursor. Omit this parameter to request the first page.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            NetworkProtectRuleSetsResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.list_network_protect_rule_sets_endpoint.call_with_http_info(**kwargs)

    def update_network_protect_endpoint(
        self,
        endpoint_id,
        network_protect_endpoint_update,
        **kwargs
    ):
        """Update a Network Protect endpoint  # noqa: E501

        Updates an endpoint. Omitted fields remain unchanged. The IP address cannot be changed; create a new endpoint if the destination changes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_network_protect_endpoint(endpoint_id, network_protect_endpoint_update, async_req=True)
        >>> result = thread.get()

        Args:
            endpoint_id (str): Unique identifier of the Network Protect endpoint.
            network_protect_endpoint_update (NetworkProtectEndpointUpdate):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            NetworkProtectEndpointResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['endpoint_id'] = \
            endpoint_id
        kwargs['network_protect_endpoint_update'] = \
            network_protect_endpoint_update
        return self.update_network_protect_endpoint_endpoint.call_with_http_info(**kwargs)

    def update_network_protect_network(
        self,
        network_id,
        network_protect_network_update,
        **kwargs
    ):
        """Update a Network Protect network  # noqa: E501

        Updates a network. Omitted fields remain unchanged. The prefix cannot be changed. Sending `endpoint_policies` replaces the complete policy list; an empty array removes every policy. Advertisement is desired state. Enabling it requires an approved LOA, a valid ROA, and a ready default-region delivery policy. A readiness failure returns a `409 Conflict` error.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_network_protect_network(network_id, network_protect_network_update, async_req=True)
        >>> result = thread.get()

        Args:
            network_id (str): Unique identifier of the Network Protect network.
            network_protect_network_update (NetworkProtectNetworkUpdate):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            NetworkProtectNetworkResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['network_id'] = \
            network_id
        kwargs['network_protect_network_update'] = \
            network_protect_network_update
        return self.update_network_protect_network_endpoint.call_with_http_info(**kwargs)

    def update_network_protect_prefix_list(
        self,
        prefix_list_id,
        network_protect_prefix_list_update,
        **kwargs
    ):
        """Update a Network Protect prefix list  # noqa: E501

        Updates a prefix list. The family cannot be changed. Sending addresses replaces the complete list; an empty array clears it when no active source-list restriction applies. Addresses are canonicalized, deduplicated, and sorted by the backend.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_network_protect_prefix_list(prefix_list_id, network_protect_prefix_list_update, async_req=True)
        >>> result = thread.get()

        Args:
            prefix_list_id (str): Unique identifier of the Network Protect prefix list.
            network_protect_prefix_list_update (NetworkProtectPrefixListUpdate):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            NetworkProtectPrefixListResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['prefix_list_id'] = \
            prefix_list_id
        kwargs['network_protect_prefix_list_update'] = \
            network_protect_prefix_list_update
        return self.update_network_protect_prefix_list_endpoint.call_with_http_info(**kwargs)

    def update_network_protect_rule_set(
        self,
        rule_set_id,
        network_protect_rule_set_update,
        **kwargs
    ):
        """Update a Network Protect rule set  # noqa: E501

        Updates a rule set. Omitted fields remain unchanged. Sending rules replaces the complete ordered list; an empty array removes every rule. Custom attachment and detachment remain restricted in this release.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_network_protect_rule_set(rule_set_id, network_protect_rule_set_update, async_req=True)
        >>> result = thread.get()

        Args:
            rule_set_id (str): Unique identifier of the Network Protect rule set.
            network_protect_rule_set_update (NetworkProtectRuleSetUpdate):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            NetworkProtectRuleSetResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['rule_set_id'] = \
            rule_set_id
        kwargs['network_protect_rule_set_update'] = \
            network_protect_rule_set_update
        return self.update_network_protect_rule_set_endpoint.call_with_http_info(**kwargs)

