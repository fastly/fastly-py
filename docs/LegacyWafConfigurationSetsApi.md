# fastly.LegacyWafConfigurationSetsApi

All URIs are relative to *https://api.fastly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_waf_config_sets**](LegacyWafConfigurationSetsApi.md#list_waf_config_sets) | **GET** /wafs/configuration_sets | List configuration sets
[**list_wafs_config_set**](LegacyWafConfigurationSetsApi.md#list_wafs_config_set) | **GET** /wafs/configuration_sets/{configuration_set_id}/relationships/wafs | List WAFs currently using a configuration set
[**use_waf_config_set**](LegacyWafConfigurationSetsApi.md#use_waf_config_set) | **PATCH** /wafs/configuration_sets/{configuration_set_id}/relationships/wafs | Apply a configuration set to a WAF


# **list_waf_config_sets**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list_waf_config_sets()

List configuration sets

List all Configuration sets.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import legacy_waf_configuration_sets_api
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
    api_instance = legacy_waf_configuration_sets_api.LegacyWafConfigurationSetsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List configuration sets
        api_response = api_instance.list_waf_config_sets()
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafConfigurationSetsApi->list_waf_config_sets: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **list_wafs_config_set**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list_wafs_config_set(configuration_set_id)

List WAFs currently using a configuration set

List the WAF objects currently using the specified configuration set.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import legacy_waf_configuration_sets_api
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
    api_instance = legacy_waf_configuration_sets_api.LegacyWafConfigurationSetsApi(api_client)
    configuration_set_id = "Cf9g2uUGZzb2W9Euo4m0oR" # str | Alphanumeric string identifying a WAF configuration set.

    # example passing only required values which don't have defaults set
    try:
        # List WAFs currently using a configuration set
        api_response = api_instance.list_wafs_config_set(configuration_set_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafConfigurationSetsApi->list_wafs_config_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_set_id** | **str**| Alphanumeric string identifying a WAF configuration set. |

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

# **use_waf_config_set**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} use_waf_config_set(configuration_set_id)

Apply a configuration set to a WAF

Update one or more WAF objects to use the specified configuration set.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import legacy_waf_configuration_sets_api
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
    api_instance = legacy_waf_configuration_sets_api.LegacyWafConfigurationSetsApi(api_client)
    configuration_set_id = "Cf9g2uUGZzb2W9Euo4m0oR" # str | Alphanumeric string identifying a WAF configuration set.
    request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Apply a configuration set to a WAF
        api_response = api_instance.use_waf_config_set(configuration_set_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafConfigurationSetsApi->use_waf_config_set: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Apply a configuration set to a WAF
        api_response = api_instance.use_waf_config_set(configuration_set_id, request_body=request_body)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafConfigurationSetsApi->use_waf_config_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_set_id** | **str**| Alphanumeric string identifying a WAF configuration set. |
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

