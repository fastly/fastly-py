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
from fastly.model.inline_response200 import InlineResponse200
from fastly.model.rate_limiter_response import RateLimiterResponse


class RateLimiterApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_rate_limiter_endpoint = _Endpoint(
            settings={
                'response_type': (RateLimiterResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/rate-limiters',
                'operation_id': 'create_rate_limiter',
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
                    'service_id',
                    'version_id',
                    'name',
                    'uri_dictionary_name',
                    'http_methods',
                    'rps_limit',
                    'window_size',
                    'client_key',
                    'penalty_box_duration',
                    'action',
                    'response_object_name',
                    'logger_type',
                    'feature_revision',
                ],
                'required': [
                    'service_id',
                    'version_id',
                ],
                'nullable': [
                    'uri_dictionary_name',
                    'response_object_name',
                ],
                'enum': [
                    'http_methods',
                    'window_size',
                    'action',
                    'logger_type',
                ],
                'validation': [
                    'name',
                    'uri_dictionary_name',
                    'http_methods',
                    'rps_limit',
                    'client_key',
                    'penalty_box_duration',
                    'action',
                    'response_object_name',
                ]
            },
            root_map={
                'validations': {
                    ('name',): {
                        'max_length': 255,
                        'min_length': 1,
                    },
                    ('uri_dictionary_name',): {
                        'max_length': 255,
                        'min_length': 1,
                    },
                    ('http_methods',): {

                        'min_items': 1,
                    },
                    ('rps_limit',): {

                        'inclusive_maximum': 10000,
                        'inclusive_minimum': 10,
                    },
                    ('client_key',): {

                        'min_items': 1,
                    },
                    ('penalty_box_duration',): {

                        'inclusive_maximum': 60,
                        'inclusive_minimum': 1,
                    },
                    ('action',): {

                        'min_length': 1,
                    },
                    ('response_object_name',): {
                        'max_length': 255,
                        'min_length': 1,
                    },
                },
                'allowed_values': {
                    ('http_methods',): {

                        "HEAD": "HEAD",
                        "OPTIONS": "OPTIONS",
                        "GET": "GET",
                        "POST": "POST",
                        "PUT": "PUT",
                        "PATCH": "PATCH",
                        "DELETE": "DELETE",
                        "TRACE": "TRACE"
                    },
                    ('window_size',): {

                        "one_second": 1,
                        "ten_seconds": 10,
                        "one_minute": 60
                    },
                    ('action',): {

                        "RESPONSE": "response",
                        "RESPONSE_OBJECT": "response_object",
                        "LOG_ONLY": "log_only"
                    },
                    ('logger_type',): {

                        "AZUREBLOB": "azureblob",
                        "BIGQUERY": "bigquery",
                        "CLOUDFILES": "cloudfiles",
                        "DATADOG": "datadog",
                        "DIGITALOCEAN": "digitalocean",
                        "ELASTICSEARCH": "elasticsearch",
                        "FTP": "ftp",
                        "GCS": "gcs",
                        "GOOGLEANALYTICS": "googleanalytics",
                        "HEROKU": "heroku",
                        "HONEYCOMB": "honeycomb",
                        "HTTP": "http",
                        "HTTPS": "https",
                        "KAFKA": "kafka",
                        "KINESIS": "kinesis",
                        "LOGENTRIES": "logentries",
                        "LOGGLY": "loggly",
                        "LOGSHUTTLE": "logshuttle",
                        "NEWRELIC": "newrelic",
                        "NEWRELICOTLP": "newrelicotlp",
                        "OPENSTACK": "openstack",
                        "PAPERTRAIL": "papertrail",
                        "PUBSUB": "pubsub",
                        "S3": "s3",
                        "SCALYR": "scalyr",
                        "SFTP": "sftp",
                        "SPLUNK": "splunk",
                        "STACKDRIVER": "stackdriver",
                        "SUMOLOGIC": "sumologic",
                        "SYSLOG": "syslog"
                    },
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'version_id':
                        (int,),
                    'name':
                        (str,),
                    'uri_dictionary_name':
                        (str, none_type,),
                    'http_methods':
                        ([str],),
                    'rps_limit':
                        (int,),
                    'window_size':
                        (int,),
                    'client_key':
                        ([str],),
                    'penalty_box_duration':
                        (int,),
                    'action':
                        (str,),
                    'response_object_name':
                        (str, none_type,),
                    'logger_type':
                        (str,),
                    'feature_revision':
                        (int,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'name': 'name',
                    'uri_dictionary_name': 'uri_dictionary_name',
                    'http_methods': 'http_methods',
                    'rps_limit': 'rps_limit',
                    'window_size': 'window_size',
                    'client_key': 'client_key',
                    'penalty_box_duration': 'penalty_box_duration',
                    'action': 'action',
                    'response_object_name': 'response_object_name',
                    'logger_type': 'logger_type',
                    'feature_revision': 'feature_revision',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'name': 'form',
                    'uri_dictionary_name': 'form',
                    'http_methods': 'form',
                    'rps_limit': 'form',
                    'window_size': 'form',
                    'client_key': 'form',
                    'penalty_box_duration': 'form',
                    'action': 'form',
                    'response_object_name': 'form',
                    'logger_type': 'form',
                    'feature_revision': 'form',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                    'http_methods': 'csv',
                    'client_key': 'csv',
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
        self.delete_rate_limiter_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse200,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/rate-limiters/{rate_limiter_id}',
                'operation_id': 'delete_rate_limiter',
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
                    'rate_limiter_id',
                ],
                'required': [
                    'rate_limiter_id',
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
                    'rate_limiter_id':
                        (str,),
                },
                'attribute_map': {
                    'rate_limiter_id': 'rate_limiter_id',
                },
                'location_map': {
                    'rate_limiter_id': 'path',
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
        self.get_rate_limiter_endpoint = _Endpoint(
            settings={
                'response_type': (RateLimiterResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/rate-limiters/{rate_limiter_id}',
                'operation_id': 'get_rate_limiter',
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
                    'rate_limiter_id',
                ],
                'required': [
                    'rate_limiter_id',
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
                    'rate_limiter_id':
                        (str,),
                },
                'attribute_map': {
                    'rate_limiter_id': 'rate_limiter_id',
                },
                'location_map': {
                    'rate_limiter_id': 'path',
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
        self.list_rate_limiters_endpoint = _Endpoint(
            settings={
                'response_type': ([RateLimiterResponse],),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/rate-limiters',
                'operation_id': 'list_rate_limiters',
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
        self.update_rate_limiter_endpoint = _Endpoint(
            settings={
                'response_type': (RateLimiterResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/rate-limiters/{rate_limiter_id}',
                'operation_id': 'update_rate_limiter',
                'http_method': 'PUT',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'rate_limiter_id',
                    'name',
                    'uri_dictionary_name',
                    'http_methods',
                    'rps_limit',
                    'window_size',
                    'client_key',
                    'penalty_box_duration',
                    'action',
                    'response_object_name',
                    'logger_type',
                    'feature_revision',
                ],
                'required': [
                    'rate_limiter_id',
                ],
                'nullable': [
                    'uri_dictionary_name',
                    'response_object_name',
                ],
                'enum': [
                    'http_methods',
                    'window_size',
                    'action',
                    'logger_type',
                ],
                'validation': [
                    'name',
                    'uri_dictionary_name',
                    'http_methods',
                    'rps_limit',
                    'client_key',
                    'penalty_box_duration',
                    'action',
                    'response_object_name',
                ]
            },
            root_map={
                'validations': {
                    ('name',): {
                        'max_length': 255,
                        'min_length': 1,
                    },
                    ('uri_dictionary_name',): {
                        'max_length': 255,
                        'min_length': 1,
                    },
                    ('http_methods',): {

                        'min_items': 1,
                    },
                    ('rps_limit',): {

                        'inclusive_maximum': 10000,
                        'inclusive_minimum': 10,
                    },
                    ('client_key',): {

                        'min_items': 1,
                    },
                    ('penalty_box_duration',): {

                        'inclusive_maximum': 60,
                        'inclusive_minimum': 1,
                    },
                    ('action',): {

                        'min_length': 1,
                    },
                    ('response_object_name',): {
                        'max_length': 255,
                        'min_length': 1,
                    },
                },
                'allowed_values': {
                    ('http_methods',): {

                        "HEAD": "HEAD",
                        "OPTIONS": "OPTIONS",
                        "GET": "GET",
                        "POST": "POST",
                        "PUT": "PUT",
                        "PATCH": "PATCH",
                        "DELETE": "DELETE",
                        "TRACE": "TRACE"
                    },
                    ('window_size',): {

                        "one_second": 1,
                        "ten_seconds": 10,
                        "one_minute": 60
                    },
                    ('action',): {

                        "RESPONSE": "response",
                        "RESPONSE_OBJECT": "response_object",
                        "LOG_ONLY": "log_only"
                    },
                    ('logger_type',): {

                        "AZUREBLOB": "azureblob",
                        "BIGQUERY": "bigquery",
                        "CLOUDFILES": "cloudfiles",
                        "DATADOG": "datadog",
                        "DIGITALOCEAN": "digitalocean",
                        "ELASTICSEARCH": "elasticsearch",
                        "FTP": "ftp",
                        "GCS": "gcs",
                        "GOOGLEANALYTICS": "googleanalytics",
                        "HEROKU": "heroku",
                        "HONEYCOMB": "honeycomb",
                        "HTTP": "http",
                        "HTTPS": "https",
                        "KAFKA": "kafka",
                        "KINESIS": "kinesis",
                        "LOGENTRIES": "logentries",
                        "LOGGLY": "loggly",
                        "LOGSHUTTLE": "logshuttle",
                        "NEWRELIC": "newrelic",
                        "NEWRELICOTLP": "newrelicotlp",
                        "OPENSTACK": "openstack",
                        "PAPERTRAIL": "papertrail",
                        "PUBSUB": "pubsub",
                        "S3": "s3",
                        "SCALYR": "scalyr",
                        "SFTP": "sftp",
                        "SPLUNK": "splunk",
                        "STACKDRIVER": "stackdriver",
                        "SUMOLOGIC": "sumologic",
                        "SYSLOG": "syslog"
                    },
                },
                'openapi_types': {
                    'rate_limiter_id':
                        (str,),
                    'name':
                        (str,),
                    'uri_dictionary_name':
                        (str, none_type,),
                    'http_methods':
                        ([str],),
                    'rps_limit':
                        (int,),
                    'window_size':
                        (int,),
                    'client_key':
                        ([str],),
                    'penalty_box_duration':
                        (int,),
                    'action':
                        (str,),
                    'response_object_name':
                        (str, none_type,),
                    'logger_type':
                        (str,),
                    'feature_revision':
                        (int,),
                },
                'attribute_map': {
                    'rate_limiter_id': 'rate_limiter_id',
                    'name': 'name',
                    'uri_dictionary_name': 'uri_dictionary_name',
                    'http_methods': 'http_methods',
                    'rps_limit': 'rps_limit',
                    'window_size': 'window_size',
                    'client_key': 'client_key',
                    'penalty_box_duration': 'penalty_box_duration',
                    'action': 'action',
                    'response_object_name': 'response_object_name',
                    'logger_type': 'logger_type',
                    'feature_revision': 'feature_revision',
                },
                'location_map': {
                    'rate_limiter_id': 'path',
                    'name': 'form',
                    'uri_dictionary_name': 'form',
                    'http_methods': 'form',
                    'rps_limit': 'form',
                    'window_size': 'form',
                    'client_key': 'form',
                    'penalty_box_duration': 'form',
                    'action': 'form',
                    'response_object_name': 'form',
                    'logger_type': 'form',
                    'feature_revision': 'form',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                    'http_methods': 'csv',
                    'client_key': 'csv',
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

    def create_rate_limiter(
        self,
        service_id,
        version_id,
        **kwargs
    ):
        """Create a rate limiter  # noqa: E501

        Create a rate limiter for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_rate_limiter(service_id, version_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.

        Keyword Args:
            name (str): A human readable name for the rate limiting rule.. [optional]
            uri_dictionary_name (str, none_type): The name of an Edge Dictionary containing URIs as keys. If not defined or `null`, all origin URIs will be rate limited.. [optional]
            http_methods ([str]): Array of HTTP methods to apply rate limiting to.. [optional]
            rps_limit (int): Upper limit of requests per second allowed by the rate limiter.. [optional]
            window_size (int): Number of seconds during which the RPS limit must be exceeded in order to trigger a violation.. [optional]
            client_key ([str]): Array of VCL variables used to generate a counter key to identify a client. Example variables include `req.http.Fastly-Client-IP`, `req.http.User-Agent`, or a custom header like `req.http.API-Key`.. [optional]
            penalty_box_duration (int): Length of time in minutes that the rate limiter is in effect after the initial violation is detected.. [optional]
            action (str): The action to take when a rate limiter violation is detected.. [optional]
            response_object_name (str, none_type): Name of existing response object. Required if `action` is `response_object`. Note that the rate limiter response is only updated to reflect the response object content when saving the rate limiter configuration.. [optional]
            logger_type (str): Name of the type of logging endpoint to be used when action is `log_only`. The logging endpoint type is used to determine the appropriate log format to use when emitting log entries.. [optional]
            feature_revision (int): Revision number of the rate limiting feature implementation. Defaults to the most recent revision.. [optional]
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
            RateLimiterResponse
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
        return self.create_rate_limiter_endpoint.call_with_http_info(**kwargs)

    def delete_rate_limiter(
        self,
        rate_limiter_id,
        **kwargs
    ):
        """Delete a rate limiter  # noqa: E501

        Delete a rate limiter by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_rate_limiter(rate_limiter_id, async_req=True)
        >>> result = thread.get()

        Args:
            rate_limiter_id (str): Alphanumeric string identifying the rate limiter.

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
        kwargs['rate_limiter_id'] = \
            rate_limiter_id
        return self.delete_rate_limiter_endpoint.call_with_http_info(**kwargs)

    def get_rate_limiter(
        self,
        rate_limiter_id,
        **kwargs
    ):
        """Get a rate limiter  # noqa: E501

        Get a rate limiter by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_rate_limiter(rate_limiter_id, async_req=True)
        >>> result = thread.get()

        Args:
            rate_limiter_id (str): Alphanumeric string identifying the rate limiter.

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
            RateLimiterResponse
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
        kwargs['rate_limiter_id'] = \
            rate_limiter_id
        return self.get_rate_limiter_endpoint.call_with_http_info(**kwargs)

    def list_rate_limiters(
        self,
        service_id,
        version_id,
        **kwargs
    ):
        """List rate limiters  # noqa: E501

        List all rate limiters for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_rate_limiters(service_id, version_id, async_req=True)
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
            [RateLimiterResponse]
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
        return self.list_rate_limiters_endpoint.call_with_http_info(**kwargs)

    def update_rate_limiter(
        self,
        rate_limiter_id,
        **kwargs
    ):
        """Update a rate limiter  # noqa: E501

        Update a rate limiter by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_rate_limiter(rate_limiter_id, async_req=True)
        >>> result = thread.get()

        Args:
            rate_limiter_id (str): Alphanumeric string identifying the rate limiter.

        Keyword Args:
            name (str): A human readable name for the rate limiting rule.. [optional]
            uri_dictionary_name (str, none_type): The name of an Edge Dictionary containing URIs as keys. If not defined or `null`, all origin URIs will be rate limited.. [optional]
            http_methods ([str]): Array of HTTP methods to apply rate limiting to.. [optional]
            rps_limit (int): Upper limit of requests per second allowed by the rate limiter.. [optional]
            window_size (int): Number of seconds during which the RPS limit must be exceeded in order to trigger a violation.. [optional]
            client_key ([str]): Array of VCL variables used to generate a counter key to identify a client. Example variables include `req.http.Fastly-Client-IP`, `req.http.User-Agent`, or a custom header like `req.http.API-Key`.. [optional]
            penalty_box_duration (int): Length of time in minutes that the rate limiter is in effect after the initial violation is detected.. [optional]
            action (str): The action to take when a rate limiter violation is detected.. [optional]
            response_object_name (str, none_type): Name of existing response object. Required if `action` is `response_object`. Note that the rate limiter response is only updated to reflect the response object content when saving the rate limiter configuration.. [optional]
            logger_type (str): Name of the type of logging endpoint to be used when action is `log_only`. The logging endpoint type is used to determine the appropriate log format to use when emitting log entries.. [optional]
            feature_revision (int): Revision number of the rate limiting feature implementation. Defaults to the most recent revision.. [optional]
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
            RateLimiterResponse
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
        kwargs['rate_limiter_id'] = \
            rate_limiter_id
        return self.update_rate_limiter_endpoint.call_with_http_info(**kwargs)

