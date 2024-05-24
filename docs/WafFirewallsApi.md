# fastly.WafFirewallsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_waf_firewall**](WafFirewallsApi.md#create_waf_firewall) | **POST** /waf/firewalls | Create a firewall
[**delete_waf_firewall**](WafFirewallsApi.md#delete_waf_firewall) | **DELETE** /waf/firewalls/{firewall_id} | Delete a firewall
[**get_waf_firewall**](WafFirewallsApi.md#get_waf_firewall) | **GET** /waf/firewalls/{firewall_id} | Get a firewall
[**list_waf_firewalls**](WafFirewallsApi.md#list_waf_firewalls) | **GET** /waf/firewalls | List firewalls
[**update_waf_firewall**](WafFirewallsApi.md#update_waf_firewall) | **PATCH** /waf/firewalls/{firewall_id} | Update a firewall


# **create_waf_firewall**
> WafFirewallResponse create_waf_firewall()

Create a firewall

Create a firewall object for a particular service and service version using a defined `prefetch_condition` and `response`. If the `prefetch_condition` or the `response` is missing from the request body, Fastly will generate a default object on your service. 

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import waf_firewalls_api
from fastly.model.waf_firewall import WafFirewall
from fastly.model.waf_firewall_response import WafFirewallResponse
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
    api_instance = waf_firewalls_api.WafFirewallsApi(api_client)
    waf_firewall = WafFirewall(
        data=WafFirewallData(
            type=TypeWafFirewall("waf_firewall"),
            attributes=WafFirewallDataAttributes(
                disabled=False,
                prefetch_condition="prefetch_condition_example",
                response="response_example",
            ),
        ),
    ) # WafFirewall |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a firewall
        api_response = api_instance.create_waf_firewall(waf_firewall=waf_firewall)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafFirewallsApi->create_waf_firewall: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **waf_firewall** | [**WafFirewall**](WafFirewall.md)|  | [optional]

### Return type

[**WafFirewallResponse**](WafFirewallResponse.md)

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

# **delete_waf_firewall**
> delete_waf_firewall(firewall_id)

Delete a firewall

Delete the firewall object for a particular service and service version. 

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import waf_firewalls_api
from fastly.model.waf_firewall import WafFirewall
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
    api_instance = waf_firewalls_api.WafFirewallsApi(api_client)
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a WAF Firewall.
    waf_firewall = WafFirewall(
        data=WafFirewallData(
            type=TypeWafFirewall("waf_firewall"),
            attributes=WafFirewallDataAttributes(
                disabled=False,
                prefetch_condition="prefetch_condition_example",
                response="response_example",
            ),
        ),
    ) # WafFirewall |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a firewall
        api_instance.delete_waf_firewall(firewall_id)
    except fastly.ApiException as e:
        print("Exception when calling WafFirewallsApi->delete_waf_firewall: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a firewall
        api_instance.delete_waf_firewall(firewall_id, waf_firewall=waf_firewall)
    except fastly.ApiException as e:
        print("Exception when calling WafFirewallsApi->delete_waf_firewall: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| Alphanumeric string identifying a WAF Firewall. |
 **waf_firewall** | [**WafFirewall**](WafFirewall.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_waf_firewall**
> WafFirewallResponse get_waf_firewall(firewall_id)

Get a firewall

Get a specific firewall object.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import waf_firewalls_api
from fastly.model.waf_firewall_response import WafFirewallResponse
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
    api_instance = waf_firewalls_api.WafFirewallsApi(api_client)
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a WAF Firewall.
    filter_service_version_number = "filter[service_version_number]_example" # str | Limit the results returned to a specific service version. (optional)
    include = "waf_firewall_versions" # str | Include related objects. Optional. (optional) if omitted the server will use the default value of "waf_firewall_versions"

    # example passing only required values which don't have defaults set
    try:
        # Get a firewall
        api_response = api_instance.get_waf_firewall(firewall_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafFirewallsApi->get_waf_firewall: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a firewall
        api_response = api_instance.get_waf_firewall(firewall_id, filter_service_version_number=filter_service_version_number, include=include)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafFirewallsApi->get_waf_firewall: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| Alphanumeric string identifying a WAF Firewall. |
 **filter_service_version_number** | **str**| Limit the results returned to a specific service version. | [optional]
 **include** | **str**| Include related objects. Optional. | [optional] if omitted the server will use the default value of "waf_firewall_versions"

### Return type

[**WafFirewallResponse**](WafFirewallResponse.md)

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

# **list_waf_firewalls**
> WafFirewallsResponse list_waf_firewalls()

List firewalls

List all firewall objects.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import waf_firewalls_api
from fastly.model.waf_firewalls_response import WafFirewallsResponse
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
    api_instance = waf_firewalls_api.WafFirewallsApi(api_client)
    page_number = 1 # int | Current page. (optional)
    page_size = 20 # int | Number of records per page. (optional) if omitted the server will use the default value of 20
    filter_service_id = "filter[service_id]_example" # str | Limit the results returned to a specific service. (optional)
    filter_service_version_number = "filter[service_version_number]_example" # str | Limit the results returned to a specific service version. (optional)
    include = "waf_firewall_versions" # str | Include related objects. Optional. (optional) if omitted the server will use the default value of "waf_firewall_versions"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List firewalls
        api_response = api_instance.list_waf_firewalls(page_number=page_number, page_size=page_size, filter_service_id=filter_service_id, filter_service_version_number=filter_service_version_number, include=include)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafFirewallsApi->list_waf_firewalls: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Current page. | [optional]
 **page_size** | **int**| Number of records per page. | [optional] if omitted the server will use the default value of 20
 **filter_service_id** | **str**| Limit the results returned to a specific service. | [optional]
 **filter_service_version_number** | **str**| Limit the results returned to a specific service version. | [optional]
 **include** | **str**| Include related objects. Optional. | [optional] if omitted the server will use the default value of "waf_firewall_versions"

### Return type

[**WafFirewallsResponse**](WafFirewallsResponse.md)

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

# **update_waf_firewall**
> WafFirewallResponse update_waf_firewall(firewall_id)

Update a firewall

Update a firewall object for a particular service and service version. Specifying a `service_version_number` is required. 

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import waf_firewalls_api
from fastly.model.waf_firewall import WafFirewall
from fastly.model.waf_firewall_response import WafFirewallResponse
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
    api_instance = waf_firewalls_api.WafFirewallsApi(api_client)
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a WAF Firewall.
    waf_firewall = WafFirewall(
        data=WafFirewallData(
            type=TypeWafFirewall("waf_firewall"),
            attributes=WafFirewallDataAttributes(
                disabled=False,
                prefetch_condition="prefetch_condition_example",
                response="response_example",
            ),
        ),
    ) # WafFirewall |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a firewall
        api_response = api_instance.update_waf_firewall(firewall_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafFirewallsApi->update_waf_firewall: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a firewall
        api_response = api_instance.update_waf_firewall(firewall_id, waf_firewall=waf_firewall)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafFirewallsApi->update_waf_firewall: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| Alphanumeric string identifying a WAF Firewall. |
 **waf_firewall** | [**WafFirewall**](WafFirewall.md)|  | [optional]

### Return type

[**WafFirewallResponse**](WafFirewallResponse.md)

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

