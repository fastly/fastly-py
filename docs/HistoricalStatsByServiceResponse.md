# HistoricalStatsByServiceResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Whether or not we were able to successfully execute the query. | [optional] 
**meta** | [**HistoricalMeta**](HistoricalMeta.md) |  | [optional] 
**msg** | **str, none_type** | If the query was not successful, this will provide a string that explains why. | [optional] 
**data** | [**{str: (HistoricalStatsData,)}**](HistoricalStatsData.md) | Contains the results of the query, organized by *service ID*, into arrays where each element describes one service over a *time span*. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


