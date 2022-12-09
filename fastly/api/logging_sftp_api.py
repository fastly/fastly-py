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
from fastly.model.logging_sftp_response import LoggingSftpResponse


class LoggingSftpApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_log_sftp_endpoint = _Endpoint(
            settings={
                'response_type': (LoggingSftpResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/logging/sftp',
                'operation_id': 'create_log_sftp',
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
                    'message_type',
                    'timestamp_format',
                    'period',
                    'gzip_level',
                    'compression_codec',
                    'address',
                    'port',
                    'password',
                    'path',
                    'public_key',
                    'secret_key',
                    'ssh_known_hosts',
                    'user',
                ],
                'required': [
                    'service_id',
                    'version_id',
                ],
                'nullable': [
                    'placement',
                    'response_condition',
                    'timestamp_format',
                    'path',
                    'public_key',
                    'secret_key',
                ],
                'enum': [
                    'placement',
                    'format_version',
                    'message_type',
                    'compression_codec',
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
                    ('message_type',): {

                        "CLASSIC": "classic",
                        "LOGGLY": "loggly",
                        "LOGPLEX": "logplex",
                        "BLANK": "blank"
                    },
                    ('compression_codec',): {

                        "ZSTD": "zstd",
                        "SNAPPY": "snappy",
                        "GZIP": "gzip"
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
                    'message_type':
                        (str,),
                    'timestamp_format':
                        (str, none_type,),
                    'period':
                        (int,),
                    'gzip_level':
                        (int,),
                    'compression_codec':
                        (str,),
                    'address':
                        (str,),
                    'port':
                        (int,),
                    'password':
                        (str,),
                    'path':
                        (str, none_type,),
                    'public_key':
                        (str, none_type,),
                    'secret_key':
                        (str, none_type,),
                    'ssh_known_hosts':
                        (str,),
                    'user':
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
                    'message_type': 'message_type',
                    'timestamp_format': 'timestamp_format',
                    'period': 'period',
                    'gzip_level': 'gzip_level',
                    'compression_codec': 'compression_codec',
                    'address': 'address',
                    'port': 'port',
                    'password': 'password',
                    'path': 'path',
                    'public_key': 'public_key',
                    'secret_key': 'secret_key',
                    'ssh_known_hosts': 'ssh_known_hosts',
                    'user': 'user',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'name': 'form',
                    'placement': 'form',
                    'format_version': 'form',
                    'response_condition': 'form',
                    'format': 'form',
                    'message_type': 'form',
                    'timestamp_format': 'form',
                    'period': 'form',
                    'gzip_level': 'form',
                    'compression_codec': 'form',
                    'address': 'form',
                    'port': 'form',
                    'password': 'form',
                    'path': 'form',
                    'public_key': 'form',
                    'secret_key': 'form',
                    'ssh_known_hosts': 'form',
                    'user': 'form',
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
        self.delete_log_sftp_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse200,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/logging/sftp/{logging_sftp_name}',
                'operation_id': 'delete_log_sftp',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'logging_sftp_name',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'logging_sftp_name',
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
                    'logging_sftp_name':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'logging_sftp_name': 'logging_sftp_name',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'logging_sftp_name': 'path',
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
        self.get_log_sftp_endpoint = _Endpoint(
            settings={
                'response_type': (LoggingSftpResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/logging/sftp/{logging_sftp_name}',
                'operation_id': 'get_log_sftp',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'logging_sftp_name',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'logging_sftp_name',
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
                    'logging_sftp_name':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'logging_sftp_name': 'logging_sftp_name',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'logging_sftp_name': 'path',
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
        self.list_log_sftp_endpoint = _Endpoint(
            settings={
                'response_type': ([LoggingSftpResponse],),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/logging/sftp',
                'operation_id': 'list_log_sftp',
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
        self.update_log_sftp_endpoint = _Endpoint(
            settings={
                'response_type': (LoggingSftpResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/logging/sftp/{logging_sftp_name}',
                'operation_id': 'update_log_sftp',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'logging_sftp_name',
                    'name',
                    'placement',
                    'format_version',
                    'response_condition',
                    'format',
                    'message_type',
                    'timestamp_format',
                    'period',
                    'gzip_level',
                    'compression_codec',
                    'address',
                    'port',
                    'password',
                    'path',
                    'public_key',
                    'secret_key',
                    'ssh_known_hosts',
                    'user',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'logging_sftp_name',
                ],
                'nullable': [
                    'placement',
                    'response_condition',
                    'timestamp_format',
                    'path',
                    'public_key',
                    'secret_key',
                ],
                'enum': [
                    'placement',
                    'format_version',
                    'message_type',
                    'compression_codec',
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
                    ('message_type',): {

                        "CLASSIC": "classic",
                        "LOGGLY": "loggly",
                        "LOGPLEX": "logplex",
                        "BLANK": "blank"
                    },
                    ('compression_codec',): {

                        "ZSTD": "zstd",
                        "SNAPPY": "snappy",
                        "GZIP": "gzip"
                    },
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'version_id':
                        (int,),
                    'logging_sftp_name':
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
                    'message_type':
                        (str,),
                    'timestamp_format':
                        (str, none_type,),
                    'period':
                        (int,),
                    'gzip_level':
                        (int,),
                    'compression_codec':
                        (str,),
                    'address':
                        (str,),
                    'port':
                        (int,),
                    'password':
                        (str,),
                    'path':
                        (str, none_type,),
                    'public_key':
                        (str, none_type,),
                    'secret_key':
                        (str, none_type,),
                    'ssh_known_hosts':
                        (str,),
                    'user':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'logging_sftp_name': 'logging_sftp_name',
                    'name': 'name',
                    'placement': 'placement',
                    'format_version': 'format_version',
                    'response_condition': 'response_condition',
                    'format': 'format',
                    'message_type': 'message_type',
                    'timestamp_format': 'timestamp_format',
                    'period': 'period',
                    'gzip_level': 'gzip_level',
                    'compression_codec': 'compression_codec',
                    'address': 'address',
                    'port': 'port',
                    'password': 'password',
                    'path': 'path',
                    'public_key': 'public_key',
                    'secret_key': 'secret_key',
                    'ssh_known_hosts': 'ssh_known_hosts',
                    'user': 'user',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'logging_sftp_name': 'path',
                    'name': 'form',
                    'placement': 'form',
                    'format_version': 'form',
                    'response_condition': 'form',
                    'format': 'form',
                    'message_type': 'form',
                    'timestamp_format': 'form',
                    'period': 'form',
                    'gzip_level': 'form',
                    'compression_codec': 'form',
                    'address': 'form',
                    'port': 'form',
                    'password': 'form',
                    'path': 'form',
                    'public_key': 'form',
                    'secret_key': 'form',
                    'ssh_known_hosts': 'form',
                    'user': 'form',
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

    def create_log_sftp(
        self,
        service_id,
        version_id,
        **kwargs
    ):
        """Create an SFTP log endpoint  # noqa: E501

        Create a SFTP for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_log_sftp(service_id, version_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.

        Keyword Args:
            name (str): The name for the real-time logging configuration.. [optional]
            placement (str, none_type): Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`. . [optional]
            format_version (int): The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`. . [optional] if omitted the server will use the default value of 2
            response_condition (str, none_type): The name of an existing condition in the configured endpoint, or leave blank to always execute.. [optional]
            format (str): A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats).. [optional] if omitted the server will use the default value of "%h %l %u %t "%r" %&gt;s %b"
            message_type (str): How the message should be formatted.. [optional] if omitted the server will use the default value of "classic"
            timestamp_format (str, none_type): A timestamp format. [optional]
            period (int): How frequently log files are finalized so they can be available for reading (in seconds).. [optional] if omitted the server will use the default value of 3600
            gzip_level (int): The level of gzip encoding when sending logs (default `0`, no compression). Specifying both `compression_codec` and `gzip_level` in the same API request will result in an error.. [optional] if omitted the server will use the default value of 0
            compression_codec (str): The codec used for compressing your logs. Valid values are `zstd`, `snappy`, and `gzip`. Specifying both `compression_codec` and `gzip_level` in the same API request will result in an error.. [optional]
            address (str): A hostname or IPv4 address.. [optional]
            port (int): The port number.. [optional] if omitted the server will use the default value of 22
            password (str): The password for the server. If both `password` and `secret_key` are passed, `secret_key` will be used in preference.. [optional]
            path (str, none_type): The path to upload logs to.. [optional] if omitted the server will use the default value of "null"
            public_key (str, none_type): A PGP public key that Fastly will use to encrypt your log files before writing them to disk.. [optional] if omitted the server will use the default value of "null"
            secret_key (str, none_type): The SSH private key for the server. If both `password` and `secret_key` are passed, `secret_key` will be used in preference.. [optional] if omitted the server will use the default value of "null"
            ssh_known_hosts (str): A list of host keys for all hosts we can connect to over SFTP.. [optional]
            user (str): The username for the server.. [optional]
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
            LoggingSftpResponse
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
        return self.create_log_sftp_endpoint.call_with_http_info(**kwargs)

    def delete_log_sftp(
        self,
        service_id,
        version_id,
        logging_sftp_name,
        **kwargs
    ):
        """Delete an SFTP log endpoint  # noqa: E501

        Delete the SFTP for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_log_sftp(service_id, version_id, logging_sftp_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            logging_sftp_name (str): The name for the real-time logging configuration.

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
        kwargs['logging_sftp_name'] = \
            logging_sftp_name
        return self.delete_log_sftp_endpoint.call_with_http_info(**kwargs)

    def get_log_sftp(
        self,
        service_id,
        version_id,
        logging_sftp_name,
        **kwargs
    ):
        """Get an SFTP log endpoint  # noqa: E501

        Get the SFTP for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_log_sftp(service_id, version_id, logging_sftp_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            logging_sftp_name (str): The name for the real-time logging configuration.

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
            LoggingSftpResponse
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
        kwargs['logging_sftp_name'] = \
            logging_sftp_name
        return self.get_log_sftp_endpoint.call_with_http_info(**kwargs)

    def list_log_sftp(
        self,
        service_id,
        version_id,
        **kwargs
    ):
        """List SFTP log endpoints  # noqa: E501

        List all of the SFTPs for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_log_sftp(service_id, version_id, async_req=True)
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
            [LoggingSftpResponse]
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
        return self.list_log_sftp_endpoint.call_with_http_info(**kwargs)

    def update_log_sftp(
        self,
        service_id,
        version_id,
        logging_sftp_name,
        **kwargs
    ):
        """Update an SFTP log endpoint  # noqa: E501

        Update the SFTP for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_log_sftp(service_id, version_id, logging_sftp_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            logging_sftp_name (str): The name for the real-time logging configuration.

        Keyword Args:
            name (str): The name for the real-time logging configuration.. [optional]
            placement (str, none_type): Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`. . [optional]
            format_version (int): The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`. . [optional] if omitted the server will use the default value of 2
            response_condition (str, none_type): The name of an existing condition in the configured endpoint, or leave blank to always execute.. [optional]
            format (str): A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats).. [optional] if omitted the server will use the default value of "%h %l %u %t "%r" %&gt;s %b"
            message_type (str): How the message should be formatted.. [optional] if omitted the server will use the default value of "classic"
            timestamp_format (str, none_type): A timestamp format. [optional]
            period (int): How frequently log files are finalized so they can be available for reading (in seconds).. [optional] if omitted the server will use the default value of 3600
            gzip_level (int): The level of gzip encoding when sending logs (default `0`, no compression). Specifying both `compression_codec` and `gzip_level` in the same API request will result in an error.. [optional] if omitted the server will use the default value of 0
            compression_codec (str): The codec used for compressing your logs. Valid values are `zstd`, `snappy`, and `gzip`. Specifying both `compression_codec` and `gzip_level` in the same API request will result in an error.. [optional]
            address (str): A hostname or IPv4 address.. [optional]
            port (int): The port number.. [optional] if omitted the server will use the default value of 22
            password (str): The password for the server. If both `password` and `secret_key` are passed, `secret_key` will be used in preference.. [optional]
            path (str, none_type): The path to upload logs to.. [optional] if omitted the server will use the default value of "null"
            public_key (str, none_type): A PGP public key that Fastly will use to encrypt your log files before writing them to disk.. [optional] if omitted the server will use the default value of "null"
            secret_key (str, none_type): The SSH private key for the server. If both `password` and `secret_key` are passed, `secret_key` will be used in preference.. [optional] if omitted the server will use the default value of "null"
            ssh_known_hosts (str): A list of host keys for all hosts we can connect to over SFTP.. [optional]
            user (str): The username for the server.. [optional]
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
            LoggingSftpResponse
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
        kwargs['logging_sftp_name'] = \
            logging_sftp_name
        return self.update_log_sftp_endpoint.call_with_http_info(**kwargs)

