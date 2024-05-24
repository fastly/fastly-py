# fastly.DictionaryInfoApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dictionary_info**](DictionaryInfoApi.md#get_dictionary_info) | **GET** /service/{service_id}/version/{version_id}/dictionary/{dictionary_id}/info | Get edge dictionary metadata


# **get_dictionary_info**
> DictionaryInfoResponse get_dictionary_info(service_id, version_id, dictionary_id)

Get edge dictionary metadata

Retrieve metadata for a single dictionary by ID for a version and service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dictionary_info_api
from fastly.model.dictionary_info_response import DictionaryInfoResponse
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
    api_instance = dictionary_info_api.DictionaryInfoApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    dictionary_id = "3vjTN8v1O7nOAY7aNDGOL" # str | Alphanumeric string identifying a Dictionary.

    # example passing only required values which don't have defaults set
    try:
        # Get edge dictionary metadata
        api_response = api_instance.get_dictionary_info(service_id, version_id, dictionary_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DictionaryInfoApi->get_dictionary_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **dictionary_id** | **str**| Alphanumeric string identifying a Dictionary. |

### Return type

[**DictionaryInfoResponse**](DictionaryInfoResponse.md)

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

