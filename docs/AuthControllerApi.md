# pyTB.AuthControllerApi

All URIs are relative to *//dashboard.digitalconstructionhub.ovh/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_user_using_post**](AuthControllerApi.md#activate_user_using_post) | **POST** /api/noauth/activate | activateUser
[**change_password_using_post**](AuthControllerApi.md#change_password_using_post) | **POST** /api/auth/changePassword | changePassword
[**check_activate_token_using_get**](AuthControllerApi.md#check_activate_token_using_get) | **GET** /api/noauth/activate{?activateToken} | checkActivateToken
[**check_reset_token_using_get**](AuthControllerApi.md#check_reset_token_using_get) | **GET** /api/noauth/resetPassword{?resetToken} | checkResetToken
[**get_user_password_policy_using_get**](AuthControllerApi.md#get_user_password_policy_using_get) | **GET** /api/noauth/userPasswordPolicy | getUserPasswordPolicy
[**get_user_using_get**](AuthControllerApi.md#get_user_using_get) | **GET** /api/auth/user | getUser
[**logout_using_post**](AuthControllerApi.md#logout_using_post) | **POST** /api/auth/logout | logout
[**request_reset_password_by_email_using_post**](AuthControllerApi.md#request_reset_password_by_email_using_post) | **POST** /api/noauth/resetPasswordByEmail | requestResetPasswordByEmail
[**reset_password_using_post**](AuthControllerApi.md#reset_password_using_post) | **POST** /api/noauth/resetPassword | resetPassword

# **activate_user_using_post**
> str activate_user_using_post(body)

activateUser

### Example
```python
from __future__ import print_function
import time
import pyTB
from pyTB.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyTB.AuthControllerApi()
body = 'body_example' # str | activateRequest

try:
    # activateUser
    api_response = api_instance.activate_user_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthControllerApi->activate_user_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| activateRequest | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_password_using_post**
> change_password_using_post(body)

changePassword

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
api_instance = pyTB.AuthControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | changePasswordRequest

try:
    # changePassword
    api_instance.change_password_using_post(body)
except ApiException as e:
    print("Exception when calling AuthControllerApi->change_password_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| changePasswordRequest | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_activate_token_using_get**
> str check_activate_token_using_get(activate_token)

checkActivateToken

### Example
```python
from __future__ import print_function
import time
import pyTB
from pyTB.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyTB.AuthControllerApi()
activate_token = 'activate_token_example' # str | activateToken

try:
    # checkActivateToken
    api_response = api_instance.check_activate_token_using_get(activate_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthControllerApi->check_activate_token_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activate_token** | **str**| activateToken | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_reset_token_using_get**
> str check_reset_token_using_get(reset_token)

checkResetToken

### Example
```python
from __future__ import print_function
import time
import pyTB
from pyTB.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyTB.AuthControllerApi()
reset_token = 'reset_token_example' # str | resetToken

try:
    # checkResetToken
    api_response = api_instance.check_reset_token_using_get(reset_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthControllerApi->check_reset_token_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reset_token** | **str**| resetToken | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_password_policy_using_get**
> UserPasswordPolicy get_user_password_policy_using_get()

getUserPasswordPolicy

### Example
```python
from __future__ import print_function
import time
import pyTB
from pyTB.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyTB.AuthControllerApi()

try:
    # getUserPasswordPolicy
    api_response = api_instance.get_user_password_policy_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthControllerApi->get_user_password_policy_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserPasswordPolicy**](UserPasswordPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_using_get**
> User get_user_using_get()

getUser

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
api_instance = pyTB.AuthControllerApi(pyTB.ApiClient(configuration))

try:
    # getUser
    api_response = api_instance.get_user_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthControllerApi->get_user_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout_using_post**
> logout_using_post()

logout

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
api_instance = pyTB.AuthControllerApi(pyTB.ApiClient(configuration))

try:
    # logout
    api_instance.logout_using_post()
except ApiException as e:
    print("Exception when calling AuthControllerApi->logout_using_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_reset_password_by_email_using_post**
> request_reset_password_by_email_using_post(body)

requestResetPasswordByEmail

### Example
```python
from __future__ import print_function
import time
import pyTB
from pyTB.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyTB.AuthControllerApi()
body = 'body_example' # str | resetPasswordByEmailRequest

try:
    # requestResetPasswordByEmail
    api_instance.request_reset_password_by_email_using_post(body)
except ApiException as e:
    print("Exception when calling AuthControllerApi->request_reset_password_by_email_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| resetPasswordByEmailRequest | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password_using_post**
> str reset_password_using_post(body)

resetPassword

### Example
```python
from __future__ import print_function
import time
import pyTB
from pyTB.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyTB.AuthControllerApi()
body = 'body_example' # str | resetPasswordRequest

try:
    # resetPassword
    api_response = api_instance.reset_password_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthControllerApi->reset_password_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| resetPasswordRequest | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

