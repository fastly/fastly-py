# fastly.EventsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event**](EventsApi.md#get_event) | **GET** /events/{event_id} | Get an event
[**list_events**](EventsApi.md#list_events) | **GET** /events | List events


# **get_event**
> EventResponse get_event(event_id)

Get an event

Get a specific event.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import events_api
from fastly.model.event_response import EventResponse
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
    api_instance = events_api.EventsApi(api_client)
    event_id = "1PTzLK8g1NRKMGu5kUb8SC" # str | Alphanumeric string identifying an event.

    # example passing only required values which don't have defaults set
    try:
        # Get an event
        api_response = api_instance.get_event(event_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling EventsApi->get_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**| Alphanumeric string identifying an event. |

### Return type

[**EventResponse**](EventResponse.md)

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

# **list_events**
> EventsResponse list_events()

List events

List all events for a particular customer. Events can be filtered by user, customer and event type. Events can be sorted by date.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import events_api
from fastly.model.events_response import EventsResponse
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
    api_instance = events_api.EventsApi(api_client)
    filter_customer_id = "x4xCwxxJxGCx123Rx5xTx" # str | Limit the results returned to a specific customer. (optional)
    filter_event_type = "filter[event_type]_example" # str | Limit the returned events to a specific `event_type`. (optional)
    filter_service_id = "filter[service_id]_example" # str | Limit the results returned to a specific service. (optional)
    filter_user_id = "filter[user_id]_example" # str | Limit the results returned to a specific user. (optional)
    filter_token_id = "filter[token_id]_example" # str | Limit the returned events to a specific token. (optional)
    filter_created_at = "filter[created_at]_example" # str | Limit the returned events to a specific time frame. Accepts sub-parameters: lt, lte, gt, gte (e.g., filter[created_at][gt]=2022-01-12).  (optional)
    filter_created_at_lte = "filter[created_at][lte]_example" # str | Return events on and before a date and time in ISO 8601 format.  (optional)
    filter_created_at_lt = "filter[created_at][lt]_example" # str | Return events before a date and time in ISO 8601 format.  (optional)
    filter_created_at_gte = "filter[created_at][gte]_example" # str | Return events on and after a date and time in ISO 8601 format.  (optional)
    filter_created_at_gt = "filter[created_at][gt]_example" # str | Return events after a date and time in ISO 8601 format.  (optional)
    page_number = 1 # int | Current page. (optional)
    page_size = 20 # int | Number of records per page. (optional) if omitted the server will use the default value of 20
    sort = "created_at" # str | The order in which to list the results by creation date. (optional) if omitted the server will use the default value of "created_at"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List events
        api_response = api_instance.list_events(filter_customer_id=filter_customer_id, filter_event_type=filter_event_type, filter_service_id=filter_service_id, filter_user_id=filter_user_id, filter_token_id=filter_token_id, filter_created_at=filter_created_at, filter_created_at_lte=filter_created_at_lte, filter_created_at_lt=filter_created_at_lt, filter_created_at_gte=filter_created_at_gte, filter_created_at_gt=filter_created_at_gt, page_number=page_number, page_size=page_size, sort=sort)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling EventsApi->list_events: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_customer_id** | **str**| Limit the results returned to a specific customer. | [optional]
 **filter_event_type** | **str**| Limit the returned events to a specific `event_type`. | [optional]
 **filter_service_id** | **str**| Limit the results returned to a specific service. | [optional]
 **filter_user_id** | **str**| Limit the results returned to a specific user. | [optional]
 **filter_token_id** | **str**| Limit the returned events to a specific token. | [optional]
 **filter_created_at** | **str**| Limit the returned events to a specific time frame. Accepts sub-parameters: lt, lte, gt, gte (e.g., filter[created_at][gt]&#x3D;2022-01-12).  | [optional]
 **filter_created_at_lte** | **str**| Return events on and before a date and time in ISO 8601 format.  | [optional]
 **filter_created_at_lt** | **str**| Return events before a date and time in ISO 8601 format.  | [optional]
 **filter_created_at_gte** | **str**| Return events on and after a date and time in ISO 8601 format.  | [optional]
 **filter_created_at_gt** | **str**| Return events after a date and time in ISO 8601 format.  | [optional]
 **page_number** | **int**| Current page. | [optional]
 **page_size** | **int**| Number of records per page. | [optional] if omitted the server will use the default value of 20
 **sort** | **str**| The order in which to list the results by creation date. | [optional] if omitted the server will use the default value of "created_at"

### Return type

[**EventsResponse**](EventsResponse.md)

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

