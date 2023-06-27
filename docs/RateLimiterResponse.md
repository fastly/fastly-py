# RateLimiterResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human readable name for the rate limiting rule. | [optional] 
**uri_dictionary_name** | **str, none_type** | The name of an Edge Dictionary containing URIs as keys. If not defined or `null`, all origin URIs will be rate limited. | [optional] 
**http_methods** | **[str]** | Array of HTTP methods to apply rate limiting to. | [optional] 
**rps_limit** | **int** | Upper limit of requests per second allowed by the rate limiter. | [optional] 
**window_size** | **int** | Number of seconds during which the RPS limit must be exceeded in order to trigger a violation. | [optional] 
**client_key** | **[str]** | Array of VCL variables used to generate a counter key to identify a client. Example variables include `req.http.Fastly-Client-IP`, `req.http.User-Agent`, or a custom header like `req.http.API-Key`. | [optional] 
**penalty_box_duration** | **int** | Length of time in minutes that the rate limiter is in effect after the initial violation is detected. | [optional] 
**action** | **str** | The action to take when a rate limiter violation is detected. | [optional] 
**response** | **{str: (str,)}, none_type** | Custom response to be sent when the rate limit is exceeded. Required if `action` is `response`. | [optional] 
**response_object_name** | **str, none_type** | Name of existing response object. Required if `action` is `response_object`. Note that the rate limiter response is only updated to reflect the response object content when saving the rate limiter configuration. | [optional] 
**logger_type** | **str** | Name of the type of logging endpoint to be used when action is `log_only`. The logging endpoint type is used to determine the appropriate log format to use when emitting log entries. | [optional] 
**feature_revision** | **int** | Revision number of the rate limiting feature implementation. Defaults to the most recent revision. | [optional] 
**service_id** | **str** |  | [optional] [readonly] 
**version** | **int** |  | [optional] [readonly] 
**created_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**deleted_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**id** | **str** | Alphanumeric string identifying the rate limiter. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


