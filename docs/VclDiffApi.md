# fastly.VclDiffApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**vcl_diff_service_versions**](VclDiffApi.md#vcl_diff_service_versions) | **GET** /service/{service_id}/vcl/diff/from/{from_version_id}/to/{to_version_id} | Get a comparison of the VCL changes between two service versions


# **vcl_diff_service_versions**
> VclDiff vcl_diff_service_versions(service_id, from_version_id, to_version_id)

Get a comparison of the VCL changes between two service versions

Get a comparison of the VCL changes between two service versions.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import vcl_diff_api
from fastly.model.vcl_diff import VclDiff
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
    api_instance = vcl_diff_api.VclDiffApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    from_version_id = 1 # int | The version number of the service to which changes in the generated VCL are being compared. Can either be a positive number from 1 to your maximum version or a negative number from -1 down (-1 is latest version etc).
    to_version_id = 2 # int | The version number of the service from which changes in the generated VCL are being compared. Uses same numbering scheme as `from`.
    format = "text" # str | Optional method to format the diff field. (optional) if omitted the server will use the default value of "text"

    # example passing only required values which don't have defaults set
    try:
        # Get a comparison of the VCL changes between two service versions
        api_response = api_instance.vcl_diff_service_versions(service_id, from_version_id, to_version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling VclDiffApi->vcl_diff_service_versions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a comparison of the VCL changes between two service versions
        api_response = api_instance.vcl_diff_service_versions(service_id, from_version_id, to_version_id, format=format)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling VclDiffApi->vcl_diff_service_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **from_version_id** | **int**| The version number of the service to which changes in the generated VCL are being compared. Can either be a positive number from 1 to your maximum version or a negative number from -1 down (-1 is latest version etc). |
 **to_version_id** | **int**| The version number of the service from which changes in the generated VCL are being compared. Uses same numbering scheme as `from`. |
 **format** | **str**| Optional method to format the diff field. | [optional] if omitted the server will use the default value of "text"

### Return type

[**VclDiff**](VclDiff.md)

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

