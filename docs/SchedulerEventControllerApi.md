# pyTB.SchedulerEventControllerApi

All URIs are relative to *//dashboard.digitalconstructionhub.ovh/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_scheduler_event_using_delete**](SchedulerEventControllerApi.md#delete_scheduler_event_using_delete) | **DELETE** /api/schedulerEvent/{schedulerEventId} | deleteSchedulerEvent
[**get_scheduler_event_by_id_using_get**](SchedulerEventControllerApi.md#get_scheduler_event_by_id_using_get) | **GET** /api/schedulerEvent/{schedulerEventId} | getSchedulerEventById
[**get_scheduler_event_info_by_id_using_get**](SchedulerEventControllerApi.md#get_scheduler_event_info_by_id_using_get) | **GET** /api/schedulerEvent/info/{schedulerEventId} | getSchedulerEventInfoById
[**get_scheduler_events_by_ids_using_get**](SchedulerEventControllerApi.md#get_scheduler_events_by_ids_using_get) | **GET** /api/schedulerEvents{?schedulerEventIds} | getSchedulerEventsByIds
[**get_scheduler_events_using_get**](SchedulerEventControllerApi.md#get_scheduler_events_using_get) | **GET** /api/schedulerEvents{?type} | getSchedulerEvents
[**save_scheduler_event_using_post**](SchedulerEventControllerApi.md#save_scheduler_event_using_post) | **POST** /api/schedulerEvent | saveSchedulerEvent

# **delete_scheduler_event_using_delete**
> delete_scheduler_event_using_delete(scheduler_event_id)

deleteSchedulerEvent

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
api_instance = pyTB.SchedulerEventControllerApi(pyTB.ApiClient(configuration))
scheduler_event_id = 'scheduler_event_id_example' # str | schedulerEventId

try:
    # deleteSchedulerEvent
    api_instance.delete_scheduler_event_using_delete(scheduler_event_id)
except ApiException as e:
    print("Exception when calling SchedulerEventControllerApi->delete_scheduler_event_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduler_event_id** | **str**| schedulerEventId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheduler_event_by_id_using_get**
> SchedulerEvent get_scheduler_event_by_id_using_get(scheduler_event_id)

getSchedulerEventById

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
api_instance = pyTB.SchedulerEventControllerApi(pyTB.ApiClient(configuration))
scheduler_event_id = 'scheduler_event_id_example' # str | schedulerEventId

try:
    # getSchedulerEventById
    api_response = api_instance.get_scheduler_event_by_id_using_get(scheduler_event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchedulerEventControllerApi->get_scheduler_event_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduler_event_id** | **str**| schedulerEventId | 

### Return type

[**SchedulerEvent**](SchedulerEvent.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheduler_event_info_by_id_using_get**
> SchedulerEventInfo get_scheduler_event_info_by_id_using_get(scheduler_event_id)

getSchedulerEventInfoById

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
api_instance = pyTB.SchedulerEventControllerApi(pyTB.ApiClient(configuration))
scheduler_event_id = 'scheduler_event_id_example' # str | schedulerEventId

try:
    # getSchedulerEventInfoById
    api_response = api_instance.get_scheduler_event_info_by_id_using_get(scheduler_event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchedulerEventControllerApi->get_scheduler_event_info_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduler_event_id** | **str**| schedulerEventId | 

### Return type

[**SchedulerEventInfo**](SchedulerEventInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheduler_events_by_ids_using_get**
> list[SchedulerEventInfo] get_scheduler_events_by_ids_using_get(scheduler_event_ids)

getSchedulerEventsByIds

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
api_instance = pyTB.SchedulerEventControllerApi(pyTB.ApiClient(configuration))
scheduler_event_ids = 'scheduler_event_ids_example' # str | schedulerEventIds

try:
    # getSchedulerEventsByIds
    api_response = api_instance.get_scheduler_events_by_ids_using_get(scheduler_event_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchedulerEventControllerApi->get_scheduler_events_by_ids_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduler_event_ids** | **str**| schedulerEventIds | 

### Return type

[**list[SchedulerEventInfo]**](SchedulerEventInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheduler_events_using_get**
> list[SchedulerEventInfo] get_scheduler_events_using_get(type=type)

getSchedulerEvents

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
api_instance = pyTB.SchedulerEventControllerApi(pyTB.ApiClient(configuration))
type = 'type_example' # str | type (optional)

try:
    # getSchedulerEvents
    api_response = api_instance.get_scheduler_events_using_get(type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchedulerEventControllerApi->get_scheduler_events_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| type | [optional] 

### Return type

[**list[SchedulerEventInfo]**](SchedulerEventInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_scheduler_event_using_post**
> SchedulerEvent save_scheduler_event_using_post(body)

saveSchedulerEvent

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
api_instance = pyTB.SchedulerEventControllerApi(pyTB.ApiClient(configuration))
body = pyTB.SchedulerEvent() # SchedulerEvent | schedulerEvent

try:
    # saveSchedulerEvent
    api_response = api_instance.save_scheduler_event_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchedulerEventControllerApi->save_scheduler_event_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SchedulerEvent**](SchedulerEvent.md)| schedulerEvent | 

### Return type

[**SchedulerEvent**](SchedulerEvent.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

