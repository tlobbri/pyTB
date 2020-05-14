# pyTB.AuditLogControllerApi

All URIs are relative to *//dashboard.digitalconstructionhub.ovh/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audit_logs_by_customer_id_using_get**](AuditLogControllerApi.md#get_audit_logs_by_customer_id_using_get) | **GET** /api/audit/logs/customer/{customerId}{?startTime,endTime,ascOrder,offset,actionTypes,limit} | getAuditLogsByCustomerId
[**get_audit_logs_by_entity_id_using_get**](AuditLogControllerApi.md#get_audit_logs_by_entity_id_using_get) | **GET** /api/audit/logs/entity/{entityType}/{entityId}{?startTime,endTime,ascOrder,offset,actionTypes,limit} | getAuditLogsByEntityId
[**get_audit_logs_by_user_id_using_get**](AuditLogControllerApi.md#get_audit_logs_by_user_id_using_get) | **GET** /api/audit/logs/user/{userId}{?startTime,endTime,ascOrder,offset,actionTypes,limit} | getAuditLogsByUserId
[**get_audit_logs_using_get**](AuditLogControllerApi.md#get_audit_logs_using_get) | **GET** /api/audit/logs{?startTime,endTime,ascOrder,offset,actionTypes,limit} | getAuditLogs

# **get_audit_logs_by_customer_id_using_get**
> TimePageDataAuditLog get_audit_logs_by_customer_id_using_get(customer_id, limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset, action_types=action_types)

getAuditLogsByCustomerId

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
api_instance = pyTB.AuditLogControllerApi(pyTB.ApiClient(configuration))
customer_id = 'customer_id_example' # str | customerId
limit = 'limit_example' # str | limit
start_time = 789 # int | startTime (optional)
end_time = 789 # int | endTime (optional)
asc_order = true # bool | ascOrder (optional)
offset = 'offset_example' # str | offset (optional)
action_types = 'action_types_example' # str | actionTypes (optional)

try:
    # getAuditLogsByCustomerId
    api_response = api_instance.get_audit_logs_by_customer_id_using_get(customer_id, limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset, action_types=action_types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditLogControllerApi->get_audit_logs_by_customer_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| customerId | 
 **limit** | **str**| limit | 
 **start_time** | **int**| startTime | [optional] 
 **end_time** | **int**| endTime | [optional] 
 **asc_order** | **bool**| ascOrder | [optional] 
 **offset** | **str**| offset | [optional] 
 **action_types** | **str**| actionTypes | [optional] 

### Return type

[**TimePageDataAuditLog**](TimePageDataAuditLog.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_logs_by_entity_id_using_get**
> TimePageDataAuditLog get_audit_logs_by_entity_id_using_get(entity_type, entity_id, limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset, action_types=action_types)

getAuditLogsByEntityId

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
api_instance = pyTB.AuditLogControllerApi(pyTB.ApiClient(configuration))
entity_type = 'entity_type_example' # str | entityType
entity_id = 'entity_id_example' # str | entityId
limit = 'limit_example' # str | limit
start_time = 789 # int | startTime (optional)
end_time = 789 # int | endTime (optional)
asc_order = true # bool | ascOrder (optional)
offset = 'offset_example' # str | offset (optional)
action_types = 'action_types_example' # str | actionTypes (optional)

try:
    # getAuditLogsByEntityId
    api_response = api_instance.get_audit_logs_by_entity_id_using_get(entity_type, entity_id, limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset, action_types=action_types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditLogControllerApi->get_audit_logs_by_entity_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| entityType | 
 **entity_id** | **str**| entityId | 
 **limit** | **str**| limit | 
 **start_time** | **int**| startTime | [optional] 
 **end_time** | **int**| endTime | [optional] 
 **asc_order** | **bool**| ascOrder | [optional] 
 **offset** | **str**| offset | [optional] 
 **action_types** | **str**| actionTypes | [optional] 

### Return type

[**TimePageDataAuditLog**](TimePageDataAuditLog.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_logs_by_user_id_using_get**
> TimePageDataAuditLog get_audit_logs_by_user_id_using_get(user_id, limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset, action_types=action_types)

getAuditLogsByUserId

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
api_instance = pyTB.AuditLogControllerApi(pyTB.ApiClient(configuration))
user_id = 'user_id_example' # str | userId
limit = 'limit_example' # str | limit
start_time = 789 # int | startTime (optional)
end_time = 789 # int | endTime (optional)
asc_order = true # bool | ascOrder (optional)
offset = 'offset_example' # str | offset (optional)
action_types = 'action_types_example' # str | actionTypes (optional)

try:
    # getAuditLogsByUserId
    api_response = api_instance.get_audit_logs_by_user_id_using_get(user_id, limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset, action_types=action_types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditLogControllerApi->get_audit_logs_by_user_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| userId | 
 **limit** | **str**| limit | 
 **start_time** | **int**| startTime | [optional] 
 **end_time** | **int**| endTime | [optional] 
 **asc_order** | **bool**| ascOrder | [optional] 
 **offset** | **str**| offset | [optional] 
 **action_types** | **str**| actionTypes | [optional] 

### Return type

[**TimePageDataAuditLog**](TimePageDataAuditLog.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_logs_using_get**
> TimePageDataAuditLog get_audit_logs_using_get(limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset, action_types=action_types)

getAuditLogs

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
api_instance = pyTB.AuditLogControllerApi(pyTB.ApiClient(configuration))
limit = 'limit_example' # str | limit
start_time = 789 # int | startTime (optional)
end_time = 789 # int | endTime (optional)
asc_order = true # bool | ascOrder (optional)
offset = 'offset_example' # str | offset (optional)
action_types = 'action_types_example' # str | actionTypes (optional)

try:
    # getAuditLogs
    api_response = api_instance.get_audit_logs_using_get(limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset, action_types=action_types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditLogControllerApi->get_audit_logs_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| limit | 
 **start_time** | **int**| startTime | [optional] 
 **end_time** | **int**| endTime | [optional] 
 **asc_order** | **bool**| ascOrder | [optional] 
 **offset** | **str**| offset | [optional] 
 **action_types** | **str**| actionTypes | [optional] 

### Return type

[**TimePageDataAuditLog**](TimePageDataAuditLog.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

