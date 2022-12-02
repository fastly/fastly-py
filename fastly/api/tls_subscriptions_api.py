"""
    Fastly API

    Via the Fastly API you can perform any of the operations that are possible within the management console,  including creating services, domains, and backends, configuring rules or uploading your own application code, as well as account operations such as user administration and billing reports. The API is organized into collections of endpoints that allow manipulation of objects related to Fastly services and accounts. For the most accurate and up-to-date API reference content, visit our [Developer Hub](https://developer.fastly.com/reference/api/)   # noqa: E501

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
from fastly.model.tls_subscription import TlsSubscription
from fastly.model.tls_subscription_response import TlsSubscriptionResponse
from fastly.model.tls_subscriptions_response import TlsSubscriptionsResponse


class TlsSubscriptionsApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_globalsign_email_challenge_endpoint = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/tls/subscriptions/{tls_subscription_id}/authorizations/{tls_authorization_id}/globalsign_email_challenges',
                'operation_id': 'create_globalsign_email_challenge',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'tls_subscription_id',
                    'tls_authorization_id',
                    'request_body',
                ],
                'required': [
                    'tls_subscription_id',
                    'tls_authorization_id',
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
                    'tls_subscription_id':
                        (str,),
                    'tls_authorization_id':
                        (str,),
                    'request_body':
                        ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                },
                'attribute_map': {
                    'tls_subscription_id': 'tls_subscription_id',
                    'tls_authorization_id': 'tls_authorization_id',
                },
                'location_map': {
                    'tls_subscription_id': 'path',
                    'tls_authorization_id': 'path',
                    'request_body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/vnd.api+json'
                ]
            },
            api_client=api_client
        )
        self.create_tls_sub_endpoint = _Endpoint(
            settings={
                'response_type': (TlsSubscriptionResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/tls/subscriptions',
                'operation_id': 'create_tls_sub',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'force',
                    'tls_subscription',
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
                    'force':
                        (bool,),
                    'tls_subscription':
                        (TlsSubscription,),
                },
                'attribute_map': {
                    'force': 'force',
                },
                'location_map': {
                    'force': 'query',
                    'tls_subscription': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.api+json'
                ],
                'content_type': [
                    'application/vnd.api+json'
                ]
            },
            api_client=api_client
        )
        self.delete_globalsign_email_challenge_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'token'
                ],
                'endpoint_path': '/tls/subscriptions/{tls_subscription_id}/authorizations/{tls_authorization_id}/globalsign_email_challenges/{globalsign_email_challenge_id}',
                'operation_id': 'delete_globalsign_email_challenge',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'tls_subscription_id',
                    'globalsign_email_challenge_id',
                    'tls_authorization_id',
                ],
                'required': [
                    'tls_subscription_id',
                    'globalsign_email_challenge_id',
                    'tls_authorization_id',
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
                    'tls_subscription_id':
                        (str,),
                    'globalsign_email_challenge_id':
                        (str,),
                    'tls_authorization_id':
                        (str,),
                },
                'attribute_map': {
                    'tls_subscription_id': 'tls_subscription_id',
                    'globalsign_email_challenge_id': 'globalsign_email_challenge_id',
                    'tls_authorization_id': 'tls_authorization_id',
                },
                'location_map': {
                    'tls_subscription_id': 'path',
                    'globalsign_email_challenge_id': 'path',
                    'tls_authorization_id': 'path',
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
        self.delete_tls_sub_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'token'
                ],
                'endpoint_path': '/tls/subscriptions/{tls_subscription_id}',
                'operation_id': 'delete_tls_sub',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'tls_subscription_id',
                ],
                'required': [
                    'tls_subscription_id',
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
                    'tls_subscription_id':
                        (str,),
                },
                'attribute_map': {
                    'tls_subscription_id': 'tls_subscription_id',
                },
                'location_map': {
                    'tls_subscription_id': 'path',
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
        self.get_tls_sub_endpoint = _Endpoint(
            settings={
                'response_type': (TlsSubscriptionResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/tls/subscriptions/{tls_subscription_id}',
                'operation_id': 'get_tls_sub',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'tls_subscription_id',
                    'include',
                ],
                'required': [
                    'tls_subscription_id',
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
                    'tls_subscription_id':
                        (str,),
                    'include':
                        (str,),
                },
                'attribute_map': {
                    'tls_subscription_id': 'tls_subscription_id',
                    'include': 'include',
                },
                'location_map': {
                    'tls_subscription_id': 'path',
                    'include': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.api+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_tls_subs_endpoint = _Endpoint(
            settings={
                'response_type': (TlsSubscriptionsResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/tls/subscriptions',
                'operation_id': 'list_tls_subs',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'filter_state',
                    'filter_tls_domains_id',
                    'filter_has_active_order',
                    'include',
                    'page_number',
                    'page_size',
                    'sort',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'sort',
                ],
                'validation': [
                    'page_size',
                ]
            },
            root_map={
                'validations': {
                    ('page_size',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                    ('sort',): {

                        "asc": "created_at",
                        "desc": "-created_at"
                    },
                },
                'openapi_types': {
                    'filter_state':
                        (str,),
                    'filter_tls_domains_id':
                        (str,),
                    'filter_has_active_order':
                        (bool,),
                    'include':
                        (str,),
                    'page_number':
                        (int,),
                    'page_size':
                        (int,),
                    'sort':
                        (str,),
                },
                'attribute_map': {
                    'filter_state': 'filter[state]',
                    'filter_tls_domains_id': 'filter[tls_domains.id]',
                    'filter_has_active_order': 'filter[has_active_order]',
                    'include': 'include',
                    'page_number': 'page[number]',
                    'page_size': 'page[size]',
                    'sort': 'sort',
                },
                'location_map': {
                    'filter_state': 'query',
                    'filter_tls_domains_id': 'query',
                    'filter_has_active_order': 'query',
                    'include': 'query',
                    'page_number': 'query',
                    'page_size': 'query',
                    'sort': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.api+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.patch_tls_sub_endpoint = _Endpoint(
            settings={
                'response_type': (TlsSubscriptionResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/tls/subscriptions/{tls_subscription_id}',
                'operation_id': 'patch_tls_sub',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'tls_subscription_id',
                    'force',
                    'tls_subscription',
                ],
                'required': [
                    'tls_subscription_id',
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
                    'tls_subscription_id':
                        (str,),
                    'force':
                        (bool,),
                    'tls_subscription':
                        (TlsSubscription,),
                },
                'attribute_map': {
                    'tls_subscription_id': 'tls_subscription_id',
                    'force': 'force',
                },
                'location_map': {
                    'tls_subscription_id': 'path',
                    'force': 'query',
                    'tls_subscription': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.api+json'
                ],
                'content_type': [
                    'application/vnd.api+json'
                ]
            },
            api_client=api_client
        )

    def create_globalsign_email_challenge(
        self,
        tls_subscription_id,
        tls_authorization_id,
        **kwargs
    ):
        """Creates a GlobalSign email challenge.  # noqa: E501

        Creates an email challenge for a domain on a GlobalSign subscription. An email challenge will generate an email that can be used to validate domain ownership. If this challenge is created, then the domain can only be validated using email for the given subscription.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_globalsign_email_challenge(tls_subscription_id, tls_authorization_id, async_req=True)
        >>> result = thread.get()

        Args:
            tls_subscription_id (str): Alphanumeric string identifying a TLS subscription.
            tls_authorization_id (str): Alphanumeric string identifying a TLS subscription.

        Keyword Args:
            request_body ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]
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
            {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
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
        kwargs['tls_subscription_id'] = \
            tls_subscription_id
        kwargs['tls_authorization_id'] = \
            tls_authorization_id
        return self.create_globalsign_email_challenge_endpoint.call_with_http_info(**kwargs)

    def create_tls_sub(
        self,
        **kwargs
    ):
        """Create a TLS subscription  # noqa: E501

        Create a new TLS subscription. This response includes a list of possible challenges to verify domain ownership.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_tls_sub(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            force (bool): A flag that allows you to edit and delete a subscription with active domains. Valid to use on PATCH and DELETE actions. As a warning, removing an active domain from a subscription or forcing the deletion of a subscription may result in breaking TLS termination to that domain. . [optional]
            tls_subscription (TlsSubscription): [optional]
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
            TlsSubscriptionResponse
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
        return self.create_tls_sub_endpoint.call_with_http_info(**kwargs)

    def delete_globalsign_email_challenge(
        self,
        tls_subscription_id,
        globalsign_email_challenge_id,
        tls_authorization_id,
        **kwargs
    ):
        """Delete a GlobalSign email challenge  # noqa: E501

        Deletes a GlobalSign email challenge. After a GlobalSign email challenge is deleted, the domain can use HTTP and DNS validation methods again.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_globalsign_email_challenge(tls_subscription_id, globalsign_email_challenge_id, tls_authorization_id, async_req=True)
        >>> result = thread.get()

        Args:
            tls_subscription_id (str): Alphanumeric string identifying a TLS subscription.
            globalsign_email_challenge_id (str): Alphanumeric string identifying a GlobalSign email challenge.
            tls_authorization_id (str): Alphanumeric string identifying a TLS subscription.

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
        kwargs['tls_subscription_id'] = \
            tls_subscription_id
        kwargs['globalsign_email_challenge_id'] = \
            globalsign_email_challenge_id
        kwargs['tls_authorization_id'] = \
            tls_authorization_id
        return self.delete_globalsign_email_challenge_endpoint.call_with_http_info(**kwargs)

    def delete_tls_sub(
        self,
        tls_subscription_id,
        **kwargs
    ):
        """Delete a TLS subscription  # noqa: E501

        Destroy a TLS subscription. A subscription cannot be destroyed if there are domains in the TLS enabled state.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_tls_sub(tls_subscription_id, async_req=True)
        >>> result = thread.get()

        Args:
            tls_subscription_id (str): Alphanumeric string identifying a TLS subscription.

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
        kwargs['tls_subscription_id'] = \
            tls_subscription_id
        return self.delete_tls_sub_endpoint.call_with_http_info(**kwargs)

    def get_tls_sub(
        self,
        tls_subscription_id,
        **kwargs
    ):
        """Get a TLS subscription  # noqa: E501

        Show a TLS subscription.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_tls_sub(tls_subscription_id, async_req=True)
        >>> result = thread.get()

        Args:
            tls_subscription_id (str): Alphanumeric string identifying a TLS subscription.

        Keyword Args:
            include (str): Include related objects. Optional, comma-separated values. Permitted values: `tls_authorizations` and `tls_authorizations.globalsign_email_challenge`. . [optional]
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
            TlsSubscriptionResponse
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
        kwargs['tls_subscription_id'] = \
            tls_subscription_id
        return self.get_tls_sub_endpoint.call_with_http_info(**kwargs)

    def list_tls_subs(
        self,
        **kwargs
    ):
        """List TLS subscriptions  # noqa: E501

        List all TLS subscriptions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_tls_subs(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            filter_state (str): Limit the returned subscriptions by state. Valid values are `pending`, `processing`, `issued`, and `renewing`. Accepts parameters: `not` (e.g., `filter[state][not]=renewing`). . [optional]
            filter_tls_domains_id (str): Limit the returned subscriptions to those that include the specific domain.. [optional]
            filter_has_active_order (bool): Limit the returned subscriptions to those that have currently active orders. Permitted values: `true`. . [optional]
            include (str): Include related objects. Optional, comma-separated values. Permitted values: `tls_authorizations` and `tls_authorizations.globalsign_email_challenge`. . [optional]
            page_number (int): Current page.. [optional]
            page_size (int): Number of records per page.. [optional] if omitted the server will use the default value of 20
            sort (str): The order in which to list the results by creation date.. [optional] if omitted the server will use the default value of "created_at"
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
            TlsSubscriptionsResponse
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
        return self.list_tls_subs_endpoint.call_with_http_info(**kwargs)

    def patch_tls_sub(
        self,
        tls_subscription_id,
        **kwargs
    ):
        """Update a TLS subscription  # noqa: E501

        Change the TLS domains or common name associated with this subscription, or update the TLS configuration for this set of domains.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.patch_tls_sub(tls_subscription_id, async_req=True)
        >>> result = thread.get()

        Args:
            tls_subscription_id (str): Alphanumeric string identifying a TLS subscription.

        Keyword Args:
            force (bool): A flag that allows you to edit and delete a subscription with active domains. Valid to use on PATCH and DELETE actions. As a warning, removing an active domain from a subscription or forcing the deletion of a subscription may result in breaking TLS termination to that domain. . [optional]
            tls_subscription (TlsSubscription): [optional]
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
            TlsSubscriptionResponse
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
        kwargs['tls_subscription_id'] = \
            tls_subscription_id
        return self.patch_tls_sub_endpoint.call_with_http_info(**kwargs)

