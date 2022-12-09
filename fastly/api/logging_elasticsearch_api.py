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
from fastly.model.logging_elasticsearch_response import LoggingElasticsearchResponse


class LoggingElasticsearchApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_log_elasticsearch_endpoint = _Endpoint(
            settings={
                'response_type': (LoggingElasticsearchResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/logging/elasticsearch',
                'operation_id': 'create_log_elasticsearch',
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
                    'tls_ca_cert',
                    'tls_client_cert',
                    'tls_client_key',
                    'tls_hostname',
                    'request_max_entries',
                    'request_max_bytes',
                    'index',
                    'url',
                    'pipeline',
                    'user',
                    'password',
                ],
                'required': [
                    'service_id',
                    'version_id',
                ],
                'nullable': [
                    'placement',
                    'response_condition',
                    'tls_ca_cert',
                    'tls_client_cert',
                    'tls_client_key',
                    'tls_hostname',
                    'pipeline',
                    'user',
                    'password',
                ],
                'enum': [
                    'placement',
                    'format_version',
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
                    'tls_ca_cert':
                        (str, none_type,),
                    'tls_client_cert':
                        (str, none_type,),
                    'tls_client_key':
                        (str, none_type,),
                    'tls_hostname':
                        (str, none_type,),
                    'request_max_entries':
                        (int,),
                    'request_max_bytes':
                        (int,),
                    'index':
                        (str,),
                    'url':
                        (str,),
                    'pipeline':
                        (str, none_type,),
                    'user':
                        (str, none_type,),
                    'password':
                        (str, none_type,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'name': 'name',
                    'placement': 'placement',
                    'format_version': 'format_version',
                    'response_condition': 'response_condition',
                    'format': 'format',
                    'tls_ca_cert': 'tls_ca_cert',
                    'tls_client_cert': 'tls_client_cert',
                    'tls_client_key': 'tls_client_key',
                    'tls_hostname': 'tls_hostname',
                    'request_max_entries': 'request_max_entries',
                    'request_max_bytes': 'request_max_bytes',
                    'index': 'index',
                    'url': 'url',
                    'pipeline': 'pipeline',
                    'user': 'user',
                    'password': 'password',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'name': 'form',
                    'placement': 'form',
                    'format_version': 'form',
                    'response_condition': 'form',
                    'format': 'form',
                    'tls_ca_cert': 'form',
                    'tls_client_cert': 'form',
                    'tls_client_key': 'form',
                    'tls_hostname': 'form',
                    'request_max_entries': 'form',
                    'request_max_bytes': 'form',
                    'index': 'form',
                    'url': 'form',
                    'pipeline': 'form',
                    'user': 'form',
                    'password': 'form',
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
        self.delete_log_elasticsearch_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse200,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/logging/elasticsearch/{logging_elasticsearch_name}',
                'operation_id': 'delete_log_elasticsearch',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'logging_elasticsearch_name',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'logging_elasticsearch_name',
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
                    'logging_elasticsearch_name':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'logging_elasticsearch_name': 'logging_elasticsearch_name',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'logging_elasticsearch_name': 'path',
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
        self.get_log_elasticsearch_endpoint = _Endpoint(
            settings={
                'response_type': (LoggingElasticsearchResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/logging/elasticsearch/{logging_elasticsearch_name}',
                'operation_id': 'get_log_elasticsearch',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'logging_elasticsearch_name',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'logging_elasticsearch_name',
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
                    'logging_elasticsearch_name':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'logging_elasticsearch_name': 'logging_elasticsearch_name',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'logging_elasticsearch_name': 'path',
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
        self.list_log_elasticsearch_endpoint = _Endpoint(
            settings={
                'response_type': ([LoggingElasticsearchResponse],),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/logging/elasticsearch',
                'operation_id': 'list_log_elasticsearch',
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
        self.update_log_elasticsearch_endpoint = _Endpoint(
            settings={
                'response_type': (LoggingElasticsearchResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/logging/elasticsearch/{logging_elasticsearch_name}',
                'operation_id': 'update_log_elasticsearch',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'logging_elasticsearch_name',
                    'name',
                    'placement',
                    'format_version',
                    'response_condition',
                    'format',
                    'tls_ca_cert',
                    'tls_client_cert',
                    'tls_client_key',
                    'tls_hostname',
                    'request_max_entries',
                    'request_max_bytes',
                    'index',
                    'url',
                    'pipeline',
                    'user',
                    'password',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'logging_elasticsearch_name',
                ],
                'nullable': [
                    'placement',
                    'response_condition',
                    'tls_ca_cert',
                    'tls_client_cert',
                    'tls_client_key',
                    'tls_hostname',
                    'pipeline',
                    'user',
                    'password',
                ],
                'enum': [
                    'placement',
                    'format_version',
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
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'version_id':
                        (int,),
                    'logging_elasticsearch_name':
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
                    'tls_ca_cert':
                        (str, none_type,),
                    'tls_client_cert':
                        (str, none_type,),
                    'tls_client_key':
                        (str, none_type,),
                    'tls_hostname':
                        (str, none_type,),
                    'request_max_entries':
                        (int,),
                    'request_max_bytes':
                        (int,),
                    'index':
                        (str,),
                    'url':
                        (str,),
                    'pipeline':
                        (str, none_type,),
                    'user':
                        (str, none_type,),
                    'password':
                        (str, none_type,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'logging_elasticsearch_name': 'logging_elasticsearch_name',
                    'name': 'name',
                    'placement': 'placement',
                    'format_version': 'format_version',
                    'response_condition': 'response_condition',
                    'format': 'format',
                    'tls_ca_cert': 'tls_ca_cert',
                    'tls_client_cert': 'tls_client_cert',
                    'tls_client_key': 'tls_client_key',
                    'tls_hostname': 'tls_hostname',
                    'request_max_entries': 'request_max_entries',
                    'request_max_bytes': 'request_max_bytes',
                    'index': 'index',
                    'url': 'url',
                    'pipeline': 'pipeline',
                    'user': 'user',
                    'password': 'password',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'logging_elasticsearch_name': 'path',
                    'name': 'form',
                    'placement': 'form',
                    'format_version': 'form',
                    'response_condition': 'form',
                    'format': 'form',
                    'tls_ca_cert': 'form',
                    'tls_client_cert': 'form',
                    'tls_client_key': 'form',
                    'tls_hostname': 'form',
                    'request_max_entries': 'form',
                    'request_max_bytes': 'form',
                    'index': 'form',
                    'url': 'form',
                    'pipeline': 'form',
                    'user': 'form',
                    'password': 'form',
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

    def create_log_elasticsearch(
        self,
        service_id,
        version_id,
        **kwargs
    ):
        """Create an Elasticsearch log endpoint  # noqa: E501

        Create a Elasticsearch logging endpoint for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_log_elasticsearch(service_id, version_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.

        Keyword Args:
            name (str): The name for the real-time logging configuration.. [optional]
            placement (str, none_type): Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`. . [optional]
            format_version (int): The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`. . [optional] if omitted the server will use the default value of 2
            response_condition (str, none_type): The name of an existing condition in the configured endpoint, or leave blank to always execute.. [optional]
            format (str): A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). Must produce valid JSON that Elasticsearch can ingest.. [optional]
            tls_ca_cert (str, none_type): A secure certificate to authenticate a server with. Must be in PEM format.. [optional] if omitted the server will use the default value of "null"
            tls_client_cert (str, none_type): The client certificate used to make authenticated requests. Must be in PEM format.. [optional] if omitted the server will use the default value of "null"
            tls_client_key (str, none_type): The client private key used to make authenticated requests. Must be in PEM format.. [optional] if omitted the server will use the default value of "null"
            tls_hostname (str, none_type): The hostname to verify the server's certificate. This should be one of the Subject Alternative Name (SAN) fields for the certificate. Common Names (CN) are not supported.. [optional] if omitted the server will use the default value of "null"
            request_max_entries (int): The maximum number of logs sent in one request. Defaults `0` for unbounded.. [optional] if omitted the server will use the default value of 0
            request_max_bytes (int): The maximum number of bytes sent in one request. Defaults `0` for unbounded.. [optional] if omitted the server will use the default value of 0
            index (str): The name of the Elasticsearch index to send documents (logs) to. The index must follow the Elasticsearch [index format rules](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-create-index.html). We support [strftime](https://www.man7.org/linux/man-pages/man3/strftime.3.html) interpolated variables inside braces prefixed with a pound symbol. For example, `#{%F}` will interpolate as `YYYY-MM-DD` with today's date.. [optional]
            url (str): The URL to stream logs to. Must use HTTPS.. [optional]
            pipeline (str, none_type): The ID of the Elasticsearch ingest pipeline to apply pre-process transformations to before indexing. Learn more about creating a pipeline in the [Elasticsearch docs](https://www.elastic.co/guide/en/elasticsearch/reference/current/ingest.html).. [optional]
            user (str, none_type): Basic Auth username.. [optional]
            password (str, none_type): Basic Auth password.. [optional]
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
            LoggingElasticsearchResponse
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
        return self.create_log_elasticsearch_endpoint.call_with_http_info(**kwargs)

    def delete_log_elasticsearch(
        self,
        service_id,
        version_id,
        logging_elasticsearch_name,
        **kwargs
    ):
        """Delete an Elasticsearch log endpoint  # noqa: E501

        Delete the Elasticsearch logging endpoint for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_log_elasticsearch(service_id, version_id, logging_elasticsearch_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            logging_elasticsearch_name (str): The name for the real-time logging configuration.

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
        kwargs['logging_elasticsearch_name'] = \
            logging_elasticsearch_name
        return self.delete_log_elasticsearch_endpoint.call_with_http_info(**kwargs)

    def get_log_elasticsearch(
        self,
        service_id,
        version_id,
        logging_elasticsearch_name,
        **kwargs
    ):
        """Get an Elasticsearch log endpoint  # noqa: E501

        Get the Elasticsearch logging endpoint for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_log_elasticsearch(service_id, version_id, logging_elasticsearch_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            logging_elasticsearch_name (str): The name for the real-time logging configuration.

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
            LoggingElasticsearchResponse
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
        kwargs['logging_elasticsearch_name'] = \
            logging_elasticsearch_name
        return self.get_log_elasticsearch_endpoint.call_with_http_info(**kwargs)

    def list_log_elasticsearch(
        self,
        service_id,
        version_id,
        **kwargs
    ):
        """List Elasticsearch log endpoints  # noqa: E501

        List all of the Elasticsearch logging endpoints for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_log_elasticsearch(service_id, version_id, async_req=True)
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
            [LoggingElasticsearchResponse]
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
        return self.list_log_elasticsearch_endpoint.call_with_http_info(**kwargs)

    def update_log_elasticsearch(
        self,
        service_id,
        version_id,
        logging_elasticsearch_name,
        **kwargs
    ):
        """Update an Elasticsearch log endpoint  # noqa: E501

        Update the Elasticsearch logging endpoint for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_log_elasticsearch(service_id, version_id, logging_elasticsearch_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            logging_elasticsearch_name (str): The name for the real-time logging configuration.

        Keyword Args:
            name (str): The name for the real-time logging configuration.. [optional]
            placement (str, none_type): Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`. . [optional]
            format_version (int): The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`. . [optional] if omitted the server will use the default value of 2
            response_condition (str, none_type): The name of an existing condition in the configured endpoint, or leave blank to always execute.. [optional]
            format (str): A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). Must produce valid JSON that Elasticsearch can ingest.. [optional]
            tls_ca_cert (str, none_type): A secure certificate to authenticate a server with. Must be in PEM format.. [optional] if omitted the server will use the default value of "null"
            tls_client_cert (str, none_type): The client certificate used to make authenticated requests. Must be in PEM format.. [optional] if omitted the server will use the default value of "null"
            tls_client_key (str, none_type): The client private key used to make authenticated requests. Must be in PEM format.. [optional] if omitted the server will use the default value of "null"
            tls_hostname (str, none_type): The hostname to verify the server's certificate. This should be one of the Subject Alternative Name (SAN) fields for the certificate. Common Names (CN) are not supported.. [optional] if omitted the server will use the default value of "null"
            request_max_entries (int): The maximum number of logs sent in one request. Defaults `0` for unbounded.. [optional] if omitted the server will use the default value of 0
            request_max_bytes (int): The maximum number of bytes sent in one request. Defaults `0` for unbounded.. [optional] if omitted the server will use the default value of 0
            index (str): The name of the Elasticsearch index to send documents (logs) to. The index must follow the Elasticsearch [index format rules](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-create-index.html). We support [strftime](https://www.man7.org/linux/man-pages/man3/strftime.3.html) interpolated variables inside braces prefixed with a pound symbol. For example, `#{%F}` will interpolate as `YYYY-MM-DD` with today's date.. [optional]
            url (str): The URL to stream logs to. Must use HTTPS.. [optional]
            pipeline (str, none_type): The ID of the Elasticsearch ingest pipeline to apply pre-process transformations to before indexing. Learn more about creating a pipeline in the [Elasticsearch docs](https://www.elastic.co/guide/en/elasticsearch/reference/current/ingest.html).. [optional]
            user (str, none_type): Basic Auth username.. [optional]
            password (str, none_type): Basic Auth password.. [optional]
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
            LoggingElasticsearchResponse
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
        kwargs['logging_elasticsearch_name'] = \
            logging_elasticsearch_name
        return self.update_log_elasticsearch_endpoint.call_with_http_info(**kwargs)

