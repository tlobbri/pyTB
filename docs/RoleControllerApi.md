# pyTB.RoleControllerApi

All URIs are relative to *//dashboard.digitalconstructionhub.ovh/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_role_using_delete**](RoleControllerApi.md#delete_role_using_delete) | **DELETE** /api/role/{roleId} | deleteRole
[**get_role_by_id_using_get**](RoleControllerApi.md#get_role_by_id_using_get) | **GET** /api/role/{roleId} | getRoleById
[**get_roles_by_ids_using_get**](RoleControllerApi.md#get_roles_by_ids_using_get) | **GET** /api/roles{?roleIds} | getRolesByIds
[**get_roles_using_get**](RoleControllerApi.md#get_roles_using_get) | **GET** /api/roles{?type,textSearch,idOffset,textOffset,limit} | getRoles
[**save_role_using_post**](RoleControllerApi.md#save_role_using_post) | **POST** /api/role | saveRole

# **delete_role_using_delete**
> delete_role_using_delete(role_id)

deleteRole

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
api_instance = pyTB.RoleControllerApi(pyTB.ApiClient(configuration))
role_id = 'role_id_example' # str | roleId

try:
    # deleteRole
    api_instance.delete_role_using_delete(role_id)
except ApiException as e:
    print("Exception when calling RoleControllerApi->delete_role_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| roleId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_by_id_using_get**
> Role get_role_by_id_using_get(role_id)

getRoleById

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
api_instance = pyTB.RoleControllerApi(pyTB.ApiClient(configuration))
role_id = 'role_id_example' # str | roleId

try:
    # getRoleById
    api_response = api_instance.get_role_by_id_using_get(role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleControllerApi->get_role_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| roleId | 

### Return type

[**Role**](Role.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_roles_by_ids_using_get**
> list[Role] get_roles_by_ids_using_get(role_ids)

getRolesByIds

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
api_instance = pyTB.RoleControllerApi(pyTB.ApiClient(configuration))
role_ids = 'role_ids_example' # str | roleIds

try:
    # getRolesByIds
    api_response = api_instance.get_roles_by_ids_using_get(role_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleControllerApi->get_roles_by_ids_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_ids** | **str**| roleIds | 

### Return type

[**list[Role]**](Role.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_roles_using_get**
> TextPageDataRole get_roles_using_get(limit, type=type, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getRoles

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
api_instance = pyTB.RoleControllerApi(pyTB.ApiClient(configuration))
limit = 'limit_example' # str | limit
type = 'type_example' # str | type (optional)
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try:
    # getRoles
    api_response = api_instance.get_roles_using_get(limit, type=type, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleControllerApi->get_roles_using_get: %s\n" % e)
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

[**TextPageDataRole**](TextPageDataRole.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_role_using_post**
> Role save_role_using_post(body)

saveRole

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
api_instance = pyTB.RoleControllerApi(pyTB.ApiClient(configuration))
body = pyTB.Role() # Role | role

try:
    # saveRole
    api_response = api_instance.save_role_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleControllerApi->save_role_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Role**](Role.md)| role | 

### Return type

[**Role**](Role.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

