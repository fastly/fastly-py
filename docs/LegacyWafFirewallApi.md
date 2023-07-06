# fastly.LegacyWafFirewallApi

All URIs are relative to *https://api.fastly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_legacy_waf_firewall_service**](LegacyWafFirewallApi.md#create_legacy_waf_firewall_service) | **POST** /service/{service_id}/version/{version_id}/wafs | Create a firewall
[**disable_legacy_waf_firewall**](LegacyWafFirewallApi.md#disable_legacy_waf_firewall) | **PATCH** /wafs/{firewall_id}/disable | Disable a firewall
[**enable_legacy_waf_firewall**](LegacyWafFirewallApi.md#enable_legacy_waf_firewall) | **PATCH** /wafs/{firewall_id}/enable | Enable a firewall
[**get_legacy_waf_firewall**](LegacyWafFirewallApi.md#get_legacy_waf_firewall) | **GET** /wafs/{firewall_id} | Get a firewall object
[**get_legacy_waf_firewall_service**](LegacyWafFirewallApi.md#get_legacy_waf_firewall_service) | **GET** /service/{service_id}/version/{version_id}/wafs/{firewall_id} | Get a firewall
[**list_legacy_waf_firewalls**](LegacyWafFirewallApi.md#list_legacy_waf_firewalls) | **GET** /wafs | List active firewalls
[**list_legacy_waf_firewalls_service**](LegacyWafFirewallApi.md#list_legacy_waf_firewalls_service) | **GET** /service/{service_id}/version/{version_id}/wafs | List firewalls
[**update_legacy_waf_firewall_service**](LegacyWafFirewallApi.md#update_legacy_waf_firewall_service) | **PATCH** /service/{service_id}/version/{version_id}/wafs/{firewall_id} | Update a firewall


# **create_legacy_waf_firewall_service**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_legacy_waf_firewall_service(service_id, version_id)

Create a firewall

Create a firewall object for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import legacy_waf_firewall_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.fastly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fastly.Configuration(
    host = "https://api.fastly.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with fastly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = legacy_waf_firewall_api.LegacyWafFirewallApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a firewall
        api_response = api_instance.create_legacy_waf_firewall_service(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafFirewallApi->create_legacy_waf_firewall_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a firewall
        api_response = api_instance.create_legacy_waf_firewall_service(service_id, version_id, request_body=request_body)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafFirewallApi->create_legacy_waf_firewall_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_legacy_waf_firewall**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} disable_legacy_waf_firewall(firewall_id)

Disable a firewall

Disable a firewall for a particular service and version. This endpoint is intended to be used in an emergency. Disabling a firewall object for a specific service and version replaces your existing WAF ruleset with an empty ruleset. While disabled, your WAF ruleset will not be applied to your origin traffic. This endpoint is only available to users assigned the role of superuser or above. This is an asynchronous action. To check on the completion of this action, use the related link returned in the response to check on the Update Status of the action.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import legacy_waf_firewall_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.fastly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fastly.Configuration(
    host = "https://api.fastly.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with fastly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = legacy_waf_firewall_api.LegacyWafFirewallApi(api_client)
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a Firewall.
    request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Disable a firewall
        api_response = api_instance.disable_legacy_waf_firewall(firewall_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafFirewallApi->disable_legacy_waf_firewall: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Disable a firewall
        api_response = api_instance.disable_legacy_waf_firewall(firewall_id, request_body=request_body)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafFirewallApi->disable_legacy_waf_firewall: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| Alphanumeric string identifying a Firewall. |
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_legacy_waf_firewall**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} enable_legacy_waf_firewall(firewall_id)

Enable a firewall

Re-enable a firewall object for a particular service and version after it has been disabled. This endpoint is intended to be used in an emergency. When a firewall object is re-enabled, a newly generated WAF ruleset VCL based on the current WAF configuration is used to replace the empty ruleset. This endpoint is only available to users assigned the role of superuser or above. This is an asynchronous action. To check on the completion of this action, use the related link returned in the response to check on the Update Status of the action.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import legacy_waf_firewall_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.fastly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fastly.Configuration(
    host = "https://api.fastly.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with fastly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = legacy_waf_firewall_api.LegacyWafFirewallApi(api_client)
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a Firewall.
    request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Enable a firewall
        api_response = api_instance.enable_legacy_waf_firewall(firewall_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafFirewallApi->enable_legacy_waf_firewall: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Enable a firewall
        api_response = api_instance.enable_legacy_waf_firewall(firewall_id, request_body=request_body)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafFirewallApi->enable_legacy_waf_firewall: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| Alphanumeric string identifying a Firewall. |
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_legacy_waf_firewall**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_legacy_waf_firewall(firewall_id)

Get a firewall object

Get a specific firewall object.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import legacy_waf_firewall_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.fastly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fastly.Configuration(
    host = "https://api.fastly.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with fastly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = legacy_waf_firewall_api.LegacyWafFirewallApi(api_client)
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a Firewall.
    include = "configuration_set" # str | Include relationships. Optional, comma separated values. Permitted values: `configuration_set`, `owasp`, `rules`, `rule_statuses`.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a firewall object
        api_response = api_instance.get_legacy_waf_firewall(firewall_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafFirewallApi->get_legacy_waf_firewall: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a firewall object
        api_response = api_instance.get_legacy_waf_firewall(firewall_id, include=include)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafFirewallApi->get_legacy_waf_firewall: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| Alphanumeric string identifying a Firewall. |
 **include** | **str**| Include relationships. Optional, comma separated values. Permitted values: `configuration_set`, `owasp`, `rules`, `rule_statuses`.  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_legacy_waf_firewall_service**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_legacy_waf_firewall_service(service_id, version_id, firewall_id)

Get a firewall

Get a specific firewall object.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import legacy_waf_firewall_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.fastly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fastly.Configuration(
    host = "https://api.fastly.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with fastly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = legacy_waf_firewall_api.LegacyWafFirewallApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a Firewall.

    # example passing only required values which don't have defaults set
    try:
        # Get a firewall
        api_response = api_instance.get_legacy_waf_firewall_service(service_id, version_id, firewall_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafFirewallApi->get_legacy_waf_firewall_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **firewall_id** | **str**| Alphanumeric string identifying a Firewall. |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_legacy_waf_firewalls**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list_legacy_waf_firewalls()

List active firewalls

List all active firewall objects.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import legacy_waf_firewall_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.fastly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fastly.Configuration(
    host = "https://api.fastly.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with fastly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = legacy_waf_firewall_api.LegacyWafFirewallApi(api_client)
    filter_rules_rule_id = "filter[rules][rule_id]_example" # str | Limit the returned firewalls to a specific rule ID. (optional)
    page_number = 1 # int | Current page. (optional)
    page_size = 20 # int | Number of records per page. (optional) if omitted the server will use the default value of 20
    include = "configuration_set" # str | Include relationships. Optional, comma separated values. Permitted values: `configuration_set`, `owasp`.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List active firewalls
        api_response = api_instance.list_legacy_waf_firewalls(filter_rules_rule_id=filter_rules_rule_id, page_number=page_number, page_size=page_size, include=include)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafFirewallApi->list_legacy_waf_firewalls: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_rules_rule_id** | **str**| Limit the returned firewalls to a specific rule ID. | [optional]
 **page_number** | **int**| Current page. | [optional]
 **page_size** | **int**| Number of records per page. | [optional] if omitted the server will use the default value of 20
 **include** | **str**| Include relationships. Optional, comma separated values. Permitted values: `configuration_set`, `owasp`.  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_legacy_waf_firewalls_service**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list_legacy_waf_firewalls_service(service_id, version_id)

List firewalls

List all firewall objects for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import legacy_waf_firewall_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.fastly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fastly.Configuration(
    host = "https://api.fastly.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with fastly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = legacy_waf_firewall_api.LegacyWafFirewallApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    page_number = 1 # int | Current page. (optional)
    page_size = 20 # int | Number of records per page. (optional) if omitted the server will use the default value of 20
    include = "configuration_set" # str | Include relationships. Optional, comma separated values. Permitted values: `configuration_set`, `owasp`.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List firewalls
        api_response = api_instance.list_legacy_waf_firewalls_service(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafFirewallApi->list_legacy_waf_firewalls_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List firewalls
        api_response = api_instance.list_legacy_waf_firewalls_service(service_id, version_id, page_number=page_number, page_size=page_size, include=include)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafFirewallApi->list_legacy_waf_firewalls_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **page_number** | **int**| Current page. | [optional]
 **page_size** | **int**| Number of records per page. | [optional] if omitted the server will use the default value of 20
 **include** | **str**| Include relationships. Optional, comma separated values. Permitted values: `configuration_set`, `owasp`.  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_legacy_waf_firewall_service**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_legacy_waf_firewall_service(service_id, version_id, firewall_id)

Update a firewall

Update a firewall object for a particular service and version. 

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import legacy_waf_firewall_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.fastly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fastly.Configuration(
    host = "https://api.fastly.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with fastly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = legacy_waf_firewall_api.LegacyWafFirewallApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a Firewall.
    request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a firewall
        api_response = api_instance.update_legacy_waf_firewall_service(service_id, version_id, firewall_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafFirewallApi->update_legacy_waf_firewall_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a firewall
        api_response = api_instance.update_legacy_waf_firewall_service(service_id, version_id, firewall_id, request_body=request_body)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafFirewallApi->update_legacy_waf_firewall_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **firewall_id** | **str**| Alphanumeric string identifying a Firewall. |
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

