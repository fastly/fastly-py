# VersionDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backends** | [**[BackendResponse]**](BackendResponse.md) | List of backends associated to this service. | [optional] 
**cache_settings** | [**[CacheSettingResponse]**](CacheSettingResponse.md) | List of cache settings associated to this service. | [optional] 
**conditions** | [**[ConditionResponse]**](ConditionResponse.md) | List of conditions associated to this service. | [optional] 
**directors** | [**[Director]**](Director.md) | List of directors associated to this service. | [optional] 
**domains** | [**[DomainResponse]**](DomainResponse.md) | List of domains associated to this service. | [optional] 
**gzips** | [**[GzipResponse]**](GzipResponse.md) | List of gzip rules associated to this service. | [optional] 
**headers** | [**[HeaderResponse]**](HeaderResponse.md) | List of headers associated to this service. | [optional] 
**healthchecks** | [**[HealthcheckResponse]**](HealthcheckResponse.md) | List of healthchecks associated to this service. | [optional] 
**request_settings** | [**[RequestSettingsResponse]**](RequestSettingsResponse.md) | List of request settings for this service. | [optional] 
**response_objects** | [**[ResponseObjectResponse]**](ResponseObjectResponse.md) | List of response objects for this service. | [optional] 
**settings** | [**VersionDetailSettings**](VersionDetailSettings.md) |  | [optional] 
**snippets** | [**[SchemasSnippetResponse]**](SchemasSnippetResponse.md) | List of VCL snippets for this service. | [optional] 
**vcls** | [**[SchemasVclResponse]**](SchemasVclResponse.md) | List of VCL files for this service. | [optional] 
**wordpress** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type]** | A list of Wordpress rules with this service. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


