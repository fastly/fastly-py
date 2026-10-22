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
from fastly.model.bot_management_bot import BotManagementBot
from fastly.model.bot_management_bot_response import BotManagementBotResponse
from fastly.model.bot_management_bots_response import BotManagementBotsResponse
from fastly.model.bot_management_categories_response import BotManagementCategoriesResponse
from fastly.model.bot_management_category import BotManagementCategory
from fastly.model.bot_management_category_response import BotManagementCategoryResponse
from fastly.model.bot_management_invalid_request_error import BotManagementInvalidRequestError
from fastly.model.bot_management_not_allowed_error import BotManagementNotAllowedError
from fastly.model.bot_management_not_authenticated_error import BotManagementNotAuthenticatedError
from fastly.model.bot_management_not_found_error import BotManagementNotFoundError
from fastly.model.bot_management_rate_limit_error import BotManagementRateLimitError
from fastly.model.bot_management_workspace import BotManagementWorkspace
from fastly.model.bot_management_workspace_bots_response import BotManagementWorkspaceBotsResponse
from fastly.model.bot_management_workspace_response import BotManagementWorkspaceResponse
from fastly.model.bot_management_workspaces_response import BotManagementWorkspacesResponse


class BotManagementApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.bot_management_get_bot_endpoint = _Endpoint(
            settings={
                'response_type': (BotManagementBotResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/bot-management/v1/workspaces/{workspace_id}/policy/categories/{category_id}/bots/{bot_id}',
                'operation_id': 'bot_management_get_bot',
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
                    'workspace_id',
                    'category_id',
                    'bot_id',
                ],
                'required': [
                    'workspace_id',
                    'category_id',
                    'bot_id',
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
                    'workspace_id':
                        (str,),
                    'category_id':
                        (str,),
                    'bot_id':
                        (str,),
                },
                'attribute_map': {
                    'workspace_id': 'workspace_id',
                    'category_id': 'category_id',
                    'bot_id': 'bot_id',
                },
                'location_map': {
                    'workspace_id': 'path',
                    'category_id': 'path',
                    'bot_id': 'path',
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
        self.bot_management_get_category_endpoint = _Endpoint(
            settings={
                'response_type': (BotManagementCategoryResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/bot-management/v1/workspaces/{workspace_id}/policy/categories/{category_id}',
                'operation_id': 'bot_management_get_category',
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
                    'workspace_id',
                    'category_id',
                ],
                'required': [
                    'workspace_id',
                    'category_id',
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
                    'workspace_id':
                        (str,),
                    'category_id':
                        (str,),
                },
                'attribute_map': {
                    'workspace_id': 'workspace_id',
                    'category_id': 'category_id',
                },
                'location_map': {
                    'workspace_id': 'path',
                    'category_id': 'path',
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
        self.bot_management_get_workspace_endpoint = _Endpoint(
            settings={
                'response_type': (BotManagementWorkspaceResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/bot-management/v1/workspaces/{workspace_id}',
                'operation_id': 'bot_management_get_workspace',
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
                    'workspace_id',
                ],
                'required': [
                    'workspace_id',
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
                    'workspace_id':
                        (str,),
                },
                'attribute_map': {
                    'workspace_id': 'workspace_id',
                },
                'location_map': {
                    'workspace_id': 'path',
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
        self.bot_management_list_bots_endpoint = _Endpoint(
            settings={
                'response_type': (BotManagementWorkspaceBotsResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/bot-management/v1/workspaces/{workspace_id}/policy/bots',
                'operation_id': 'bot_management_list_bots',
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
                    'workspace_id',
                    'limit',
                    'cursor',
                ],
                'required': [
                    'workspace_id',
                ],
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

                        'inclusive_maximum': 1000,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'workspace_id':
                        (str,),
                    'limit':
                        (int,),
                    'cursor':
                        (str,),
                },
                'attribute_map': {
                    'workspace_id': 'workspace_id',
                    'limit': 'limit',
                    'cursor': 'cursor',
                },
                'location_map': {
                    'workspace_id': 'path',
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
        self.bot_management_list_categories_endpoint = _Endpoint(
            settings={
                'response_type': (BotManagementCategoriesResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/bot-management/v1/workspaces/{workspace_id}/policy/categories',
                'operation_id': 'bot_management_list_categories',
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
                    'workspace_id',
                    'limit',
                    'cursor',
                ],
                'required': [
                    'workspace_id',
                ],
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

                        'inclusive_maximum': 1000,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'workspace_id':
                        (str,),
                    'limit':
                        (int,),
                    'cursor':
                        (str,),
                },
                'attribute_map': {
                    'workspace_id': 'workspace_id',
                    'limit': 'limit',
                    'cursor': 'cursor',
                },
                'location_map': {
                    'workspace_id': 'path',
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
        self.bot_management_list_category_bots_endpoint = _Endpoint(
            settings={
                'response_type': (BotManagementBotsResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/bot-management/v1/workspaces/{workspace_id}/policy/categories/{category_id}/bots',
                'operation_id': 'bot_management_list_category_bots',
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
                    'workspace_id',
                    'category_id',
                    'limit',
                    'cursor',
                ],
                'required': [
                    'workspace_id',
                    'category_id',
                ],
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

                        'inclusive_maximum': 1000,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'workspace_id':
                        (str,),
                    'category_id':
                        (str,),
                    'limit':
                        (int,),
                    'cursor':
                        (str,),
                },
                'attribute_map': {
                    'workspace_id': 'workspace_id',
                    'category_id': 'category_id',
                    'limit': 'limit',
                    'cursor': 'cursor',
                },
                'location_map': {
                    'workspace_id': 'path',
                    'category_id': 'path',
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
        self.bot_management_list_workspaces_endpoint = _Endpoint(
            settings={
                'response_type': (BotManagementWorkspacesResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/bot-management/v1/workspaces',
                'operation_id': 'bot_management_list_workspaces',
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
                    'service_id',
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

                        'inclusive_maximum': 1000,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'limit':
                        (int,),
                    'cursor':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'limit': 'limit',
                    'cursor': 'cursor',
                },
                'location_map': {
                    'service_id': 'query',
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
        self.bot_management_update_bot_endpoint = _Endpoint(
            settings={
                'response_type': (BotManagementBotResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/bot-management/v1/workspaces/{workspace_id}/policy/categories/{category_id}/bots/{bot_id}',
                'operation_id': 'bot_management_update_bot',
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
                    'workspace_id',
                    'category_id',
                    'bot_id',
                    'bot_management_bot',
                ],
                'required': [
                    'workspace_id',
                    'category_id',
                    'bot_id',
                    'bot_management_bot',
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
                    'workspace_id':
                        (str,),
                    'category_id':
                        (str,),
                    'bot_id':
                        (str,),
                    'bot_management_bot':
                        (BotManagementBot,),
                },
                'attribute_map': {
                    'workspace_id': 'workspace_id',
                    'category_id': 'category_id',
                    'bot_id': 'bot_id',
                },
                'location_map': {
                    'workspace_id': 'path',
                    'category_id': 'path',
                    'bot_id': 'path',
                    'bot_management_bot': 'body',
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
        self.bot_management_update_category_endpoint = _Endpoint(
            settings={
                'response_type': (BotManagementCategoryResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/bot-management/v1/workspaces/{workspace_id}/policy/categories/{category_id}',
                'operation_id': 'bot_management_update_category',
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
                    'workspace_id',
                    'category_id',
                    'bot_management_category',
                ],
                'required': [
                    'workspace_id',
                    'category_id',
                    'bot_management_category',
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
                    'workspace_id':
                        (str,),
                    'category_id':
                        (str,),
                    'bot_management_category':
                        (BotManagementCategory,),
                },
                'attribute_map': {
                    'workspace_id': 'workspace_id',
                    'category_id': 'category_id',
                },
                'location_map': {
                    'workspace_id': 'path',
                    'category_id': 'path',
                    'bot_management_category': 'body',
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
        self.bot_management_update_workspace_endpoint = _Endpoint(
            settings={
                'response_type': (BotManagementWorkspaceResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/bot-management/v1/workspaces/{workspace_id}',
                'operation_id': 'bot_management_update_workspace',
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
                    'workspace_id',
                    'bot_management_workspace',
                ],
                'required': [
                    'workspace_id',
                    'bot_management_workspace',
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
                    'workspace_id':
                        (str,),
                    'bot_management_workspace':
                        (BotManagementWorkspace,),
                },
                'attribute_map': {
                    'workspace_id': 'workspace_id',
                },
                'location_map': {
                    'workspace_id': 'path',
                    'bot_management_workspace': 'body',
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

    def bot_management_get_bot(
        self,
        workspace_id,
        category_id,
        bot_id,
        **kwargs
    ):
        """Get a bot  # noqa: E501

        Get the attributes of a bot in a category.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.bot_management_get_bot(workspace_id, category_id, bot_id, async_req=True)
        >>> result = thread.get()

        Args:
            workspace_id (str): The ID of the bot management workspace.
            category_id (str): The ID of the bot category.
            bot_id (str): The ID of the bot.

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
            BotManagementBotResponse
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
        kwargs['workspace_id'] = \
            workspace_id
        kwargs['category_id'] = \
            category_id
        kwargs['bot_id'] = \
            bot_id
        return self.bot_management_get_bot_endpoint.call_with_http_info(**kwargs)

    def bot_management_get_category(
        self,
        workspace_id,
        category_id,
        **kwargs
    ):
        """Get a category  # noqa: E501

        Get the attributes of a bot category.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.bot_management_get_category(workspace_id, category_id, async_req=True)
        >>> result = thread.get()

        Args:
            workspace_id (str): The ID of the bot management workspace.
            category_id (str): The ID of the bot category.

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
            BotManagementCategoryResponse
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
        kwargs['workspace_id'] = \
            workspace_id
        kwargs['category_id'] = \
            category_id
        return self.bot_management_get_category_endpoint.call_with_http_info(**kwargs)

    def bot_management_get_workspace(
        self,
        workspace_id,
        **kwargs
    ):
        """Get a workspace  # noqa: E501

        Retrieve a bot management workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.bot_management_get_workspace(workspace_id, async_req=True)
        >>> result = thread.get()

        Args:
            workspace_id (str): The ID of the bot management workspace.

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
            BotManagementWorkspaceResponse
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
        kwargs['workspace_id'] = \
            workspace_id
        return self.bot_management_get_workspace_endpoint.call_with_http_info(**kwargs)

    def bot_management_list_bots(
        self,
        workspace_id,
        **kwargs
    ):
        """List all bots in a workspace  # noqa: E501

        List all bots in a workspace's policy across all categories.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.bot_management_list_bots(workspace_id, async_req=True)
        >>> result = thread.get()

        Args:
            workspace_id (str): The ID of the bot management workspace.

        Keyword Args:
            limit (int): Limit how many results are returned.. [optional] if omitted the server will use the default value of 100
            cursor (str): Cursor for pagination. Use the `next_cursor` value from a previous response to request the next page of results.. [optional]
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
            BotManagementWorkspaceBotsResponse
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
        kwargs['workspace_id'] = \
            workspace_id
        return self.bot_management_list_bots_endpoint.call_with_http_info(**kwargs)

    def bot_management_list_categories(
        self,
        workspace_id,
        **kwargs
    ):
        """List categories  # noqa: E501

        List all bot categories in a workspace's policy. Each category has an action that applies to every bot in the category. To list the bots themselves, use [list all bots in a workspace](#bot-management-list-bots) or [list bots in a category](#bot-management-list-category-bots).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.bot_management_list_categories(workspace_id, async_req=True)
        >>> result = thread.get()

        Args:
            workspace_id (str): The ID of the bot management workspace.

        Keyword Args:
            limit (int): Limit how many results are returned.. [optional] if omitted the server will use the default value of 100
            cursor (str): Cursor for pagination. Use the `next_cursor` value from a previous response to request the next page of results.. [optional]
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
            BotManagementCategoriesResponse
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
        kwargs['workspace_id'] = \
            workspace_id
        return self.bot_management_list_categories_endpoint.call_with_http_info(**kwargs)

    def bot_management_list_category_bots(
        self,
        workspace_id,
        category_id,
        **kwargs
    ):
        """List bots in a category  # noqa: E501

        List all bots in a bot category.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.bot_management_list_category_bots(workspace_id, category_id, async_req=True)
        >>> result = thread.get()

        Args:
            workspace_id (str): The ID of the bot management workspace.
            category_id (str): The ID of the bot category.

        Keyword Args:
            limit (int): Limit how many results are returned.. [optional] if omitted the server will use the default value of 100
            cursor (str): Cursor for pagination. Use the `next_cursor` value from a previous response to request the next page of results.. [optional]
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
            BotManagementBotsResponse
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
        kwargs['workspace_id'] = \
            workspace_id
        kwargs['category_id'] = \
            category_id
        return self.bot_management_list_category_bots_endpoint.call_with_http_info(**kwargs)

    def bot_management_list_workspaces(
        self,
        **kwargs
    ):
        """List workspaces  # noqa: E501

        List bot management workspaces.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.bot_management_list_workspaces(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            service_id (str): Filter results to the workspace attached to this service. Returns an empty list if the service is not attached to a workspace.. [optional]
            limit (int): Limit how many results are returned.. [optional] if omitted the server will use the default value of 100
            cursor (str): Cursor for pagination. Use the `next_cursor` value from a previous response to request the next page of results.. [optional]
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
            BotManagementWorkspacesResponse
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
        return self.bot_management_list_workspaces_endpoint.call_with_http_info(**kwargs)

    def bot_management_update_bot(
        self,
        workspace_id,
        category_id,
        bot_id,
        bot_management_bot,
        **kwargs
    ):
        """Set a bot action  # noqa: E501

        Set the action for a bot. Set the action to 'inherit' to apply the category's action or to a specific value to override the category's action.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.bot_management_update_bot(workspace_id, category_id, bot_id, bot_management_bot, async_req=True)
        >>> result = thread.get()

        Args:
            workspace_id (str): The ID of the bot management workspace.
            category_id (str): The ID of the bot category.
            bot_id (str): The ID of the bot.
            bot_management_bot (BotManagementBot):

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
            BotManagementBotResponse
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
        kwargs['workspace_id'] = \
            workspace_id
        kwargs['category_id'] = \
            category_id
        kwargs['bot_id'] = \
            bot_id
        kwargs['bot_management_bot'] = \
            bot_management_bot
        return self.bot_management_update_bot_endpoint.call_with_http_info(**kwargs)

    def bot_management_update_category(
        self,
        workspace_id,
        category_id,
        bot_management_category,
        **kwargs
    ):
        """Set a category action  # noqa: E501

        Set the action for a bot category. Every bot in the category configured with the 'inherit' action uses the action set for the category.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.bot_management_update_category(workspace_id, category_id, bot_management_category, async_req=True)
        >>> result = thread.get()

        Args:
            workspace_id (str): The ID of the bot management workspace.
            category_id (str): The ID of the bot category.
            bot_management_category (BotManagementCategory):

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
            BotManagementCategoryResponse
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
        kwargs['workspace_id'] = \
            workspace_id
        kwargs['category_id'] = \
            category_id
        kwargs['bot_management_category'] = \
            bot_management_category
        return self.bot_management_update_category_endpoint.call_with_http_info(**kwargs)

    def bot_management_update_workspace(
        self,
        workspace_id,
        bot_management_workspace,
        **kwargs
    ):
        """Update a workspace  # noqa: E501

        Update the attributes of a bot management workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.bot_management_update_workspace(workspace_id, bot_management_workspace, async_req=True)
        >>> result = thread.get()

        Args:
            workspace_id (str): The ID of the bot management workspace.
            bot_management_workspace (BotManagementWorkspace):

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
            BotManagementWorkspaceResponse
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
        kwargs['workspace_id'] = \
            workspace_id
        kwargs['bot_management_workspace'] = \
            bot_management_workspace
        return self.bot_management_update_workspace_endpoint.call_with_http_info(**kwargs)

