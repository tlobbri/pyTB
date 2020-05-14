# pyTB.OwnerControllerApi

All URIs are relative to *//dashboard.digitalconstructionhub.ovh/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_owner_to_customer_using_post**](OwnerControllerApi.md#change_owner_to_customer_using_post) | **POST** /api/owner/CUSTOMER/{ownerId}/{entityType}/{entityId} | changeOwnerToCustomer
[**change_owner_to_tenant_using_post**](OwnerControllerApi.md#change_owner_to_tenant_using_post) | **POST** /api/owner/TENANT/{ownerId}/{entityType}/{entityId} | changeOwnerToTenant

# **change_owner_to_customer_using_post**
> change_owner_to_customer_using_post(owner_id, entity_type, entity_id)

changeOwnerToCustomer

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
api_instance = pyTB.OwnerControllerApi(pyTB.ApiClient(configuration))
owner_id = 'owner_id_example' # str | ownerId
entity_type = 'entity_type_example' # str | entityType
entity_id = 'entity_id_example' # str | entityId

try:
    # changeOwnerToCustomer
    api_instance.change_owner_to_customer_using_post(owner_id, entity_type, entity_id)
except ApiException as e:
    print("Exception when calling OwnerControllerApi->change_owner_to_customer_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id** | **str**| ownerId | 
 **entity_type** | **str**| entityType | 
 **entity_id** | **str**| entityId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_owner_to_tenant_using_post**
> change_owner_to_tenant_using_post(owner_id, entity_type, entity_id)

changeOwnerToTenant

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
api_instance = pyTB.OwnerControllerApi(pyTB.ApiClient(configuration))
owner_id = 'owner_id_example' # str | ownerId
entity_type = 'entity_type_example' # str | entityType
entity_id = 'entity_id_example' # str | entityId

try:
    # changeOwnerToTenant
    api_instance.change_owner_to_tenant_using_post(owner_id, entity_type, entity_id)
except ApiException as e:
    print("Exception when calling OwnerControllerApi->change_owner_to_tenant_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id** | **str**| ownerId | 
 **entity_type** | **str**| entityType | 
 **entity_id** | **str**| entityId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

