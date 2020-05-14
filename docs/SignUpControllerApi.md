# pyTB.SignUpControllerApi

All URIs are relative to *//dashboard.digitalconstructionhub.ovh/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_privacy_policy_using_post**](SignUpControllerApi.md#accept_privacy_policy_using_post) | **POST** /api/signup/acceptPrivacyPolicy | acceptPrivacyPolicy
[**activate_email_using_get**](SignUpControllerApi.md#activate_email_using_get) | **GET** /api/noauth/activateEmail{?emailCode} | activateEmail
[**activate_user_by_email_code_using_post**](SignUpControllerApi.md#activate_user_by_email_code_using_post) | **POST** /api/noauth/activateByEmailCode{?emailCode} | activateUserByEmailCode
[**privacy_policy_accepted_using_get**](SignUpControllerApi.md#privacy_policy_accepted_using_get) | **GET** /api/signup/privacyPolicyAccepted | privacyPolicyAccepted
[**resend_email_activation_using_post**](SignUpControllerApi.md#resend_email_activation_using_post) | **POST** /api/noauth/resendEmailActivation{?email} | resendEmailActivation
[**sign_up_using_post**](SignUpControllerApi.md#sign_up_using_post) | **POST** /api/noauth/signup | signUp

# **accept_privacy_policy_using_post**
> str accept_privacy_policy_using_post()

acceptPrivacyPolicy

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
api_instance = pyTB.SignUpControllerApi(pyTB.ApiClient(configuration))

try:
    # acceptPrivacyPolicy
    api_response = api_instance.accept_privacy_policy_using_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignUpControllerApi->accept_privacy_policy_using_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activate_email_using_get**
> str activate_email_using_get(email_code)

activateEmail

### Example
```python
from __future__ import print_function
import time
import pyTB
from pyTB.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyTB.SignUpControllerApi()
email_code = 'email_code_example' # str | emailCode

try:
    # activateEmail
    api_response = api_instance.activate_email_using_get(email_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignUpControllerApi->activate_email_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_code** | **str**| emailCode | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activate_user_by_email_code_using_post**
> str activate_user_by_email_code_using_post(email_code)

activateUserByEmailCode

### Example
```python
from __future__ import print_function
import time
import pyTB
from pyTB.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyTB.SignUpControllerApi()
email_code = 'email_code_example' # str | emailCode

try:
    # activateUserByEmailCode
    api_response = api_instance.activate_user_by_email_code_using_post(email_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignUpControllerApi->activate_user_by_email_code_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_code** | **str**| emailCode | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **privacy_policy_accepted_using_get**
> bool privacy_policy_accepted_using_get()

privacyPolicyAccepted

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
api_instance = pyTB.SignUpControllerApi(pyTB.ApiClient(configuration))

try:
    # privacyPolicyAccepted
    api_response = api_instance.privacy_policy_accepted_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignUpControllerApi->privacy_policy_accepted_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_email_activation_using_post**
> resend_email_activation_using_post(email)

resendEmailActivation

### Example
```python
from __future__ import print_function
import time
import pyTB
from pyTB.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyTB.SignUpControllerApi()
email = 'email_example' # str | email

try:
    # resendEmailActivation
    api_instance.resend_email_activation_using_post(email)
except ApiException as e:
    print("Exception when calling SignUpControllerApi->resend_email_activation_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| email | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_up_using_post**
> str sign_up_using_post(body)

signUp

### Example
```python
from __future__ import print_function
import time
import pyTB
from pyTB.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyTB.SignUpControllerApi()
body = pyTB.SignUpRequest() # SignUpRequest | signUpRequest

try:
    # signUp
    api_response = api_instance.sign_up_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignUpControllerApi->sign_up_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SignUpRequest**](SignUpRequest.md)| signUpRequest | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

