# pyTB.DashboardControllerApi

All URIs are relative to *//dashboard.digitalconstructionhub.ovh/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_dashboard_using_delete**](DashboardControllerApi.md#delete_dashboard_using_delete) | **DELETE** /api/dashboard/{dashboardId} | deleteDashboard
[**get_dashboard_by_id_using_get**](DashboardControllerApi.md#get_dashboard_by_id_using_get) | **GET** /api/dashboard/{dashboardId} | getDashboardById
[**get_dashboard_info_by_id_using_get**](DashboardControllerApi.md#get_dashboard_info_by_id_using_get) | **GET** /api/dashboard/info/{dashboardId} | getDashboardInfoById
[**get_dashboards_by_entity_group_id_using_get**](DashboardControllerApi.md#get_dashboards_by_entity_group_id_using_get) | **GET** /api/entityGroup/{entityGroupId}/dashboards{?limit,startTime,endTime,ascOrder,offset} | getDashboardsByEntityGroupId
[**get_dashboards_by_ids_using_get**](DashboardControllerApi.md#get_dashboards_by_ids_using_get) | **GET** /api/dashboards{?dashboardIds} | getDashboardsByIds
[**get_group_dashboards_using_get**](DashboardControllerApi.md#get_group_dashboards_using_get) | **GET** /api/entityGroup/{entityGroupId}/dashboards{?textSearch,idOffset,textOffset,limit} | getGroupDashboards
[**get_max_datapoints_limit_using_get**](DashboardControllerApi.md#get_max_datapoints_limit_using_get) | **GET** /api/dashboard/maxDatapointsLimit | getMaxDatapointsLimit
[**get_server_time_using_get**](DashboardControllerApi.md#get_server_time_using_get) | **GET** /api/dashboard/serverTime | getServerTime
[**get_tenant_dashboards_using_get**](DashboardControllerApi.md#get_tenant_dashboards_using_get) | **GET** /api/tenant/dashboards{?textSearch,idOffset,textOffset,limit} | getTenantDashboards
[**get_tenant_dashboards_using_get1**](DashboardControllerApi.md#get_tenant_dashboards_using_get1) | **GET** /api/tenant/{tenantId}/dashboards{?textSearch,idOffset,textOffset,limit} | getTenantDashboards
[**get_user_dashboards_using_get**](DashboardControllerApi.md#get_user_dashboards_using_get) | **GET** /api/user/dashboards{?textSearch,idOffset,textOffset,operation,userId,limit} | getUserDashboards
[**save_dashboard_using_post**](DashboardControllerApi.md#save_dashboard_using_post) | **POST** /api/dashboard{?entityGroupId} | saveDashboard

# **delete_dashboard_using_delete**
> delete_dashboard_using_delete(dashboard_id)

deleteDashboard

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
api_instance = pyTB.DashboardControllerApi(pyTB.ApiClient(configuration))
dashboard_id = 'dashboard_id_example' # str | dashboardId

try:
    # deleteDashboard
    api_instance.delete_dashboard_using_delete(dashboard_id)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->delete_dashboard_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| dashboardId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_by_id_using_get**
> Dashboard get_dashboard_by_id_using_get(dashboard_id)

getDashboardById

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
api_instance = pyTB.DashboardControllerApi(pyTB.ApiClient(configuration))
dashboard_id = 'dashboard_id_example' # str | dashboardId

try:
    # getDashboardById
    api_response = api_instance.get_dashboard_by_id_using_get(dashboard_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->get_dashboard_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| dashboardId | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_info_by_id_using_get**
> DashboardInfo get_dashboard_info_by_id_using_get(dashboard_id)

getDashboardInfoById

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
api_instance = pyTB.DashboardControllerApi(pyTB.ApiClient(configuration))
dashboard_id = 'dashboard_id_example' # str | dashboardId

try:
    # getDashboardInfoById
    api_response = api_instance.get_dashboard_info_by_id_using_get(dashboard_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->get_dashboard_info_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| dashboardId | 

### Return type

[**DashboardInfo**](DashboardInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboards_by_entity_group_id_using_get**
> TimePageDataDashboardInfo get_dashboards_by_entity_group_id_using_get(entity_group_id, limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset)

getDashboardsByEntityGroupId

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
api_instance = pyTB.DashboardControllerApi(pyTB.ApiClient(configuration))
entity_group_id = 'entity_group_id_example' # str | entityGroupId
limit = 56 # int | Page link limit
start_time = 789 # int | startTime (optional)
end_time = 789 # int | endTime (optional)
asc_order = true # bool | ascOrder (optional)
offset = 'offset_example' # str | offset (optional)

try:
    # getDashboardsByEntityGroupId
    api_response = api_instance.get_dashboards_by_entity_group_id_using_get(entity_group_id, limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->get_dashboards_by_entity_group_id_using_get: %s\n" % e)
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

[**TimePageDataDashboardInfo**](TimePageDataDashboardInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboards_by_ids_using_get**
> list[DashboardInfo] get_dashboards_by_ids_using_get(dashboard_ids)

getDashboardsByIds

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
api_instance = pyTB.DashboardControllerApi(pyTB.ApiClient(configuration))
dashboard_ids = 'dashboard_ids_example' # str | dashboardIds

try:
    # getDashboardsByIds
    api_response = api_instance.get_dashboards_by_ids_using_get(dashboard_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->get_dashboards_by_ids_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_ids** | **str**| dashboardIds | 

### Return type

[**list[DashboardInfo]**](DashboardInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_dashboards_using_get**
> TextPageDataDashboardInfo get_group_dashboards_using_get(entity_group_id, limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getGroupDashboards

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
api_instance = pyTB.DashboardControllerApi(pyTB.ApiClient(configuration))
entity_group_id = 'entity_group_id_example' # str | entityGroupId
limit = 'limit_example' # str | limit
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try:
    # getGroupDashboards
    api_response = api_instance.get_group_dashboards_using_get(entity_group_id, limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->get_group_dashboards_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_group_id** | **str**| entityGroupId | 
 **limit** | **str**| limit | 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataDashboardInfo**](TextPageDataDashboardInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_max_datapoints_limit_using_get**
> int get_max_datapoints_limit_using_get()

getMaxDatapointsLimit

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
api_instance = pyTB.DashboardControllerApi(pyTB.ApiClient(configuration))

try:
    # getMaxDatapointsLimit
    api_response = api_instance.get_max_datapoints_limit_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->get_max_datapoints_limit_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**int**

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_time_using_get**
> int get_server_time_using_get()

getServerTime

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
api_instance = pyTB.DashboardControllerApi(pyTB.ApiClient(configuration))

try:
    # getServerTime
    api_response = api_instance.get_server_time_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->get_server_time_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**int**

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_dashboards_using_get**
> TextPageDataDashboardInfo get_tenant_dashboards_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getTenantDashboards

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
api_instance = pyTB.DashboardControllerApi(pyTB.ApiClient(configuration))
limit = 'limit_example' # str | limit
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try:
    # getTenantDashboards
    api_response = api_instance.get_tenant_dashboards_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->get_tenant_dashboards_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| limit | 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataDashboardInfo**](TextPageDataDashboardInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_dashboards_using_get1**
> TextPageDataDashboardInfo get_tenant_dashboards_using_get1(tenant_id, limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getTenantDashboards

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
api_instance = pyTB.DashboardControllerApi(pyTB.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | tenantId
limit = 'limit_example' # str | limit
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try:
    # getTenantDashboards
    api_response = api_instance.get_tenant_dashboards_using_get1(tenant_id, limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->get_tenant_dashboards_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenantId | 
 **limit** | **str**| limit | 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataDashboardInfo**](TextPageDataDashboardInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_dashboards_using_get**
> TextPageDataDashboardInfo get_user_dashboards_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset, operation=operation, user_id=user_id)

getUserDashboards

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
api_instance = pyTB.DashboardControllerApi(pyTB.ApiClient(configuration))
limit = 'limit_example' # str | limit
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)
operation = 'operation_example' # str | operation (optional)
user_id = 'user_id_example' # str | userId (optional)

try:
    # getUserDashboards
    api_response = api_instance.get_user_dashboards_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset, operation=operation, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->get_user_dashboards_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| limit | 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 
 **operation** | **str**| operation | [optional] 
 **user_id** | **str**| userId | [optional] 

### Return type

[**TextPageDataDashboardInfo**](TextPageDataDashboardInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_dashboard_using_post**
> Dashboard save_dashboard_using_post(body, entity_group_id=entity_group_id)

saveDashboard

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
api_instance = pyTB.DashboardControllerApi(pyTB.ApiClient(configuration))
body = pyTB.Dashboard() # Dashboard | dashboard
entity_group_id = 'entity_group_id_example' # str | entityGroupId (optional)

try:
    # saveDashboard
    api_response = api_instance.save_dashboard_using_post(body, entity_group_id=entity_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardControllerApi->save_dashboard_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Dashboard**](Dashboard.md)| dashboard | 
 **entity_group_id** | **str**| entityGroupId | [optional] 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

