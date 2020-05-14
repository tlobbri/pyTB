# pyTB.OceanConnectIntegrationControllerApi

All URIs are relative to *//dashboard.digitalconstructionhub.ovh/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**process_request_using_delete**](OceanConnectIntegrationControllerApi.md#process_request_using_delete) | **DELETE** /api/v1/integrations/oceanconnect/{routingKey} | processRequest
[**process_request_using_get**](OceanConnectIntegrationControllerApi.md#process_request_using_get) | **GET** /api/v1/integrations/oceanconnect/{routingKey} | processRequest
[**process_request_using_head**](OceanConnectIntegrationControllerApi.md#process_request_using_head) | **HEAD** /api/v1/integrations/oceanconnect/{routingKey} | processRequest
[**process_request_using_options**](OceanConnectIntegrationControllerApi.md#process_request_using_options) | **OPTIONS** /api/v1/integrations/oceanconnect/{routingKey} | processRequest
[**process_request_using_patch**](OceanConnectIntegrationControllerApi.md#process_request_using_patch) | **PATCH** /api/v1/integrations/oceanconnect/{routingKey} | processRequest
[**process_request_using_post2**](OceanConnectIntegrationControllerApi.md#process_request_using_post2) | **POST** /api/v1/integrations/oceanconnect/{routingKey} | processRequest
[**process_request_using_put**](OceanConnectIntegrationControllerApi.md#process_request_using_put) | **PUT** /api/v1/integrations/oceanconnect/{routingKey} | processRequest

# **process_request_using_delete**
> DeferredResultResponseEntity process_request_using_delete(body, request_headers, routing_key)

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
api_instance = pyTB.OceanConnectIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequest
    api_response = api_instance.process_request_using_delete(body, request_headers, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OceanConnectIntegrationControllerApi->process_request_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| msg | 
 **request_headers** | [**Object**](.md)| requestHeaders | 
 **routing_key** | **str**| routingKey | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_using_get**
> DeferredResultResponseEntity process_request_using_get(body, request_headers, routing_key)

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
api_instance = pyTB.OceanConnectIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequest
    api_response = api_instance.process_request_using_get(body, request_headers, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OceanConnectIntegrationControllerApi->process_request_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| msg | 
 **request_headers** | [**Object**](.md)| requestHeaders | 
 **routing_key** | **str**| routingKey | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_using_head**
> DeferredResultResponseEntity process_request_using_head(body, request_headers, routing_key)

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
api_instance = pyTB.OceanConnectIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequest
    api_response = api_instance.process_request_using_head(body, request_headers, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OceanConnectIntegrationControllerApi->process_request_using_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| msg | 
 **request_headers** | [**Object**](.md)| requestHeaders | 
 **routing_key** | **str**| routingKey | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_using_options**
> DeferredResultResponseEntity process_request_using_options(body, request_headers, routing_key)

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
api_instance = pyTB.OceanConnectIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequest
    api_response = api_instance.process_request_using_options(body, request_headers, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OceanConnectIntegrationControllerApi->process_request_using_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| msg | 
 **request_headers** | [**Object**](.md)| requestHeaders | 
 **routing_key** | **str**| routingKey | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_using_patch**
> DeferredResultResponseEntity process_request_using_patch(body, request_headers, routing_key)

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
api_instance = pyTB.OceanConnectIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequest
    api_response = api_instance.process_request_using_patch(body, request_headers, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OceanConnectIntegrationControllerApi->process_request_using_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| msg | 
 **request_headers** | [**Object**](.md)| requestHeaders | 
 **routing_key** | **str**| routingKey | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_using_post2**
> DeferredResultResponseEntity process_request_using_post2(body, request_headers, routing_key)

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
api_instance = pyTB.OceanConnectIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequest
    api_response = api_instance.process_request_using_post2(body, request_headers, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OceanConnectIntegrationControllerApi->process_request_using_post2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| msg | 
 **request_headers** | [**Object**](.md)| requestHeaders | 
 **routing_key** | **str**| routingKey | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_using_put**
> DeferredResultResponseEntity process_request_using_put(body, request_headers, routing_key)

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
api_instance = pyTB.OceanConnectIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequest
    api_response = api_instance.process_request_using_put(body, request_headers, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OceanConnectIntegrationControllerApi->process_request_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| msg | 
 **request_headers** | [**Object**](.md)| requestHeaders | 
 **routing_key** | **str**| routingKey | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

