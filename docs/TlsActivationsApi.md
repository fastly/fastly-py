# fastly.TlsActivationsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tls_activation**](TlsActivationsApi.md#create_tls_activation) | **POST** /tls/activations | Enable TLS for a domain using a custom certificate
[**delete_tls_activation**](TlsActivationsApi.md#delete_tls_activation) | **DELETE** /tls/activations/{tls_activation_id} | Disable TLS on a domain
[**get_tls_activation**](TlsActivationsApi.md#get_tls_activation) | **GET** /tls/activations/{tls_activation_id} | Get a TLS activation
[**list_tls_activations**](TlsActivationsApi.md#list_tls_activations) | **GET** /tls/activations | List TLS activations
[**update_tls_activation**](TlsActivationsApi.md#update_tls_activation) | **PATCH** /tls/activations/{tls_activation_id} | Update a certificate


# **create_tls_activation**
> TlsActivationResponse create_tls_activation()

Enable TLS for a domain using a custom certificate

Enable TLS for a particular TLS domain and certificate combination. These relationships must be specified to create the TLS activation.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_activations_api
from fastly.model.tls_activation import TlsActivation
from fastly.model.tls_activation_response import TlsActivationResponse
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
    api_instance = tls_activations_api.TlsActivationsApi(api_client)
    tls_activation = TlsActivation(
        data=TlsActivationData(
            type=TypeTlsActivation("tls_activation"),
            relationships=RelationshipsForTlsActivation(),
        ),
    ) # TlsActivation |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Enable TLS for a domain using a custom certificate
        api_response = api_instance.create_tls_activation(tls_activation=tls_activation)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsActivationsApi->create_tls_activation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tls_activation** | [**TlsActivation**](TlsActivation.md)|  | [optional]

### Return type

[**TlsActivationResponse**](TlsActivationResponse.md)

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

# **delete_tls_activation**
> delete_tls_activation(tls_activation_id)

Disable TLS on a domain

Disable TLS on the domain associated with this TLS activation.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_activations_api
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
    api_instance = tls_activations_api.TlsActivationsApi(api_client)
    tls_activation_id = "aCtguUGZzb2W9Euo4moOR" # str | Alphanumeric string identifying a TLS activation.

    # example passing only required values which don't have defaults set
    try:
        # Disable TLS on a domain
        api_instance.delete_tls_activation(tls_activation_id)
    except fastly.ApiException as e:
        print("Exception when calling TlsActivationsApi->delete_tls_activation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tls_activation_id** | **str**| Alphanumeric string identifying a TLS activation. |

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

# **get_tls_activation**
> TlsActivationResponse get_tls_activation(tls_activation_id)

Get a TLS activation

Show a TLS activation.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_activations_api
from fastly.model.tls_activation_response import TlsActivationResponse
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
    api_instance = tls_activations_api.TlsActivationsApi(api_client)
    tls_activation_id = "aCtguUGZzb2W9Euo4moOR" # str | Alphanumeric string identifying a TLS activation.
    include = "tls_certificate,tls_configuration,tls_domain" # str | Include related objects. Optional, comma-separated values. Permitted values: `tls_certificate`, `tls_configuration`, and `tls_domain`.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a TLS activation
        api_response = api_instance.get_tls_activation(tls_activation_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsActivationsApi->get_tls_activation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a TLS activation
        api_response = api_instance.get_tls_activation(tls_activation_id, include=include)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsActivationsApi->get_tls_activation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tls_activation_id** | **str**| Alphanumeric string identifying a TLS activation. |
 **include** | **str**| Include related objects. Optional, comma-separated values. Permitted values: `tls_certificate`, `tls_configuration`, and `tls_domain`.  | [optional]

### Return type

[**TlsActivationResponse**](TlsActivationResponse.md)

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

# **list_tls_activations**
> TlsActivationsResponse list_tls_activations()

List TLS activations

List all TLS activations.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_activations_api
from fastly.model.tls_activations_response import TlsActivationsResponse
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
    api_instance = tls_activations_api.TlsActivationsApi(api_client)
    filter_tls_certificate_id = "filter[tls_certificate.id]_example" # str | Limit the returned activations to a specific certificate. (optional)
    filter_tls_configuration_id = "filter[tls_configuration.id]_example" # str | Limit the returned activations to a specific TLS configuration. (optional)
    filter_tls_domain_id = "filter[tls_domain.id]_example" # str | Limit the returned rules to a specific domain name. (optional)
    include = "tls_certificate,tls_configuration,tls_domain" # str | Include related objects. Optional, comma-separated values. Permitted values: `tls_certificate`, `tls_configuration`, and `tls_domain`.  (optional)
    page_number = 1 # int | Current page. (optional)
    page_size = 20 # int | Number of records per page. (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List TLS activations
        api_response = api_instance.list_tls_activations(filter_tls_certificate_id=filter_tls_certificate_id, filter_tls_configuration_id=filter_tls_configuration_id, filter_tls_domain_id=filter_tls_domain_id, include=include, page_number=page_number, page_size=page_size)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsActivationsApi->list_tls_activations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_tls_certificate_id** | **str**| Limit the returned activations to a specific certificate. | [optional]
 **filter_tls_configuration_id** | **str**| Limit the returned activations to a specific TLS configuration. | [optional]
 **filter_tls_domain_id** | **str**| Limit the returned rules to a specific domain name. | [optional]
 **include** | **str**| Include related objects. Optional, comma-separated values. Permitted values: `tls_certificate`, `tls_configuration`, and `tls_domain`.  | [optional]
 **page_number** | **int**| Current page. | [optional]
 **page_size** | **int**| Number of records per page. | [optional] if omitted the server will use the default value of 20

### Return type

[**TlsActivationsResponse**](TlsActivationsResponse.md)

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

# **update_tls_activation**
> TlsActivationResponse update_tls_activation(tls_activation_id)

Update a certificate

Update the certificate used to terminate TLS traffic for the domain associated with this TLS activation.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_activations_api
from fastly.model.tls_activation import TlsActivation
from fastly.model.tls_activation_response import TlsActivationResponse
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
    api_instance = tls_activations_api.TlsActivationsApi(api_client)
    tls_activation_id = "aCtguUGZzb2W9Euo4moOR" # str | Alphanumeric string identifying a TLS activation.
    tls_activation = TlsActivation(
        data=TlsActivationData(
            type=TypeTlsActivation("tls_activation"),
            relationships=RelationshipsForTlsActivation(),
        ),
    ) # TlsActivation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a certificate
        api_response = api_instance.update_tls_activation(tls_activation_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsActivationsApi->update_tls_activation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a certificate
        api_response = api_instance.update_tls_activation(tls_activation_id, tls_activation=tls_activation)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsActivationsApi->update_tls_activation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tls_activation_id** | **str**| Alphanumeric string identifying a TLS activation. |
 **tls_activation** | [**TlsActivation**](TlsActivation.md)|  | [optional]

### Return type

[**TlsActivationResponse**](TlsActivationResponse.md)

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

