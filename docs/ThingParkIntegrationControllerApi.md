# pyTB.ThingParkIntegrationControllerApi

All URIs are relative to *//dashboard.digitalconstructionhub.ovh/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**process_request_tpe_using_delete**](ThingParkIntegrationControllerApi.md#process_request_tpe_using_delete) | **DELETE** /api/v1/integrations/tpe/{routingKey}{?allRequestParams} | processRequestTPE
[**process_request_tpe_using_get**](ThingParkIntegrationControllerApi.md#process_request_tpe_using_get) | **GET** /api/v1/integrations/tpe/{routingKey}{?allRequestParams} | processRequestTPE
[**process_request_tpe_using_head**](ThingParkIntegrationControllerApi.md#process_request_tpe_using_head) | **HEAD** /api/v1/integrations/tpe/{routingKey}{?allRequestParams} | processRequestTPE
[**process_request_tpe_using_options**](ThingParkIntegrationControllerApi.md#process_request_tpe_using_options) | **OPTIONS** /api/v1/integrations/tpe/{routingKey}{?allRequestParams} | processRequestTPE
[**process_request_tpe_using_patch**](ThingParkIntegrationControllerApi.md#process_request_tpe_using_patch) | **PATCH** /api/v1/integrations/tpe/{routingKey}{?allRequestParams} | processRequestTPE
[**process_request_tpe_using_post**](ThingParkIntegrationControllerApi.md#process_request_tpe_using_post) | **POST** /api/v1/integrations/tpe/{routingKey}{?allRequestParams} | processRequestTPE
[**process_request_tpe_using_put**](ThingParkIntegrationControllerApi.md#process_request_tpe_using_put) | **PUT** /api/v1/integrations/tpe/{routingKey}{?allRequestParams} | processRequestTPE
[**process_request_using_delete3**](ThingParkIntegrationControllerApi.md#process_request_using_delete3) | **DELETE** /api/v1/integrations/thingpark/{routingKey}{?allRequestParams} | processRequest
[**process_request_using_get3**](ThingParkIntegrationControllerApi.md#process_request_using_get3) | **GET** /api/v1/integrations/thingpark/{routingKey}{?allRequestParams} | processRequest
[**process_request_using_head3**](ThingParkIntegrationControllerApi.md#process_request_using_head3) | **HEAD** /api/v1/integrations/thingpark/{routingKey}{?allRequestParams} | processRequest
[**process_request_using_options3**](ThingParkIntegrationControllerApi.md#process_request_using_options3) | **OPTIONS** /api/v1/integrations/thingpark/{routingKey}{?allRequestParams} | processRequest
[**process_request_using_patch3**](ThingParkIntegrationControllerApi.md#process_request_using_patch3) | **PATCH** /api/v1/integrations/thingpark/{routingKey}{?allRequestParams} | processRequest
[**process_request_using_post5**](ThingParkIntegrationControllerApi.md#process_request_using_post5) | **POST** /api/v1/integrations/thingpark/{routingKey}{?allRequestParams} | processRequest
[**process_request_using_put3**](ThingParkIntegrationControllerApi.md#process_request_using_put3) | **PUT** /api/v1/integrations/thingpark/{routingKey}{?allRequestParams} | processRequest

# **process_request_tpe_using_delete**
> DeferredResultResponseEntity process_request_tpe_using_delete(body, request_headers, all_request_params, routing_key)

processRequestTPE

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
api_instance = pyTB.ThingParkIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
all_request_params = pyTB.Object() # Object | allRequestParams
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequestTPE
    api_response = api_instance.process_request_tpe_using_delete(body, request_headers, all_request_params, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThingParkIntegrationControllerApi->process_request_tpe_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| msg | 
 **request_headers** | [**Object**](.md)| requestHeaders | 
 **all_request_params** | [**Object**](.md)| allRequestParams | 
 **routing_key** | **str**| routingKey | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_tpe_using_get**
> DeferredResultResponseEntity process_request_tpe_using_get(body, request_headers, all_request_params, routing_key)

processRequestTPE

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
api_instance = pyTB.ThingParkIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
all_request_params = pyTB.Object() # Object | allRequestParams
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequestTPE
    api_response = api_instance.process_request_tpe_using_get(body, request_headers, all_request_params, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThingParkIntegrationControllerApi->process_request_tpe_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| msg | 
 **request_headers** | [**Object**](.md)| requestHeaders | 
 **all_request_params** | [**Object**](.md)| allRequestParams | 
 **routing_key** | **str**| routingKey | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_tpe_using_head**
> DeferredResultResponseEntity process_request_tpe_using_head(body, request_headers, all_request_params, routing_key)

processRequestTPE

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
api_instance = pyTB.ThingParkIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
all_request_params = pyTB.Object() # Object | allRequestParams
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequestTPE
    api_response = api_instance.process_request_tpe_using_head(body, request_headers, all_request_params, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThingParkIntegrationControllerApi->process_request_tpe_using_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| msg | 
 **request_headers** | [**Object**](.md)| requestHeaders | 
 **all_request_params** | [**Object**](.md)| allRequestParams | 
 **routing_key** | **str**| routingKey | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_tpe_using_options**
> DeferredResultResponseEntity process_request_tpe_using_options(body, request_headers, all_request_params, routing_key)

processRequestTPE

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
api_instance = pyTB.ThingParkIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
all_request_params = pyTB.Object() # Object | allRequestParams
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequestTPE
    api_response = api_instance.process_request_tpe_using_options(body, request_headers, all_request_params, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThingParkIntegrationControllerApi->process_request_tpe_using_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| msg | 
 **request_headers** | [**Object**](.md)| requestHeaders | 
 **all_request_params** | [**Object**](.md)| allRequestParams | 
 **routing_key** | **str**| routingKey | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_tpe_using_patch**
> DeferredResultResponseEntity process_request_tpe_using_patch(body, request_headers, all_request_params, routing_key)

processRequestTPE

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
api_instance = pyTB.ThingParkIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
all_request_params = pyTB.Object() # Object | allRequestParams
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequestTPE
    api_response = api_instance.process_request_tpe_using_patch(body, request_headers, all_request_params, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThingParkIntegrationControllerApi->process_request_tpe_using_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| msg | 
 **request_headers** | [**Object**](.md)| requestHeaders | 
 **all_request_params** | [**Object**](.md)| allRequestParams | 
 **routing_key** | **str**| routingKey | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_tpe_using_post**
> DeferredResultResponseEntity process_request_tpe_using_post(body, request_headers, all_request_params, routing_key)

processRequestTPE

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
api_instance = pyTB.ThingParkIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
all_request_params = pyTB.Object() # Object | allRequestParams
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequestTPE
    api_response = api_instance.process_request_tpe_using_post(body, request_headers, all_request_params, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThingParkIntegrationControllerApi->process_request_tpe_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| msg | 
 **request_headers** | [**Object**](.md)| requestHeaders | 
 **all_request_params** | [**Object**](.md)| allRequestParams | 
 **routing_key** | **str**| routingKey | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_tpe_using_put**
> DeferredResultResponseEntity process_request_tpe_using_put(body, request_headers, all_request_params, routing_key)

processRequestTPE

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
api_instance = pyTB.ThingParkIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
all_request_params = pyTB.Object() # Object | allRequestParams
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequestTPE
    api_response = api_instance.process_request_tpe_using_put(body, request_headers, all_request_params, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThingParkIntegrationControllerApi->process_request_tpe_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| msg | 
 **request_headers** | [**Object**](.md)| requestHeaders | 
 **all_request_params** | [**Object**](.md)| allRequestParams | 
 **routing_key** | **str**| routingKey | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_using_delete3**
> DeferredResultResponseEntity process_request_using_delete3(body, request_headers, all_request_params, routing_key)

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
api_instance = pyTB.ThingParkIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
all_request_params = pyTB.Object() # Object | allRequestParams
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequest
    api_response = api_instance.process_request_using_delete3(body, request_headers, all_request_params, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThingParkIntegrationControllerApi->process_request_using_delete3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| msg | 
 **request_headers** | [**Object**](.md)| requestHeaders | 
 **all_request_params** | [**Object**](.md)| allRequestParams | 
 **routing_key** | **str**| routingKey | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_using_get3**
> DeferredResultResponseEntity process_request_using_get3(body, request_headers, all_request_params, routing_key)

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
api_instance = pyTB.ThingParkIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
all_request_params = pyTB.Object() # Object | allRequestParams
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequest
    api_response = api_instance.process_request_using_get3(body, request_headers, all_request_params, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThingParkIntegrationControllerApi->process_request_using_get3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| msg | 
 **request_headers** | [**Object**](.md)| requestHeaders | 
 **all_request_params** | [**Object**](.md)| allRequestParams | 
 **routing_key** | **str**| routingKey | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_using_head3**
> DeferredResultResponseEntity process_request_using_head3(body, request_headers, all_request_params, routing_key)

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
api_instance = pyTB.ThingParkIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
all_request_params = pyTB.Object() # Object | allRequestParams
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequest
    api_response = api_instance.process_request_using_head3(body, request_headers, all_request_params, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThingParkIntegrationControllerApi->process_request_using_head3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| msg | 
 **request_headers** | [**Object**](.md)| requestHeaders | 
 **all_request_params** | [**Object**](.md)| allRequestParams | 
 **routing_key** | **str**| routingKey | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_using_options3**
> DeferredResultResponseEntity process_request_using_options3(body, request_headers, all_request_params, routing_key)

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
api_instance = pyTB.ThingParkIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
all_request_params = pyTB.Object() # Object | allRequestParams
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequest
    api_response = api_instance.process_request_using_options3(body, request_headers, all_request_params, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThingParkIntegrationControllerApi->process_request_using_options3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| msg | 
 **request_headers** | [**Object**](.md)| requestHeaders | 
 **all_request_params** | [**Object**](.md)| allRequestParams | 
 **routing_key** | **str**| routingKey | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_using_patch3**
> DeferredResultResponseEntity process_request_using_patch3(body, request_headers, all_request_params, routing_key)

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
api_instance = pyTB.ThingParkIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
all_request_params = pyTB.Object() # Object | allRequestParams
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequest
    api_response = api_instance.process_request_using_patch3(body, request_headers, all_request_params, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThingParkIntegrationControllerApi->process_request_using_patch3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| msg | 
 **request_headers** | [**Object**](.md)| requestHeaders | 
 **all_request_params** | [**Object**](.md)| allRequestParams | 
 **routing_key** | **str**| routingKey | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_using_post5**
> DeferredResultResponseEntity process_request_using_post5(body, request_headers, all_request_params, routing_key)

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
api_instance = pyTB.ThingParkIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
all_request_params = pyTB.Object() # Object | allRequestParams
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequest
    api_response = api_instance.process_request_using_post5(body, request_headers, all_request_params, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThingParkIntegrationControllerApi->process_request_using_post5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| msg | 
 **request_headers** | [**Object**](.md)| requestHeaders | 
 **all_request_params** | [**Object**](.md)| allRequestParams | 
 **routing_key** | **str**| routingKey | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_request_using_put3**
> DeferredResultResponseEntity process_request_using_put3(body, request_headers, all_request_params, routing_key)

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
api_instance = pyTB.ThingParkIntegrationControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | msg
request_headers = pyTB.Object() # Object | requestHeaders
all_request_params = pyTB.Object() # Object | allRequestParams
routing_key = 'routing_key_example' # str | routingKey

try:
    # processRequest
    api_response = api_instance.process_request_using_put3(body, request_headers, all_request_params, routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThingParkIntegrationControllerApi->process_request_using_put3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| msg | 
 **request_headers** | [**Object**](.md)| requestHeaders | 
 **all_request_params** | [**Object**](.md)| allRequestParams | 
 **routing_key** | **str**| routingKey | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

