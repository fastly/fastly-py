# fastly.AiRuntimeControlProvidersApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**arc_get_bedrock_setup**](AiRuntimeControlProvidersApi.md#arc_get_bedrock_setup) | **GET** /ai-runtime-control/v1/providers/bedrock/setup | Get Bedrock setup information
[**arc_get_models_for_provider**](AiRuntimeControlProvidersApi.md#arc_get_models_for_provider) | **GET** /ai-runtime-control/v1/providers/{provider_id}/models | Get models for a provider
[**arc_get_supported_providers**](AiRuntimeControlProvidersApi.md#arc_get_supported_providers) | **GET** /ai-runtime-control/v1/providers | Get supported providers


# **arc_get_bedrock_setup**
> ArcBedrockSetupResponse arc_get_bedrock_setup()

Get Bedrock setup information

Returns the AI Runtime Control IAM role Amazon Resource Name (ARN) and external ID to reference in your AWS account's IAM trust policy before creating an `aws-iam` [provider connection](https://www.fastly.com/documentation/reference/api/ai-runtime-control/provider-connections#arc-create-provider-connection) to Amazon Bedrock.  Requires AWS IAM authentication to be enabled on your account. If it isn't, this endpoint returns a 404 response. 

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import ai_runtime_control_providers_api
from fastly.model.arc_bedrock_setup_response import ArcBedrockSetupResponse
from fastly.model.arc_error import ArcError
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
    api_instance = ai_runtime_control_providers_api.AiRuntimeControlProvidersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Bedrock setup information
        api_response = api_instance.arc_get_bedrock_setup()
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AiRuntimeControlProvidersApi->arc_get_bedrock_setup: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ArcBedrockSetupResponse**](ArcBedrockSetupResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bedrock setup information. |  -  |
**401** | User is not authenticated. |  -  |
**403** | Customer is not entitled to AI Runtime Control. |  -  |
**404** | Entity not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **arc_get_models_for_provider**
> ArcModelsResponse arc_get_models_for_provider(provider_id)

Get models for a provider

Returns the models available for a specific provider.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import ai_runtime_control_providers_api
from fastly.model.arc_models_response import ArcModelsResponse
from fastly.model.arc_error import ArcError
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
    api_instance = ai_runtime_control_providers_api.AiRuntimeControlProvidersApi(api_client)
    provider_id = "anthropic" # str | The ID of the provider.

    # example passing only required values which don't have defaults set
    try:
        # Get models for a provider
        api_response = api_instance.arc_get_models_for_provider(provider_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AiRuntimeControlProvidersApi->arc_get_models_for_provider: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| The ID of the provider. |

### Return type

[**ArcModelsResponse**](ArcModelsResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of models available for the provider. |  -  |
**401** | User is not authenticated. |  -  |
**403** | Customer is not entitled to AI Runtime Control. |  -  |
**404** | Entity not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **arc_get_supported_providers**
> ArcProvidersResponse arc_get_supported_providers()

Get supported providers

Returns the AI providers supported by AI Runtime Control, with each provider's available models nested within.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import ai_runtime_control_providers_api
from fastly.model.arc_providers_response import ArcProvidersResponse
from fastly.model.arc_error import ArcError
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
    api_instance = ai_runtime_control_providers_api.AiRuntimeControlProvidersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get supported providers
        api_response = api_instance.arc_get_supported_providers()
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AiRuntimeControlProvidersApi->arc_get_supported_providers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ArcProvidersResponse**](ArcProvidersResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of supported providers. |  -  |
**401** | User is not authenticated. |  -  |
**403** | Customer is not entitled to AI Runtime Control. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

