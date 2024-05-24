# fastly.StarApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_star**](StarApi.md#create_service_star) | **POST** /stars | Create a star
[**delete_service_star**](StarApi.md#delete_service_star) | **DELETE** /stars/{star_id} | Delete a star
[**get_service_star**](StarApi.md#get_service_star) | **GET** /stars/{star_id} | Get a star
[**list_service_stars**](StarApi.md#list_service_stars) | **GET** /stars | List stars


# **create_service_star**
> StarResponse create_service_star()

Create a star

Create star.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import star_api
from fastly.model.star import Star
from fastly.model.star_response import StarResponse
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
    api_instance = star_api.StarApi(api_client)
    star = Star(
        data=StarData(
            type=TypeStar("star"),
            relationships=RelationshipsForStar(),
        ),
    ) # Star |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a star
        api_response = api_instance.create_service_star(star=star)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling StarApi->create_service_star: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **star** | [**Star**](Star.md)|  | [optional]

### Return type

[**StarResponse**](StarResponse.md)

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

# **delete_service_star**
> delete_service_star(star_id)

Delete a star

Delete star.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import star_api
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
    api_instance = star_api.StarApi(api_client)
    star_id = "3krg2uUGZzb2W9Euo4moOY" # str | Alphanumeric string identifying a star.

    # example passing only required values which don't have defaults set
    try:
        # Delete a star
        api_instance.delete_service_star(star_id)
    except fastly.ApiException as e:
        print("Exception when calling StarApi->delete_service_star: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **star_id** | **str**| Alphanumeric string identifying a star. |

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

# **get_service_star**
> StarResponse get_service_star(star_id)

Get a star

Show star.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import star_api
from fastly.model.star_response import StarResponse
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
    api_instance = star_api.StarApi(api_client)
    star_id = "3krg2uUGZzb2W9Euo4moOY" # str | Alphanumeric string identifying a star.

    # example passing only required values which don't have defaults set
    try:
        # Get a star
        api_response = api_instance.get_service_star(star_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling StarApi->get_service_star: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **star_id** | **str**| Alphanumeric string identifying a star. |

### Return type

[**StarResponse**](StarResponse.md)

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

# **list_service_stars**
> bool, date, datetime, dict, float, int, list, str, none_type list_service_stars()

List stars

List stars.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import star_api
from fastly.model.pagination import Pagination
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
    api_instance = star_api.StarApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List stars
        api_response = api_instance.list_service_stars()
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling StarApi->list_service_stars: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

