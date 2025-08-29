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
from fastly.model.list_attack_report import ListAttackReport
from fastly.model.list_signal_report import ListSignalReport


class NgwafReportsApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_attacks_report_endpoint = _Endpoint(
            settings={
                'response_type': (ListAttackReport,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/ngwaf/v1/reports/attacks',
                'operation_id': 'get_attacks_report',
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
                    '_from',
                    'to',
                ],
                'required': [
                    '_from',
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
                    '_from':
                        (datetime,),
                    'to':
                        (datetime,),
                },
                'attribute_map': {
                    '_from': 'from',
                    'to': 'to',
                },
                'location_map': {
                    '_from': 'query',
                    'to': 'query',
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
        self.get_signals_report_endpoint = _Endpoint(
            settings={
                'response_type': (ListSignalReport,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/ngwaf/v1/reports/signals',
                'operation_id': 'get_signals_report',
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
                    '_from',
                    'to',
                    'signal_type',
                ],
                'required': [
                    '_from',
                ],
                'nullable': [
                ],
                'enum': [
                    'signal_type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('signal_type',): {

                        "ACCOUNT": "account",
                        "ANOMALY": "anomaly",
                        "ATTACK": "attack",
                        "BOT": "bot",
                        "ALL": "all"
                    },
                },
                'openapi_types': {
                    '_from':
                        (datetime,),
                    'to':
                        (datetime,),
                    'signal_type':
                        (str,),
                },
                'attribute_map': {
                    '_from': 'from',
                    'to': 'to',
                    'signal_type': 'signal_type',
                },
                'location_map': {
                    '_from': 'query',
                    'to': 'query',
                    'signal_type': 'query',
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

    def get_attacks_report(
        self,
        _from,
        **kwargs
    ):
        """Get attacks report  # noqa: E501

        Get attacks report  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_attacks_report(_from, async_req=True)
        >>> result = thread.get()

        Args:
            _from (datetime): The start of a time range in RFC 3339 format.

        Keyword Args:
            to (datetime): The end of a time range in RFC 3339 format. Defaults to the current time.. [optional]
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
            ListAttackReport
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
        kwargs['_from'] = \
            _from
        return self.get_attacks_report_endpoint.call_with_http_info(**kwargs)

    def get_signals_report(
        self,
        _from,
        **kwargs
    ):
        """Get signals report  # noqa: E501

        Get signals report  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_signals_report(_from, async_req=True)
        >>> result = thread.get()

        Args:
            _from (datetime): The start of a time range in RFC 3339 format.

        Keyword Args:
            to (datetime): The end of a time range in RFC 3339 format. Defaults to the current time.. [optional]
            signal_type (str): The type of signal. [optional]
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
            ListSignalReport
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
        kwargs['_from'] = \
            _from
        return self.get_signals_report_endpoint.call_with_http_info(**kwargs)

