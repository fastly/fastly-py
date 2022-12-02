# BillingTotal

Complete summary of the billing information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandwidth** | **float** | The total amount of bandwidth used this month (See bandwidth_units for measurement). | [optional] 
**bandwidth_cost** | **float** | The cost of the bandwidth used this month in USD. | [optional] 
**bandwidth_units** | **str, none_type** | Bandwidth measurement units based on billing plan. | [optional] 
**cost** | **float** | The final amount to be paid. | [optional] 
**cost_before_discount** | **float** | Total incurred cost plus extras cost. | [optional] 
**discount** | **float** | Calculated discount rate. | [optional] 
**extras** | [**[BillingTotalExtras]**](BillingTotalExtras.md) | A list of any extras for this invoice. | [optional] 
**extras_cost** | **float** | Total cost of all extras. | [optional] 
**incurred_cost** | **float** | The total cost of bandwidth and requests used this month. | [optional] 
**overage** | **float** | How much over the plan minimum has been incurred. | [optional] 
**plan_code** | **str** | The short code the plan this invoice was generated under. | [optional] 
**plan_minimum** | **float** | The minimum cost of this plan. | [optional] 
**plan_name** | **str** | The name of the plan this invoice was generated under. | [optional] 
**requests** | **float** | The total number of requests used this month. | [optional] 
**requests_cost** | **float** | The cost of the requests used this month. | [optional] 
**terms** | **str** | Payment terms. Almost always Net15. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


