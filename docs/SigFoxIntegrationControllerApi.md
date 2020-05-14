# pyTB.SigFoxIntegrationControllerApi

All URIs are relative to *//dashboard.digitalconstructionhub.ovh/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**process_request_using_delete1**](SigFoxIntegrationControllerApi.md#process_request_using_delete1) | **DELETE** /api/v1/integrations/sigfox/{routingKey} | processRequest
[**process_request_using_get1**](SigFoxIntegrationControllerApi.md#process_request_using_get1) | **GET** /api/v1/integrations/sigfox/{routingKey} | processRequest
[**process_request_using_head1**](SigFoxIntegrationControllerApi.md#process_request_using_head1) | **HEAD** /api/v1/integrations/sigfox/{routingKey} | processRequest
[**process_request_using_options1**](SigFoxIntegrationControllerApi.md#process_request_using_options1) | **OPTIONS** /api/v1/integrations/sigfox/{routingKey} | processRequest
[**process_request_using_patch1**](SigFoxIntegrationControllerApi.md#process_request_using_patch1) | **PATCH** /api/v1/integrations/sigfox/{routingKey} | processRequest
[**process_request_using_post3**](SigFoxIntegrationControllerApi.md#process_request_using_post3) | **POST** /api/v1/integrations/sigfox/{routingKey} | processRequest
[**process_request_using_put1**](SigFoxIntegrationControllerApi.md#process_request_using_put1) | **PUT** /api/v1/integrations/sigfox/{routingKey} | processRequest

# **process_request_using_delete1**
> DeferredResultResponseEntity process_request_using_delete1(body, request_headers, routing_key)

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
api_instance = pyTB.SigFoxIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequest
    api_response = api_instance.process_request_using_delete1(body, request_headers, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SigFoxIntegrationControllerApi->process_request_using_delete1: %s\n" % e)
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

# **process_request_using_get1**
> DeferredResultResponseEntity process_request_using_get1(body, request_headers, routing_key)

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
api_instance = pyTB.SigFoxIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequest
    api_response = api_instance.process_request_using_get1(body, request_headers, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SigFoxIntegrationControllerApi->process_request_using_get1: %s\n" % e)
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

# **process_request_using_head1**
> DeferredResultResponseEntity process_request_using_head1(body, request_headers, routing_key)

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
api_instance = pyTB.SigFoxIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequest
    api_response = api_instance.process_request_using_head1(body, request_headers, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SigFoxIntegrationControllerApi->process_request_using_head1: %s\n" % e)
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

# **process_request_using_options1**
> DeferredResultResponseEntity process_request_using_options1(body, request_headers, routing_key)

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
api_instance = pyTB.SigFoxIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequest
    api_response = api_instance.process_request_using_options1(body, request_headers, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SigFoxIntegrationControllerApi->process_request_using_options1: %s\n" % e)
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

# **process_request_using_patch1**
> DeferredResultResponseEntity process_request_using_patch1(body, request_headers, routing_key)

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
api_instance = pyTB.SigFoxIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequest
    api_response = api_instance.process_request_using_patch1(body, request_headers, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SigFoxIntegrationControllerApi->process_request_using_patch1: %s\n" % e)
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

# **process_request_using_post3**
> DeferredResultResponseEntity process_request_using_post3(body, request_headers, routing_key)

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
api_instance = pyTB.SigFoxIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequest
    api_response = api_instance.process_request_using_post3(body, request_headers, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SigFoxIntegrationControllerApi->process_request_using_post3: %s\n" % e)
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

# **process_request_using_put1**
> DeferredResultResponseEntity process_request_using_put1(body, request_headers, routing_key)

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
api_instance = pyTB.SigFoxIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequest
    api_response = api_instance.process_request_using_put1(body, request_headers, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SigFoxIntegrationControllerApi->process_request_using_put1: %s\n" % e)
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

