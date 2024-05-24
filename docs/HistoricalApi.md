# fastly.HistoricalApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_hist_stats**](HistoricalApi.md#get_hist_stats) | **GET** /stats | Get historical stats
[**get_hist_stats_aggregated**](HistoricalApi.md#get_hist_stats_aggregated) | **GET** /stats/aggregate | Get aggregated historical stats
[**get_hist_stats_field**](HistoricalApi.md#get_hist_stats_field) | **GET** /stats/field/{field} | Get historical stats for a single field
[**get_hist_stats_service**](HistoricalApi.md#get_hist_stats_service) | **GET** /stats/service/{service_id} | Get historical stats for a single service
[**get_hist_stats_service_field**](HistoricalApi.md#get_hist_stats_service_field) | **GET** /stats/service/{service_id}/field/{field} | Get historical stats for a single service/field combination
[**get_regions**](HistoricalApi.md#get_regions) | **GET** /stats/regions | Get region codes
[**get_usage**](HistoricalApi.md#get_usage) | **GET** /stats/usage | Get usage statistics
[**get_usage_month**](HistoricalApi.md#get_usage_month) | **GET** /stats/usage_by_month | Get month-to-date usage statistics
[**get_usage_service**](HistoricalApi.md#get_usage_service) | **GET** /stats/usage_by_service | Get usage statistics per service


# **get_hist_stats**
> HistoricalStatsByServiceResponse get_hist_stats()

Get historical stats

Fetches historical stats for each of your Fastly services and groups the results by service ID.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import historical_api
from fastly.model.historical_stats_by_service_response import HistoricalStatsByServiceResponse
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
    api_instance = historical_api.HistoricalApi(api_client)
    _from = "2020-04-09T18:14:30Z" # str | Timestamp that defines the start of the window for which to fetch statistics, including the timestamp itself. Accepts Unix timestamps, or any form of input parsable by the [Chronic Ruby library](https://github.com/mojombo/chronic), such as 'yesterday', or 'two weeks ago'. Default varies based on the value of `by`.  (optional)
    to = "2020-04-09T18:14:30Z" # str | Timestamp that defines the end of the window for which to fetch statistics. Accepts the same formats as `from`.  (optional) if omitted the server will use the default value of "now"
    by = "day" # str | Duration of sample windows. One of:   * `hour` - Group data by hour.   * `minute` - Group data by minute.   * `day` - Group data by day.  (optional) if omitted the server will use the default value of "day"
    region = "usa" # str | Limit query to a specific geographic region. One of:   * `usa` - North America.   * `europe` - Europe.   * `anzac` - Australia and New Zealand.   * `asia` - Asia.   * `asia_india` - India.   * `asia_southkorea` - South Korea.   * `africa_std` - Africa.   * `southamerica_std` - South America.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get historical stats
        api_response = api_instance.get_hist_stats(_from=_from, to=to, by=by, region=region)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling HistoricalApi->get_hist_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**| Timestamp that defines the start of the window for which to fetch statistics, including the timestamp itself. Accepts Unix timestamps, or any form of input parsable by the [Chronic Ruby library](https://github.com/mojombo/chronic), such as &#39;yesterday&#39;, or &#39;two weeks ago&#39;. Default varies based on the value of `by`.  | [optional]
 **to** | **str**| Timestamp that defines the end of the window for which to fetch statistics. Accepts the same formats as `from`.  | [optional] if omitted the server will use the default value of "now"
 **by** | **str**| Duration of sample windows. One of:   * `hour` - Group data by hour.   * `minute` - Group data by minute.   * `day` - Group data by day.  | [optional] if omitted the server will use the default value of "day"
 **region** | **str**| Limit query to a specific geographic region. One of:   * `usa` - North America.   * `europe` - Europe.   * `anzac` - Australia and New Zealand.   * `asia` - Asia.   * `asia_india` - India.   * `asia_southkorea` - South Korea.   * `africa_std` - Africa.   * `southamerica_std` - South America.  | [optional]

### Return type

[**HistoricalStatsByServiceResponse**](HistoricalStatsByServiceResponse.md)

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

# **get_hist_stats_aggregated**
> HistoricalStatsAggregatedResponse get_hist_stats_aggregated()

Get aggregated historical stats

Fetches historical stats information aggregated across all of your Fastly services.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import historical_api
from fastly.model.historical_stats_aggregated_response import HistoricalStatsAggregatedResponse
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
    api_instance = historical_api.HistoricalApi(api_client)
    _from = "2020-04-09T18:14:30Z" # str | Timestamp that defines the start of the window for which to fetch statistics, including the timestamp itself. Accepts Unix timestamps, or any form of input parsable by the [Chronic Ruby library](https://github.com/mojombo/chronic), such as 'yesterday', or 'two weeks ago'. Default varies based on the value of `by`.  (optional)
    to = "2020-04-09T18:14:30Z" # str | Timestamp that defines the end of the window for which to fetch statistics. Accepts the same formats as `from`.  (optional) if omitted the server will use the default value of "now"
    by = "day" # str | Duration of sample windows. One of:   * `hour` - Group data by hour.   * `minute` - Group data by minute.   * `day` - Group data by day.  (optional) if omitted the server will use the default value of "day"
    region = "usa" # str | Limit query to a specific geographic region. One of:   * `usa` - North America.   * `europe` - Europe.   * `anzac` - Australia and New Zealand.   * `asia` - Asia.   * `asia_india` - India.   * `asia_southkorea` - South Korea.   * `africa_std` - Africa.   * `southamerica_std` - South America.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get aggregated historical stats
        api_response = api_instance.get_hist_stats_aggregated(_from=_from, to=to, by=by, region=region)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling HistoricalApi->get_hist_stats_aggregated: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**| Timestamp that defines the start of the window for which to fetch statistics, including the timestamp itself. Accepts Unix timestamps, or any form of input parsable by the [Chronic Ruby library](https://github.com/mojombo/chronic), such as &#39;yesterday&#39;, or &#39;two weeks ago&#39;. Default varies based on the value of `by`.  | [optional]
 **to** | **str**| Timestamp that defines the end of the window for which to fetch statistics. Accepts the same formats as `from`.  | [optional] if omitted the server will use the default value of "now"
 **by** | **str**| Duration of sample windows. One of:   * `hour` - Group data by hour.   * `minute` - Group data by minute.   * `day` - Group data by day.  | [optional] if omitted the server will use the default value of "day"
 **region** | **str**| Limit query to a specific geographic region. One of:   * `usa` - North America.   * `europe` - Europe.   * `anzac` - Australia and New Zealand.   * `asia` - Asia.   * `asia_india` - India.   * `asia_southkorea` - South Korea.   * `africa_std` - Africa.   * `southamerica_std` - South America.  | [optional]

### Return type

[**HistoricalStatsAggregatedResponse**](HistoricalStatsAggregatedResponse.md)

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

# **get_hist_stats_field**
> HistoricalStatsByServiceResponse get_hist_stats_field(field)

Get historical stats for a single field

Fetches the specified field from the historical stats for each of your services and groups the results by service ID.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import historical_api
from fastly.model.historical_stats_by_service_response import HistoricalStatsByServiceResponse
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
    api_instance = historical_api.HistoricalApi(api_client)
    field = "hit_ratio" # str | Name of the stats field.
    _from = "2020-04-09T18:14:30Z" # str | Timestamp that defines the start of the window for which to fetch statistics, including the timestamp itself. Accepts Unix timestamps, or any form of input parsable by the [Chronic Ruby library](https://github.com/mojombo/chronic), such as 'yesterday', or 'two weeks ago'. Default varies based on the value of `by`.  (optional)
    to = "2020-04-09T18:14:30Z" # str | Timestamp that defines the end of the window for which to fetch statistics. Accepts the same formats as `from`.  (optional) if omitted the server will use the default value of "now"
    by = "day" # str | Duration of sample windows. One of:   * `hour` - Group data by hour.   * `minute` - Group data by minute.   * `day` - Group data by day.  (optional) if omitted the server will use the default value of "day"
    region = "usa" # str | Limit query to a specific geographic region. One of:   * `usa` - North America.   * `europe` - Europe.   * `anzac` - Australia and New Zealand.   * `asia` - Asia.   * `asia_india` - India.   * `asia_southkorea` - South Korea.   * `africa_std` - Africa.   * `southamerica_std` - South America.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get historical stats for a single field
        api_response = api_instance.get_hist_stats_field(field)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling HistoricalApi->get_hist_stats_field: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get historical stats for a single field
        api_response = api_instance.get_hist_stats_field(field, _from=_from, to=to, by=by, region=region)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling HistoricalApi->get_hist_stats_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **str**| Name of the stats field. |
 **_from** | **str**| Timestamp that defines the start of the window for which to fetch statistics, including the timestamp itself. Accepts Unix timestamps, or any form of input parsable by the [Chronic Ruby library](https://github.com/mojombo/chronic), such as &#39;yesterday&#39;, or &#39;two weeks ago&#39;. Default varies based on the value of `by`.  | [optional]
 **to** | **str**| Timestamp that defines the end of the window for which to fetch statistics. Accepts the same formats as `from`.  | [optional] if omitted the server will use the default value of "now"
 **by** | **str**| Duration of sample windows. One of:   * `hour` - Group data by hour.   * `minute` - Group data by minute.   * `day` - Group data by day.  | [optional] if omitted the server will use the default value of "day"
 **region** | **str**| Limit query to a specific geographic region. One of:   * `usa` - North America.   * `europe` - Europe.   * `anzac` - Australia and New Zealand.   * `asia` - Asia.   * `asia_india` - India.   * `asia_southkorea` - South Korea.   * `africa_std` - Africa.   * `southamerica_std` - South America.  | [optional]

### Return type

[**HistoricalStatsByServiceResponse**](HistoricalStatsByServiceResponse.md)

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

# **get_hist_stats_service**
> HistoricalStatsAggregatedResponse get_hist_stats_service(service_id)

Get historical stats for a single service

Fetches historical stats for a given service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import historical_api
from fastly.model.historical_stats_aggregated_response import HistoricalStatsAggregatedResponse
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
    api_instance = historical_api.HistoricalApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    _from = "2020-04-09T18:14:30Z" # str | Timestamp that defines the start of the window for which to fetch statistics, including the timestamp itself. Accepts Unix timestamps, or any form of input parsable by the [Chronic Ruby library](https://github.com/mojombo/chronic), such as 'yesterday', or 'two weeks ago'. Default varies based on the value of `by`.  (optional)
    to = "2020-04-09T18:14:30Z" # str | Timestamp that defines the end of the window for which to fetch statistics. Accepts the same formats as `from`.  (optional) if omitted the server will use the default value of "now"
    by = "day" # str | Duration of sample windows. One of:   * `hour` - Group data by hour.   * `minute` - Group data by minute.   * `day` - Group data by day.  (optional) if omitted the server will use the default value of "day"
    region = "usa" # str | Limit query to a specific geographic region. One of:   * `usa` - North America.   * `europe` - Europe.   * `anzac` - Australia and New Zealand.   * `asia` - Asia.   * `asia_india` - India.   * `asia_southkorea` - South Korea.   * `africa_std` - Africa.   * `southamerica_std` - South America.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get historical stats for a single service
        api_response = api_instance.get_hist_stats_service(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling HistoricalApi->get_hist_stats_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get historical stats for a single service
        api_response = api_instance.get_hist_stats_service(service_id, _from=_from, to=to, by=by, region=region)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling HistoricalApi->get_hist_stats_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **_from** | **str**| Timestamp that defines the start of the window for which to fetch statistics, including the timestamp itself. Accepts Unix timestamps, or any form of input parsable by the [Chronic Ruby library](https://github.com/mojombo/chronic), such as &#39;yesterday&#39;, or &#39;two weeks ago&#39;. Default varies based on the value of `by`.  | [optional]
 **to** | **str**| Timestamp that defines the end of the window for which to fetch statistics. Accepts the same formats as `from`.  | [optional] if omitted the server will use the default value of "now"
 **by** | **str**| Duration of sample windows. One of:   * `hour` - Group data by hour.   * `minute` - Group data by minute.   * `day` - Group data by day.  | [optional] if omitted the server will use the default value of "day"
 **region** | **str**| Limit query to a specific geographic region. One of:   * `usa` - North America.   * `europe` - Europe.   * `anzac` - Australia and New Zealand.   * `asia` - Asia.   * `asia_india` - India.   * `asia_southkorea` - South Korea.   * `africa_std` - Africa.   * `southamerica_std` - South America.  | [optional]

### Return type

[**HistoricalStatsAggregatedResponse**](HistoricalStatsAggregatedResponse.md)

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

# **get_hist_stats_service_field**
> HistoricalStatsAggregatedResponse get_hist_stats_service_field(service_id, field)

Get historical stats for a single service/field combination

Fetches the specified field from the historical stats for a given service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import historical_api
from fastly.model.historical_stats_aggregated_response import HistoricalStatsAggregatedResponse
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
    api_instance = historical_api.HistoricalApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    field = "hit_ratio" # str | Name of the stats field.
    _from = "2020-04-09T18:14:30Z" # str | Timestamp that defines the start of the window for which to fetch statistics, including the timestamp itself. Accepts Unix timestamps, or any form of input parsable by the [Chronic Ruby library](https://github.com/mojombo/chronic), such as 'yesterday', or 'two weeks ago'. Default varies based on the value of `by`.  (optional)
    to = "2020-04-09T18:14:30Z" # str | Timestamp that defines the end of the window for which to fetch statistics. Accepts the same formats as `from`.  (optional) if omitted the server will use the default value of "now"
    by = "day" # str | Duration of sample windows. One of:   * `hour` - Group data by hour.   * `minute` - Group data by minute.   * `day` - Group data by day.  (optional) if omitted the server will use the default value of "day"
    region = "usa" # str | Limit query to a specific geographic region. One of:   * `usa` - North America.   * `europe` - Europe.   * `anzac` - Australia and New Zealand.   * `asia` - Asia.   * `asia_india` - India.   * `asia_southkorea` - South Korea.   * `africa_std` - Africa.   * `southamerica_std` - South America.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get historical stats for a single service/field combination
        api_response = api_instance.get_hist_stats_service_field(service_id, field)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling HistoricalApi->get_hist_stats_service_field: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get historical stats for a single service/field combination
        api_response = api_instance.get_hist_stats_service_field(service_id, field, _from=_from, to=to, by=by, region=region)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling HistoricalApi->get_hist_stats_service_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **field** | **str**| Name of the stats field. |
 **_from** | **str**| Timestamp that defines the start of the window for which to fetch statistics, including the timestamp itself. Accepts Unix timestamps, or any form of input parsable by the [Chronic Ruby library](https://github.com/mojombo/chronic), such as &#39;yesterday&#39;, or &#39;two weeks ago&#39;. Default varies based on the value of `by`.  | [optional]
 **to** | **str**| Timestamp that defines the end of the window for which to fetch statistics. Accepts the same formats as `from`.  | [optional] if omitted the server will use the default value of "now"
 **by** | **str**| Duration of sample windows. One of:   * `hour` - Group data by hour.   * `minute` - Group data by minute.   * `day` - Group data by day.  | [optional] if omitted the server will use the default value of "day"
 **region** | **str**| Limit query to a specific geographic region. One of:   * `usa` - North America.   * `europe` - Europe.   * `anzac` - Australia and New Zealand.   * `asia` - Asia.   * `asia_india` - India.   * `asia_southkorea` - South Korea.   * `africa_std` - Africa.   * `southamerica_std` - South America.  | [optional]

### Return type

[**HistoricalStatsAggregatedResponse**](HistoricalStatsAggregatedResponse.md)

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

# **get_regions**
> HistoricalRegionsResponse get_regions()

Get region codes

Fetches the list of codes for regions that are covered by the Fastly CDN service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import historical_api
from fastly.model.historical_regions_response import HistoricalRegionsResponse
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
    api_instance = historical_api.HistoricalApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get region codes
        api_response = api_instance.get_regions()
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling HistoricalApi->get_regions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**HistoricalRegionsResponse**](HistoricalRegionsResponse.md)

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

# **get_usage**
> HistoricalUsageAggregatedResponse get_usage()

Get usage statistics

Returns usage information aggregated across all Fastly services and grouped by region. To aggregate across all Fastly services by time period, see [`/stats/aggregate`](#get-hist-stats-aggregated).

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import historical_api
from fastly.model.historical_usage_aggregated_response import HistoricalUsageAggregatedResponse
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
    api_instance = historical_api.HistoricalApi(api_client)
    _from = "2020-04-09T18:14:30Z" # str | Timestamp that defines the start of the window for which to fetch statistics, including the timestamp itself. Accepts Unix timestamps, or any form of input parsable by the [Chronic Ruby library](https://github.com/mojombo/chronic), such as 'yesterday', or 'two weeks ago'. Default varies based on the value of `by`.  (optional)
    to = "2020-04-09T18:14:30Z" # str | Timestamp that defines the end of the window for which to fetch statistics. Accepts the same formats as `from`.  (optional) if omitted the server will use the default value of "now"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get usage statistics
        api_response = api_instance.get_usage(_from=_from, to=to)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling HistoricalApi->get_usage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**| Timestamp that defines the start of the window for which to fetch statistics, including the timestamp itself. Accepts Unix timestamps, or any form of input parsable by the [Chronic Ruby library](https://github.com/mojombo/chronic), such as &#39;yesterday&#39;, or &#39;two weeks ago&#39;. Default varies based on the value of `by`.  | [optional]
 **to** | **str**| Timestamp that defines the end of the window for which to fetch statistics. Accepts the same formats as `from`.  | [optional] if omitted the server will use the default value of "now"

### Return type

[**HistoricalUsageAggregatedResponse**](HistoricalUsageAggregatedResponse.md)

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

# **get_usage_month**
> HistoricalUsageMonthResponse get_usage_month()

Get month-to-date usage statistics

Returns month-to-date usage details for a given month and year. Usage details are aggregated by service and across all Fastly services, and then grouped by region. This endpoint does not use the `from` or `to` fields for selecting the date for which data is requested. Instead, it uses `month` and `year` integer fields. Both fields are optional and default to the current month and year respectively. When set, an optional `billable_units` field will convert bandwidth to GB and divide requests by 10,000.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import historical_api
from fastly.model.historical_usage_month_response import HistoricalUsageMonthResponse
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
    api_instance = historical_api.HistoricalApi(api_client)
    year = "2020" # str | 4-digit year. (optional)
    month = "05" # str | 2-digit month. (optional)
    billable_units = True # bool | If `true`, return results as billable units. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get month-to-date usage statistics
        api_response = api_instance.get_usage_month(year=year, month=month, billable_units=billable_units)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling HistoricalApi->get_usage_month: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **str**| 4-digit year. | [optional]
 **month** | **str**| 2-digit month. | [optional]
 **billable_units** | **bool**| If `true`, return results as billable units. | [optional]

### Return type

[**HistoricalUsageMonthResponse**](HistoricalUsageMonthResponse.md)

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

# **get_usage_service**
> HistoricalUsageServiceResponse get_usage_service()

Get usage statistics per service

Returns usage information aggregated by service and grouped by service and region. For service stats by time period, see [`/stats`](#get-hist-stats) and [`/stats/field/:field`](#get-hist-stats-field).

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import historical_api
from fastly.model.historical_usage_service_response import HistoricalUsageServiceResponse
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
    api_instance = historical_api.HistoricalApi(api_client)
    _from = "2020-04-09T18:14:30Z" # str | Timestamp that defines the start of the window for which to fetch statistics, including the timestamp itself. Accepts Unix timestamps, or any form of input parsable by the [Chronic Ruby library](https://github.com/mojombo/chronic), such as 'yesterday', or 'two weeks ago'. Default varies based on the value of `by`.  (optional)
    to = "2020-04-09T18:14:30Z" # str | Timestamp that defines the end of the window for which to fetch statistics. Accepts the same formats as `from`.  (optional) if omitted the server will use the default value of "now"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get usage statistics per service
        api_response = api_instance.get_usage_service(_from=_from, to=to)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling HistoricalApi->get_usage_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**| Timestamp that defines the start of the window for which to fetch statistics, including the timestamp itself. Accepts Unix timestamps, or any form of input parsable by the [Chronic Ruby library](https://github.com/mojombo/chronic), such as &#39;yesterday&#39;, or &#39;two weeks ago&#39;. Default varies based on the value of `by`.  | [optional]
 **to** | **str**| Timestamp that defines the end of the window for which to fetch statistics. Accepts the same formats as `from`.  | [optional] if omitted the server will use the default value of "now"

### Return type

[**HistoricalUsageServiceResponse**](HistoricalUsageServiceResponse.md)

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

