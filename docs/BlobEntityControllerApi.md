# pyTB.BlobEntityControllerApi

All URIs are relative to *//dashboard.digitalconstructionhub.ovh/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_blob_entity_using_delete**](BlobEntityControllerApi.md#delete_blob_entity_using_delete) | **DELETE** /api/blobEntity/{blobEntityId} | deleteBlobEntity
[**download_blob_entity_using_get**](BlobEntityControllerApi.md#download_blob_entity_using_get) | **GET** /api/blobEntity/{blobEntityId}/download | downloadBlobEntity
[**get_blob_entities_by_ids_using_get**](BlobEntityControllerApi.md#get_blob_entities_by_ids_using_get) | **GET** /api/blobEntities{?blobEntityIds} | getBlobEntitiesByIds
[**get_blob_entities_using_get**](BlobEntityControllerApi.md#get_blob_entities_using_get) | **GET** /api/blobEntities{?limit,type,startTime,endTime,ascOrder,offset} | getBlobEntities
[**get_blob_entity_info_by_id_using_get**](BlobEntityControllerApi.md#get_blob_entity_info_by_id_using_get) | **GET** /api/blobEntity/info/{blobEntityId} | getBlobEntityInfoById

# **delete_blob_entity_using_delete**
> delete_blob_entity_using_delete(blob_entity_id)

deleteBlobEntity

### Example
```python
from __future__ import print_function
import time
import pyTB
from pyTB.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Authorization
configuration = pyTB.Configuration()
configuration.api_key['X-Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pyTB.BlobEntityControllerApi(pyTB.ApiClient(configuration))
blob_entity_id = 'blob_entity_id_example' # str | blobEntityId

try:
    # deleteBlobEntity
    api_instance.delete_blob_entity_using_delete(blob_entity_id)
except ApiException as e:
    print("Exception when calling BlobEntityControllerApi->delete_blob_entity_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blob_entity_id** | **str**| blobEntityId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_blob_entity_using_get**
> Resource download_blob_entity_using_get(blob_entity_id)

downloadBlobEntity

### Example
```python
from __future__ import print_function
import time
import pyTB
from pyTB.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Authorization
configuration = pyTB.Configuration()
configuration.api_key['X-Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pyTB.BlobEntityControllerApi(pyTB.ApiClient(configuration))
blob_entity_id = 'blob_entity_id_example' # str | blobEntityId

try:
    # downloadBlobEntity
    api_response = api_instance.download_blob_entity_using_get(blob_entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlobEntityControllerApi->download_blob_entity_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blob_entity_id** | **str**| blobEntityId | 

### Return type

[**Resource**](Resource.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blob_entities_by_ids_using_get**
> list[BlobEntityInfo] get_blob_entities_by_ids_using_get(blob_entity_ids)

getBlobEntitiesByIds

### Example
```python
from __future__ import print_function
import time
import pyTB
from pyTB.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Authorization
configuration = pyTB.Configuration()
configuration.api_key['X-Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pyTB.BlobEntityControllerApi(pyTB.ApiClient(configuration))
blob_entity_ids = 'blob_entity_ids_example' # str | blobEntityIds

try:
    # getBlobEntitiesByIds
    api_response = api_instance.get_blob_entities_by_ids_using_get(blob_entity_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlobEntityControllerApi->get_blob_entities_by_ids_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blob_entity_ids** | **str**| blobEntityIds | 

### Return type

[**list[BlobEntityInfo]**](BlobEntityInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blob_entities_using_get**
> TimePageDataBlobEntityInfo get_blob_entities_using_get(limit, type=type, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset)

getBlobEntities

### Example
```python
from __future__ import print_function
import time
import pyTB
from pyTB.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Authorization
configuration = pyTB.Configuration()
configuration.api_key['X-Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pyTB.BlobEntityControllerApi(pyTB.ApiClient(configuration))
limit = 56 # int | limit
type = 'type_example' # str | type (optional)
start_time = 789 # int | startTime (optional)
end_time = 789 # int | endTime (optional)
asc_order = true # bool | ascOrder (optional)
offset = 'offset_example' # str | offset (optional)

try:
    # getBlobEntities
    api_response = api_instance.get_blob_entities_using_get(limit, type=type, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlobEntityControllerApi->get_blob_entities_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| limit | 
 **type** | **str**| type | [optional] 
 **start_time** | **int**| startTime | [optional] 
 **end_time** | **int**| endTime | [optional] 
 **asc_order** | **bool**| ascOrder | [optional] 
 **offset** | **str**| offset | [optional] 

### Return type

[**TimePageDataBlobEntityInfo**](TimePageDataBlobEntityInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blob_entity_info_by_id_using_get**
> BlobEntityInfo get_blob_entity_info_by_id_using_get(blob_entity_id)

getBlobEntityInfoById

### Example
```python
from __future__ import print_function
import time
import pyTB
from pyTB.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Authorization
configuration = pyTB.Configuration()
configuration.api_key['X-Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pyTB.BlobEntityControllerApi(pyTB.ApiClient(configuration))
blob_entity_id = 'blob_entity_id_example' # str | blobEntityId

try:
    # getBlobEntityInfoById
    api_response = api_instance.get_blob_entity_info_by_id_using_get(blob_entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlobEntityControllerApi->get_blob_entity_info_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blob_entity_id** | **str**| blobEntityId | 

### Return type

[**BlobEntityInfo**](BlobEntityInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

