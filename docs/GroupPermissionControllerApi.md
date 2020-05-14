# pyTB.GroupPermissionControllerApi

All URIs are relative to *//dashboard.digitalconstructionhub.ovh/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_group_permission_using_delete**](GroupPermissionControllerApi.md#delete_group_permission_using_delete) | **DELETE** /api/groupPermission/{groupPermissionId} | deleteGroupPermission
[**get_entity_group_permissions_using_get**](GroupPermissionControllerApi.md#get_entity_group_permissions_using_get) | **GET** /api/entityGroup/{entityGroupId}/groupPermissions | getEntityGroupPermissions
[**get_group_permission_by_id_using_get**](GroupPermissionControllerApi.md#get_group_permission_by_id_using_get) | **GET** /api/groupPermission/{groupPermissionId} | getGroupPermissionById
[**get_user_group_permissions_using_get**](GroupPermissionControllerApi.md#get_user_group_permissions_using_get) | **GET** /api/userGroup/{userGroupId}/groupPermissions | getUserGroupPermissions
[**save_group_permission_using_post**](GroupPermissionControllerApi.md#save_group_permission_using_post) | **POST** /api/groupPermission | saveGroupPermission

# **delete_group_permission_using_delete**
> delete_group_permission_using_delete(group_permission_id)

deleteGroupPermission

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
api_instance = pyTB.GroupPermissionControllerApi(pyTB.ApiClient(configuration))
group_permission_id = 'group_permission_id_example' # str | groupPermissionId

try:
    # deleteGroupPermission
    api_instance.delete_group_permission_using_delete(group_permission_id)
except ApiException as e:
    print("Exception when calling GroupPermissionControllerApi->delete_group_permission_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_permission_id** | **str**| groupPermissionId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_group_permissions_using_get**
> list[GroupPermissionInfo] get_entity_group_permissions_using_get(entity_group_id)

getEntityGroupPermissions

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
api_instance = pyTB.GroupPermissionControllerApi(pyTB.ApiClient(configuration))
entity_group_id = 'entity_group_id_example' # str | entityGroupId

try:
    # getEntityGroupPermissions
    api_response = api_instance.get_entity_group_permissions_using_get(entity_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupPermissionControllerApi->get_entity_group_permissions_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_group_id** | **str**| entityGroupId | 

### Return type

[**list[GroupPermissionInfo]**](GroupPermissionInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_permission_by_id_using_get**
> GroupPermission get_group_permission_by_id_using_get(group_permission_id)

getGroupPermissionById

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
api_instance = pyTB.GroupPermissionControllerApi(pyTB.ApiClient(configuration))
group_permission_id = 'group_permission_id_example' # str | groupPermissionId

try:
    # getGroupPermissionById
    api_response = api_instance.get_group_permission_by_id_using_get(group_permission_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupPermissionControllerApi->get_group_permission_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_permission_id** | **str**| groupPermissionId | 

### Return type

[**GroupPermission**](GroupPermission.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_group_permissions_using_get**
> list[GroupPermissionInfo] get_user_group_permissions_using_get(user_group_id)

getUserGroupPermissions

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
api_instance = pyTB.GroupPermissionControllerApi(pyTB.ApiClient(configuration))
user_group_id = 'user_group_id_example' # str | userGroupId

try:
    # getUserGroupPermissions
    api_response = api_instance.get_user_group_permissions_using_get(user_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupPermissionControllerApi->get_user_group_permissions_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**| userGroupId | 

### Return type

[**list[GroupPermissionInfo]**](GroupPermissionInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_group_permission_using_post**
> GroupPermission save_group_permission_using_post(body)

saveGroupPermission

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
api_instance = pyTB.GroupPermissionControllerApi(pyTB.ApiClient(configuration))
body = pyTB.GroupPermission() # GroupPermission | groupPermission

try:
    # saveGroupPermission
    api_response = api_instance.save_group_permission_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupPermissionControllerApi->save_group_permission_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupPermission**](GroupPermission.md)| groupPermission | 

### Return type

[**GroupPermission**](GroupPermission.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

