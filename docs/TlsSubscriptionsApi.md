# fastly.TlsSubscriptionsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_globalsign_email_challenge**](TlsSubscriptionsApi.md#create_globalsign_email_challenge) | **POST** /tls/subscriptions/{tls_subscription_id}/authorizations/{tls_authorization_id}/globalsign_email_challenges | Creates a GlobalSign email challenge.
[**create_tls_sub**](TlsSubscriptionsApi.md#create_tls_sub) | **POST** /tls/subscriptions | Create a TLS subscription
[**delete_globalsign_email_challenge**](TlsSubscriptionsApi.md#delete_globalsign_email_challenge) | **DELETE** /tls/subscriptions/{tls_subscription_id}/authorizations/{tls_authorization_id}/globalsign_email_challenges/{globalsign_email_challenge_id} | Delete a GlobalSign email challenge
[**delete_tls_sub**](TlsSubscriptionsApi.md#delete_tls_sub) | **DELETE** /tls/subscriptions/{tls_subscription_id} | Delete a TLS subscription
[**get_tls_sub**](TlsSubscriptionsApi.md#get_tls_sub) | **GET** /tls/subscriptions/{tls_subscription_id} | Get a TLS subscription
[**list_tls_subs**](TlsSubscriptionsApi.md#list_tls_subs) | **GET** /tls/subscriptions | List TLS subscriptions
[**patch_tls_sub**](TlsSubscriptionsApi.md#patch_tls_sub) | **PATCH** /tls/subscriptions/{tls_subscription_id} | Update a TLS subscription


# **create_globalsign_email_challenge**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_globalsign_email_challenge(tls_subscription_id, tls_authorization_id)

Creates a GlobalSign email challenge.

Creates an email challenge for a domain on a GlobalSign subscription. An email challenge will generate an email that can be used to validate domain ownership. If this challenge is created, then the domain can only be validated using email for the given subscription. 

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_subscriptions_api
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
    api_instance = tls_subscriptions_api.TlsSubscriptionsApi(api_client)
    tls_subscription_id = "sU3guUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a TLS subscription.
    tls_authorization_id = "aU3guUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a TLS subscription.
    request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Creates a GlobalSign email challenge.
        api_response = api_instance.create_globalsign_email_challenge(tls_subscription_id, tls_authorization_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsSubscriptionsApi->create_globalsign_email_challenge: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a GlobalSign email challenge.
        api_response = api_instance.create_globalsign_email_challenge(tls_subscription_id, tls_authorization_id, request_body=request_body)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsSubscriptionsApi->create_globalsign_email_challenge: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tls_subscription_id** | **str**| Alphanumeric string identifying a TLS subscription. |
 **tls_authorization_id** | **str**| Alphanumeric string identifying a TLS subscription. |
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tls_sub**
> TlsSubscriptionResponse create_tls_sub()

Create a TLS subscription

Create a new TLS subscription. This response includes a list of possible challenges to verify domain ownership.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_subscriptions_api
from fastly.model.tls_subscription_response import TlsSubscriptionResponse
from fastly.model.tls_subscription import TlsSubscription
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
    api_instance = tls_subscriptions_api.TlsSubscriptionsApi(api_client)
    force = True # bool | A flag that allows you to edit and delete a subscription with active domains. Valid to use on PATCH and DELETE actions. As a warning, removing an active domain from a subscription or forcing the deletion of a subscription may result in breaking TLS termination to that domain.  (optional)
    tls_subscription = TlsSubscription(
        data=TlsSubscriptionData(
            type=TypeTlsSubscription("tls_subscription"),
            attributes=TlsSubscriptionDataAttributes(
                certificate_authority="certainly",
            ),
            relationships=RelationshipsForTlsSubscription(),
        ),
    ) # TlsSubscription |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a TLS subscription
        api_response = api_instance.create_tls_sub(force=force, tls_subscription=tls_subscription)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsSubscriptionsApi->create_tls_sub: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **force** | **bool**| A flag that allows you to edit and delete a subscription with active domains. Valid to use on PATCH and DELETE actions. As a warning, removing an active domain from a subscription or forcing the deletion of a subscription may result in breaking TLS termination to that domain.  | [optional]
 **tls_subscription** | [**TlsSubscription**](TlsSubscription.md)|  | [optional]

### Return type

[**TlsSubscriptionResponse**](TlsSubscriptionResponse.md)

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

# **delete_globalsign_email_challenge**
> delete_globalsign_email_challenge(tls_subscription_id, tls_authorization_id, globalsign_email_challenge_id)

Delete a GlobalSign email challenge

Deletes a GlobalSign email challenge. After a GlobalSign email challenge is deleted, the domain can use HTTP and DNS validation methods again.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_subscriptions_api
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
    api_instance = tls_subscriptions_api.TlsSubscriptionsApi(api_client)
    tls_subscription_id = "sU3guUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a TLS subscription.
    tls_authorization_id = "aU3guUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a TLS subscription.
    globalsign_email_challenge_id = "gU3guUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a GlobalSign email challenge.

    # example passing only required values which don't have defaults set
    try:
        # Delete a GlobalSign email challenge
        api_instance.delete_globalsign_email_challenge(tls_subscription_id, tls_authorization_id, globalsign_email_challenge_id)
    except fastly.ApiException as e:
        print("Exception when calling TlsSubscriptionsApi->delete_globalsign_email_challenge: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tls_subscription_id** | **str**| Alphanumeric string identifying a TLS subscription. |
 **tls_authorization_id** | **str**| Alphanumeric string identifying a TLS subscription. |
 **globalsign_email_challenge_id** | **str**| Alphanumeric string identifying a GlobalSign email challenge. |

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

# **delete_tls_sub**
> delete_tls_sub(tls_subscription_id)

Delete a TLS subscription

Destroy a TLS subscription. A subscription cannot be destroyed if there are domains in the TLS enabled state.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_subscriptions_api
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
    api_instance = tls_subscriptions_api.TlsSubscriptionsApi(api_client)
    tls_subscription_id = "sU3guUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a TLS subscription.

    # example passing only required values which don't have defaults set
    try:
        # Delete a TLS subscription
        api_instance.delete_tls_sub(tls_subscription_id)
    except fastly.ApiException as e:
        print("Exception when calling TlsSubscriptionsApi->delete_tls_sub: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tls_subscription_id** | **str**| Alphanumeric string identifying a TLS subscription. |

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

# **get_tls_sub**
> TlsSubscriptionResponse get_tls_sub(tls_subscription_id)

Get a TLS subscription

Show a TLS subscription.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_subscriptions_api
from fastly.model.tls_subscription_response import TlsSubscriptionResponse
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
    api_instance = tls_subscriptions_api.TlsSubscriptionsApi(api_client)
    tls_subscription_id = "sU3guUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a TLS subscription.
    include = "tls_authorizations" # str | Include related objects. Optional, comma-separated values. Permitted values: `tls_authorizations`, `tls_authorizations.globalsign_email_challenge`, `tls_authorizations.self_managed_http_challenge`, and `tls_certificates`.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a TLS subscription
        api_response = api_instance.get_tls_sub(tls_subscription_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsSubscriptionsApi->get_tls_sub: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a TLS subscription
        api_response = api_instance.get_tls_sub(tls_subscription_id, include=include)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsSubscriptionsApi->get_tls_sub: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tls_subscription_id** | **str**| Alphanumeric string identifying a TLS subscription. |
 **include** | **str**| Include related objects. Optional, comma-separated values. Permitted values: `tls_authorizations`, `tls_authorizations.globalsign_email_challenge`, `tls_authorizations.self_managed_http_challenge`, and `tls_certificates`.  | [optional]

### Return type

[**TlsSubscriptionResponse**](TlsSubscriptionResponse.md)

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

# **list_tls_subs**
> TlsSubscriptionsResponse list_tls_subs()

List TLS subscriptions

List all TLS subscriptions.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_subscriptions_api
from fastly.model.tls_subscriptions_response import TlsSubscriptionsResponse
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
    api_instance = tls_subscriptions_api.TlsSubscriptionsApi(api_client)
    filter_state = "filter[state]_example" # str | Limit the returned subscriptions by state. Valid values are `pending`, `processing`, `issued`, `renewing`, and `failed`. Accepts parameters: `not` (e.g., `filter[state][not]=renewing`).  (optional)
    filter_tls_domains_id = "filter[tls_domains.id]_example" # str | Limit the returned subscriptions to those that include the specific domain. (optional)
    filter_has_active_order = True # bool | Limit the returned subscriptions to those that have currently active orders. Permitted values: `true`.  (optional)
    filter_certificate_authority = "filter[certificate_authority]_example" # str | Limit the returned subscriptions to a specific certification authority. Values may include `certainly`, `lets-encrypt`, or `globalsign`.  (optional)
    sort = "-created_at" # str | The order in which to list the results. (optional) if omitted the server will use the default value of "-created_at"
    include = "tls_authorizations" # str | Include related objects. Optional, comma-separated values. Permitted values: `tls_authorizations`, `tls_authorizations.globalsign_email_challenge`, `tls_authorizations.self_managed_http_challenge`, and `tls_certificates`.  (optional)
    page_number = 1 # int | Current page. (optional)
    page_size = 20 # int | Number of records per page. (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List TLS subscriptions
        api_response = api_instance.list_tls_subs(filter_state=filter_state, filter_tls_domains_id=filter_tls_domains_id, filter_has_active_order=filter_has_active_order, filter_certificate_authority=filter_certificate_authority, sort=sort, include=include, page_number=page_number, page_size=page_size)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsSubscriptionsApi->list_tls_subs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_state** | **str**| Limit the returned subscriptions by state. Valid values are `pending`, `processing`, `issued`, `renewing`, and `failed`. Accepts parameters: `not` (e.g., `filter[state][not]&#x3D;renewing`).  | [optional]
 **filter_tls_domains_id** | **str**| Limit the returned subscriptions to those that include the specific domain. | [optional]
 **filter_has_active_order** | **bool**| Limit the returned subscriptions to those that have currently active orders. Permitted values: `true`.  | [optional]
 **filter_certificate_authority** | **str**| Limit the returned subscriptions to a specific certification authority. Values may include `certainly`, `lets-encrypt`, or `globalsign`.  | [optional]
 **sort** | **str**| The order in which to list the results. | [optional] if omitted the server will use the default value of "-created_at"
 **include** | **str**| Include related objects. Optional, comma-separated values. Permitted values: `tls_authorizations`, `tls_authorizations.globalsign_email_challenge`, `tls_authorizations.self_managed_http_challenge`, and `tls_certificates`.  | [optional]
 **page_number** | **int**| Current page. | [optional]
 **page_size** | **int**| Number of records per page. | [optional] if omitted the server will use the default value of 20

### Return type

[**TlsSubscriptionsResponse**](TlsSubscriptionsResponse.md)

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

# **patch_tls_sub**
> TlsSubscriptionResponse patch_tls_sub(tls_subscription_id)

Update a TLS subscription

Change the TLS domains or common name associated with this subscription, update the TLS configuration for this set of domains, or retry a subscription with state `failed` by setting the state to `retry`.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_subscriptions_api
from fastly.model.tls_subscription_response import TlsSubscriptionResponse
from fastly.model.tls_subscription import TlsSubscription
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
    api_instance = tls_subscriptions_api.TlsSubscriptionsApi(api_client)
    tls_subscription_id = "sU3guUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a TLS subscription.
    force = True # bool | A flag that allows you to edit and delete a subscription with active domains. Valid to use on PATCH and DELETE actions. As a warning, removing an active domain from a subscription or forcing the deletion of a subscription may result in breaking TLS termination to that domain.  (optional)
    tls_subscription = TlsSubscription(
        data=TlsSubscriptionData(
            type=TypeTlsSubscription("tls_subscription"),
            attributes=TlsSubscriptionDataAttributes(
                certificate_authority="certainly",
            ),
            relationships=RelationshipsForTlsSubscription(),
        ),
    ) # TlsSubscription |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a TLS subscription
        api_response = api_instance.patch_tls_sub(tls_subscription_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsSubscriptionsApi->patch_tls_sub: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a TLS subscription
        api_response = api_instance.patch_tls_sub(tls_subscription_id, force=force, tls_subscription=tls_subscription)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsSubscriptionsApi->patch_tls_sub: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tls_subscription_id** | **str**| Alphanumeric string identifying a TLS subscription. |
 **force** | **bool**| A flag that allows you to edit and delete a subscription with active domains. Valid to use on PATCH and DELETE actions. As a warning, removing an active domain from a subscription or forcing the deletion of a subscription may result in breaking TLS termination to that domain.  | [optional]
 **tls_subscription** | [**TlsSubscription**](TlsSubscription.md)|  | [optional]

### Return type

[**TlsSubscriptionResponse**](TlsSubscriptionResponse.md)

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

