# pyTB.CustomMenuControllerApi

All URIs are relative to *//dashboard.digitalconstructionhub.ovh/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_custom_menu_using_get**](CustomMenuControllerApi.md#get_current_custom_menu_using_get) | **GET** /api/customMenu/currentCustomMenu | getCurrentCustomMenu
[**get_custom_menu_using_get**](CustomMenuControllerApi.md#get_custom_menu_using_get) | **GET** /api/customMenu/customMenu | getCustomMenu
[**save_custom_menu_using_post**](CustomMenuControllerApi.md#save_custom_menu_using_post) | **POST** /api/customMenu/customMenu | saveCustomMenu

# **get_current_custom_menu_using_get**
> CustomMenu get_current_custom_menu_using_get()

getCurrentCustomMenu

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
api_instance = pyTB.CustomMenuControllerApi(pyTB.ApiClient(configuration))

try:
    # getCurrentCustomMenu
    api_response = api_instance.get_current_custom_menu_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomMenuControllerApi->get_current_custom_menu_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomMenu**](CustomMenu.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_menu_using_get**
> CustomMenu get_custom_menu_using_get()

getCustomMenu

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
api_instance = pyTB.CustomMenuControllerApi(pyTB.ApiClient(configuration))

try:
    # getCustomMenu
    api_response = api_instance.get_custom_menu_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomMenuControllerApi->get_custom_menu_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomMenu**](CustomMenu.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_custom_menu_using_post**
> CustomMenu save_custom_menu_using_post(body=body)

saveCustomMenu

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
api_instance = pyTB.CustomMenuControllerApi(pyTB.ApiClient(configuration))
body = pyTB.CustomMenu() # CustomMenu | customMenu (optional)

try:
    # saveCustomMenu
    api_response = api_instance.save_custom_menu_using_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomMenuControllerApi->save_custom_menu_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomMenu**](CustomMenu.md)| customMenu | [optional] 

### Return type

[**CustomMenu**](CustomMenu.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

