# pyTB.EntityGroupControllerApi

All URIs are relative to *//dashboard.digitalconstructionhub.ovh/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_entities_to_entity_group_using_post**](EntityGroupControllerApi.md#add_entities_to_entity_group_using_post) | **POST** /api/entityGroup/{entityGroupId}/addEntities | addEntitiesToEntityGroup
[**delete_entity_group_using_delete**](EntityGroupControllerApi.md#delete_entity_group_using_delete) | **DELETE** /api/entityGroup/{entityGroupId} | deleteEntityGroup
[**get_enitity_group_by_owner_and_name_and_type_using_get**](EntityGroupControllerApi.md#get_enitity_group_by_owner_and_name_and_type_using_get) | **GET** /api/entityGroup/{ownerType}/{ownerId}/{groupType}/{groupName} | getEnitityGroupByOwnerAndNameAndType
[**get_entities_using_get**](EntityGroupControllerApi.md#get_entities_using_get) | **GET** /api/entityGroup/{entityGroupId}/entities{?limit,startTime,endTime,ascOrder,offset} | getEntities
[**get_entity_group_all_by_owner_and_type_using_get**](EntityGroupControllerApi.md#get_entity_group_all_by_owner_and_type_using_get) | **GET** /api/entityGroup/all/{ownerType}/{ownerId}/{groupType} | getEntityGroupAllByOwnerAndType
[**get_entity_group_by_id_using_get**](EntityGroupControllerApi.md#get_entity_group_by_id_using_get) | **GET** /api/entityGroup/{entityGroupId} | getEntityGroupById
[**get_entity_groups_by_ids_using_get**](EntityGroupControllerApi.md#get_entity_groups_by_ids_using_get) | **GET** /api/entityGroups{?entityGroupIds} | getEntityGroupsByIds
[**get_entity_groups_by_owner_and_type_using_get**](EntityGroupControllerApi.md#get_entity_groups_by_owner_and_type_using_get) | **GET** /api/entityGroups/{ownerType}/{ownerId}/{groupType} | getEntityGroupsByOwnerAndType
[**get_entity_groups_by_type_using_get**](EntityGroupControllerApi.md#get_entity_groups_by_type_using_get) | **GET** /api/entityGroups/{groupType} | getEntityGroupsByType
[**get_entity_groups_for_entity_using_get**](EntityGroupControllerApi.md#get_entity_groups_for_entity_using_get) | **GET** /api/entityGroups/{entityType}/{entityId} | getEntityGroupsForEntity
[**get_group_entity_using_get**](EntityGroupControllerApi.md#get_group_entity_using_get) | **GET** /api/entityGroup/{entityGroupId}/{entityId} | getGroupEntity
[**get_owners_using_get**](EntityGroupControllerApi.md#get_owners_using_get) | **GET** /api/owners{?textSearch,idOffset,textOffset,limit} | getOwners
[**make_entity_group_private_using_post**](EntityGroupControllerApi.md#make_entity_group_private_using_post) | **POST** /api/entityGroup/{entityGroupId}/makePrivate | makeEntityGroupPrivate
[**make_entity_group_public_using_post**](EntityGroupControllerApi.md#make_entity_group_public_using_post) | **POST** /api/entityGroup/{entityGroupId}/makePublic | makeEntityGroupPublic
[**remove_entities_from_entity_group_using_post**](EntityGroupControllerApi.md#remove_entities_from_entity_group_using_post) | **POST** /api/entityGroup/{entityGroupId}/deleteEntities | removeEntitiesFromEntityGroup
[**save_entity_group_using_post**](EntityGroupControllerApi.md#save_entity_group_using_post) | **POST** /api/entityGroup | saveEntityGroup

# **add_entities_to_entity_group_using_post**
> add_entities_to_entity_group_using_post(body, entity_group_id)

addEntitiesToEntityGroup

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
api_instance = pyTB.EntityGroupControllerApi(pyTB.ApiClient(configuration))
body = ['body_example'] # list[str] | strEntityIds
entity_group_id = 'entity_group_id_example' # str | entityGroupId

try:
    # addEntitiesToEntityGroup
    api_instance.add_entities_to_entity_group_using_post(body, entity_group_id)
except ApiException as e:
    print("Exception when calling EntityGroupControllerApi->add_entities_to_entity_group_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| strEntityIds | 
 **entity_group_id** | **str**| entityGroupId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_entity_group_using_delete**
> delete_entity_group_using_delete(entity_group_id)

deleteEntityGroup

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
api_instance = pyTB.EntityGroupControllerApi(pyTB.ApiClient(configuration))
entity_group_id = 'entity_group_id_example' # str | entityGroupId

try:
    # deleteEntityGroup
    api_instance.delete_entity_group_using_delete(entity_group_id)
except ApiException as e:
    print("Exception when calling EntityGroupControllerApi->delete_entity_group_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_group_id** | **str**| entityGroupId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enitity_group_by_owner_and_name_and_type_using_get**
> EntityGroupInfo get_enitity_group_by_owner_and_name_and_type_using_get(owner_type, owner_id, group_type, group_name)

getEnitityGroupByOwnerAndNameAndType

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
api_instance = pyTB.EntityGroupControllerApi(pyTB.ApiClient(configuration))
owner_type = 'owner_type_example' # str | ownerType
owner_id = 'owner_id_example' # str | ownerId
group_type = 'group_type_example' # str | EntityGroup type
group_name = 'group_name_example' # str | groupName

try:
    # getEnitityGroupByOwnerAndNameAndType
    api_response = api_instance.get_enitity_group_by_owner_and_name_and_type_using_get(owner_type, owner_id, group_type, group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityGroupControllerApi->get_enitity_group_by_owner_and_name_and_type_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_type** | **str**| ownerType | 
 **owner_id** | **str**| ownerId | 
 **group_type** | **str**| EntityGroup type | 
 **group_name** | **str**| groupName | 

### Return type

[**EntityGroupInfo**](EntityGroupInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entities_using_get**
> TimePageDataShortEntityView get_entities_using_get(entity_group_id, limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset)

getEntities

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
api_instance = pyTB.EntityGroupControllerApi(pyTB.ApiClient(configuration))
entity_group_id = 'entity_group_id_example' # str | entityGroupId
limit = 56 # int | Page link limit
start_time = 789 # int | startTime (optional)
end_time = 789 # int | endTime (optional)
asc_order = true # bool | ascOrder (optional)
offset = 'offset_example' # str | offset (optional)

try:
    # getEntities
    api_response = api_instance.get_entities_using_get(entity_group_id, limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityGroupControllerApi->get_entities_using_get: %s\n" % e)
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

[**TimePageDataShortEntityView**](TimePageDataShortEntityView.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_group_all_by_owner_and_type_using_get**
> EntityGroupInfo get_entity_group_all_by_owner_and_type_using_get(owner_type, owner_id, group_type)

getEntityGroupAllByOwnerAndType

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
api_instance = pyTB.EntityGroupControllerApi(pyTB.ApiClient(configuration))
owner_type = 'owner_type_example' # str | ownerType
owner_id = 'owner_id_example' # str | ownerId
group_type = 'group_type_example' # str | EntityGroup type

try:
    # getEntityGroupAllByOwnerAndType
    api_response = api_instance.get_entity_group_all_by_owner_and_type_using_get(owner_type, owner_id, group_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityGroupControllerApi->get_entity_group_all_by_owner_and_type_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_type** | **str**| ownerType | 
 **owner_id** | **str**| ownerId | 
 **group_type** | **str**| EntityGroup type | 

### Return type

[**EntityGroupInfo**](EntityGroupInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_group_by_id_using_get**
> EntityGroupInfo get_entity_group_by_id_using_get(entity_group_id)

getEntityGroupById

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
api_instance = pyTB.EntityGroupControllerApi(pyTB.ApiClient(configuration))
entity_group_id = 'entity_group_id_example' # str | entityGroupId

try:
    # getEntityGroupById
    api_response = api_instance.get_entity_group_by_id_using_get(entity_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityGroupControllerApi->get_entity_group_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_group_id** | **str**| entityGroupId | 

### Return type

[**EntityGroupInfo**](EntityGroupInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_groups_by_ids_using_get**
> list[EntityGroup] get_entity_groups_by_ids_using_get(entity_group_ids)

getEntityGroupsByIds

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
api_instance = pyTB.EntityGroupControllerApi(pyTB.ApiClient(configuration))
entity_group_ids = 'entity_group_ids_example' # str | entityGroupIds

try:
    # getEntityGroupsByIds
    api_response = api_instance.get_entity_groups_by_ids_using_get(entity_group_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityGroupControllerApi->get_entity_groups_by_ids_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_group_ids** | **str**| entityGroupIds | 

### Return type

[**list[EntityGroup]**](EntityGroup.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_groups_by_owner_and_type_using_get**
> list[EntityGroupInfo] get_entity_groups_by_owner_and_type_using_get(owner_type, owner_id, group_type)

getEntityGroupsByOwnerAndType

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
api_instance = pyTB.EntityGroupControllerApi(pyTB.ApiClient(configuration))
owner_type = 'owner_type_example' # str | ownerType
owner_id = 'owner_id_example' # str | ownerId
group_type = 'group_type_example' # str | EntityGroup type

try:
    # getEntityGroupsByOwnerAndType
    api_response = api_instance.get_entity_groups_by_owner_and_type_using_get(owner_type, owner_id, group_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityGroupControllerApi->get_entity_groups_by_owner_and_type_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_type** | **str**| ownerType | 
 **owner_id** | **str**| ownerId | 
 **group_type** | **str**| EntityGroup type | 

### Return type

[**list[EntityGroupInfo]**](EntityGroupInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_groups_by_type_using_get**
> list[EntityGroupInfo] get_entity_groups_by_type_using_get(group_type)

getEntityGroupsByType

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
api_instance = pyTB.EntityGroupControllerApi(pyTB.ApiClient(configuration))
group_type = 'group_type_example' # str | EntityGroup type

try:
    # getEntityGroupsByType
    api_response = api_instance.get_entity_groups_by_type_using_get(group_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityGroupControllerApi->get_entity_groups_by_type_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_type** | **str**| EntityGroup type | 

### Return type

[**list[EntityGroupInfo]**](EntityGroupInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_groups_for_entity_using_get**
> list[EntityGroupId] get_entity_groups_for_entity_using_get(entity_type, entity_id)

getEntityGroupsForEntity

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
api_instance = pyTB.EntityGroupControllerApi(pyTB.ApiClient(configuration))
entity_type = 'entity_type_example' # str | Entity type
entity_id = 'entity_id_example' # str | entityId

try:
    # getEntityGroupsForEntity
    api_response = api_instance.get_entity_groups_for_entity_using_get(entity_type, entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityGroupControllerApi->get_entity_groups_for_entity_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| Entity type | 
 **entity_id** | **str**| entityId | 

### Return type

[**list[EntityGroupId]**](EntityGroupId.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_entity_using_get**
> ShortEntityView get_group_entity_using_get(entity_group_id, entity_id)

getGroupEntity

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
api_instance = pyTB.EntityGroupControllerApi(pyTB.ApiClient(configuration))
entity_group_id = 'entity_group_id_example' # str | entityGroupId
entity_id = 'entity_id_example' # str | entityId

try:
    # getGroupEntity
    api_response = api_instance.get_group_entity_using_get(entity_group_id, entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityGroupControllerApi->get_group_entity_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_group_id** | **str**| entityGroupId | 
 **entity_id** | **str**| entityId | 

### Return type

[**ShortEntityView**](ShortEntityView.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_owners_using_get**
> TextPageDataContactBasedobject get_owners_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getOwners

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
api_instance = pyTB.EntityGroupControllerApi(pyTB.ApiClient(configuration))
limit = 'limit_example' # str | limit
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try:
    # getOwners
    api_response = api_instance.get_owners_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityGroupControllerApi->get_owners_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| limit | 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataContactBasedobject**](TextPageDataContactBasedobject.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **make_entity_group_private_using_post**
> make_entity_group_private_using_post(entity_group_id)

makeEntityGroupPrivate

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
api_instance = pyTB.EntityGroupControllerApi(pyTB.ApiClient(configuration))
entity_group_id = 'entity_group_id_example' # str | entityGroupId

try:
    # makeEntityGroupPrivate
    api_instance.make_entity_group_private_using_post(entity_group_id)
except ApiException as e:
    print("Exception when calling EntityGroupControllerApi->make_entity_group_private_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_group_id** | **str**| entityGroupId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **make_entity_group_public_using_post**
> make_entity_group_public_using_post(entity_group_id)

makeEntityGroupPublic

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
api_instance = pyTB.EntityGroupControllerApi(pyTB.ApiClient(configuration))
entity_group_id = 'entity_group_id_example' # str | entityGroupId

try:
    # makeEntityGroupPublic
    api_instance.make_entity_group_public_using_post(entity_group_id)
except ApiException as e:
    print("Exception when calling EntityGroupControllerApi->make_entity_group_public_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_group_id** | **str**| entityGroupId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_entities_from_entity_group_using_post**
> remove_entities_from_entity_group_using_post(body, entity_group_id)

removeEntitiesFromEntityGroup

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
api_instance = pyTB.EntityGroupControllerApi(pyTB.ApiClient(configuration))
body = ['body_example'] # list[str] | strEntityIds
entity_group_id = 'entity_group_id_example' # str | entityGroupId

try:
    # removeEntitiesFromEntityGroup
    api_instance.remove_entities_from_entity_group_using_post(body, entity_group_id)
except ApiException as e:
    print("Exception when calling EntityGroupControllerApi->remove_entities_from_entity_group_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| strEntityIds | 
 **entity_group_id** | **str**| entityGroupId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_entity_group_using_post**
> EntityGroupInfo save_entity_group_using_post(body)

saveEntityGroup

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
api_instance = pyTB.EntityGroupControllerApi(pyTB.ApiClient(configuration))
body = pyTB.EntityGroup() # EntityGroup | entityGroup

try:
    # saveEntityGroup
    api_response = api_instance.save_entity_group_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityGroupControllerApi->save_entity_group_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntityGroup**](EntityGroup.md)| entityGroup | 

### Return type

[**EntityGroupInfo**](EntityGroupInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

