# pyTB.CustomTranslationControllerApi

All URIs are relative to *//dashboard.digitalconstructionhub.ovh/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_custom_translation_using_get**](CustomTranslationControllerApi.md#get_current_custom_translation_using_get) | **GET** /api/customTranslation/currentCustomTranslation | getCurrentCustomTranslation
[**get_custom_translation_using_get**](CustomTranslationControllerApi.md#get_custom_translation_using_get) | **GET** /api/customTranslation/customTranslation | getCustomTranslation
[**save_custom_translation_using_post**](CustomTranslationControllerApi.md#save_custom_translation_using_post) | **POST** /api/customTranslation/customTranslation | saveCustomTranslation

# **get_current_custom_translation_using_get**
> CustomTranslation get_current_custom_translation_using_get()

getCurrentCustomTranslation

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
api_instance = pyTB.CustomTranslationControllerApi(pyTB.ApiClient(configuration))

try:
    # getCurrentCustomTranslation
    api_response = api_instance.get_current_custom_translation_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomTranslationControllerApi->get_current_custom_translation_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomTranslation**](CustomTranslation.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_translation_using_get**
> CustomTranslation get_custom_translation_using_get()

getCustomTranslation

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
api_instance = pyTB.CustomTranslationControllerApi(pyTB.ApiClient(configuration))

try:
    # getCustomTranslation
    api_response = api_instance.get_custom_translation_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomTranslationControllerApi->get_custom_translation_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomTranslation**](CustomTranslation.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_custom_translation_using_post**
> CustomTranslation save_custom_translation_using_post(body)

saveCustomTranslation

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
api_instance = pyTB.CustomTranslationControllerApi(pyTB.ApiClient(configuration))
body = pyTB.CustomTranslation() # CustomTranslation | customTranslation

try:
    # saveCustomTranslation
    api_response = api_instance.save_custom_translation_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomTranslationControllerApi->save_custom_translation_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomTranslation**](CustomTranslation.md)| customTranslation | 

### Return type

[**CustomTranslation**](CustomTranslation.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

