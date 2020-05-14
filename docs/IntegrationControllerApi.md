# pyTB.IntegrationControllerApi

All URIs are relative to *//dashboard.digitalconstructionhub.ovh/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_integration_using_delete**](IntegrationControllerApi.md#delete_integration_using_delete) | **DELETE** /api/integration/{integrationId} | deleteIntegration
[**get_integration_by_id_using_get**](IntegrationControllerApi.md#get_integration_by_id_using_get) | **GET** /api/integration/{integrationId} | getIntegrationById
[**get_integration_by_routing_key_using_get**](IntegrationControllerApi.md#get_integration_by_routing_key_using_get) | **GET** /api/integration/routingKey/{routingKey} | getIntegrationByRoutingKey
[**get_integrations_by_ids_using_get**](IntegrationControllerApi.md#get_integrations_by_ids_using_get) | **GET** /api/integrations{?integrationIds} | getIntegrationsByIds
[**get_integrations_using_get**](IntegrationControllerApi.md#get_integrations_using_get) | **GET** /api/integrations{?textSearch,idOffset,textOffset,limit} | getIntegrations
[**save_integration_using_post**](IntegrationControllerApi.md#save_integration_using_post) | **POST** /api/integration | saveIntegration

# **delete_integration_using_delete**
> delete_integration_using_delete(integration_id)

deleteIntegration

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
api_instance = pyTB.IntegrationControllerApi(pyTB.ApiClient(configuration))
integration_id = 'integration_id_example' # str | integrationId

try:
    # deleteIntegration
    api_instance.delete_integration_using_delete(integration_id)
except ApiException as e:
    print("Exception when calling IntegrationControllerApi->delete_integration_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**| integrationId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integration_by_id_using_get**
> Integration get_integration_by_id_using_get(integration_id)

getIntegrationById

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
api_instance = pyTB.IntegrationControllerApi(pyTB.ApiClient(configuration))
integration_id = 'integration_id_example' # str | integrationId

try:
    # getIntegrationById
    api_response = api_instance.get_integration_by_id_using_get(integration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationControllerApi->get_integration_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**| integrationId | 

### Return type

[**Integration**](Integration.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integration_by_routing_key_using_get**
> Integration get_integration_by_routing_key_using_get(routing_key)

getIntegrationByRoutingKey

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
api_instance = pyTB.IntegrationControllerApi(pyTB.ApiClient(configuration))
routing_key = 'routing_key_example' # str | routingKey

try:
    # getIntegrationByRoutingKey
    api_response = api_instance.get_integration_by_routing_key_using_get(routing_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationControllerApi->get_integration_by_routing_key_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **routing_key** | **str**| routingKey | 

### Return type

[**Integration**](Integration.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integrations_by_ids_using_get**
> list[Integration] get_integrations_by_ids_using_get(integration_ids)

getIntegrationsByIds

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
api_instance = pyTB.IntegrationControllerApi(pyTB.ApiClient(configuration))
integration_ids = 'integration_ids_example' # str | integrationIds

try:
    # getIntegrationsByIds
    api_response = api_instance.get_integrations_by_ids_using_get(integration_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationControllerApi->get_integrations_by_ids_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_ids** | **str**| integrationIds | 

### Return type

[**list[Integration]**](Integration.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integrations_using_get**
> TextPageDataIntegration get_integrations_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getIntegrations

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
api_instance = pyTB.IntegrationControllerApi(pyTB.ApiClient(configuration))
limit = 'limit_example' # str | limit
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try:
    # getIntegrations
    api_response = api_instance.get_integrations_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationControllerApi->get_integrations_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| limit | 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataIntegration**](TextPageDataIntegration.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_integration_using_post**
> Integration save_integration_using_post(body)

saveIntegration

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
api_instance = pyTB.IntegrationControllerApi(pyTB.ApiClient(configuration))
body = pyTB.Integration() # Integration | integration

try:
    # saveIntegration
    api_response = api_instance.save_integration_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationControllerApi->save_integration_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Integration**](Integration.md)| integration | 

### Return type

[**Integration**](Integration.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

