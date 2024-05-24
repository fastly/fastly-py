# DefaultSettingsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resize_filter** | **str** | The type of filter to use while resizing an image. | defaults to "lanczos3"
**webp** | **bool** | Controls whether or not to default to WebP output when the client supports it. This is equivalent to adding \&quot;auto&#x3D;webp\&quot; to all image optimizer requests.  | defaults to False
**webp_quality** | **int** | The default quality to use with WebP output. This can be overridden with the second option in the \&quot;quality\&quot; URL parameter on specific image optimizer requests.  | defaults to 85
**jpeg_type** | **str** | The default type of JPEG output to use. This can be overridden with \&quot;format&#x3D;bjpeg\&quot; and \&quot;format&#x3D;pjpeg\&quot; on specific image optimizer requests.  | defaults to "auto"
**jpeg_quality** | **int** | The default quality to use with JPEG output. This can be overridden with the \&quot;quality\&quot; parameter on specific image optimizer requests.  | defaults to 85
**upscale** | **bool** | Whether or not we should allow output images to render at sizes larger than input.  | defaults to False
**allow_video** | **bool** | Enables GIF to MP4 transformations on this service. | defaults to False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


