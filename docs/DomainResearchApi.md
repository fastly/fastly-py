# fastly.DomainResearchApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**domain_status**](DomainResearchApi.md#domain_status) | **GET** /domain-management/v1/tools/status | Domain status
[**suggest_domains**](DomainResearchApi.md#suggest_domains) | **GET** /domain-management/v1/tools/suggest | Suggest domains


# **domain_status**
> Status domain_status(domain)

Domain status

The `Status` method checks the availability status of a single domain name.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import domain_research_api
from fastly.model.status import Status
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
    api_instance = domain_research_api.DomainResearchApi(api_client)
    domain = "acmecoffee.shop" # str | 
    scope = "estimate" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Domain status
        api_response = api_instance.domain_status(domain)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DomainResearchApi->domain_status: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Domain status
        api_response = api_instance.domain_status(domain, scope=scope)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DomainResearchApi->domain_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**|  |
 **scope** | **str**|  | [optional]

### Return type

[**Status**](Status.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suggest_domains**
> InlineResponse2006 suggest_domains(query)

Suggest domains

The `Suggest` method performs a real-time query of the search term(s) against the [known zone database](http://zonedb.org), making recommendations, stemming, and applying Unicode folding, IDN normalization, registrar supported-zone restrictions, and other refinements. **Note:** `Suggest` method responses do not include domain availability status. 

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import domain_research_api
from fastly.model.inline_response2006 import InlineResponse2006
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
    api_instance = domain_research_api.DomainResearchApi(api_client)
    query = "foo%20bar" # str | 
    defaults = "club" # str |  (optional)
    keywords = "food,kitchen" # str |  (optional)
    location = "de" # str |  (optional)
    vendor = "dnsimple.com" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Suggest domains
        api_response = api_instance.suggest_domains(query)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DomainResearchApi->suggest_domains: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Suggest domains
        api_response = api_instance.suggest_domains(query, defaults=defaults, keywords=keywords, location=location, vendor=vendor)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DomainResearchApi->suggest_domains: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  |
 **defaults** | **str**|  | [optional]
 **keywords** | **str**|  | [optional]
 **location** | **str**|  | [optional]
 **vendor** | **str**|  | [optional]

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

