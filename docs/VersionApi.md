# fastly.VersionApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_service_version**](VersionApi.md#activate_service_version) | **PUT** /service/{service_id}/version/{version_id}/activate | Activate a service version
[**activate_service_version_environment**](VersionApi.md#activate_service_version_environment) | **PUT** /service/{service_id}/version/{version_id}/activate/{environment_name} | Activate a service version on the specified environment
[**clone_service_version**](VersionApi.md#clone_service_version) | **PUT** /service/{service_id}/version/{version_id}/clone | Clone a service version
[**create_service_version**](VersionApi.md#create_service_version) | **POST** /service/{service_id}/version | Create a service version
[**deactivate_service_version**](VersionApi.md#deactivate_service_version) | **PUT** /service/{service_id}/version/{version_id}/deactivate | Deactivate a service version
[**deactivate_service_version_environment**](VersionApi.md#deactivate_service_version_environment) | **PUT** /service/{service_id}/version/{version_id}/deactivate/{environment_name} | Deactivate a service version on an environment
[**get_service_version**](VersionApi.md#get_service_version) | **GET** /service/{service_id}/version/{version_id} | Get a version of a service
[**list_service_versions**](VersionApi.md#list_service_versions) | **GET** /service/{service_id}/version | List versions of a service
[**lock_service_version**](VersionApi.md#lock_service_version) | **PUT** /service/{service_id}/version/{version_id}/lock | Lock a service version
[**update_service_version**](VersionApi.md#update_service_version) | **PUT** /service/{service_id}/version/{version_id} | Update a service version
[**validate_service_version**](VersionApi.md#validate_service_version) | **GET** /service/{service_id}/version/{version_id}/validate | Validate a service version


# **activate_service_version**
> VersionResponse activate_service_version(service_id, version_id)

Activate a service version

Activate the current version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import version_api
from fastly.model.version_response import VersionResponse
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
    api_instance = version_api.VersionApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # Activate a service version
        api_response = api_instance.activate_service_version(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling VersionApi->activate_service_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**VersionResponse**](VersionResponse.md)

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

# **activate_service_version_environment**
> VersionResponse activate_service_version_environment(service_id, version_id, environment_name)

Activate a service version on the specified environment

Activate a version on a given environment, i.e. \"staging\"

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import version_api
from fastly.model.version_response import VersionResponse
from fastly.model.environment_name import EnvironmentName
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
    api_instance = version_api.VersionApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    environment_name = EnvironmentName("staging") # EnvironmentName | 

    # example passing only required values which don't have defaults set
    try:
        # Activate a service version on the specified environment
        api_response = api_instance.activate_service_version_environment(service_id, version_id, environment_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling VersionApi->activate_service_version_environment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **environment_name** | **EnvironmentName**|  |

### Return type

[**VersionResponse**](VersionResponse.md)

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

# **clone_service_version**
> Version clone_service_version(service_id, version_id)

Clone a service version

Clone the current configuration into a new version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import version_api
from fastly.model.version import Version
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
    api_instance = version_api.VersionApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # Clone a service version
        api_response = api_instance.clone_service_version(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling VersionApi->clone_service_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**Version**](Version.md)

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

# **create_service_version**
> VersionCreateResponse create_service_version(service_id)

Create a service version

Create a version for a particular service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import version_api
from fastly.model.version_create_response import VersionCreateResponse
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
    api_instance = version_api.VersionApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.

    # example passing only required values which don't have defaults set
    try:
        # Create a service version
        api_response = api_instance.create_service_version(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling VersionApi->create_service_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |

### Return type

[**VersionCreateResponse**](VersionCreateResponse.md)

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

# **deactivate_service_version**
> VersionResponse deactivate_service_version(service_id, version_id)

Deactivate a service version

Deactivate the current version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import version_api
from fastly.model.version_response import VersionResponse
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
    api_instance = version_api.VersionApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # Deactivate a service version
        api_response = api_instance.deactivate_service_version(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling VersionApi->deactivate_service_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**VersionResponse**](VersionResponse.md)

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

# **deactivate_service_version_environment**
> VersionResponse deactivate_service_version_environment(service_id, version_id, environment_name)

Deactivate a service version on an environment

Deactivate the current version on a given environment, i.e. \"staging\"

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import version_api
from fastly.model.version_response import VersionResponse
from fastly.model.environment_name import EnvironmentName
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
    api_instance = version_api.VersionApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    environment_name = EnvironmentName("staging") # EnvironmentName | 

    # example passing only required values which don't have defaults set
    try:
        # Deactivate a service version on an environment
        api_response = api_instance.deactivate_service_version_environment(service_id, version_id, environment_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling VersionApi->deactivate_service_version_environment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **environment_name** | **EnvironmentName**|  |

### Return type

[**VersionResponse**](VersionResponse.md)

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

# **get_service_version**
> VersionResponse get_service_version(service_id, version_id)

Get a version of a service

Get the version for a particular service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import version_api
from fastly.model.version_response import VersionResponse
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
    api_instance = version_api.VersionApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # Get a version of a service
        api_response = api_instance.get_service_version(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling VersionApi->get_service_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**VersionResponse**](VersionResponse.md)

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

# **list_service_versions**
> [VersionResponse] list_service_versions(service_id)

List versions of a service

List the versions for a particular service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import version_api
from fastly.model.version_response import VersionResponse
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
    api_instance = version_api.VersionApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.

    # example passing only required values which don't have defaults set
    try:
        # List versions of a service
        api_response = api_instance.list_service_versions(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling VersionApi->list_service_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |

### Return type

[**[VersionResponse]**](VersionResponse.md)

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

# **lock_service_version**
> Version lock_service_version(service_id, version_id)

Lock a service version

Locks the specified version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import version_api
from fastly.model.version import Version
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
    api_instance = version_api.VersionApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # Lock a service version
        api_response = api_instance.lock_service_version(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling VersionApi->lock_service_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**Version**](Version.md)

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

# **update_service_version**
> VersionResponse update_service_version(service_id, version_id)

Update a service version

Update a particular version for a particular service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import version_api
from fastly.model.version_response import VersionResponse
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
    api_instance = version_api.VersionApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    active = False # bool | Whether this is the active version or not. (optional) if omitted the server will use the default value of False
    comment = "" # str, none_type | A freeform descriptive note. (optional)
    deployed = True # bool | Unused at this time. (optional)
    locked = False # bool | Whether this version is locked or not. Objects can not be added or edited on locked versions. (optional) if omitted the server will use the default value of False
    number = 1 # int | The number of this version. (optional)
    staging = False # bool | Unused at this time. (optional) if omitted the server will use the default value of False
    testing = False # bool | Unused at this time. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Update a service version
        api_response = api_instance.update_service_version(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling VersionApi->update_service_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a service version
        api_response = api_instance.update_service_version(service_id, version_id, active=active, comment=comment, deployed=deployed, locked=locked, number=number, staging=staging, testing=testing)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling VersionApi->update_service_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **active** | **bool**| Whether this is the active version or not. | [optional] if omitted the server will use the default value of False
 **comment** | **str, none_type**| A freeform descriptive note. | [optional]
 **deployed** | **bool**| Unused at this time. | [optional]
 **locked** | **bool**| Whether this version is locked or not. Objects can not be added or edited on locked versions. | [optional] if omitted the server will use the default value of False
 **number** | **int**| The number of this version. | [optional]
 **staging** | **bool**| Unused at this time. | [optional] if omitted the server will use the default value of False
 **testing** | **bool**| Unused at this time. | [optional] if omitted the server will use the default value of False

### Return type

[**VersionResponse**](VersionResponse.md)

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

# **validate_service_version**
> InlineResponse200 validate_service_version(service_id, version_id)

Validate a service version

Validate the version for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import version_api
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
    api_instance = version_api.VersionApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # Validate a service version
        api_response = api_instance.validate_service_version(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling VersionApi->validate_service_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

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

