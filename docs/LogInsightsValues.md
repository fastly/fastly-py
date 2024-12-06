# LogInsightsValues


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache_hit_ratio** | **float** | The cache hit ratio for the URL specified in the dimension. | [optional] 
**region** | **str** | The client&#39;s country subdivision code as defined by ISO 3166-2. | [optional] 
**region_chr** | **float** | The cache hit ratio for the region. | [optional] 
**region_error_rate** | **float** | The error rate for the region. | [optional] 
**url** | **str** | The HTTP request path. | [optional] 
**rate_per_status** | **float** | The URL accounts for this percentage of the status code in this dimension. | [optional] 
**rate_per_url** | **float** | The rate at which the reason in this dimension occurs among responses to this URL with a 503 status code. | [optional] 
**_503_rate_per_url** | **float** | The rate at which 503 status codes are returned for this URL. | [optional] 
**browser_version** | **str** | The version of the client&#39;s browser. | [optional] 
**rate** | **float** | The percentage of requests matching the value in the current dimension. | [optional] 
**average_bandwidth_bytes** | **float** | The average bandwidth in bytes for responses to requests to the URL in the current dimension. | [optional] 
**bandwidth_percentage** | **float** | The total bandwidth percentage for all responses to requests to the URL in the current dimension. | [optional] 
**average_response_time** | **float** | The average time in seconds to respond to requests to the URL in the current dimension. | [optional] 
**p95_response_time** | **float** | The P95 time in seconds to respond to requests to the URL in the current dimension. | [optional] 
**response_time_percentage** | **float** | The total percentage of time to respond to all requests to the URL in the current dimension. | [optional] 
**miss_rate** | **float** | The miss rate for requests to the URL in the current dimension. | [optional] 
**request_percentage** | **float** | The percentage of all requests made to the URL in the current dimension. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


