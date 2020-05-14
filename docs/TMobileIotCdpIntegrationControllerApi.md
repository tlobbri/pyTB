# pyTB.TMobileIotCdpIntegrationControllerApi

All URIs are relative to *//dashboard.digitalconstructionhub.ovh/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**process_request_using_delete2**](TMobileIotCdpIntegrationControllerApi.md#process_request_using_delete2) | **DELETE** /api/v1/integrations/tmobile_iot_cdp/{routingKey} | processRequest
[**process_request_using_get2**](TMobileIotCdpIntegrationControllerApi.md#process_request_using_get2) | **GET** /api/v1/integrations/tmobile_iot_cdp/{routingKey} | processRequest
[**process_request_using_head2**](TMobileIotCdpIntegrationControllerApi.md#process_request_using_head2) | **HEAD** /api/v1/integrations/tmobile_iot_cdp/{routingKey} | processRequest
[**process_request_using_options2**](TMobileIotCdpIntegrationControllerApi.md#process_request_using_options2) | **OPTIONS** /api/v1/integrations/tmobile_iot_cdp/{routingKey} | processRequest
[**process_request_using_patch2**](TMobileIotCdpIntegrationControllerApi.md#process_request_using_patch2) | **PATCH** /api/v1/integrations/tmobile_iot_cdp/{routingKey} | processRequest
[**process_request_using_post4**](TMobileIotCdpIntegrationControllerApi.md#process_request_using_post4) | **POST** /api/v1/integrations/tmobile_iot_cdp/{routingKey} | processRequest
[**process_request_using_put2**](TMobileIotCdpIntegrationControllerApi.md#process_request_using_put2) | **PUT** /api/v1/integrations/tmobile_iot_cdp/{routingKey} | processRequest

# **process_request_using_delete2**
> DeferredResultResponseEntity process_request_using_delete2(body, request_headers, routing_key)

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
api_instance = pyTB.TMobileIotCdpIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequest
    api_response = api_instance.process_request_using_delete2(body, request_headers, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TMobileIotCdpIntegrationControllerApi->process_request_using_delete2: %s\n" % e)
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

# **process_request_using_get2**
> DeferredResultResponseEntity process_request_using_get2(body, request_headers, routing_key)

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
api_instance = pyTB.TMobileIotCdpIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequest
    api_response = api_instance.process_request_using_get2(body, request_headers, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TMobileIotCdpIntegrationControllerApi->process_request_using_get2: %s\n" % e)
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

# **process_request_using_head2**
> DeferredResultResponseEntity process_request_using_head2(body, request_headers, routing_key)

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
api_instance = pyTB.TMobileIotCdpIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequest
    api_response = api_instance.process_request_using_head2(body, request_headers, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TMobileIotCdpIntegrationControllerApi->process_request_using_head2: %s\n" % e)
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

# **process_request_using_options2**
> DeferredResultResponseEntity process_request_using_options2(body, request_headers, routing_key)

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
api_instance = pyTB.TMobileIotCdpIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequest
    api_response = api_instance.process_request_using_options2(body, request_headers, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TMobileIotCdpIntegrationControllerApi->process_request_using_options2: %s\n" % e)
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

# **process_request_using_patch2**
> DeferredResultResponseEntity process_request_using_patch2(body, request_headers, routing_key)

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
api_instance = pyTB.TMobileIotCdpIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequest
    api_response = api_instance.process_request_using_patch2(body, request_headers, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TMobileIotCdpIntegrationControllerApi->process_request_using_patch2: %s\n" % e)
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

# **process_request_using_post4**
> DeferredResultResponseEntity process_request_using_post4(body, request_headers, routing_key)

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
api_instance = pyTB.TMobileIotCdpIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequest
    api_response = api_instance.process_request_using_post4(body, request_headers, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TMobileIotCdpIntegrationControllerApi->process_request_using_post4: %s\n" % e)
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

# **process_request_using_put2**
> DeferredResultResponseEntity process_request_using_put2(body, request_headers, routing_key)

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
api_instance = pyTB.TMobileIotCdpIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequest
    api_response = api_instance.process_request_using_put2(body, request_headers, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TMobileIotCdpIntegrationControllerApi->process_request_using_put2: %s\n" % e)
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

