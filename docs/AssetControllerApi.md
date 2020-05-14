# pyTB.AssetControllerApi

All URIs are relative to *//dashboard.digitalconstructionhub.ovh/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_asset_using_delete**](AssetControllerApi.md#delete_asset_using_delete) | **DELETE** /api/asset/{assetId} | deleteAsset
[**find_by_query_using_post**](AssetControllerApi.md#find_by_query_using_post) | **POST** /api/assets | findByQuery
[**get_asset_by_id_using_get**](AssetControllerApi.md#get_asset_by_id_using_get) | **GET** /api/asset/{assetId} | getAssetById
[**get_asset_types_using_get**](AssetControllerApi.md#get_asset_types_using_get) | **GET** /api/asset/types | getAssetTypes
[**get_assets_by_entity_group_id_using_get**](AssetControllerApi.md#get_assets_by_entity_group_id_using_get) | **GET** /api/entityGroup/{entityGroupId}/assets{?limit,startTime,endTime,ascOrder,offset} | getAssetsByEntityGroupId
[**get_assets_by_ids_using_get**](AssetControllerApi.md#get_assets_by_ids_using_get) | **GET** /api/assets{?assetIds} | getAssetsByIds
[**get_customer_assets_using_get**](AssetControllerApi.md#get_customer_assets_using_get) | **GET** /api/customer/{customerId}/assets{?type,textSearch,idOffset,textOffset,limit} | getCustomerAssets
[**get_tenant_asset_using_get**](AssetControllerApi.md#get_tenant_asset_using_get) | **GET** /api/tenant/assets{?assetName} | getTenantAsset
[**get_tenant_assets_using_get**](AssetControllerApi.md#get_tenant_assets_using_get) | **GET** /api/tenant/assets{?type,textSearch,idOffset,textOffset,limit} | getTenantAssets
[**get_user_assets_using_get**](AssetControllerApi.md#get_user_assets_using_get) | **GET** /api/user/assets{?type,textSearch,idOffset,textOffset,limit} | getUserAssets
[**save_asset_using_post**](AssetControllerApi.md#save_asset_using_post) | **POST** /api/asset{?entityGroupId} | saveAsset

# **delete_asset_using_delete**
> delete_asset_using_delete(asset_id)

deleteAsset

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
api_instance = pyTB.AssetControllerApi(pyTB.ApiClient(configuration))
asset_id = 'asset_id_example' # str | assetId

try:
    # deleteAsset
    api_instance.delete_asset_using_delete(asset_id)
except ApiException as e:
    print("Exception when calling AssetControllerApi->delete_asset_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| assetId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_query_using_post**
> list[Asset] find_by_query_using_post(body)

findByQuery

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
api_instance = pyTB.AssetControllerApi(pyTB.ApiClient(configuration))
body = pyTB.AssetSearchQuery() # AssetSearchQuery | query

try:
    # findByQuery
    api_response = api_instance.find_by_query_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetControllerApi->find_by_query_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssetSearchQuery**](AssetSearchQuery.md)| query | 

### Return type

[**list[Asset]**](Asset.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_by_id_using_get**
> Asset get_asset_by_id_using_get(asset_id)

getAssetById

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
api_instance = pyTB.AssetControllerApi(pyTB.ApiClient(configuration))
asset_id = 'asset_id_example' # str | assetId

try:
    # getAssetById
    api_response = api_instance.get_asset_by_id_using_get(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetControllerApi->get_asset_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| assetId | 

### Return type

[**Asset**](Asset.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_types_using_get**
> list[EntitySubtype] get_asset_types_using_get()

getAssetTypes

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
api_instance = pyTB.AssetControllerApi(pyTB.ApiClient(configuration))

try:
    # getAssetTypes
    api_response = api_instance.get_asset_types_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetControllerApi->get_asset_types_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EntitySubtype]**](EntitySubtype.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assets_by_entity_group_id_using_get**
> TimePageDataAsset get_assets_by_entity_group_id_using_get(entity_group_id, limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset)

getAssetsByEntityGroupId

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
api_instance = pyTB.AssetControllerApi(pyTB.ApiClient(configuration))
entity_group_id = 'entity_group_id_example' # str | entityGroupId
limit = 56 # int | Page link limit
start_time = 789 # int | startTime (optional)
end_time = 789 # int | endTime (optional)
asc_order = true # bool | ascOrder (optional)
offset = 'offset_example' # str | offset (optional)

try:
    # getAssetsByEntityGroupId
    api_response = api_instance.get_assets_by_entity_group_id_using_get(entity_group_id, limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetControllerApi->get_assets_by_entity_group_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_group_id** | **str**| entityGroupId | 
 **limit** | **int**| Page link limit | 
 **start_time** | **int**| startTime | [optional] 
 **end_time** | **int**| endTime | [optional] 
 **asc_order** | **bool**| ascOrder | [optional] 
 **offset** | **str**| offset | [optional] 

### Return type

[**TimePageDataAsset**](TimePageDataAsset.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assets_by_ids_using_get**
> list[Asset] get_assets_by_ids_using_get(asset_ids)

getAssetsByIds

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
api_instance = pyTB.AssetControllerApi(pyTB.ApiClient(configuration))
asset_ids = 'asset_ids_example' # str | assetIds

try:
    # getAssetsByIds
    api_response = api_instance.get_assets_by_ids_using_get(asset_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetControllerApi->get_assets_by_ids_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_ids** | **str**| assetIds | 

### Return type

[**list[Asset]**](Asset.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_assets_using_get**
> TextPageDataAsset get_customer_assets_using_get(customer_id, limit, type=type, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getCustomerAssets

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
api_instance = pyTB.AssetControllerApi(pyTB.ApiClient(configuration))
customer_id = 'customer_id_example' # str | customerId
limit = 'limit_example' # str | limit
type = 'type_example' # str | type (optional)
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try:
    # getCustomerAssets
    api_response = api_instance.get_customer_assets_using_get(customer_id, limit, type=type, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetControllerApi->get_customer_assets_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| customerId | 
 **limit** | **str**| limit | 
 **type** | **str**| type | [optional] 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataAsset**](TextPageDataAsset.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_asset_using_get**
> Asset get_tenant_asset_using_get(asset_name)

getTenantAsset

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
api_instance = pyTB.AssetControllerApi(pyTB.ApiClient(configuration))
asset_name = 'asset_name_example' # str | assetName

try:
    # getTenantAsset
    api_response = api_instance.get_tenant_asset_using_get(asset_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetControllerApi->get_tenant_asset_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_name** | **str**| assetName | 

### Return type

[**Asset**](Asset.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_assets_using_get**
> TextPageDataAsset get_tenant_assets_using_get(limit, type=type, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getTenantAssets

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
api_instance = pyTB.AssetControllerApi(pyTB.ApiClient(configuration))
limit = 'limit_example' # str | limit
type = 'type_example' # str | type (optional)
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try:
    # getTenantAssets
    api_response = api_instance.get_tenant_assets_using_get(limit, type=type, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetControllerApi->get_tenant_assets_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| limit | 
 **type** | **str**| type | [optional] 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataAsset**](TextPageDataAsset.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_assets_using_get**
> TextPageDataAsset get_user_assets_using_get(limit, type=type, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getUserAssets

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
api_instance = pyTB.AssetControllerApi(pyTB.ApiClient(configuration))
limit = 'limit_example' # str | limit
type = 'type_example' # str | type (optional)
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try:
    # getUserAssets
    api_response = api_instance.get_user_assets_using_get(limit, type=type, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetControllerApi->get_user_assets_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| limit | 
 **type** | **str**| type | [optional] 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataAsset**](TextPageDataAsset.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_asset_using_post**
> Asset save_asset_using_post(body, entity_group_id=entity_group_id)

saveAsset

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
api_instance = pyTB.AssetControllerApi(pyTB.ApiClient(configuration))
body = pyTB.Asset() # Asset | asset
entity_group_id = 'entity_group_id_example' # str | entityGroupId (optional)

try:
    # saveAsset
    api_response = api_instance.save_asset_using_post(body, entity_group_id=entity_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetControllerApi->save_asset_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Asset**](Asset.md)| asset | 
 **entity_group_id** | **str**| entityGroupId | [optional] 

### Return type

[**Asset**](Asset.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

