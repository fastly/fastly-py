# NetworkProtectRoaStatus

Whether a Route Origin Authorization permits Fastly to announce this prefix. Fastly refreshes this on a schedule; reading a network never triggers a check, so this can be older than the moment you read it. A status of `pending` means no check has completed; `valid` authorizes Fastly at this prefix length; `invalid` means a covering ROA does not authorize Fastly; and `not_found` means no ROA covers the prefix. The controller may omit an unrecognized status, and omission is not an authorization result. A valid ROA alone does not make a network ready for advertisement.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Whether a Route Origin Authorization permits Fastly to announce this prefix. Fastly refreshes this on a schedule; reading a network never triggers a check, so this can be older than the moment you read it. A status of `pending` means no check has completed; `valid` authorizes Fastly at this prefix length; `invalid` means a covering ROA does not authorize Fastly; and `not_found` means no ROA covers the prefix. The controller may omit an unrecognized status, and omission is not an authorization result. A valid ROA alone does not make a network ready for advertisement. |  must be one of ["pending", "valid", "invalid", "not_found", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


