# fastly.WafExclusionsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_waf_rule_exclusion**](WafExclusionsApi.md#create_waf_rule_exclusion) | **POST** /waf/firewalls/{firewall_id}/versions/{firewall_version_number}/exclusions | Create a WAF rule exclusion
[**delete_waf_rule_exclusion**](WafExclusionsApi.md#delete_waf_rule_exclusion) | **DELETE** /waf/firewalls/{firewall_id}/versions/{firewall_version_number}/exclusions/{exclusion_number} | Delete a WAF rule exclusion
[**get_waf_rule_exclusion**](WafExclusionsApi.md#get_waf_rule_exclusion) | **GET** /waf/firewalls/{firewall_id}/versions/{firewall_version_number}/exclusions/{exclusion_number} | Get a WAF rule exclusion
[**list_waf_rule_exclusions**](WafExclusionsApi.md#list_waf_rule_exclusions) | **GET** /waf/firewalls/{firewall_id}/versions/{firewall_version_number}/exclusions | List WAF rule exclusions
[**update_waf_rule_exclusion**](WafExclusionsApi.md#update_waf_rule_exclusion) | **PATCH** /waf/firewalls/{firewall_id}/versions/{firewall_version_number}/exclusions/{exclusion_number} | Update a WAF rule exclusion


# **create_waf_rule_exclusion**
> WafExclusionResponse create_waf_rule_exclusion(firewall_id, firewall_version_number)

Create a WAF rule exclusion

Create a WAF exclusion for a particular firewall version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import waf_exclusions_api
from fastly.model.waf_exclusion_response import WafExclusionResponse
from fastly.model.waf_exclusion import WafExclusion
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
    api_instance = waf_exclusions_api.WafExclusionsApi(api_client)
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a WAF Firewall.
    firewall_version_number = 1 # int | Integer identifying a WAF firewall version.
    waf_exclusion = WafExclusion(
        data=WafExclusionData(
            type=TypeWafExclusion("waf_exclusion"),
            attributes=WafExclusionDataAttributes(
                condition="condition_example",
                exclusion_type="rule",
                logging=True,
                name="name_example",
                number=1,
                variable="req.cookies",
            ),
            relationships=RelationshipsForWafExclusion(),
        ),
    ) # WafExclusion |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a WAF rule exclusion
        api_response = api_instance.create_waf_rule_exclusion(firewall_id, firewall_version_number)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafExclusionsApi->create_waf_rule_exclusion: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a WAF rule exclusion
        api_response = api_instance.create_waf_rule_exclusion(firewall_id, firewall_version_number, waf_exclusion=waf_exclusion)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafExclusionsApi->create_waf_rule_exclusion: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| Alphanumeric string identifying a WAF Firewall. |
 **firewall_version_number** | **int**| Integer identifying a WAF firewall version. |
 **waf_exclusion** | [**WafExclusion**](WafExclusion.md)|  | [optional]

### Return type

[**WafExclusionResponse**](WafExclusionResponse.md)

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

# **delete_waf_rule_exclusion**
> delete_waf_rule_exclusion(firewall_id, firewall_version_number, exclusion_number)

Delete a WAF rule exclusion

Delete a WAF exclusion for a particular firewall version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import waf_exclusions_api
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
    api_instance = waf_exclusions_api.WafExclusionsApi(api_client)
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a WAF Firewall.
    firewall_version_number = 1 # int | Integer identifying a WAF firewall version.
    exclusion_number = 1 # int | A numeric ID identifying a WAF exclusion.

    # example passing only required values which don't have defaults set
    try:
        # Delete a WAF rule exclusion
        api_instance.delete_waf_rule_exclusion(firewall_id, firewall_version_number, exclusion_number)
    except fastly.ApiException as e:
        print("Exception when calling WafExclusionsApi->delete_waf_rule_exclusion: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| Alphanumeric string identifying a WAF Firewall. |
 **firewall_version_number** | **int**| Integer identifying a WAF firewall version. |
 **exclusion_number** | **int**| A numeric ID identifying a WAF exclusion. |

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_waf_rule_exclusion**
> WafExclusionResponse get_waf_rule_exclusion(firewall_id, firewall_version_number, exclusion_number)

Get a WAF rule exclusion

Get a specific WAF exclusion object.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import waf_exclusions_api
from fastly.model.waf_exclusion_response import WafExclusionResponse
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
    api_instance = waf_exclusions_api.WafExclusionsApi(api_client)
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a WAF Firewall.
    firewall_version_number = 1 # int | Integer identifying a WAF firewall version.
    exclusion_number = 1 # int | A numeric ID identifying a WAF exclusion.

    # example passing only required values which don't have defaults set
    try:
        # Get a WAF rule exclusion
        api_response = api_instance.get_waf_rule_exclusion(firewall_id, firewall_version_number, exclusion_number)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafExclusionsApi->get_waf_rule_exclusion: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| Alphanumeric string identifying a WAF Firewall. |
 **firewall_version_number** | **int**| Integer identifying a WAF firewall version. |
 **exclusion_number** | **int**| A numeric ID identifying a WAF exclusion. |

### Return type

[**WafExclusionResponse**](WafExclusionResponse.md)

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

# **list_waf_rule_exclusions**
> WafExclusionsResponse list_waf_rule_exclusions(firewall_id, firewall_version_number)

List WAF rule exclusions

List all exclusions for a particular firewall version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import waf_exclusions_api
from fastly.model.waf_exclusions_response import WafExclusionsResponse
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
    api_instance = waf_exclusions_api.WafExclusionsApi(api_client)
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a WAF Firewall.
    firewall_version_number = 1 # int | Integer identifying a WAF firewall version.
    filter_exclusion_type = "rule" # str | Filters the results based on this exclusion type. (optional)
    filter_name = "filter[name]_example" # str | Filters the results based on name. (optional)
    filter_waf_rules_modsec_rule_id = 1 # int | Filters the results based on this ModSecurity rule ID. (optional)
    page_number = 1 # int | Current page. (optional)
    page_size = 20 # int | Number of records per page. (optional) if omitted the server will use the default value of 20
    include = "waf_rules" # str | Include relationships. Optional, comma-separated values. Permitted values: `waf_rules` and `waf_rule_revisions`.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List WAF rule exclusions
        api_response = api_instance.list_waf_rule_exclusions(firewall_id, firewall_version_number)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafExclusionsApi->list_waf_rule_exclusions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List WAF rule exclusions
        api_response = api_instance.list_waf_rule_exclusions(firewall_id, firewall_version_number, filter_exclusion_type=filter_exclusion_type, filter_name=filter_name, filter_waf_rules_modsec_rule_id=filter_waf_rules_modsec_rule_id, page_number=page_number, page_size=page_size, include=include)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafExclusionsApi->list_waf_rule_exclusions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| Alphanumeric string identifying a WAF Firewall. |
 **firewall_version_number** | **int**| Integer identifying a WAF firewall version. |
 **filter_exclusion_type** | **str**| Filters the results based on this exclusion type. | [optional]
 **filter_name** | **str**| Filters the results based on name. | [optional]
 **filter_waf_rules_modsec_rule_id** | **int**| Filters the results based on this ModSecurity rule ID. | [optional]
 **page_number** | **int**| Current page. | [optional]
 **page_size** | **int**| Number of records per page. | [optional] if omitted the server will use the default value of 20
 **include** | **str**| Include relationships. Optional, comma-separated values. Permitted values: `waf_rules` and `waf_rule_revisions`.  | [optional]

### Return type

[**WafExclusionsResponse**](WafExclusionsResponse.md)

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

# **update_waf_rule_exclusion**
> WafExclusionResponse update_waf_rule_exclusion(firewall_id, firewall_version_number, exclusion_number)

Update a WAF rule exclusion

Update a WAF exclusion for a particular firewall version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import waf_exclusions_api
from fastly.model.waf_exclusion_response import WafExclusionResponse
from fastly.model.waf_exclusion import WafExclusion
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
    api_instance = waf_exclusions_api.WafExclusionsApi(api_client)
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a WAF Firewall.
    firewall_version_number = 1 # int | Integer identifying a WAF firewall version.
    exclusion_number = 1 # int | A numeric ID identifying a WAF exclusion.
    waf_exclusion = WafExclusion(
        data=WafExclusionData(
            type=TypeWafExclusion("waf_exclusion"),
            attributes=WafExclusionDataAttributes(
                condition="condition_example",
                exclusion_type="rule",
                logging=True,
                name="name_example",
                number=1,
                variable="req.cookies",
            ),
            relationships=RelationshipsForWafExclusion(),
        ),
    ) # WafExclusion |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a WAF rule exclusion
        api_response = api_instance.update_waf_rule_exclusion(firewall_id, firewall_version_number, exclusion_number)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafExclusionsApi->update_waf_rule_exclusion: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a WAF rule exclusion
        api_response = api_instance.update_waf_rule_exclusion(firewall_id, firewall_version_number, exclusion_number, waf_exclusion=waf_exclusion)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafExclusionsApi->update_waf_rule_exclusion: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| Alphanumeric string identifying a WAF Firewall. |
 **firewall_version_number** | **int**| Integer identifying a WAF firewall version. |
 **exclusion_number** | **int**| A numeric ID identifying a WAF exclusion. |
 **waf_exclusion** | [**WafExclusion**](WafExclusion.md)|  | [optional]

### Return type

[**WafExclusionResponse**](WafExclusionResponse.md)

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

