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
from fastly.model.customer_response import CustomerResponse
from fastly.model.inline_response200 import InlineResponse200
from fastly.model.schemas_user_response import SchemasUserResponse


class CustomerApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.delete_customer_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse200,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/customer/{customer_id}',
                'operation_id': 'delete_customer',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                ],
                'required': [
                    'customer_id',
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
                    'customer_id':
                        (str,),
                },
                'attribute_map': {
                    'customer_id': 'customer_id',
                },
                'location_map': {
                    'customer_id': 'path',
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
        self.get_customer_endpoint = _Endpoint(
            settings={
                'response_type': (CustomerResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/customer/{customer_id}',
                'operation_id': 'get_customer',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                ],
                'required': [
                    'customer_id',
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
                    'customer_id':
                        (str,),
                },
                'attribute_map': {
                    'customer_id': 'customer_id',
                },
                'location_map': {
                    'customer_id': 'path',
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
        self.get_logged_in_customer_endpoint = _Endpoint(
            settings={
                'response_type': (CustomerResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/current_customer',
                'operation_id': 'get_logged_in_customer',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
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
                },
                'attribute_map': {
                },
                'location_map': {
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
        self.list_users_endpoint = _Endpoint(
            settings={
                'response_type': ([SchemasUserResponse],),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/customer/{customer_id}/users',
                'operation_id': 'list_users',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                ],
                'required': [
                    'customer_id',
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
                    'customer_id':
                        (str,),
                },
                'attribute_map': {
                    'customer_id': 'customer_id',
                },
                'location_map': {
                    'customer_id': 'path',
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
        self.update_customer_endpoint = _Endpoint(
            settings={
                'response_type': (CustomerResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/customer/{customer_id}',
                'operation_id': 'update_customer',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                    'billing_contact_id',
                    'billing_network_type',
                    'billing_ref',
                    'can_configure_wordpress',
                    'can_reset_passwords',
                    'can_upload_vcl',
                    'force_2fa',
                    'force_sso',
                    'has_account_panel',
                    'has_improved_events',
                    'has_improved_ssl_config',
                    'has_openstack_logging',
                    'has_pci',
                    'has_pci_passwords',
                    'ip_whitelist',
                    'legal_contact_id',
                    'name',
                    'owner_id',
                    'phone_number',
                    'postal_address',
                    'pricing_plan',
                    'pricing_plan_id',
                    'security_contact_id',
                    'technical_contact_id',
                ],
                'required': [
                    'customer_id',
                ],
                'nullable': [
                    'billing_contact_id',
                    'billing_ref',
                    'can_configure_wordpress',
                    'legal_contact_id',
                    'postal_address',
                    'security_contact_id',
                    'technical_contact_id',
                ],
                'enum': [
                    'billing_network_type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('billing_network_type',): {

                        "PUBLIC": "public",
                        "PRIVATE": "private"
                    },
                },
                'openapi_types': {
                    'customer_id':
                        (str,),
                    'billing_contact_id':
                        (str, none_type,),
                    'billing_network_type':
                        (str,),
                    'billing_ref':
                        (str, none_type,),
                    'can_configure_wordpress':
                        (bool, none_type,),
                    'can_reset_passwords':
                        (bool,),
                    'can_upload_vcl':
                        (bool,),
                    'force_2fa':
                        (bool,),
                    'force_sso':
                        (bool,),
                    'has_account_panel':
                        (bool,),
                    'has_improved_events':
                        (bool,),
                    'has_improved_ssl_config':
                        (bool,),
                    'has_openstack_logging':
                        (bool,),
                    'has_pci':
                        (bool,),
                    'has_pci_passwords':
                        (bool,),
                    'ip_whitelist':
                        (str,),
                    'legal_contact_id':
                        (str, none_type,),
                    'name':
                        (str,),
                    'owner_id':
                        (str,),
                    'phone_number':
                        (str,),
                    'postal_address':
                        (str, none_type,),
                    'pricing_plan':
                        (str,),
                    'pricing_plan_id':
                        (str,),
                    'security_contact_id':
                        (str, none_type,),
                    'technical_contact_id':
                        (str, none_type,),
                },
                'attribute_map': {
                    'customer_id': 'customer_id',
                    'billing_contact_id': 'billing_contact_id',
                    'billing_network_type': 'billing_network_type',
                    'billing_ref': 'billing_ref',
                    'can_configure_wordpress': 'can_configure_wordpress',
                    'can_reset_passwords': 'can_reset_passwords',
                    'can_upload_vcl': 'can_upload_vcl',
                    'force_2fa': 'force_2fa',
                    'force_sso': 'force_sso',
                    'has_account_panel': 'has_account_panel',
                    'has_improved_events': 'has_improved_events',
                    'has_improved_ssl_config': 'has_improved_ssl_config',
                    'has_openstack_logging': 'has_openstack_logging',
                    'has_pci': 'has_pci',
                    'has_pci_passwords': 'has_pci_passwords',
                    'ip_whitelist': 'ip_whitelist',
                    'legal_contact_id': 'legal_contact_id',
                    'name': 'name',
                    'owner_id': 'owner_id',
                    'phone_number': 'phone_number',
                    'postal_address': 'postal_address',
                    'pricing_plan': 'pricing_plan',
                    'pricing_plan_id': 'pricing_plan_id',
                    'security_contact_id': 'security_contact_id',
                    'technical_contact_id': 'technical_contact_id',
                },
                'location_map': {
                    'customer_id': 'path',
                    'billing_contact_id': 'form',
                    'billing_network_type': 'form',
                    'billing_ref': 'form',
                    'can_configure_wordpress': 'form',
                    'can_reset_passwords': 'form',
                    'can_upload_vcl': 'form',
                    'force_2fa': 'form',
                    'force_sso': 'form',
                    'has_account_panel': 'form',
                    'has_improved_events': 'form',
                    'has_improved_ssl_config': 'form',
                    'has_openstack_logging': 'form',
                    'has_pci': 'form',
                    'has_pci_passwords': 'form',
                    'ip_whitelist': 'form',
                    'legal_contact_id': 'form',
                    'name': 'form',
                    'owner_id': 'form',
                    'phone_number': 'form',
                    'postal_address': 'form',
                    'pricing_plan': 'form',
                    'pricing_plan_id': 'form',
                    'security_contact_id': 'form',
                    'technical_contact_id': 'form',
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

    def delete_customer(
        self,
        customer_id,
        **kwargs
    ):
        """Delete a customer  # noqa: E501

        Delete a customer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_customer(customer_id, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): Alphanumeric string identifying the customer.

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
        kwargs['customer_id'] = \
            customer_id
        return self.delete_customer_endpoint.call_with_http_info(**kwargs)

    def get_customer(
        self,
        customer_id,
        **kwargs
    ):
        """Get a customer  # noqa: E501

        Get a specific customer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_customer(customer_id, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): Alphanumeric string identifying the customer.

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
            CustomerResponse
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
        kwargs['customer_id'] = \
            customer_id
        return self.get_customer_endpoint.call_with_http_info(**kwargs)

    def get_logged_in_customer(
        self,
        **kwargs
    ):
        """Get the logged in customer  # noqa: E501

        Get the logged in customer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_logged_in_customer(async_req=True)
        >>> result = thread.get()


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
            CustomerResponse
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
        return self.get_logged_in_customer_endpoint.call_with_http_info(**kwargs)

    def list_users(
        self,
        customer_id,
        **kwargs
    ):
        """List users  # noqa: E501

        List all users from a specified customer id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_users(customer_id, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): Alphanumeric string identifying the customer.

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
            [SchemasUserResponse]
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
        kwargs['customer_id'] = \
            customer_id
        return self.list_users_endpoint.call_with_http_info(**kwargs)

    def update_customer(
        self,
        customer_id,
        **kwargs
    ):
        """Update a customer  # noqa: E501

        Update a customer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_customer(customer_id, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): Alphanumeric string identifying the customer.

        Keyword Args:
            billing_contact_id (str, none_type): The alphanumeric string representing the primary billing contact.. [optional]
            billing_network_type (str): Customer's current network revenue type.. [optional]
            billing_ref (str, none_type): Used for adding purchased orders to customer's account.. [optional]
            can_configure_wordpress (bool, none_type): Whether this customer can view or edit wordpress.. [optional]
            can_reset_passwords (bool): Whether this customer can reset passwords.. [optional]
            can_upload_vcl (bool): Whether this customer can upload VCL.. [optional]
            force_2fa (bool): Specifies whether 2FA is forced or not forced on the customer account. Logs out non-2FA users once 2FA is force enabled.. [optional]
            force_sso (bool): Specifies whether SSO is forced or not forced on the customer account.. [optional]
            has_account_panel (bool): Specifies whether the account has access or does not have access to the account panel.. [optional]
            has_improved_events (bool): Specifies whether the account has access or does not have access to the improved events.. [optional]
            has_improved_ssl_config (bool): Whether this customer can view or edit the SSL config.. [optional]
            has_openstack_logging (bool): Specifies whether the account has enabled or not enabled openstack logging.. [optional]
            has_pci (bool): Specifies whether the account can edit PCI for a service.. [optional]
            has_pci_passwords (bool): Specifies whether PCI passwords are required for the account.. [optional]
            ip_whitelist (str): The range of IP addresses authorized to access the customer account.. [optional]
            legal_contact_id (str, none_type): The alphanumeric string identifying the account's legal contact.. [optional]
            name (str): The name of the customer, generally the company name.. [optional]
            owner_id (str): The alphanumeric string identifying the account owner.. [optional]
            phone_number (str): The phone number associated with the account.. [optional]
            postal_address (str, none_type): The postal address associated with the account.. [optional]
            pricing_plan (str): The pricing plan this customer is under.. [optional]
            pricing_plan_id (str): The alphanumeric string identifying the pricing plan.. [optional]
            security_contact_id (str, none_type): The alphanumeric string identifying the account's security contact.. [optional]
            technical_contact_id (str, none_type): The alphanumeric string identifying the account's technical contact.. [optional]
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
            CustomerResponse
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
        kwargs['customer_id'] = \
            customer_id
        return self.update_customer_endpoint.call_with_http_info(**kwargs)

