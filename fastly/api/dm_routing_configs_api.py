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
from fastly.model.draft_diff import DraftDiff
from fastly.model.draft_update import DraftUpdate
from fastly.model.path_create import PathCreate
from fastly.model.path_response import PathResponse
from fastly.model.path_update import PathUpdate
from fastly.model.paths_response import PathsResponse
from fastly.model.routing_config import RoutingConfig
from fastly.model.routing_config_response import RoutingConfigResponse
from fastly.model.routing_config_version_response import RoutingConfigVersionResponse
from fastly.model.routing_configs_response import RoutingConfigsResponse
from fastly.model.rule_create import RuleCreate
from fastly.model.rule_response import RuleResponse
from fastly.model.rule_update import RuleUpdate
from fastly.model.rules_response import RulesResponse
from fastly.model.versions_response import VersionsResponse


class DmRoutingConfigsApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.activate_dm_routing_config_draft_endpoint = _Endpoint(
            settings={
                'response_type': (RoutingConfigVersionResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/domain-management/v1/routing-configs/{config_id}/activate',
                'operation_id': 'activate_dm_routing_config_draft',
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
                    'config_id',
                ],
                'required': [
                    'config_id',
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
                    'config_id':
                        (str,),
                },
                'attribute_map': {
                    'config_id': 'config_id',
                },
                'location_map': {
                    'config_id': 'path',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.create_dm_routing_config_endpoint = _Endpoint(
            settings={
                'response_type': (RoutingConfigResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/domain-management/v1/routing-configs',
                'operation_id': 'create_dm_routing_config',
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
                    'routing_config',
                ],
                'required': [],
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
                    'routing_config':
                        (RoutingConfig,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'routing_config': 'body',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.create_dm_routing_config_path_endpoint = _Endpoint(
            settings={
                'response_type': (PathResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/domain-management/v1/routing-configs/{config_id}/paths',
                'operation_id': 'create_dm_routing_config_path',
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
                    'config_id',
                    'path_create',
                ],
                'required': [
                    'config_id',
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
                    'config_id':
                        (str,),
                    'path_create':
                        (PathCreate,),
                },
                'attribute_map': {
                    'config_id': 'config_id',
                },
                'location_map': {
                    'config_id': 'path',
                    'path_create': 'body',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.create_dm_routing_config_rule_endpoint = _Endpoint(
            settings={
                'response_type': (RuleResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/domain-management/v1/routing-configs/{config_id}/paths/{path_id}/rules',
                'operation_id': 'create_dm_routing_config_rule',
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
                    'config_id',
                    'path_id',
                    'rule_create',
                ],
                'required': [
                    'config_id',
                    'path_id',
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
                    'config_id':
                        (str,),
                    'path_id':
                        (str,),
                    'rule_create':
                        (RuleCreate,),
                },
                'attribute_map': {
                    'config_id': 'config_id',
                    'path_id': 'path_id',
                },
                'location_map': {
                    'config_id': 'path',
                    'path_id': 'path',
                    'rule_create': 'body',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.deactivate_dm_routing_config_endpoint = _Endpoint(
            settings={
                'response_type': (RoutingConfigResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/domain-management/v1/routing-configs/{config_id}/deactivate',
                'operation_id': 'deactivate_dm_routing_config',
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
                    'config_id',
                ],
                'required': [
                    'config_id',
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
                    'config_id':
                        (str,),
                },
                'attribute_map': {
                    'config_id': 'config_id',
                },
                'location_map': {
                    'config_id': 'path',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.delete_dm_routing_config_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'token'
                ],
                'endpoint_path': '/domain-management/v1/routing-configs/{config_id}',
                'operation_id': 'delete_dm_routing_config',
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
                    'config_id',
                    'force',
                ],
                'required': [
                    'config_id',
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
                    'config_id':
                        (str,),
                    'force':
                        (bool,),
                },
                'attribute_map': {
                    'config_id': 'config_id',
                    'force': 'force',
                },
                'location_map': {
                    'config_id': 'path',
                    'force': 'query',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client
        )
        self.delete_dm_routing_config_inactive_versions_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'token'
                ],
                'endpoint_path': '/domain-management/v1/routing-configs/{config_id}/versions/inactive',
                'operation_id': 'delete_dm_routing_config_inactive_versions',
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
                    'config_id',
                ],
                'required': [
                    'config_id',
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
                    'config_id':
                        (str,),
                },
                'attribute_map': {
                    'config_id': 'config_id',
                },
                'location_map': {
                    'config_id': 'path',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client
        )
        self.delete_dm_routing_config_path_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'token'
                ],
                'endpoint_path': '/domain-management/v1/routing-configs/{config_id}/paths/{path_id}',
                'operation_id': 'delete_dm_routing_config_path',
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
                    'config_id',
                    'path_id',
                ],
                'required': [
                    'config_id',
                    'path_id',
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
                    'config_id':
                        (str,),
                    'path_id':
                        (str,),
                },
                'attribute_map': {
                    'config_id': 'config_id',
                    'path_id': 'path_id',
                },
                'location_map': {
                    'config_id': 'path',
                    'path_id': 'path',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client
        )
        self.delete_dm_routing_config_rule_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'token'
                ],
                'endpoint_path': '/domain-management/v1/routing-configs/{config_id}/paths/{path_id}/rules/{rule_id}',
                'operation_id': 'delete_dm_routing_config_rule',
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
                    'config_id',
                    'path_id',
                    'rule_id',
                ],
                'required': [
                    'config_id',
                    'path_id',
                    'rule_id',
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
                    'config_id':
                        (str,),
                    'path_id':
                        (str,),
                    'rule_id':
                        (str,),
                },
                'attribute_map': {
                    'config_id': 'config_id',
                    'path_id': 'path_id',
                    'rule_id': 'rule_id',
                },
                'location_map': {
                    'config_id': 'path',
                    'path_id': 'path',
                    'rule_id': 'path',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client
        )
        self.discard_dm_routing_config_draft_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'token'
                ],
                'endpoint_path': '/domain-management/v1/routing-configs/{config_id}/draft',
                'operation_id': 'discard_dm_routing_config_draft',
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
                    'config_id',
                ],
                'required': [
                    'config_id',
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
                    'config_id':
                        (str,),
                },
                'attribute_map': {
                    'config_id': 'config_id',
                },
                'location_map': {
                    'config_id': 'path',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_dm_routing_config_endpoint = _Endpoint(
            settings={
                'response_type': (RoutingConfigResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/domain-management/v1/routing-configs/{config_id}',
                'operation_id': 'get_dm_routing_config',
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
                    'config_id',
                ],
                'required': [
                    'config_id',
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
                    'config_id':
                        (str,),
                },
                'attribute_map': {
                    'config_id': 'config_id',
                },
                'location_map': {
                    'config_id': 'path',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_dm_routing_config_draft_diff_endpoint = _Endpoint(
            settings={
                'response_type': (DraftDiff,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/domain-management/v1/routing-configs/{config_id}/draft/diff',
                'operation_id': 'get_dm_routing_config_draft_diff',
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
                    'config_id',
                ],
                'required': [
                    'config_id',
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
                    'config_id':
                        (str,),
                },
                'attribute_map': {
                    'config_id': 'config_id',
                },
                'location_map': {
                    'config_id': 'path',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_dm_routing_config_path_endpoint = _Endpoint(
            settings={
                'response_type': (PathResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/domain-management/v1/routing-configs/{config_id}/paths/{path_id}',
                'operation_id': 'get_dm_routing_config_path',
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
                    'config_id',
                    'path_id',
                ],
                'required': [
                    'config_id',
                    'path_id',
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
                    'config_id':
                        (str,),
                    'path_id':
                        (str,),
                },
                'attribute_map': {
                    'config_id': 'config_id',
                    'path_id': 'path_id',
                },
                'location_map': {
                    'config_id': 'path',
                    'path_id': 'path',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_dm_routing_config_rule_endpoint = _Endpoint(
            settings={
                'response_type': (RuleResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/domain-management/v1/routing-configs/{config_id}/paths/{path_id}/rules/{rule_id}',
                'operation_id': 'get_dm_routing_config_rule',
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
                    'config_id',
                    'path_id',
                    'rule_id',
                ],
                'required': [
                    'config_id',
                    'path_id',
                    'rule_id',
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
                    'config_id':
                        (str,),
                    'path_id':
                        (str,),
                    'rule_id':
                        (str,),
                },
                'attribute_map': {
                    'config_id': 'config_id',
                    'path_id': 'path_id',
                    'rule_id': 'rule_id',
                },
                'location_map': {
                    'config_id': 'path',
                    'path_id': 'path',
                    'rule_id': 'path',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_dm_routing_config_paths_endpoint = _Endpoint(
            settings={
                'response_type': (PathsResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/domain-management/v1/routing-configs/{config_id}/paths',
                'operation_id': 'list_dm_routing_config_paths',
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
                    'config_id',
                    'path',
                    'match',
                    'sort',
                    'cursor',
                    'limit',
                ],
                'required': [
                    'config_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'match',
                    'sort',
                ],
                'validation': [
                    'limit',
                ]
            },
            root_map={
                'validations': {
                    ('limit',): {

                        'inclusive_maximum': 100,
                    },
                },
                'allowed_values': {
                    ('match',): {

                        "path_match_exact": "exact",
                        "path_match_starts_with": "starts_with",
                        "path_match_ends_with": "ends_with",
                        "path_match_contains": "contains"
                    },
                    ('sort',): {

                        "path_sort_created_at_asc": "created_at",
                        "path_sort_created_at_desc": "-created_at",
                        "path_sort_id_asc": "id",
                        "path_sort_id_desc": "-id",
                        "path_sort_path_asc": "path",
                        "path_sort_path_desc": "-path"
                    },
                },
                'openapi_types': {
                    'config_id':
                        (str,),
                    'path':
                        (str,),
                    'match':
                        (str,),
                    'sort':
                        (str,),
                    'cursor':
                        (str,),
                    'limit':
                        (int,),
                },
                'attribute_map': {
                    'config_id': 'config_id',
                    'path': 'path',
                    'match': 'match',
                    'sort': 'sort',
                    'cursor': 'cursor',
                    'limit': 'limit',
                },
                'location_map': {
                    'config_id': 'path',
                    'path': 'query',
                    'match': 'query',
                    'sort': 'query',
                    'cursor': 'query',
                    'limit': 'query',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_dm_routing_config_rules_endpoint = _Endpoint(
            settings={
                'response_type': (RulesResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/domain-management/v1/routing-configs/{config_id}/paths/{path_id}/rules',
                'operation_id': 'list_dm_routing_config_rules',
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
                    'config_id',
                    'path_id',
                    'sort',
                    'cursor',
                    'limit',
                ],
                'required': [
                    'config_id',
                    'path_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'sort',
                ],
                'validation': [
                    'limit',
                ]
            },
            root_map={
                'validations': {
                    ('limit',): {

                        'inclusive_maximum': 100,
                    },
                },
                'allowed_values': {
                    ('sort',): {

                        "rule_sort_created_at_asc": "created_at",
                        "rule_sort_created_at_desc": "-created_at",
                        "rule_sort_position_asc": "position",
                        "rule_sort_position_desc": "-position"
                    },
                },
                'openapi_types': {
                    'config_id':
                        (str,),
                    'path_id':
                        (str,),
                    'sort':
                        (str,),
                    'cursor':
                        (str,),
                    'limit':
                        (int,),
                },
                'attribute_map': {
                    'config_id': 'config_id',
                    'path_id': 'path_id',
                    'sort': 'sort',
                    'cursor': 'cursor',
                    'limit': 'limit',
                },
                'location_map': {
                    'config_id': 'path',
                    'path_id': 'path',
                    'sort': 'query',
                    'cursor': 'query',
                    'limit': 'query',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_dm_routing_config_versions_endpoint = _Endpoint(
            settings={
                'response_type': (VersionsResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/domain-management/v1/routing-configs/{config_id}/versions',
                'operation_id': 'list_dm_routing_config_versions',
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
                    'config_id',
                    'sort',
                    'cursor',
                    'limit',
                ],
                'required': [
                    'config_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'sort',
                ],
                'validation': [
                    'limit',
                ]
            },
            root_map={
                'validations': {
                    ('limit',): {

                        'inclusive_maximum': 100,
                    },
                },
                'allowed_values': {
                    ('sort',): {

                        "version_sort_activated_at_asc": "activated_at",
                        "version_sort_activated_at_desc": "-activated_at",
                        "version_sort_created_at_asc": "created_at",
                        "version_sort_created_at_desc": "-created_at"
                    },
                },
                'openapi_types': {
                    'config_id':
                        (str,),
                    'sort':
                        (str,),
                    'cursor':
                        (str,),
                    'limit':
                        (int,),
                },
                'attribute_map': {
                    'config_id': 'config_id',
                    'sort': 'sort',
                    'cursor': 'cursor',
                    'limit': 'limit',
                },
                'location_map': {
                    'config_id': 'path',
                    'sort': 'query',
                    'cursor': 'query',
                    'limit': 'query',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_dm_routing_configs_endpoint = _Endpoint(
            settings={
                'response_type': (RoutingConfigsResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/domain-management/v1/routing-configs',
                'operation_id': 'list_dm_routing_configs',
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
                    'state',
                    'sort',
                    'cursor',
                    'limit',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'state',
                    'sort',
                ],
                'validation': [
                    'limit',
                ]
            },
            root_map={
                'validations': {
                    ('limit',): {

                        'inclusive_maximum': 100,
                    },
                },
                'allowed_values': {
                    ('state',): {

                        "DRAFT-ONLY": "draft-only",
                        "ACTIVE": "active",
                        "ACTIVE-WITH-DRAFT": "active-with-draft"
                    },
                    ('sort',): {

                        "config_sort_created_at_asc": "created_at",
                        "config_sort_created_at_desc": "-created_at",
                        "config_sort_id_asc": "id",
                        "config_sort_id_desc": "-id",
                        "config_sort_name_asc": "name",
                        "config_sort_name_desc": "-name"
                    },
                },
                'openapi_types': {
                    'state':
                        ([str],),
                    'sort':
                        (str,),
                    'cursor':
                        (str,),
                    'limit':
                        (int,),
                },
                'attribute_map': {
                    'state': 'state',
                    'sort': 'sort',
                    'cursor': 'cursor',
                    'limit': 'limit',
                },
                'location_map': {
                    'state': 'query',
                    'sort': 'query',
                    'cursor': 'query',
                    'limit': 'query',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                    'state': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.reactivate_dm_routing_config_version_endpoint = _Endpoint(
            settings={
                'response_type': (RoutingConfigVersionResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/domain-management/v1/routing-configs/{config_id}/versions/{version_id}/activate',
                'operation_id': 'reactivate_dm_routing_config_version',
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
                    'config_id',
                    'version_id',
                ],
                'required': [
                    'config_id',
                    'version_id',
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
                    'config_id':
                        (str,),
                    'version_id':
                        (str,),
                },
                'attribute_map': {
                    'config_id': 'config_id',
                    'version_id': 'version_id',
                },
                'location_map': {
                    'config_id': 'path',
                    'version_id': 'path',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.update_dm_routing_config_draft_endpoint = _Endpoint(
            settings={
                'response_type': (RoutingConfigVersionResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/domain-management/v1/routing-configs/{config_id}/draft',
                'operation_id': 'update_dm_routing_config_draft',
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
                    'config_id',
                    'draft_update',
                ],
                'required': [
                    'config_id',
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
                    'config_id':
                        (str,),
                    'draft_update':
                        (DraftUpdate,),
                },
                'attribute_map': {
                    'config_id': 'config_id',
                },
                'location_map': {
                    'config_id': 'path',
                    'draft_update': 'body',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.update_dm_routing_config_path_endpoint = _Endpoint(
            settings={
                'response_type': (PathResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/domain-management/v1/routing-configs/{config_id}/paths/{path_id}',
                'operation_id': 'update_dm_routing_config_path',
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
                    'config_id',
                    'path_id',
                    'path_update',
                ],
                'required': [
                    'config_id',
                    'path_id',
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
                    'config_id':
                        (str,),
                    'path_id':
                        (str,),
                    'path_update':
                        (PathUpdate,),
                },
                'attribute_map': {
                    'config_id': 'config_id',
                    'path_id': 'path_id',
                },
                'location_map': {
                    'config_id': 'path',
                    'path_id': 'path',
                    'path_update': 'body',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.update_dm_routing_config_rule_endpoint = _Endpoint(
            settings={
                'response_type': (RuleResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/domain-management/v1/routing-configs/{config_id}/paths/{path_id}/rules/{rule_id}',
                'operation_id': 'update_dm_routing_config_rule',
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
                    'config_id',
                    'path_id',
                    'rule_id',
                    'rule_update',
                ],
                'required': [
                    'config_id',
                    'path_id',
                    'rule_id',
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
                    'config_id':
                        (str,),
                    'path_id':
                        (str,),
                    'rule_id':
                        (str,),
                    'rule_update':
                        (RuleUpdate,),
                },
                'attribute_map': {
                    'config_id': 'config_id',
                    'path_id': 'path_id',
                    'rule_id': 'rule_id',
                },
                'location_map': {
                    'config_id': 'path',
                    'path_id': 'path',
                    'rule_id': 'path',
                    'rule_update': 'body',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def activate_dm_routing_config_draft(
        self,
        config_id,
        **kwargs
    ):
        """Activate the draft  # noqa: E501

        Activate the current draft version. The previously active version, if any, becomes inactive but is retained in version history.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.activate_dm_routing_config_draft(config_id, async_req=True)
        >>> result = thread.get()

        Args:
            config_id (str):

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
            RoutingConfigVersionResponse
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
        kwargs['config_id'] = \
            config_id
        return self.activate_dm_routing_config_draft_endpoint.call_with_http_info(**kwargs)

    def create_dm_routing_config(
        self,
        **kwargs
    ):
        """Create a routing config  # noqa: E501

        Create a new routing config. An optional `initial_version` may be provided to seed the config with paths and rules in a single request, and may also be activated immediately.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_dm_routing_config(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            routing_config (RoutingConfig): [optional]
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
            RoutingConfigResponse
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
        return self.create_dm_routing_config_endpoint.call_with_http_info(**kwargs)

    def create_dm_routing_config_path(
        self,
        config_id,
        **kwargs
    ):
        """Create a path  # noqa: E501

        Add a new path to the config's draft version. If no draft exists, one is created automatically by cloning the active version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_dm_routing_config_path(config_id, async_req=True)
        >>> result = thread.get()

        Args:
            config_id (str):

        Keyword Args:
            path_create (PathCreate): [optional]
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
            PathResponse
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
        kwargs['config_id'] = \
            config_id
        return self.create_dm_routing_config_path_endpoint.call_with_http_info(**kwargs)

    def create_dm_routing_config_rule(
        self,
        config_id,
        path_id,
        **kwargs
    ):
        """Create a rule  # noqa: E501

        Add a new rule to a path on the config's draft version. If no draft exists, one is created automatically by cloning the active version. A rule with an empty `conditions` array is a default (catch-all) rule and there can be at most one default rule per path.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_dm_routing_config_rule(config_id, path_id, async_req=True)
        >>> result = thread.get()

        Args:
            config_id (str):
            path_id (str):

        Keyword Args:
            rule_create (RuleCreate): [optional]
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
            RuleResponse
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
        kwargs['config_id'] = \
            config_id
        kwargs['path_id'] = \
            path_id
        return self.create_dm_routing_config_rule_endpoint.call_with_http_info(**kwargs)

    def deactivate_dm_routing_config(
        self,
        config_id,
        **kwargs
    ):
        """Deactivate a routing config  # noqa: E501

        Clear the active version designation. This is a bookkeeping operation only — it does not stop edge traffic. Minerva continues serving the last-activated version until the domain association is removed in Spotless. Only removing the routing config from the domain (via Spotless) triggers Neptune to drop the reference, which causes Minerva to stop fetching and eventually clean up the cached config. Idempotent: returns 200 even if already deactivated.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.deactivate_dm_routing_config(config_id, async_req=True)
        >>> result = thread.get()

        Args:
            config_id (str):

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
            RoutingConfigResponse
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
        kwargs['config_id'] = \
            config_id
        return self.deactivate_dm_routing_config_endpoint.call_with_http_info(**kwargs)

    def delete_dm_routing_config(
        self,
        config_id,
        **kwargs
    ):
        """Delete a routing config  # noqa: E501

        Delete a routing config. By default, configs that have an active version cannot be deleted. Pass `force=true` to bypass the active-version check — this is destructive and will immediately stop traffic routing for any paths the config serves. The `force` parameter does **not** bypass the domain-association check; if domains are still associated, deletion is rejected with 409 regardless of `force`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_dm_routing_config(config_id, async_req=True)
        >>> result = thread.get()

        Args:
            config_id (str):

        Keyword Args:
            force (bool): When `true`, allows deleting a routing config that has an active version. This is destructive — traffic routing for any paths served by the config will stop immediately.. [optional] if omitted the server will use the default value of False
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
        kwargs['config_id'] = \
            config_id
        return self.delete_dm_routing_config_endpoint.call_with_http_info(**kwargs)

    def delete_dm_routing_config_inactive_versions(
        self,
        config_id,
        **kwargs
    ):
        """Delete inactive versions  # noqa: E501

        Delete all inactive versions for a routing config. The currently active version, if any, is retained.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_dm_routing_config_inactive_versions(config_id, async_req=True)
        >>> result = thread.get()

        Args:
            config_id (str):

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
        kwargs['config_id'] = \
            config_id
        return self.delete_dm_routing_config_inactive_versions_endpoint.call_with_http_info(**kwargs)

    def delete_dm_routing_config_path(
        self,
        config_id,
        path_id,
        **kwargs
    ):
        """Delete a path  # noqa: E501

        Delete a path from the config's draft version. If no draft exists, one is created automatically by cloning the active version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_dm_routing_config_path(config_id, path_id, async_req=True)
        >>> result = thread.get()

        Args:
            config_id (str):
            path_id (str):

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
        kwargs['config_id'] = \
            config_id
        kwargs['path_id'] = \
            path_id
        return self.delete_dm_routing_config_path_endpoint.call_with_http_info(**kwargs)

    def delete_dm_routing_config_rule(
        self,
        config_id,
        path_id,
        rule_id,
        **kwargs
    ):
        """Delete a rule  # noqa: E501

        Delete a rule from the config's draft version. If no draft exists, one is created automatically by cloning the active version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_dm_routing_config_rule(config_id, path_id, rule_id, async_req=True)
        >>> result = thread.get()

        Args:
            config_id (str):
            path_id (str):
            rule_id (str):

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
        kwargs['config_id'] = \
            config_id
        kwargs['path_id'] = \
            path_id
        kwargs['rule_id'] = \
            rule_id
        return self.delete_dm_routing_config_rule_endpoint.call_with_http_info(**kwargs)

    def discard_dm_routing_config_draft(
        self,
        config_id,
        **kwargs
    ):
        """Discard the draft  # noqa: E501

        Delete the current draft version, reverting any unactivated changes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.discard_dm_routing_config_draft(config_id, async_req=True)
        >>> result = thread.get()

        Args:
            config_id (str):

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
        kwargs['config_id'] = \
            config_id
        return self.discard_dm_routing_config_draft_endpoint.call_with_http_info(**kwargs)

    def get_dm_routing_config(
        self,
        config_id,
        **kwargs
    ):
        """Get a routing config  # noqa: E501

        Retrieve a single routing config by its identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dm_routing_config(config_id, async_req=True)
        >>> result = thread.get()

        Args:
            config_id (str):

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
            RoutingConfigResponse
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
        kwargs['config_id'] = \
            config_id
        return self.get_dm_routing_config_endpoint.call_with_http_info(**kwargs)

    def get_dm_routing_config_draft_diff(
        self,
        config_id,
        **kwargs
    ):
        """Get the draft diff  # noqa: E501

        Compare the current draft version against the active version and return the paths and rules that have been added, modified, or deleted.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dm_routing_config_draft_diff(config_id, async_req=True)
        >>> result = thread.get()

        Args:
            config_id (str):

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
            DraftDiff
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
        kwargs['config_id'] = \
            config_id
        return self.get_dm_routing_config_draft_diff_endpoint.call_with_http_info(**kwargs)

    def get_dm_routing_config_path(
        self,
        config_id,
        path_id,
        **kwargs
    ):
        """Get a path  # noqa: E501

        Retrieve a single path by its stable identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dm_routing_config_path(config_id, path_id, async_req=True)
        >>> result = thread.get()

        Args:
            config_id (str):
            path_id (str):

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
            PathResponse
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
        kwargs['config_id'] = \
            config_id
        kwargs['path_id'] = \
            path_id
        return self.get_dm_routing_config_path_endpoint.call_with_http_info(**kwargs)

    def get_dm_routing_config_rule(
        self,
        config_id,
        path_id,
        rule_id,
        **kwargs
    ):
        """Get a rule  # noqa: E501

        Retrieve a single rule by its stable identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dm_routing_config_rule(config_id, path_id, rule_id, async_req=True)
        >>> result = thread.get()

        Args:
            config_id (str):
            path_id (str):
            rule_id (str):

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
            RuleResponse
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
        kwargs['config_id'] = \
            config_id
        kwargs['path_id'] = \
            path_id
        kwargs['rule_id'] = \
            rule_id
        return self.get_dm_routing_config_rule_endpoint.call_with_http_info(**kwargs)

    def list_dm_routing_config_paths(
        self,
        config_id,
        **kwargs
    ):
        """List paths  # noqa: E501

        List paths for the config. Returns paths from the active version if one exists, otherwise from the draft.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_dm_routing_config_paths(config_id, async_req=True)
        >>> result = thread.get()

        Args:
            config_id (str):

        Keyword Args:
            path (str): Filter results by path pattern. The match strategy is controlled by the `match` parameter.. [optional]
            match (str): How to match the value of the `path` filter against existing path patterns. Has no effect unless `path` is also provided.. [optional] if omitted the server will use the default value of "exact"
            sort (str): The order in which to list the results.. [optional] if omitted the server will use the default value of "-created_at"
            cursor (str): Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty.. [optional]
            limit (int): Limit how many results are returned.. [optional] if omitted the server will use the default value of 20
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
            PathsResponse
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
        kwargs['config_id'] = \
            config_id
        return self.list_dm_routing_config_paths_endpoint.call_with_http_info(**kwargs)

    def list_dm_routing_config_rules(
        self,
        config_id,
        path_id,
        **kwargs
    ):
        """List rules  # noqa: E501

        List all rules for a path in evaluation order.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_dm_routing_config_rules(config_id, path_id, async_req=True)
        >>> result = thread.get()

        Args:
            config_id (str):
            path_id (str):

        Keyword Args:
            sort (str): The order in which to list the results.. [optional] if omitted the server will use the default value of "position"
            cursor (str): Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty.. [optional]
            limit (int): Limit how many results are returned.. [optional] if omitted the server will use the default value of 20
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
            RulesResponse
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
        kwargs['config_id'] = \
            config_id
        kwargs['path_id'] = \
            path_id
        return self.list_dm_routing_config_rules_endpoint.call_with_http_info(**kwargs)

    def list_dm_routing_config_versions(
        self,
        config_id,
        **kwargs
    ):
        """List versions  # noqa: E501

        List all versions for a routing config.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_dm_routing_config_versions(config_id, async_req=True)
        >>> result = thread.get()

        Args:
            config_id (str):

        Keyword Args:
            sort (str): The order in which to list the results.. [optional] if omitted the server will use the default value of "-activated_at"
            cursor (str): Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty.. [optional]
            limit (int): Limit how many results are returned.. [optional] if omitted the server will use the default value of 20
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
            VersionsResponse
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
        kwargs['config_id'] = \
            config_id
        return self.list_dm_routing_config_versions_endpoint.call_with_http_info(**kwargs)

    def list_dm_routing_configs(
        self,
        **kwargs
    ):
        """List routing configs  # noqa: E501

        List all routing configs for the authenticated customer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_dm_routing_configs(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            state ([str]): Filter configs by lifecycle state. Accepts a comma-separated list of state values (e.g. `?state=active,active-with-draft`). Returns only configs whose current state matches one of the provided values. Returns 400 if any value is not a recognised state.. [optional]
            sort (str): The order in which to list the results.. [optional] if omitted the server will use the default value of "-created_at"
            cursor (str): Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty.. [optional]
            limit (int): Limit how many results are returned.. [optional] if omitted the server will use the default value of 20
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
            RoutingConfigsResponse
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
        return self.list_dm_routing_configs_endpoint.call_with_http_info(**kwargs)

    def reactivate_dm_routing_config_version(
        self,
        config_id,
        version_id,
        **kwargs
    ):
        """Reactivate a version  # noqa: E501

        Reactivate a previously-active version. The currently active version, if any, becomes inactive but is retained in version history.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.reactivate_dm_routing_config_version(config_id, version_id, async_req=True)
        >>> result = thread.get()

        Args:
            config_id (str):
            version_id (str):

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
            RoutingConfigVersionResponse
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
        kwargs['config_id'] = \
            config_id
        kwargs['version_id'] = \
            version_id
        return self.reactivate_dm_routing_config_version_endpoint.call_with_http_info(**kwargs)

    def update_dm_routing_config_draft(
        self,
        config_id,
        **kwargs
    ):
        """Update the draft  # noqa: E501

        Update metadata on the draft version, such as its comment. If no draft exists, one is created automatically by cloning the active version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_dm_routing_config_draft(config_id, async_req=True)
        >>> result = thread.get()

        Args:
            config_id (str):

        Keyword Args:
            draft_update (DraftUpdate): [optional]
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
            RoutingConfigVersionResponse
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
        kwargs['config_id'] = \
            config_id
        return self.update_dm_routing_config_draft_endpoint.call_with_http_info(**kwargs)

    def update_dm_routing_config_path(
        self,
        config_id,
        path_id,
        **kwargs
    ):
        """Update a path  # noqa: E501

        Update a path on the config's draft version. If no draft exists, one is created automatically by cloning the active version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_dm_routing_config_path(config_id, path_id, async_req=True)
        >>> result = thread.get()

        Args:
            config_id (str):
            path_id (str):

        Keyword Args:
            path_update (PathUpdate): [optional]
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
            PathResponse
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
        kwargs['config_id'] = \
            config_id
        kwargs['path_id'] = \
            path_id
        return self.update_dm_routing_config_path_endpoint.call_with_http_info(**kwargs)

    def update_dm_routing_config_rule(
        self,
        config_id,
        path_id,
        rule_id,
        **kwargs
    ):
        """Update a rule  # noqa: E501

        Update a rule on the config's draft version. If no draft exists, one is created automatically by cloning the active version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_dm_routing_config_rule(config_id, path_id, rule_id, async_req=True)
        >>> result = thread.get()

        Args:
            config_id (str):
            path_id (str):
            rule_id (str):

        Keyword Args:
            rule_update (RuleUpdate): [optional]
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
            RuleResponse
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
        kwargs['config_id'] = \
            config_id
        kwargs['path_id'] = \
            path_id
        kwargs['rule_id'] = \
            rule_id
        return self.update_dm_routing_config_rule_endpoint.call_with_http_info(**kwargs)

