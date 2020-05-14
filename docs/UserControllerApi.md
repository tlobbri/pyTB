# pyTB.UserControllerApi

All URIs are relative to *//dashboard.digitalconstructionhub.ovh/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user_using_delete**](UserControllerApi.md#delete_user_using_delete) | **DELETE** /api/user/{userId} | deleteUser
[**get_activation_link_using_get**](UserControllerApi.md#get_activation_link_using_get) | **GET** /api/user/{userId}/activationLink | getActivationLink
[**get_all_customer_users_using_get**](UserControllerApi.md#get_all_customer_users_using_get) | **GET** /api/customer/users{?textSearch,idOffset,textOffset,limit} | getAllCustomerUsers
[**get_customer_users_using_get**](UserControllerApi.md#get_customer_users_using_get) | **GET** /api/customer/{customerId}/users{?textSearch,idOffset,textOffset,limit} | getCustomerUsers
[**get_tenant_admins_using_get**](UserControllerApi.md#get_tenant_admins_using_get) | **GET** /api/tenant/{tenantId}/users{?textSearch,idOffset,textOffset,limit} | getTenantAdmins
[**get_user_by_id_using_get**](UserControllerApi.md#get_user_by_id_using_get) | **GET** /api/user/{userId} | getUserById
[**get_user_token_using_get**](UserControllerApi.md#get_user_token_using_get) | **GET** /api/user/{userId}/token | getUserToken
[**get_user_users_using_get**](UserControllerApi.md#get_user_users_using_get) | **GET** /api/user/users{?textSearch,idOffset,textOffset,limit} | getUserUsers
[**get_users_by_entity_group_id_using_get**](UserControllerApi.md#get_users_by_entity_group_id_using_get) | **GET** /api/entityGroup/{entityGroupId}/users{?limit,startTime,endTime,ascOrder,offset} | getUsersByEntityGroupId
[**get_users_by_ids_using_get**](UserControllerApi.md#get_users_by_ids_using_get) | **GET** /api/users{?userIds} | getUsersByIds
[**is_user_token_access_enabled_using_get**](UserControllerApi.md#is_user_token_access_enabled_using_get) | **GET** /api/user/tokenAccessEnabled | isUserTokenAccessEnabled
[**save_user_using_post**](UserControllerApi.md#save_user_using_post) | **POST** /api/user{?sendActivationMail,entityGroupId} | saveUser
[**send_activation_email_using_post**](UserControllerApi.md#send_activation_email_using_post) | **POST** /api/user/sendActivationMail{?email} | sendActivationEmail
[**set_user_credentials_enabled_using_post**](UserControllerApi.md#set_user_credentials_enabled_using_post) | **POST** /api/user/{userId}/userCredentialsEnabled{?userCredentialsEnabled} | setUserCredentialsEnabled

# **delete_user_using_delete**
> delete_user_using_delete(user_id)

deleteUser

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
api_instance = pyTB.UserControllerApi(pyTB.ApiClient(configuration))
user_id = 'user_id_example' # str | userId

try:
    # deleteUser
    api_instance.delete_user_using_delete(user_id)
except ApiException as e:
    print("Exception when calling UserControllerApi->delete_user_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| userId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activation_link_using_get**
> str get_activation_link_using_get(user_id)

getActivationLink

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
api_instance = pyTB.UserControllerApi(pyTB.ApiClient(configuration))
user_id = 'user_id_example' # str | userId

try:
    # getActivationLink
    api_response = api_instance.get_activation_link_using_get(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserControllerApi->get_activation_link_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| userId | 

### Return type

**str**

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_customer_users_using_get**
> TextPageDataUser get_all_customer_users_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getAllCustomerUsers

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
api_instance = pyTB.UserControllerApi(pyTB.ApiClient(configuration))
limit = 'limit_example' # str | limit
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try:
    # getAllCustomerUsers
    api_response = api_instance.get_all_customer_users_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserControllerApi->get_all_customer_users_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| limit | 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataUser**](TextPageDataUser.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_users_using_get**
> TextPageDataUser get_customer_users_using_get(customer_id, limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getCustomerUsers

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
api_instance = pyTB.UserControllerApi(pyTB.ApiClient(configuration))
customer_id = 'customer_id_example' # str | customerId
limit = 'limit_example' # str | limit
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try:
    # getCustomerUsers
    api_response = api_instance.get_customer_users_using_get(customer_id, limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserControllerApi->get_customer_users_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| customerId | 
 **limit** | **str**| limit | 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataUser**](TextPageDataUser.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_admins_using_get**
> TextPageDataUser get_tenant_admins_using_get(tenant_id, limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getTenantAdmins

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
api_instance = pyTB.UserControllerApi(pyTB.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | tenantId
limit = 'limit_example' # str | limit
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try:
    # getTenantAdmins
    api_response = api_instance.get_tenant_admins_using_get(tenant_id, limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserControllerApi->get_tenant_admins_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenantId | 
 **limit** | **str**| limit | 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataUser**](TextPageDataUser.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_id_using_get**
> User get_user_by_id_using_get(user_id)

getUserById

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
api_instance = pyTB.UserControllerApi(pyTB.ApiClient(configuration))
user_id = 'user_id_example' # str | userId

try:
    # getUserById
    api_response = api_instance.get_user_by_id_using_get(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserControllerApi->get_user_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| userId | 

### Return type

[**User**](User.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_token_using_get**
> str get_user_token_using_get(user_id)

getUserToken

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
api_instance = pyTB.UserControllerApi(pyTB.ApiClient(configuration))
user_id = 'user_id_example' # str | userId

try:
    # getUserToken
    api_response = api_instance.get_user_token_using_get(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserControllerApi->get_user_token_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| userId | 

### Return type

**str**

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_users_using_get**
> TextPageDataUser get_user_users_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getUserUsers

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
api_instance = pyTB.UserControllerApi(pyTB.ApiClient(configuration))
limit = 'limit_example' # str | limit
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try:
    # getUserUsers
    api_response = api_instance.get_user_users_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserControllerApi->get_user_users_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| limit | 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataUser**](TextPageDataUser.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_by_entity_group_id_using_get**
> TimePageDataUser get_users_by_entity_group_id_using_get(entity_group_id, limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset)

getUsersByEntityGroupId

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
api_instance = pyTB.UserControllerApi(pyTB.ApiClient(configuration))
entity_group_id = 'entity_group_id_example' # str | entityGroupId
limit = 56 # int | Page link limit
start_time = 789 # int | startTime (optional)
end_time = 789 # int | endTime (optional)
asc_order = true # bool | ascOrder (optional)
offset = 'offset_example' # str | offset (optional)

try:
    # getUsersByEntityGroupId
    api_response = api_instance.get_users_by_entity_group_id_using_get(entity_group_id, limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserControllerApi->get_users_by_entity_group_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_group_id** | **str**| entityGroupId | 
 **limit** | **int**| Page link limit | 
 **start_time** | **int**| startTime | [optional] 
 **end_time** | **int**| endTime | [optional] 
 **asc_order** | **bool**| ascOrder | [optional] 
 **offset** | **str**| offset | [optional] 

### Return type

[**TimePageDataUser**](TimePageDataUser.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_by_ids_using_get**
> list[User] get_users_by_ids_using_get(user_ids)

getUsersByIds

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
api_instance = pyTB.UserControllerApi(pyTB.ApiClient(configuration))
user_ids = 'user_ids_example' # str | userIds

try:
    # getUsersByIds
    api_response = api_instance.get_users_by_ids_using_get(user_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserControllerApi->get_users_by_ids_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_ids** | **str**| userIds | 

### Return type

[**list[User]**](User.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_user_token_access_enabled_using_get**
> bool is_user_token_access_enabled_using_get()

isUserTokenAccessEnabled

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
api_instance = pyTB.UserControllerApi(pyTB.ApiClient(configuration))

try:
    # isUserTokenAccessEnabled
    api_response = api_instance.is_user_token_access_enabled_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserControllerApi->is_user_token_access_enabled_using_get: %s\n" % e)
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

# **save_user_using_post**
> User save_user_using_post(body, send_activation_mail=send_activation_mail, entity_group_id=entity_group_id)

saveUser

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
api_instance = pyTB.UserControllerApi(pyTB.ApiClient(configuration))
body = pyTB.User() # User | user
send_activation_mail = true # bool | sendActivationMail (optional)
entity_group_id = 'entity_group_id_example' # str | entityGroupId (optional)

try:
    # saveUser
    api_response = api_instance.save_user_using_post(body, send_activation_mail=send_activation_mail, entity_group_id=entity_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserControllerApi->save_user_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**User**](User.md)| user | 
 **send_activation_mail** | **bool**| sendActivationMail | [optional] 
 **entity_group_id** | **str**| entityGroupId | [optional] 

### Return type

[**User**](User.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_activation_email_using_post**
> send_activation_email_using_post(email)

sendActivationEmail

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
api_instance = pyTB.UserControllerApi(pyTB.ApiClient(configuration))
email = 'email_example' # str | email

try:
    # sendActivationEmail
    api_instance.send_activation_email_using_post(email)
except ApiException as e:
    print("Exception when calling UserControllerApi->send_activation_email_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| email | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_credentials_enabled_using_post**
> set_user_credentials_enabled_using_post(user_id, user_credentials_enabled=user_credentials_enabled)

setUserCredentialsEnabled

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
api_instance = pyTB.UserControllerApi(pyTB.ApiClient(configuration))
user_id = 'user_id_example' # str | userId
user_credentials_enabled = true # bool | userCredentialsEnabled (optional)

try:
    # setUserCredentialsEnabled
    api_instance.set_user_credentials_enabled_using_post(user_id, user_credentials_enabled=user_credentials_enabled)
except ApiException as e:
    print("Exception when calling UserControllerApi->set_user_credentials_enabled_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| userId | 
 **user_credentials_enabled** | **bool**| userCredentialsEnabled | [optional] 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

