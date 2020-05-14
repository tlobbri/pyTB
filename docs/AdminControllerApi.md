# pyTB.AdminControllerApi

All URIs are relative to *//dashboard.digitalconstructionhub.ovh/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_updates_using_get**](AdminControllerApi.md#check_updates_using_get) | **GET** /api/admin/updates | checkUpdates
[**get_admin_settings_using_get**](AdminControllerApi.md#get_admin_settings_using_get) | **GET** /api/admin/settings/{key}{?systemByDefault} | getAdminSettings
[**get_security_settings_using_get**](AdminControllerApi.md#get_security_settings_using_get) | **GET** /api/admin/securitySettings | getSecuritySettings
[**save_admin_settings_using_post**](AdminControllerApi.md#save_admin_settings_using_post) | **POST** /api/admin/settings | saveAdminSettings
[**save_security_settings_using_post**](AdminControllerApi.md#save_security_settings_using_post) | **POST** /api/admin/securitySettings | saveSecuritySettings
[**send_test_mail_using_post**](AdminControllerApi.md#send_test_mail_using_post) | **POST** /api/admin/settings/testMail | sendTestMail

# **check_updates_using_get**
> UpdateMessage check_updates_using_get()

checkUpdates

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
api_instance = pyTB.AdminControllerApi(pyTB.ApiClient(configuration))

try:
    # checkUpdates
    api_response = api_instance.check_updates_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminControllerApi->check_updates_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UpdateMessage**](UpdateMessage.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_settings_using_get**
> AdminSettings get_admin_settings_using_get(key, system_by_default=system_by_default)

getAdminSettings

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
api_instance = pyTB.AdminControllerApi(pyTB.ApiClient(configuration))
key = 'key_example' # str | key
system_by_default = true # bool | systemByDefault (optional)

try:
    # getAdminSettings
    api_response = api_instance.get_admin_settings_using_get(key, system_by_default=system_by_default)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminControllerApi->get_admin_settings_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| key | 
 **system_by_default** | **bool**| systemByDefault | [optional] 

### Return type

[**AdminSettings**](AdminSettings.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_security_settings_using_get**
> SecuritySettings get_security_settings_using_get()

getSecuritySettings

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
api_instance = pyTB.AdminControllerApi(pyTB.ApiClient(configuration))

try:
    # getSecuritySettings
    api_response = api_instance.get_security_settings_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminControllerApi->get_security_settings_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SecuritySettings**](SecuritySettings.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_admin_settings_using_post**
> AdminSettings save_admin_settings_using_post(body)

saveAdminSettings

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
api_instance = pyTB.AdminControllerApi(pyTB.ApiClient(configuration))
body = pyTB.AdminSettings() # AdminSettings | adminSettings

try:
    # saveAdminSettings
    api_response = api_instance.save_admin_settings_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminControllerApi->save_admin_settings_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminSettings**](AdminSettings.md)| adminSettings | 

### Return type

[**AdminSettings**](AdminSettings.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_security_settings_using_post**
> SecuritySettings save_security_settings_using_post(body)

saveSecuritySettings

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
api_instance = pyTB.AdminControllerApi(pyTB.ApiClient(configuration))
body = pyTB.SecuritySettings() # SecuritySettings | securitySettings

try:
    # saveSecuritySettings
    api_response = api_instance.save_security_settings_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminControllerApi->save_security_settings_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SecuritySettings**](SecuritySettings.md)| securitySettings | 

### Return type

[**SecuritySettings**](SecuritySettings.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_test_mail_using_post**
> send_test_mail_using_post(body)

sendTestMail

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
api_instance = pyTB.AdminControllerApi(pyTB.ApiClient(configuration))
body = pyTB.AdminSettings() # AdminSettings | adminSettings

try:
    # sendTestMail
    api_instance.send_test_mail_using_post(body)
except ApiException as e:
    print("Exception when calling AdminControllerApi->send_test_mail_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminSettings**](AdminSettings.md)| adminSettings | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

