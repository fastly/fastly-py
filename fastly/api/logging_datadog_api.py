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
from fastly.model.inline_response200 import InlineResponse200
from fastly.model.logging_datadog_response import LoggingDatadogResponse


class LoggingDatadogApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_log_datadog_endpoint = _Endpoint(
            settings={
                'response_type': (LoggingDatadogResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/logging/datadog',
                'operation_id': 'create_log_datadog',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'name',
                    'placement',
                    'format_version',
                    'response_condition',
                    'format',
                    'region',
                    'token',
                ],
                'required': [
                    'service_id',
                    'version_id',
                ],
                'nullable': [
                    'placement',
                    'response_condition',
                ],
                'enum': [
                    'placement',
                    'format_version',
                    'region',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('placement',): {
                        'None': None,
                        "NONE": "none",
                        "WAF_DEBUG": "waf_debug",
                        "NULL": "null"
                    },
                    ('format_version',): {

                        "v1": 1,
                        "v2": 2
                    },
                    ('region',): {

                        "US": "US",
                        "EU": "EU"
                    },
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'version_id':
                        (int,),
                    'name':
                        (str,),
                    'placement':
                        (str, none_type,),
                    'format_version':
                        (int,),
                    'response_condition':
                        (str, none_type,),
                    'format':
                        (str,),
                    'region':
                        (str,),
                    'token':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'name': 'name',
                    'placement': 'placement',
                    'format_version': 'format_version',
                    'response_condition': 'response_condition',
                    'format': 'format',
                    'region': 'region',
                    'token': 'token',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'name': 'form',
                    'placement': 'form',
                    'format_version': 'form',
                    'response_condition': 'form',
                    'format': 'form',
                    'region': 'form',
                    'token': 'form',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/x-www-form-urlencoded'
                ]
            },
            api_client=api_client
        )
        self.delete_log_datadog_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse200,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/logging/datadog/{logging_datadog_name}',
                'operation_id': 'delete_log_datadog',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'logging_datadog_name',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'logging_datadog_name',
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
                    'service_id':
                        (str,),
                    'version_id':
                        (int,),
                    'logging_datadog_name':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'logging_datadog_name': 'logging_datadog_name',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'logging_datadog_name': 'path',
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
        self.get_log_datadog_endpoint = _Endpoint(
            settings={
                'response_type': (LoggingDatadogResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/logging/datadog/{logging_datadog_name}',
                'operation_id': 'get_log_datadog',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'logging_datadog_name',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'logging_datadog_name',
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
                    'service_id':
                        (str,),
                    'version_id':
                        (int,),
                    'logging_datadog_name':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'logging_datadog_name': 'logging_datadog_name',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'logging_datadog_name': 'path',
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
        self.list_log_datadog_endpoint = _Endpoint(
            settings={
                'response_type': ([LoggingDatadogResponse],),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/logging/datadog',
                'operation_id': 'list_log_datadog',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                ],
                'required': [
                    'service_id',
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
                    'service_id':
                        (str,),
                    'version_id':
                        (int,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
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
        self.update_log_datadog_endpoint = _Endpoint(
            settings={
                'response_type': (LoggingDatadogResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/logging/datadog/{logging_datadog_name}',
                'operation_id': 'update_log_datadog',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'logging_datadog_name',
                    'name',
                    'placement',
                    'format_version',
                    'response_condition',
                    'format',
                    'region',
                    'token',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'logging_datadog_name',
                ],
                'nullable': [
                    'placement',
                    'response_condition',
                ],
                'enum': [
                    'placement',
                    'format_version',
                    'region',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('placement',): {
                        'None': None,
                        "NONE": "none",
                        "WAF_DEBUG": "waf_debug",
                        "NULL": "null"
                    },
                    ('format_version',): {

                        "v1": 1,
                        "v2": 2
                    },
                    ('region',): {

                        "US": "US",
                        "EU": "EU"
                    },
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'version_id':
                        (int,),
                    'logging_datadog_name':
                        (str,),
                    'name':
                        (str,),
                    'placement':
                        (str, none_type,),
                    'format_version':
                        (int,),
                    'response_condition':
                        (str, none_type,),
                    'format':
                        (str,),
                    'region':
                        (str,),
                    'token':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'logging_datadog_name': 'logging_datadog_name',
                    'name': 'name',
                    'placement': 'placement',
                    'format_version': 'format_version',
                    'response_condition': 'response_condition',
                    'format': 'format',
                    'region': 'region',
                    'token': 'token',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'logging_datadog_name': 'path',
                    'name': 'form',
                    'placement': 'form',
                    'format_version': 'form',
                    'response_condition': 'form',
                    'format': 'form',
                    'region': 'form',
                    'token': 'form',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/x-www-form-urlencoded'
                ]
            },
            api_client=api_client
        )

    def create_log_datadog(
        self,
        service_id,
        version_id,
        **kwargs
    ):
        """Create a Datadog log endpoint  # noqa: E501

        Create a Datadog logging object for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_log_datadog(service_id, version_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.

        Keyword Args:
            name (str): The name for the real-time logging configuration.. [optional]
            placement (str, none_type): Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`. . [optional]
            format_version (int): The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`. . [optional] if omitted the server will use the default value of 2
            response_condition (str, none_type): The name of an existing condition in the configured endpoint, or leave blank to always execute.. [optional]
            format (str): A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). Must produce valid JSON that Datadog can ingest. . [optional] if omitted the server will use the default value of "{"ddsource":"fastly","service":"%{req.service_id}V","date":"%{begin:%Y-%m-%dT%H:%M:%S%Z}t","time_start":"%{begin:%Y-%m-%dT%H:%M:%S%Z}t","time_end":"%{end:%Y-%m-%dT%H:%M:%S%Z}t","http":{"request_time_ms":"%D","method":"%m","url":"%{json.escape(req.url)}V","useragent":"%{User-Agent}i","referer":"%{Referer}i","protocol":"%H","request_x_forwarded_for":"%{X-Forwarded-For}i","status_code":"%s"},"network":{"client":{"ip":"%h","name":"%{client.as.name}V","number":"%{client.as.number}V","connection_speed":"%{client.geo.conn_speed}V"},"destination":{"ip":"%A"},"geoip":{"geo_city":"%{client.geo.city.utf8}V","geo_country_code":"%{client.geo.country_code}V","geo_continent_code":"%{client.geo.continent_code}V","geo_region":"%{client.geo.region}V"},"bytes_written":"%B","bytes_read":"%{req.body_bytes_read}V"},"host":"%{Fastly-Orig-Host}i","origin_host":"%v","is_ipv6":"%{if(req.is_ipv6, \"true\", \"false\")}V","is_tls":"%{if(req.is_ssl, \"true\", \"false\")}V","tls_client_protocol":"%{json.escape(tls.client.protocol)}V","tls_client_servername":"%{json.escape(tls.client.servername)}V","tls_client_cipher":"%{json.escape(tls.client.cipher)}V","tls_client_cipher_sha":"%{json.escape(tls.client.ciphers_sha)}V","tls_client_tlsexts_sha":"%{json.escape(tls.client.tlsexts_sha)}V","is_h2":"%{if(fastly_info.is_h2, \"true\", \"false\")}V","is_h2_push":"%{if(fastly_info.h2.is_push, \"true\", \"false\")}V","h2_stream_id":"%{fastly_info.h2.stream_id}V","request_accept_content":"%{Accept}i","request_accept_language":"%{Accept-Language}i","request_accept_encoding":"%{Accept-Encoding}i","request_accept_charset":"%{Accept-Charset}i","request_connection":"%{Connection}i","request_dnt":"%{DNT}i","request_forwarded":"%{Forwarded}i","request_via":"%{Via}i","request_cache_control":"%{Cache-Control}i","request_x_requested_with":"%{X-Requested-With}i","request_x_att_device_id":"%{X-ATT-Device-Id}i","content_type":"%{Content-Type}o","is_cacheable":"%{if(fastly_info.state~\"^(HIT|MISS)$\", \"true\", \"false\")}V","response_age":"%{Age}o","response_cache_control":"%{Cache-Control}o","response_expires":"%{Expires}o","response_last_modified":"%{Last-Modified}o","response_tsv":"%{TSV}o","server_datacenter":"%{server.datacenter}V","req_header_size":"%{req.header_bytes_read}V","resp_header_size":"%{resp.header_bytes_written}V","socket_cwnd":"%{client.socket.cwnd}V","socket_nexthop":"%{client.socket.nexthop}V","socket_tcpi_rcv_mss":"%{client.socket.tcpi_rcv_mss}V","socket_tcpi_snd_mss":"%{client.socket.tcpi_snd_mss}V","socket_tcpi_rtt":"%{client.socket.tcpi_rtt}V","socket_tcpi_rttvar":"%{client.socket.tcpi_rttvar}V","socket_tcpi_rcv_rtt":"%{client.socket.tcpi_rcv_rtt}V","socket_tcpi_rcv_space":"%{client.socket.tcpi_rcv_space}V","socket_tcpi_last_data_sent":"%{client.socket.tcpi_last_data_sent}V","socket_tcpi_total_retrans":"%{client.socket.tcpi_total_retrans}V","socket_tcpi_delta_retrans":"%{client.socket.tcpi_delta_retrans}V","socket_ploss":"%{client.socket.ploss}V"}"
            region (str): The region that log data will be sent to.. [optional] if omitted the server will use the default value of "US"
            token (str): The API key from your Datadog account. Required.. [optional]
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
            LoggingDatadogResponse
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
        kwargs['service_id'] = \
            service_id
        kwargs['version_id'] = \
            version_id
        return self.create_log_datadog_endpoint.call_with_http_info(**kwargs)

    def delete_log_datadog(
        self,
        service_id,
        version_id,
        logging_datadog_name,
        **kwargs
    ):
        """Delete a Datadog log endpoint  # noqa: E501

        Delete the Datadog logging object for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_log_datadog(service_id, version_id, logging_datadog_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            logging_datadog_name (str): The name for the real-time logging configuration.

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
            InlineResponse200
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
        kwargs['service_id'] = \
            service_id
        kwargs['version_id'] = \
            version_id
        kwargs['logging_datadog_name'] = \
            logging_datadog_name
        return self.delete_log_datadog_endpoint.call_with_http_info(**kwargs)

    def get_log_datadog(
        self,
        service_id,
        version_id,
        logging_datadog_name,
        **kwargs
    ):
        """Get a Datadog log endpoint  # noqa: E501

        Get the details for a Datadog logging object for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_log_datadog(service_id, version_id, logging_datadog_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            logging_datadog_name (str): The name for the real-time logging configuration.

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
            LoggingDatadogResponse
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
        kwargs['service_id'] = \
            service_id
        kwargs['version_id'] = \
            version_id
        kwargs['logging_datadog_name'] = \
            logging_datadog_name
        return self.get_log_datadog_endpoint.call_with_http_info(**kwargs)

    def list_log_datadog(
        self,
        service_id,
        version_id,
        **kwargs
    ):
        """List Datadog log endpoints  # noqa: E501

        List all of the Datadog logging objects for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_log_datadog(service_id, version_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.

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
            [LoggingDatadogResponse]
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
        kwargs['service_id'] = \
            service_id
        kwargs['version_id'] = \
            version_id
        return self.list_log_datadog_endpoint.call_with_http_info(**kwargs)

    def update_log_datadog(
        self,
        service_id,
        version_id,
        logging_datadog_name,
        **kwargs
    ):
        """Update a Datadog log endpoint  # noqa: E501

        Update the Datadog logging object for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_log_datadog(service_id, version_id, logging_datadog_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            logging_datadog_name (str): The name for the real-time logging configuration.

        Keyword Args:
            name (str): The name for the real-time logging configuration.. [optional]
            placement (str, none_type): Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`. . [optional]
            format_version (int): The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`. . [optional] if omitted the server will use the default value of 2
            response_condition (str, none_type): The name of an existing condition in the configured endpoint, or leave blank to always execute.. [optional]
            format (str): A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). Must produce valid JSON that Datadog can ingest. . [optional] if omitted the server will use the default value of "{"ddsource":"fastly","service":"%{req.service_id}V","date":"%{begin:%Y-%m-%dT%H:%M:%S%Z}t","time_start":"%{begin:%Y-%m-%dT%H:%M:%S%Z}t","time_end":"%{end:%Y-%m-%dT%H:%M:%S%Z}t","http":{"request_time_ms":"%D","method":"%m","url":"%{json.escape(req.url)}V","useragent":"%{User-Agent}i","referer":"%{Referer}i","protocol":"%H","request_x_forwarded_for":"%{X-Forwarded-For}i","status_code":"%s"},"network":{"client":{"ip":"%h","name":"%{client.as.name}V","number":"%{client.as.number}V","connection_speed":"%{client.geo.conn_speed}V"},"destination":{"ip":"%A"},"geoip":{"geo_city":"%{client.geo.city.utf8}V","geo_country_code":"%{client.geo.country_code}V","geo_continent_code":"%{client.geo.continent_code}V","geo_region":"%{client.geo.region}V"},"bytes_written":"%B","bytes_read":"%{req.body_bytes_read}V"},"host":"%{Fastly-Orig-Host}i","origin_host":"%v","is_ipv6":"%{if(req.is_ipv6, \"true\", \"false\")}V","is_tls":"%{if(req.is_ssl, \"true\", \"false\")}V","tls_client_protocol":"%{json.escape(tls.client.protocol)}V","tls_client_servername":"%{json.escape(tls.client.servername)}V","tls_client_cipher":"%{json.escape(tls.client.cipher)}V","tls_client_cipher_sha":"%{json.escape(tls.client.ciphers_sha)}V","tls_client_tlsexts_sha":"%{json.escape(tls.client.tlsexts_sha)}V","is_h2":"%{if(fastly_info.is_h2, \"true\", \"false\")}V","is_h2_push":"%{if(fastly_info.h2.is_push, \"true\", \"false\")}V","h2_stream_id":"%{fastly_info.h2.stream_id}V","request_accept_content":"%{Accept}i","request_accept_language":"%{Accept-Language}i","request_accept_encoding":"%{Accept-Encoding}i","request_accept_charset":"%{Accept-Charset}i","request_connection":"%{Connection}i","request_dnt":"%{DNT}i","request_forwarded":"%{Forwarded}i","request_via":"%{Via}i","request_cache_control":"%{Cache-Control}i","request_x_requested_with":"%{X-Requested-With}i","request_x_att_device_id":"%{X-ATT-Device-Id}i","content_type":"%{Content-Type}o","is_cacheable":"%{if(fastly_info.state~\"^(HIT|MISS)$\", \"true\", \"false\")}V","response_age":"%{Age}o","response_cache_control":"%{Cache-Control}o","response_expires":"%{Expires}o","response_last_modified":"%{Last-Modified}o","response_tsv":"%{TSV}o","server_datacenter":"%{server.datacenter}V","req_header_size":"%{req.header_bytes_read}V","resp_header_size":"%{resp.header_bytes_written}V","socket_cwnd":"%{client.socket.cwnd}V","socket_nexthop":"%{client.socket.nexthop}V","socket_tcpi_rcv_mss":"%{client.socket.tcpi_rcv_mss}V","socket_tcpi_snd_mss":"%{client.socket.tcpi_snd_mss}V","socket_tcpi_rtt":"%{client.socket.tcpi_rtt}V","socket_tcpi_rttvar":"%{client.socket.tcpi_rttvar}V","socket_tcpi_rcv_rtt":"%{client.socket.tcpi_rcv_rtt}V","socket_tcpi_rcv_space":"%{client.socket.tcpi_rcv_space}V","socket_tcpi_last_data_sent":"%{client.socket.tcpi_last_data_sent}V","socket_tcpi_total_retrans":"%{client.socket.tcpi_total_retrans}V","socket_tcpi_delta_retrans":"%{client.socket.tcpi_delta_retrans}V","socket_ploss":"%{client.socket.ploss}V"}"
            region (str): The region that log data will be sent to.. [optional] if omitted the server will use the default value of "US"
            token (str): The API key from your Datadog account. Required.. [optional]
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
            LoggingDatadogResponse
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
        kwargs['service_id'] = \
            service_id
        kwargs['version_id'] = \
            version_id
        kwargs['logging_datadog_name'] = \
            logging_datadog_name
        return self.update_log_datadog_endpoint.call_with_http_info(**kwargs)

