# fastly.VclApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_vcl**](VclApi.md#create_custom_vcl) | **POST** /service/{service_id}/version/{version_id}/vcl | Create a custom VCL file
[**delete_custom_vcl**](VclApi.md#delete_custom_vcl) | **DELETE** /service/{service_id}/version/{version_id}/vcl/{vcl_name} | Delete a custom VCL file
[**get_custom_vcl**](VclApi.md#get_custom_vcl) | **GET** /service/{service_id}/version/{version_id}/vcl/{vcl_name} | Get a custom VCL file
[**get_custom_vcl_boilerplate**](VclApi.md#get_custom_vcl_boilerplate) | **GET** /service/{service_id}/version/{version_id}/boilerplate | Get boilerplate VCL
[**get_custom_vcl_generated**](VclApi.md#get_custom_vcl_generated) | **GET** /service/{service_id}/version/{version_id}/generated_vcl | Get the generated VCL for a service
[**get_custom_vcl_generated_highlighted**](VclApi.md#get_custom_vcl_generated_highlighted) | **GET** /service/{service_id}/version/{version_id}/generated_vcl/content | Get the generated VCL with syntax highlighting
[**get_custom_vcl_highlighted**](VclApi.md#get_custom_vcl_highlighted) | **GET** /service/{service_id}/version/{version_id}/vcl/{vcl_name}/content | Get a custom VCL file with syntax highlighting
[**get_custom_vcl_raw**](VclApi.md#get_custom_vcl_raw) | **GET** /service/{service_id}/version/{version_id}/vcl/{vcl_name}/download | Download a custom VCL file
[**lint_vcl_default**](VclApi.md#lint_vcl_default) | **POST** /vcl_lint | Lint (validate) VCL using a default set of flags.
[**lint_vcl_for_service**](VclApi.md#lint_vcl_for_service) | **POST** /service/{service_id}/lint | Lint (validate) VCL using flags set for the service.
[**list_custom_vcl**](VclApi.md#list_custom_vcl) | **GET** /service/{service_id}/version/{version_id}/vcl | List custom VCL files
[**set_custom_vcl_main**](VclApi.md#set_custom_vcl_main) | **PUT** /service/{service_id}/version/{version_id}/vcl/{vcl_name}/main | Set a custom VCL file as main
[**update_custom_vcl**](VclApi.md#update_custom_vcl) | **PUT** /service/{service_id}/version/{version_id}/vcl/{vcl_name} | Update a custom VCL file


# **create_custom_vcl**
> VclResponse create_custom_vcl(service_id, version_id)

Create a custom VCL file

Upload a VCL for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import vcl_api
from fastly.model.vcl_response import VclResponse
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
    api_instance = vcl_api.VclApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    content = "content_example" # str | The VCL code to be included. (optional)
    main = True # bool | Set to `true` when this is the main VCL, otherwise `false`. (optional)
    name = "test-vcl" # str | The name of this VCL. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a custom VCL file
        api_response = api_instance.create_custom_vcl(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling VclApi->create_custom_vcl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a custom VCL file
        api_response = api_instance.create_custom_vcl(service_id, version_id, content=content, main=main, name=name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling VclApi->create_custom_vcl: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **content** | **str**| The VCL code to be included. | [optional]
 **main** | **bool**| Set to `true` when this is the main VCL, otherwise `false`. | [optional]
 **name** | **str**| The name of this VCL. | [optional]

### Return type

[**VclResponse**](VclResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_vcl**
> InlineResponse200 delete_custom_vcl(service_id, version_id, vcl_name)

Delete a custom VCL file

Delete the uploaded VCL for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import vcl_api
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
    api_instance = vcl_api.VclApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    vcl_name = "test-vcl" # str | The name of this VCL.

    # example passing only required values which don't have defaults set
    try:
        # Delete a custom VCL file
        api_response = api_instance.delete_custom_vcl(service_id, version_id, vcl_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling VclApi->delete_custom_vcl: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **vcl_name** | **str**| The name of this VCL. |

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

# **get_custom_vcl**
> VclResponse get_custom_vcl(service_id, version_id, vcl_name)

Get a custom VCL file

Get the uploaded VCL for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import vcl_api
from fastly.model.vcl_response import VclResponse
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
    api_instance = vcl_api.VclApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    vcl_name = "test-vcl" # str | The name of this VCL.
    no_content = "0" # str | Omit VCL content. (optional) if omitted the server will use the default value of "0"

    # example passing only required values which don't have defaults set
    try:
        # Get a custom VCL file
        api_response = api_instance.get_custom_vcl(service_id, version_id, vcl_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling VclApi->get_custom_vcl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a custom VCL file
        api_response = api_instance.get_custom_vcl(service_id, version_id, vcl_name, no_content=no_content)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling VclApi->get_custom_vcl: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **vcl_name** | **str**| The name of this VCL. |
 **no_content** | **str**| Omit VCL content. | [optional] if omitted the server will use the default value of "0"

### Return type

[**VclResponse**](VclResponse.md)

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

# **get_custom_vcl_boilerplate**
> str get_custom_vcl_boilerplate(service_id, version_id)

Get boilerplate VCL

Return boilerplate VCL with the service's TTL from the [settings](https://www.fastly.com/documentation/reference/api/vcl-services/settings/).

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import vcl_api
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
    api_instance = vcl_api.VclApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # Get boilerplate VCL
        api_response = api_instance.get_custom_vcl_boilerplate(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling VclApi->get_custom_vcl_boilerplate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

**str**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_vcl_generated**
> VclResponse get_custom_vcl_generated(service_id, version_id)

Get the generated VCL for a service

Display the generated VCL for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import vcl_api
from fastly.model.vcl_response import VclResponse
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
    api_instance = vcl_api.VclApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # Get the generated VCL for a service
        api_response = api_instance.get_custom_vcl_generated(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling VclApi->get_custom_vcl_generated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**VclResponse**](VclResponse.md)

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

# **get_custom_vcl_generated_highlighted**
> VclSyntaxHighlightingResponse get_custom_vcl_generated_highlighted(service_id, version_id)

Get the generated VCL with syntax highlighting

Display the content of generated VCL with HTML syntax highlighting. Include line numbers by sending `lineno=true` as a request parameter.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import vcl_api
from fastly.model.vcl_syntax_highlighting_response import VclSyntaxHighlightingResponse
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
    api_instance = vcl_api.VclApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # Get the generated VCL with syntax highlighting
        api_response = api_instance.get_custom_vcl_generated_highlighted(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling VclApi->get_custom_vcl_generated_highlighted: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**VclSyntaxHighlightingResponse**](VclSyntaxHighlightingResponse.md)

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

# **get_custom_vcl_highlighted**
> VclSyntaxHighlightingResponse get_custom_vcl_highlighted(service_id, version_id, vcl_name)

Get a custom VCL file with syntax highlighting

Get the uploaded VCL for a particular service and version with HTML syntax highlighting. Include line numbers by sending `lineno=true` as a request parameter.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import vcl_api
from fastly.model.vcl_syntax_highlighting_response import VclSyntaxHighlightingResponse
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
    api_instance = vcl_api.VclApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    vcl_name = "test-vcl" # str | The name of this VCL.

    # example passing only required values which don't have defaults set
    try:
        # Get a custom VCL file with syntax highlighting
        api_response = api_instance.get_custom_vcl_highlighted(service_id, version_id, vcl_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling VclApi->get_custom_vcl_highlighted: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **vcl_name** | **str**| The name of this VCL. |

### Return type

[**VclSyntaxHighlightingResponse**](VclSyntaxHighlightingResponse.md)

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

# **get_custom_vcl_raw**
> str get_custom_vcl_raw(service_id, version_id, vcl_name)

Download a custom VCL file

Download the specified VCL.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import vcl_api
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
    api_instance = vcl_api.VclApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    vcl_name = "test-vcl" # str | The name of this VCL.

    # example passing only required values which don't have defaults set
    try:
        # Download a custom VCL file
        api_response = api_instance.get_custom_vcl_raw(service_id, version_id, vcl_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling VclApi->get_custom_vcl_raw: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **vcl_name** | **str**| The name of this VCL. |

### Return type

**str**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lint_vcl_default**
> ValidatorResult lint_vcl_default(inline_object1)

Lint (validate) VCL using a default set of flags.

This endpoint validates the submitted VCL against a default set of enabled flags. Consider using the `/service/{service_id}/lint` operation to validate VCL in the context of a specific service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import vcl_api
from fastly.model.validator_result import ValidatorResult
from fastly.model.inline_object1 import InlineObject1
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
    api_instance = vcl_api.VclApi(api_client)
    inline_object1 = InlineObject1(
        vcl="vcl_example",
    ) # InlineObject1 | 

    # example passing only required values which don't have defaults set
    try:
        # Lint (validate) VCL using a default set of flags.
        api_response = api_instance.lint_vcl_default(inline_object1)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling VclApi->lint_vcl_default: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  |

### Return type

[**ValidatorResult**](ValidatorResult.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lint_vcl_for_service**
> ValidatorResult lint_vcl_for_service(service_id, inline_object)

Lint (validate) VCL using flags set for the service.

Services may have flags set by a Fastly employee or by the purchase of products as addons to the service, which modify the way VCL is interpreted by that service.  This endpoint validates the submitted VCL in the context of the specified service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import vcl_api
from fastly.model.validator_result import ValidatorResult
from fastly.model.inline_object import InlineObject
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
    api_instance = vcl_api.VclApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    inline_object = InlineObject(
        vcl="vcl_example",
    ) # InlineObject | 

    # example passing only required values which don't have defaults set
    try:
        # Lint (validate) VCL using flags set for the service.
        api_response = api_instance.lint_vcl_for_service(service_id, inline_object)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling VclApi->lint_vcl_for_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **inline_object** | [**InlineObject**](InlineObject.md)|  |

### Return type

[**ValidatorResult**](ValidatorResult.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_custom_vcl**
> [VclResponse] list_custom_vcl(service_id, version_id)

List custom VCL files

List the uploaded VCLs for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import vcl_api
from fastly.model.vcl_response import VclResponse
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
    api_instance = vcl_api.VclApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # List custom VCL files
        api_response = api_instance.list_custom_vcl(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling VclApi->list_custom_vcl: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**[VclResponse]**](VclResponse.md)

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

# **set_custom_vcl_main**
> VclResponse set_custom_vcl_main(service_id, version_id, vcl_name)

Set a custom VCL file as main

Set the specified VCL as the main.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import vcl_api
from fastly.model.vcl_response import VclResponse
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
    api_instance = vcl_api.VclApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    vcl_name = "test-vcl" # str | The name of this VCL.

    # example passing only required values which don't have defaults set
    try:
        # Set a custom VCL file as main
        api_response = api_instance.set_custom_vcl_main(service_id, version_id, vcl_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling VclApi->set_custom_vcl_main: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **vcl_name** | **str**| The name of this VCL. |

### Return type

[**VclResponse**](VclResponse.md)

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

# **update_custom_vcl**
> VclResponse update_custom_vcl(service_id, version_id, vcl_name)

Update a custom VCL file

Update the uploaded VCL for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import vcl_api
from fastly.model.vcl_response import VclResponse
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
    api_instance = vcl_api.VclApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    vcl_name = "test-vcl" # str | The name of this VCL.
    content = "content_example" # str | The VCL code to be included. (optional)
    main = True # bool | Set to `true` when this is the main VCL, otherwise `false`. (optional)
    name = "test-vcl" # str | The name of this VCL. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a custom VCL file
        api_response = api_instance.update_custom_vcl(service_id, version_id, vcl_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling VclApi->update_custom_vcl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a custom VCL file
        api_response = api_instance.update_custom_vcl(service_id, version_id, vcl_name, content=content, main=main, name=name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling VclApi->update_custom_vcl: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **vcl_name** | **str**| The name of this VCL. |
 **content** | **str**| The VCL code to be included. | [optional]
 **main** | **bool**| Set to `true` when this is the main VCL, otherwise `false`. | [optional]
 **name** | **str**| The name of this VCL. | [optional]

### Return type

[**VclResponse**](VclResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

