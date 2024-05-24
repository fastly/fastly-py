# fastly.PublishApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**publish**](PublishApi.md#publish) | **POST** /service/{service_id}/publish/ | Send messages to Fanout subscribers


# **publish**
> str publish(service_id)

Send messages to Fanout subscribers

Send one or more messages to [Fanout](https://www.fastly.com/documentation/learning/concepts/real-time-messaging/fanout) subscribers. Each message specifies a channel, and Fanout will deliver the message to all subscribers of its channel. > **IMPORTANT:** For compatibility with GRIP, this endpoint requires a trailing slash, and the API token may be provided in the `Authorization` header (instead of the `Fastly-Key` header) using the `Bearer` scheme. 

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import publish_api
from fastly.model.publish_request import PublishRequest
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
    api_instance = publish_api.PublishApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    publish_request = PublishRequest(
        items=[
            PublishItem(
                channel="channel_example",
                id="id_example",
                prev_id="prev_id_example",
                formats=PublishItemFormats(
                    http_response=HttpResponseFormat(
                        code=200,
                        reason="reason_example",
                        headers={
                            "key": "key_example",
                        },
                        body="body_example",
                        body_bin="body_bin_example",
                    ),
                    http_stream=HttpStreamFormat(
                        content="content_example",
                        content_bin="content_bin_example",
                    ),
                    ws_message=WsMessageFormat(
                        content="content_example",
                        content_bin="content_bin_example",
                    ),
                ),
            ),
        ],
    ) # PublishRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send messages to Fanout subscribers
        api_response = api_instance.publish(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling PublishApi->publish: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send messages to Fanout subscribers
        api_response = api_instance.publish(service_id, publish_request=publish_request)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling PublishApi->publish: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **publish_request** | [**PublishRequest**](PublishRequest.md)|  | [optional]

### Return type

**str**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

