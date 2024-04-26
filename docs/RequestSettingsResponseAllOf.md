# RequestSettingsResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bypass_busy_wait** | **str, none_type** | Disable collapsed forwarding, so you don&#39;t wait for other objects to origin. | [optional] 
**force_miss** | **str, none_type** | Allows you to force a cache miss for the request. Replaces the item in the cache if the content is cacheable. | [optional] 
**force_ssl** | **str** | Forces the request use SSL (redirects a non-SSL to SSL). | [optional] 
**geo_headers** | **str, none_type** | Injects Fastly-Geo-Country, Fastly-Geo-City, and Fastly-Geo-Region into the request headers. | [optional] 
**max_stale_age** | **str, none_type** | How old an object is allowed to be to serve stale-if-error or stale-while-revalidate. | [optional] 
**timer_support** | **str, none_type** | Injects the X-Timer info into the request for viewing origin fetch durations. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


