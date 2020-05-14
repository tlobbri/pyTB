# pyTB.WhiteLabelingControllerApi

All URIs are relative to *//dashboard.digitalconstructionhub.ovh/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_login_white_label_params_using_get**](WhiteLabelingControllerApi.md#get_current_login_white_label_params_using_get) | **GET** /api/whiteLabel/currentLoginWhiteLabelParams | getCurrentLoginWhiteLabelParams
[**get_current_white_label_params_using_get**](WhiteLabelingControllerApi.md#get_current_white_label_params_using_get) | **GET** /api/whiteLabel/currentWhiteLabelParams | getCurrentWhiteLabelParams
[**get_login_white_label_params_using_get**](WhiteLabelingControllerApi.md#get_login_white_label_params_using_get) | **GET** /api/noauth/whiteLabel/loginWhiteLabelParams{?logoImageChecksum,faviconChecksum} | getLoginWhiteLabelParams
[**get_white_label_params_using_get**](WhiteLabelingControllerApi.md#get_white_label_params_using_get) | **GET** /api/whiteLabel/whiteLabelParams{?logoImageChecksum,faviconChecksum} | getWhiteLabelParams
[**is_customer_white_labeling_allowed_using_get**](WhiteLabelingControllerApi.md#is_customer_white_labeling_allowed_using_get) | **GET** /api/whiteLabel/isCustomerWhiteLabelingAllowed | isCustomerWhiteLabelingAllowed
[**is_white_labeling_allowed_using_get**](WhiteLabelingControllerApi.md#is_white_labeling_allowed_using_get) | **GET** /api/whiteLabel/isWhiteLabelingAllowed | isWhiteLabelingAllowed
[**preview_white_label_params_using_post**](WhiteLabelingControllerApi.md#preview_white_label_params_using_post) | **POST** /api/whiteLabel/previewWhiteLabelParams | previewWhiteLabelParams
[**save_login_white_label_params_using_post**](WhiteLabelingControllerApi.md#save_login_white_label_params_using_post) | **POST** /api/whiteLabel/loginWhiteLabelParams | saveLoginWhiteLabelParams
[**save_white_label_params_using_post**](WhiteLabelingControllerApi.md#save_white_label_params_using_post) | **POST** /api/whiteLabel/whiteLabelParams | saveWhiteLabelParams

# **get_current_login_white_label_params_using_get**
> LoginWhiteLabelingParams get_current_login_white_label_params_using_get()

getCurrentLoginWhiteLabelParams

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
api_instance = pyTB.WhiteLabelingControllerApi(pyTB.ApiClient(configuration))

try:
    # getCurrentLoginWhiteLabelParams
    api_response = api_instance.get_current_login_white_label_params_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhiteLabelingControllerApi->get_current_login_white_label_params_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LoginWhiteLabelingParams**](LoginWhiteLabelingParams.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_white_label_params_using_get**
> WhiteLabelingParams get_current_white_label_params_using_get()

getCurrentWhiteLabelParams

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
api_instance = pyTB.WhiteLabelingControllerApi(pyTB.ApiClient(configuration))

try:
    # getCurrentWhiteLabelParams
    api_response = api_instance.get_current_white_label_params_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhiteLabelingControllerApi->get_current_white_label_params_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WhiteLabelingParams**](WhiteLabelingParams.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_login_white_label_params_using_get**
> LoginWhiteLabelingParams get_login_white_label_params_using_get(logo_image_checksum=logo_image_checksum, favicon_checksum=favicon_checksum)

getLoginWhiteLabelParams

### Example
```python
from __future__ import print_function
import time
import pyTB
from pyTB.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyTB.WhiteLabelingControllerApi()
logo_image_checksum = 'logo_image_checksum_example' # str | logoImageChecksum (optional)
favicon_checksum = 'favicon_checksum_example' # str | faviconChecksum (optional)

try:
    # getLoginWhiteLabelParams
    api_response = api_instance.get_login_white_label_params_using_get(logo_image_checksum=logo_image_checksum, favicon_checksum=favicon_checksum)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhiteLabelingControllerApi->get_login_white_label_params_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logo_image_checksum** | **str**| logoImageChecksum | [optional] 
 **favicon_checksum** | **str**| faviconChecksum | [optional] 

### Return type

[**LoginWhiteLabelingParams**](LoginWhiteLabelingParams.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_white_label_params_using_get**
> WhiteLabelingParams get_white_label_params_using_get(logo_image_checksum=logo_image_checksum, favicon_checksum=favicon_checksum)

getWhiteLabelParams

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
api_instance = pyTB.WhiteLabelingControllerApi(pyTB.ApiClient(configuration))
logo_image_checksum = 'logo_image_checksum_example' # str | logoImageChecksum (optional)
favicon_checksum = 'favicon_checksum_example' # str | faviconChecksum (optional)

try:
    # getWhiteLabelParams
    api_response = api_instance.get_white_label_params_using_get(logo_image_checksum=logo_image_checksum, favicon_checksum=favicon_checksum)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhiteLabelingControllerApi->get_white_label_params_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logo_image_checksum** | **str**| logoImageChecksum | [optional] 
 **favicon_checksum** | **str**| faviconChecksum | [optional] 

### Return type

[**WhiteLabelingParams**](WhiteLabelingParams.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_customer_white_labeling_allowed_using_get**
> bool is_customer_white_labeling_allowed_using_get()

isCustomerWhiteLabelingAllowed

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
api_instance = pyTB.WhiteLabelingControllerApi(pyTB.ApiClient(configuration))

try:
    # isCustomerWhiteLabelingAllowed
    api_response = api_instance.is_customer_white_labeling_allowed_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhiteLabelingControllerApi->is_customer_white_labeling_allowed_using_get: %s\n" % e)
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

# **is_white_labeling_allowed_using_get**
> bool is_white_labeling_allowed_using_get()

isWhiteLabelingAllowed

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
api_instance = pyTB.WhiteLabelingControllerApi(pyTB.ApiClient(configuration))

try:
    # isWhiteLabelingAllowed
    api_response = api_instance.is_white_labeling_allowed_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhiteLabelingControllerApi->is_white_labeling_allowed_using_get: %s\n" % e)
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

# **preview_white_label_params_using_post**
> WhiteLabelingParams preview_white_label_params_using_post(body)

previewWhiteLabelParams

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
api_instance = pyTB.WhiteLabelingControllerApi(pyTB.ApiClient(configuration))
body = pyTB.WhiteLabelingParams() # WhiteLabelingParams | whiteLabelingParams

try:
    # previewWhiteLabelParams
    api_response = api_instance.preview_white_label_params_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhiteLabelingControllerApi->preview_white_label_params_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WhiteLabelingParams**](WhiteLabelingParams.md)| whiteLabelingParams | 

### Return type

[**WhiteLabelingParams**](WhiteLabelingParams.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_login_white_label_params_using_post**
> LoginWhiteLabelingParams save_login_white_label_params_using_post(body)

saveLoginWhiteLabelParams

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
api_instance = pyTB.WhiteLabelingControllerApi(pyTB.ApiClient(configuration))
body = pyTB.LoginWhiteLabelingParams() # LoginWhiteLabelingParams | loginWhiteLabelingParams

try:
    # saveLoginWhiteLabelParams
    api_response = api_instance.save_login_white_label_params_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhiteLabelingControllerApi->save_login_white_label_params_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginWhiteLabelingParams**](LoginWhiteLabelingParams.md)| loginWhiteLabelingParams | 

### Return type

[**LoginWhiteLabelingParams**](LoginWhiteLabelingParams.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_white_label_params_using_post**
> WhiteLabelingParams save_white_label_params_using_post(body)

saveWhiteLabelParams

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
api_instance = pyTB.WhiteLabelingControllerApi(pyTB.ApiClient(configuration))
body = pyTB.WhiteLabelingParams() # WhiteLabelingParams | whiteLabelingParams

try:
    # saveWhiteLabelParams
    api_response = api_instance.save_white_label_params_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhiteLabelingControllerApi->save_white_label_params_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WhiteLabelingParams**](WhiteLabelingParams.md)| whiteLabelingParams | 

### Return type

[**WhiteLabelingParams**](WhiteLabelingParams.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

