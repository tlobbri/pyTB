# pyTB.EntityViewControllerApi

All URIs are relative to *//dashboard.digitalconstructionhub.ovh/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_entity_view_using_delete**](EntityViewControllerApi.md#delete_entity_view_using_delete) | **DELETE** /api/entityView/{entityViewId} | deleteEntityView
[**find_by_query_using_post3**](EntityViewControllerApi.md#find_by_query_using_post3) | **POST** /api/entityViews | findByQuery
[**get_customer_entity_views_using_get**](EntityViewControllerApi.md#get_customer_entity_views_using_get) | **GET** /api/customer/{customerId}/entityViews{?type,textSearch,idOffset,textOffset,limit} | getCustomerEntityViews
[**get_entity_view_by_id_using_get**](EntityViewControllerApi.md#get_entity_view_by_id_using_get) | **GET** /api/entityView/{entityViewId} | getEntityViewById
[**get_entity_view_types_using_get**](EntityViewControllerApi.md#get_entity_view_types_using_get) | **GET** /api/entityView/types | getEntityViewTypes
[**get_entity_views_by_entity_group_id_using_get**](EntityViewControllerApi.md#get_entity_views_by_entity_group_id_using_get) | **GET** /api/entityGroup/{entityGroupId}/entityViews{?limit,startTime,endTime,ascOrder,offset} | getEntityViewsByEntityGroupId
[**get_entity_views_by_ids_using_get**](EntityViewControllerApi.md#get_entity_views_by_ids_using_get) | **GET** /api/entityViews{?entityViewIds} | getEntityViewsByIds
[**get_tenant_entity_view_using_get**](EntityViewControllerApi.md#get_tenant_entity_view_using_get) | **GET** /api/tenant/entityViews{?entityViewName} | getTenantEntityView
[**get_tenant_entity_views_using_get**](EntityViewControllerApi.md#get_tenant_entity_views_using_get) | **GET** /api/tenant/entityViews{?type,textSearch,idOffset,textOffset,limit} | getTenantEntityViews
[**get_user_entity_views_using_get**](EntityViewControllerApi.md#get_user_entity_views_using_get) | **GET** /api/user/entityViews{?type,textSearch,idOffset,textOffset,limit} | getUserEntityViews
[**save_entity_view_using_post**](EntityViewControllerApi.md#save_entity_view_using_post) | **POST** /api/entityView{?entityGroupId} | saveEntityView

# **delete_entity_view_using_delete**
> delete_entity_view_using_delete(entity_view_id)

deleteEntityView

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
api_instance = pyTB.EntityViewControllerApi(pyTB.ApiClient(configuration))
entity_view_id = 'entity_view_id_example' # str | entityViewId

try:
    # deleteEntityView
    api_instance.delete_entity_view_using_delete(entity_view_id)
except ApiException as e:
    print("Exception when calling EntityViewControllerApi->delete_entity_view_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_view_id** | **str**| entityViewId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_query_using_post3**
> list[EntityView] find_by_query_using_post3(body)

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
api_instance = pyTB.EntityViewControllerApi(pyTB.ApiClient(configuration))
body = pyTB.EntityViewSearchQuery() # EntityViewSearchQuery | query

try:
    # findByQuery
    api_response = api_instance.find_by_query_using_post3(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityViewControllerApi->find_by_query_using_post3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntityViewSearchQuery**](EntityViewSearchQuery.md)| query | 

### Return type

[**list[EntityView]**](EntityView.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_entity_views_using_get**
> TextPageDataEntityView get_customer_entity_views_using_get(customer_id, limit, type=type, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getCustomerEntityViews

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
api_instance = pyTB.EntityViewControllerApi(pyTB.ApiClient(configuration))
customer_id = 'customer_id_example' # str | customerId
limit = 'limit_example' # str | limit
type = 'type_example' # str | type (optional)
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try:
    # getCustomerEntityViews
    api_response = api_instance.get_customer_entity_views_using_get(customer_id, limit, type=type, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityViewControllerApi->get_customer_entity_views_using_get: %s\n" % e)
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

[**TextPageDataEntityView**](TextPageDataEntityView.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_view_by_id_using_get**
> EntityView get_entity_view_by_id_using_get(entity_view_id)

getEntityViewById

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
api_instance = pyTB.EntityViewControllerApi(pyTB.ApiClient(configuration))
entity_view_id = 'entity_view_id_example' # str | entityViewId

try:
    # getEntityViewById
    api_response = api_instance.get_entity_view_by_id_using_get(entity_view_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityViewControllerApi->get_entity_view_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_view_id** | **str**| entityViewId | 

### Return type

[**EntityView**](EntityView.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_view_types_using_get**
> list[EntitySubtype] get_entity_view_types_using_get()

getEntityViewTypes

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
api_instance = pyTB.EntityViewControllerApi(pyTB.ApiClient(configuration))

try:
    # getEntityViewTypes
    api_response = api_instance.get_entity_view_types_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityViewControllerApi->get_entity_view_types_using_get: %s\n" % e)
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

# **get_entity_views_by_entity_group_id_using_get**
> TimePageDataEntityView get_entity_views_by_entity_group_id_using_get(entity_group_id, limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset)

getEntityViewsByEntityGroupId

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
api_instance = pyTB.EntityViewControllerApi(pyTB.ApiClient(configuration))
entity_group_id = 'entity_group_id_example' # str | entityGroupId
limit = 56 # int | Page link limit
start_time = 789 # int | startTime (optional)
end_time = 789 # int | endTime (optional)
asc_order = true # bool | ascOrder (optional)
offset = 'offset_example' # str | offset (optional)

try:
    # getEntityViewsByEntityGroupId
    api_response = api_instance.get_entity_views_by_entity_group_id_using_get(entity_group_id, limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityViewControllerApi->get_entity_views_by_entity_group_id_using_get: %s\n" % e)
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

[**TimePageDataEntityView**](TimePageDataEntityView.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_views_by_ids_using_get**
> list[EntityView] get_entity_views_by_ids_using_get(entity_view_ids)

getEntityViewsByIds

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
api_instance = pyTB.EntityViewControllerApi(pyTB.ApiClient(configuration))
entity_view_ids = 'entity_view_ids_example' # str | entityViewIds

try:
    # getEntityViewsByIds
    api_response = api_instance.get_entity_views_by_ids_using_get(entity_view_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityViewControllerApi->get_entity_views_by_ids_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_view_ids** | **str**| entityViewIds | 

### Return type

[**list[EntityView]**](EntityView.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_entity_view_using_get**
> EntityView get_tenant_entity_view_using_get(entity_view_name)

getTenantEntityView

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
api_instance = pyTB.EntityViewControllerApi(pyTB.ApiClient(configuration))
entity_view_name = 'entity_view_name_example' # str | entityViewName

try:
    # getTenantEntityView
    api_response = api_instance.get_tenant_entity_view_using_get(entity_view_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityViewControllerApi->get_tenant_entity_view_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_view_name** | **str**| entityViewName | 

### Return type

[**EntityView**](EntityView.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_entity_views_using_get**
> TextPageDataEntityView get_tenant_entity_views_using_get(limit, type=type, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getTenantEntityViews

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
api_instance = pyTB.EntityViewControllerApi(pyTB.ApiClient(configuration))
limit = 'limit_example' # str | limit
type = 'type_example' # str | type (optional)
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try:
    # getTenantEntityViews
    api_response = api_instance.get_tenant_entity_views_using_get(limit, type=type, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityViewControllerApi->get_tenant_entity_views_using_get: %s\n" % e)
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

[**TextPageDataEntityView**](TextPageDataEntityView.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_entity_views_using_get**
> TextPageDataEntityView get_user_entity_views_using_get(limit, type=type, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getUserEntityViews

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
api_instance = pyTB.EntityViewControllerApi(pyTB.ApiClient(configuration))
limit = 'limit_example' # str | limit
type = 'type_example' # str | type (optional)
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try:
    # getUserEntityViews
    api_response = api_instance.get_user_entity_views_using_get(limit, type=type, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityViewControllerApi->get_user_entity_views_using_get: %s\n" % e)
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

[**TextPageDataEntityView**](TextPageDataEntityView.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_entity_view_using_post**
> EntityView save_entity_view_using_post(body, entity_group_id=entity_group_id)

saveEntityView

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
api_instance = pyTB.EntityViewControllerApi(pyTB.ApiClient(configuration))
body = pyTB.EntityView() # EntityView | entityView
entity_group_id = 'entity_group_id_example' # str | entityGroupId (optional)

try:
    # saveEntityView
    api_response = api_instance.save_entity_view_using_post(body, entity_group_id=entity_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityViewControllerApi->save_entity_view_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntityView**](EntityView.md)| entityView | 
 **entity_group_id** | **str**| entityGroupId | [optional] 

### Return type

[**EntityView**](EntityView.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

