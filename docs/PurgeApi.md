# fastly.PurgeApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_purge_tag**](PurgeApi.md#bulk_purge_tag) | **POST** /service/{service_id}/purge | Purge multiple surrogate key tags
[**purge_all**](PurgeApi.md#purge_all) | **POST** /service/{service_id}/purge_all | Purge everything from a service
[**purge_single_url**](PurgeApi.md#purge_single_url) | **POST** /purge/{cached_url} | Purge a URL
[**purge_tag**](PurgeApi.md#purge_tag) | **POST** /service/{service_id}/purge/{surrogate_key} | Purge by surrogate key tag


# **bulk_purge_tag**
> PurgeKeysResponse bulk_purge_tag(service_id)

Purge multiple surrogate key tags

Instant Purge a particular service of items tagged with surrogate keys. Up to 256 surrogate keys can be purged in one batch request. As an alternative to sending the keys in a JSON object in the body of the request, this endpoint also supports listing keys in a <code>Surrogate-Key</code> request header, e.g. <code>Surrogate-Key: key_1 key_2 key_3</code>. 

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import purge_api
from fastly.model.purge_keys_response import PurgeKeysResponse
from fastly.model.purge_response import PurgeResponse
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
    api_instance = purge_api.PurgeApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    fastly_soft_purge = 1 # int | If present, this header triggers the purge to be 'soft', which marks the affected object as stale rather than making it inaccessible.  Typically set to \"1\" when used, but the value is not important. (optional)
    surrogate_key = "key_1 key_2 key_3" # str | Purge multiple surrogate key tags using a request header. Not required if a JSON POST body is specified. (optional)
    purge_response = PurgeResponse(
        status="status_example",
    ) # PurgeResponse |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Purge multiple surrogate key tags
        api_response = api_instance.bulk_purge_tag(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling PurgeApi->bulk_purge_tag: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Purge multiple surrogate key tags
        api_response = api_instance.bulk_purge_tag(service_id, fastly_soft_purge=fastly_soft_purge, surrogate_key=surrogate_key, purge_response=purge_response)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling PurgeApi->bulk_purge_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **fastly_soft_purge** | **int**| If present, this header triggers the purge to be &#39;soft&#39;, which marks the affected object as stale rather than making it inaccessible.  Typically set to \&quot;1\&quot; when used, but the value is not important. | [optional]
 **surrogate_key** | **str**| Purge multiple surrogate key tags using a request header. Not required if a JSON POST body is specified. | [optional]
 **purge_response** | [**PurgeResponse**](PurgeResponse.md)|  | [optional]

### Return type

[**PurgeKeysResponse**](PurgeKeysResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purge_all**
> InlineResponse200 purge_all(service_id)

Purge everything from a service

Instant Purge everything from a service.  Purge-all requests cannot be done in soft mode and will always immediately invalidate all cached content associated with the service. To do a soft-purge-all, consider applying a constant [surrogate key](https://docs.fastly.com/en/guides/getting-started-with-surrogate-keys) tag (e.g., `\"all\"`) to all objects. 

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import purge_api
from fastly.model.inline_response200 import InlineResponse200
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
    api_instance = purge_api.PurgeApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.

    # example passing only required values which don't have defaults set
    try:
        # Purge everything from a service
        api_response = api_instance.purge_all(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling PurgeApi->purge_all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |

### Return type

[**InlineResponse200**](InlineResponse200.md)

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

# **purge_single_url**
> PurgeResponse purge_single_url(cached_url)

Purge a URL

Instant Purge an individual URL.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import purge_api
from fastly.model.purge_response import PurgeResponse
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
    api_instance = purge_api.PurgeApi(api_client)
    cached_url = "www.example.com/path/to/object-to-purge" # str | URL of object in cache to be purged.
    fastly_soft_purge = 1 # int | If present, this header triggers the purge to be 'soft', which marks the affected object as stale rather than making it inaccessible.  Typically set to \"1\" when used, but the value is not important. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Purge a URL
        api_response = api_instance.purge_single_url(cached_url)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling PurgeApi->purge_single_url: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Purge a URL
        api_response = api_instance.purge_single_url(cached_url, fastly_soft_purge=fastly_soft_purge)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling PurgeApi->purge_single_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cached_url** | **str**| URL of object in cache to be purged. |
 **fastly_soft_purge** | **int**| If present, this header triggers the purge to be &#39;soft&#39;, which marks the affected object as stale rather than making it inaccessible.  Typically set to \&quot;1\&quot; when used, but the value is not important. | [optional]

### Return type

[**PurgeResponse**](PurgeResponse.md)

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

# **purge_tag**
> PurgeResponse purge_tag(service_id, surrogate_key)

Purge by surrogate key tag

Instant Purge a particular service of items tagged with a Surrogate Key. Only one surrogate key can be purged at a time. Multiple keys can be purged using a batch surrogate key purge request.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import purge_api
from fastly.model.purge_response import PurgeResponse
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
    api_instance = purge_api.PurgeApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    surrogate_key = "key_1" # str | Surrogate keys are used to efficiently purge content from cache. Instead of purging your entire site or individual URLs, you can tag related assets (like all images and descriptions associated with a single product) with surrogate keys, and these grouped URLs can be purged in a single request.
    fastly_soft_purge = 1 # int | If present, this header triggers the purge to be 'soft', which marks the affected object as stale rather than making it inaccessible.  Typically set to \"1\" when used, but the value is not important. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Purge by surrogate key tag
        api_response = api_instance.purge_tag(service_id, surrogate_key)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling PurgeApi->purge_tag: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Purge by surrogate key tag
        api_response = api_instance.purge_tag(service_id, surrogate_key, fastly_soft_purge=fastly_soft_purge)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling PurgeApi->purge_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **surrogate_key** | **str**| Surrogate keys are used to efficiently purge content from cache. Instead of purging your entire site or individual URLs, you can tag related assets (like all images and descriptions associated with a single product) with surrogate keys, and these grouped URLs can be purged in a single request. |
 **fastly_soft_purge** | **int**| If present, this header triggers the purge to be &#39;soft&#39;, which marks the affected object as stale rather than making it inaccessible.  Typically set to \&quot;1\&quot; when used, but the value is not important. | [optional]

### Return type

[**PurgeResponse**](PurgeResponse.md)

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

