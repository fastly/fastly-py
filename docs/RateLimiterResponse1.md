# RateLimiterResponse1

Custom response to be sent when the rate limit is exceeded. Required if `action` is `response`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code for custom limit enforcement response. | [optional] 
**content_type** | **str** | MIME type for custom limit enforcement response. | [optional] 
**content** | **str** | Response body for custom limit enforcement response. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


