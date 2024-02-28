# DirectorResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backends** | [**[Backend]**](Backend.md) | List of backends associated to a director. | [optional] 
**capacity** | **int** | Unused. | [optional] 
**comment** | **str, none_type** | A freeform descriptive note. | [optional] 
**name** | **str** | Name for the Director. | [optional] 
**quorum** | **int** | The percentage of capacity that needs to be up for a director to be considered up. `0` to `100`. | [optional]  if omitted the server will use the default value of 75
**shield** | **str, none_type** | Selected POP to serve as a shield for the backends. Defaults to `null` meaning no origin shielding if not set. Refer to the [POPs API endpoint](https://www.fastly.com/documentation/reference/api/utils/pops/) to get a list of available POPs used for shielding. | [optional]  if omitted the server will use the default value of "null"
**type** | **int** | What type of load balance group to use. | [optional]  if omitted the server will use the default value of 1
**retries** | **int** | How many backends to search if it fails. | [optional]  if omitted the server will use the default value of 5
**service_id** | **str** |  | [optional] [readonly] 
**version** | **int** |  | [optional] [readonly] 
**created_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**deleted_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**updated_at** | **datetime, none_type** | Date and time in ISO 8601 format. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


