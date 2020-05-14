# pyTB.SelfRegistrationControllerApi

All URIs are relative to *//dashboard.digitalconstructionhub.ovh/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_privacy_policy_using_get**](SelfRegistrationControllerApi.md#get_privacy_policy_using_get) | **GET** /api/noauth/selfRegistration/privacyPolicy | getPrivacyPolicy
[**get_self_registration_params_using_get**](SelfRegistrationControllerApi.md#get_self_registration_params_using_get) | **GET** /api/selfRegistration/selfRegistrationParams | getSelfRegistrationParams
[**get_sign_up_self_registration_params_using_get**](SelfRegistrationControllerApi.md#get_sign_up_self_registration_params_using_get) | **GET** /api/noauth/selfRegistration/signUpSelfRegistrationParams | getSignUpSelfRegistrationParams
[**save_self_registration_params_using_post**](SelfRegistrationControllerApi.md#save_self_registration_params_using_post) | **POST** /api/selfRegistration/selfRegistrationParams | saveSelfRegistrationParams

# **get_privacy_policy_using_get**
> str get_privacy_policy_using_get()

getPrivacyPolicy

### Example
```python
from __future__ import print_function
import time
import pyTB
from pyTB.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyTB.SelfRegistrationControllerApi()

try:
    # getPrivacyPolicy
    api_response = api_instance.get_privacy_policy_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelfRegistrationControllerApi->get_privacy_policy_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self_registration_params_using_get**
> SelfRegistrationParams get_self_registration_params_using_get()

getSelfRegistrationParams

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
api_instance = pyTB.SelfRegistrationControllerApi(pyTB.ApiClient(configuration))

try:
    # getSelfRegistrationParams
    api_response = api_instance.get_self_registration_params_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelfRegistrationControllerApi->get_self_registration_params_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SelfRegistrationParams**](SelfRegistrationParams.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sign_up_self_registration_params_using_get**
> SignUpSelfRegistrationParams get_sign_up_self_registration_params_using_get()

getSignUpSelfRegistrationParams

### Example
```python
from __future__ import print_function
import time
import pyTB
from pyTB.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyTB.SelfRegistrationControllerApi()

try:
    # getSignUpSelfRegistrationParams
    api_response = api_instance.get_sign_up_self_registration_params_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelfRegistrationControllerApi->get_sign_up_self_registration_params_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SignUpSelfRegistrationParams**](SignUpSelfRegistrationParams.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_self_registration_params_using_post**
> SelfRegistrationParams save_self_registration_params_using_post(body)

saveSelfRegistrationParams

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
api_instance = pyTB.SelfRegistrationControllerApi(pyTB.ApiClient(configuration))
body = pyTB.SelfRegistrationParams() # SelfRegistrationParams | selfRegistrationParams

try:
    # saveSelfRegistrationParams
    api_response = api_instance.save_self_registration_params_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelfRegistrationControllerApi->save_self_registration_params_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SelfRegistrationParams**](SelfRegistrationParams.md)| selfRegistrationParams | 

### Return type

[**SelfRegistrationParams**](SelfRegistrationParams.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

