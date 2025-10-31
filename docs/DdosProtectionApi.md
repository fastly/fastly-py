# fastly.DdosProtectionApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**ddos_protection_event_get**](DdosProtectionApi.md#ddos_protection_event_get) | **GET** /ddos-protection/v1/events/{event_id} | Get event by ID
[**ddos_protection_event_list**](DdosProtectionApi.md#ddos_protection_event_list) | **GET** /ddos-protection/v1/events | Get events
[**ddos_protection_event_rule_list**](DdosProtectionApi.md#ddos_protection_event_rule_list) | **GET** /ddos-protection/v1/events/{event_id}/rules | Get all rules for an event
[**ddos_protection_rule_get**](DdosProtectionApi.md#ddos_protection_rule_get) | **GET** /ddos-protection/v1/rules/{rule_id} | Get a rule by ID
[**ddos_protection_rule_patch**](DdosProtectionApi.md#ddos_protection_rule_patch) | **PATCH** /ddos-protection/v1/rules/{rule_id} | Update rule
[**ddos_protection_traffic_stats_rule_get**](DdosProtectionApi.md#ddos_protection_traffic_stats_rule_get) | **GET** /ddos-protection/v1/events/{event_id}/rules/{rule_id}/traffic-stats | Get traffic stats for a rule


# **ddos_protection_event_get**
> DdosProtectionEvent ddos_protection_event_get(event_id)

Get event by ID

Get event by ID.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import ddos_protection_api
from fastly.model.ddos_protection_not_found import DdosProtectionNotFound
from fastly.model.ddos_protection_event import DdosProtectionEvent
from fastly.model.ddos_protection_not_authenticated import DdosProtectionNotAuthenticated
from fastly.model.ddos_protection_error import DdosProtectionError
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
    api_instance = ddos_protection_api.DdosProtectionApi(api_client)
    event_id = "54de69dcba53b02fbf000018" # str | Unique ID of the event.

    # example passing only required values which don't have defaults set
    try:
        # Get event by ID
        api_response = api_instance.ddos_protection_event_get(event_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DdosProtectionApi->ddos_protection_event_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**| Unique ID of the event. |

### Return type

[**DdosProtectionEvent**](DdosProtectionEvent.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | User is not authenticated. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ddos_protection_event_list**
> InlineResponse2002 ddos_protection_event_list()

Get events

Get events.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import ddos_protection_api
from fastly.model.ddos_protection_not_found import DdosProtectionNotFound
from fastly.model.inline_response2002 import InlineResponse2002
from fastly.model.ddos_protection_not_authenticated import DdosProtectionNotAuthenticated
from fastly.model.ddos_protection_error import DdosProtectionError
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
    api_instance = ddos_protection_api.DdosProtectionApi(api_client)
    cursor = "cursor_example" # str | Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. (optional)
    limit = 20 # int | Limit how many results are returned. (optional) if omitted the server will use the default value of 20
    service_id = "service_id_example" # str | Filter results based on a service_id. (optional)
    _from = dateutil_parser('2023-01-01T02:30:00Z') # datetime | Represents the start of a date-time range expressed in RFC 3339 format. (optional)
    to = dateutil_parser('2023-01-01T02:30:00Z') # datetime | Represents the end of a date-time range expressed in RFC 3339 format. (optional)
    name = "name_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get events
        api_response = api_instance.ddos_protection_event_list(cursor=cursor, limit=limit, service_id=service_id, _from=_from, to=to, name=name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DdosProtectionApi->ddos_protection_event_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. | [optional]
 **limit** | **int**| Limit how many results are returned. | [optional] if omitted the server will use the default value of 20
 **service_id** | **str**| Filter results based on a service_id. | [optional]
 **_from** | **datetime**| Represents the start of a date-time range expressed in RFC 3339 format. | [optional]
 **to** | **datetime**| Represents the end of a date-time range expressed in RFC 3339 format. | [optional]
 **name** | **str**|  | [optional]

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | User is not authenticated. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ddos_protection_event_rule_list**
> InlineResponse2003 ddos_protection_event_rule_list(event_id)

Get all rules for an event

Get all rules for an event.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import ddos_protection_api
from fastly.model.inline_response2003 import InlineResponse2003
from fastly.model.ddos_protection_not_found import DdosProtectionNotFound
from fastly.model.ddos_protection_not_authenticated import DdosProtectionNotAuthenticated
from fastly.model.ddos_protection_error import DdosProtectionError
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
    api_instance = ddos_protection_api.DdosProtectionApi(api_client)
    event_id = "54de69dcba53b02fbf000018" # str | Unique ID of the event.
    cursor = "cursor_example" # str | Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. (optional)
    limit = 20 # int | Limit how many results are returned. (optional) if omitted the server will use the default value of 20
    include = "include_example" # str | Include relationships. Optional. Comma-separated values. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all rules for an event
        api_response = api_instance.ddos_protection_event_rule_list(event_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DdosProtectionApi->ddos_protection_event_rule_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all rules for an event
        api_response = api_instance.ddos_protection_event_rule_list(event_id, cursor=cursor, limit=limit, include=include)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DdosProtectionApi->ddos_protection_event_rule_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**| Unique ID of the event. |
 **cursor** | **str**| Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. | [optional]
 **limit** | **int**| Limit how many results are returned. | [optional] if omitted the server will use the default value of 20
 **include** | **str**| Include relationships. Optional. Comma-separated values. | [optional]

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | User is not authenticated. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ddos_protection_rule_get**
> DdosProtectionRule ddos_protection_rule_get(rule_id)

Get a rule by ID

Get a rule by ID.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import ddos_protection_api
from fastly.model.ddos_protection_not_found import DdosProtectionNotFound
from fastly.model.ddos_protection_not_authenticated import DdosProtectionNotAuthenticated
from fastly.model.ddos_protection_error import DdosProtectionError
from fastly.model.ddos_protection_rule import DdosProtectionRule
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
    api_instance = ddos_protection_api.DdosProtectionApi(api_client)
    rule_id = "54de69dcba53b02fbf000018" # str | Unique ID of the rule.

    # example passing only required values which don't have defaults set
    try:
        # Get a rule by ID
        api_response = api_instance.ddos_protection_rule_get(rule_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DdosProtectionApi->ddos_protection_rule_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| Unique ID of the rule. |

### Return type

[**DdosProtectionRule**](DdosProtectionRule.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | User is not authenticated. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ddos_protection_rule_patch**
> DdosProtectionRule ddos_protection_rule_patch(rule_id)

Update rule

Update rule.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import ddos_protection_api
from fastly.model.ddos_protection_not_found import DdosProtectionNotFound
from fastly.model.ddos_protection_not_authorized import DdosProtectionNotAuthorized
from fastly.model.ddos_protection_not_authenticated import DdosProtectionNotAuthenticated
from fastly.model.ddos_protection_invalid_request import DdosProtectionInvalidRequest
from fastly.model.ddos_protection_error import DdosProtectionError
from fastly.model.ddos_protection_rule import DdosProtectionRule
from fastly.model.ddos_protection_rule_patch import DdosProtectionRulePatch
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
    api_instance = ddos_protection_api.DdosProtectionApi(api_client)
    rule_id = "54de69dcba53b02fbf000018" # str | Unique ID of the rule.
    ddos_protection_rule_patch = DdosProtectionRulePatch(
        action="default",
    ) # DdosProtectionRulePatch |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update rule
        api_response = api_instance.ddos_protection_rule_patch(rule_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DdosProtectionApi->ddos_protection_rule_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update rule
        api_response = api_instance.ddos_protection_rule_patch(rule_id, ddos_protection_rule_patch=ddos_protection_rule_patch)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DdosProtectionApi->ddos_protection_rule_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| Unique ID of the rule. |
 **ddos_protection_rule_patch** | [**DdosProtectionRulePatch**](DdosProtectionRulePatch.md)|  | [optional]

### Return type

[**DdosProtectionRule**](DdosProtectionRule.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not authorized. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ddos_protection_traffic_stats_rule_get**
> DdosProtectionTrafficStats ddos_protection_traffic_stats_rule_get(event_id, rule_id)

Get traffic stats for a rule

Get traffic stats for a rule.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import ddos_protection_api
from fastly.model.ddos_protection_not_found import DdosProtectionNotFound
from fastly.model.ddos_protection_not_authenticated import DdosProtectionNotAuthenticated
from fastly.model.ddos_protection_traffic_stats import DdosProtectionTrafficStats
from fastly.model.ddos_protection_error import DdosProtectionError
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
    api_instance = ddos_protection_api.DdosProtectionApi(api_client)
    event_id = "54de69dcba53b02fbf000018" # str | Unique ID of the event.
    rule_id = "54de69dcba53b02fbf000018" # str | Unique ID of the rule.

    # example passing only required values which don't have defaults set
    try:
        # Get traffic stats for a rule
        api_response = api_instance.ddos_protection_traffic_stats_rule_get(event_id, rule_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DdosProtectionApi->ddos_protection_traffic_stats_rule_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**| Unique ID of the event. |
 **rule_id** | **str**| Unique ID of the rule. |

### Return type

[**DdosProtectionTrafficStats**](DdosProtectionTrafficStats.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | User is not authenticated. |  -  |
**404** | Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

