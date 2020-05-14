# pyTB.UserPermissionsControllerApi

All URIs are relative to *//dashboard.digitalconstructionhub.ovh/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_allowed_permissions_using_get**](UserPermissionsControllerApi.md#get_allowed_permissions_using_get) | **GET** /api/permissions/allowedPermissions | getAllowedPermissions

# **get_allowed_permissions_using_get**
> AllowedPermissionsInfo get_allowed_permissions_using_get()

getAllowedPermissions

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
api_instance = pyTB.UserPermissionsControllerApi(pyTB.ApiClient(configuration))

try:
    # getAllowedPermissions
    api_response = api_instance.get_allowed_permissions_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserPermissionsControllerApi->get_allowed_permissions_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AllowedPermissionsInfo**](AllowedPermissionsInfo.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

