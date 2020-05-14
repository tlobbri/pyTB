# pyTB.HttpIntegrationControllerApi

All URIs are relative to *//dashboard.digitalconstructionhub.ovh/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_status_using_get**](HttpIntegrationControllerApi.md#check_status_using_get) | **GET** /api/v1/integrations/http/{routingKey}{?requestParams} | checkStatus
[**process_request_using_post**](HttpIntegrationControllerApi.md#process_request_using_post) | **POST** /api/v1/integrations/http/{routingKey} | processRequest
[**process_request_using_post1**](HttpIntegrationControllerApi.md#process_request_using_post1) | **POST** /api/v1/integrations/http/{routingKey}/{suffix} | processRequest

# **check_status_using_get**
> DeferredResultResponseEntity check_status_using_get(routing_key, request_params, request_headers)

checkStatus

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
api_instance = pyTB.HttpIntegrationControllerApi(pyTB.ApiClient(configuration))
routing_key = 'routing_key_example' # str | routingKey
request_params = pyTB.Object() # Object | requestParams
request_headers = pyTB.Object() # Object | requestHeaders

try:
    # checkStatus
    api_response = api_instance.check_status_using_get(routing_key, request_params, request_headers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HttpIntegrationControllerApi->check_status_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **routing_key** | **str**| routingKey | 
 **request_params** | [**Object**](.md)| requestParams | 
 **request_headers** | [**Object**](.md)| requestHeaders | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_using_post**
> DeferredResultResponseEntity process_request_using_post(body, request_headers, routing_key, suffix)

processRequest

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
api_instance = pyTB.HttpIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
routing_key = 'routing_key_example' # str | routingKey
suffix = 'suffix_example' # str | suffix

try:
    # processRequest
    api_response = api_instance.process_request_using_post(body, request_headers, routing_key, suffix)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HttpIntegrationControllerApi->process_request_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| msg | 
 **request_headers** | [**Object**](.md)| requestHeaders | 
 **routing_key** | **str**| routingKey | 
 **suffix** | **str**| suffix | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_using_post1**
> DeferredResultResponseEntity process_request_using_post1(body, request_headers, routing_key, suffix)

processRequest

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
api_instance = pyTB.HttpIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
routing_key = 'routing_key_example' # str | routingKey
suffix = 'suffix_example' # str | suffix

try:
    # processRequest
    api_response = api_instance.process_request_using_post1(body, request_headers, routing_key, suffix)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HttpIntegrationControllerApi->process_request_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| msg | 
 **request_headers** | [**Object**](.md)| requestHeaders | 
 **routing_key** | **str**| routingKey | 
 **suffix** | **str**| suffix | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

