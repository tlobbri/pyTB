# pyTB.ConverterControllerApi

All URIs are relative to *//dashboard.digitalconstructionhub.ovh/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_converter_using_delete**](ConverterControllerApi.md#delete_converter_using_delete) | **DELETE** /api/converter/{converterId} | deleteConverter
[**get_converter_by_id_using_get**](ConverterControllerApi.md#get_converter_by_id_using_get) | **GET** /api/converter/{converterId} | getConverterById
[**get_converters_by_ids_using_get**](ConverterControllerApi.md#get_converters_by_ids_using_get) | **GET** /api/converters{?converterIds} | getConvertersByIds
[**get_converters_using_get**](ConverterControllerApi.md#get_converters_using_get) | **GET** /api/converters{?textSearch,idOffset,textOffset,limit} | getConverters
[**get_latest_converter_debug_input_using_get**](ConverterControllerApi.md#get_latest_converter_debug_input_using_get) | **GET** /api/converter/{converterId}/debugIn | getLatestConverterDebugInput
[**save_converter_using_post**](ConverterControllerApi.md#save_converter_using_post) | **POST** /api/converter | saveConverter
[**test_down_link_converter_using_post**](ConverterControllerApi.md#test_down_link_converter_using_post) | **POST** /api/converter/testDownLink | testDownLinkConverter
[**test_up_link_converter_using_post**](ConverterControllerApi.md#test_up_link_converter_using_post) | **POST** /api/converter/testUpLink | testUpLinkConverter

# **delete_converter_using_delete**
> delete_converter_using_delete(converter_id)

deleteConverter

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
api_instance = pyTB.ConverterControllerApi(pyTB.ApiClient(configuration))
converter_id = 'converter_id_example' # str | converterId

try:
    # deleteConverter
    api_instance.delete_converter_using_delete(converter_id)
except ApiException as e:
    print("Exception when calling ConverterControllerApi->delete_converter_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **converter_id** | **str**| converterId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_converter_by_id_using_get**
> Converter get_converter_by_id_using_get(converter_id)

getConverterById

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
api_instance = pyTB.ConverterControllerApi(pyTB.ApiClient(configuration))
converter_id = 'converter_id_example' # str | converterId

try:
    # getConverterById
    api_response = api_instance.get_converter_by_id_using_get(converter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConverterControllerApi->get_converter_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **converter_id** | **str**| converterId | 

### Return type

[**Converter**](Converter.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_converters_by_ids_using_get**
> list[Converter] get_converters_by_ids_using_get(converter_ids)

getConvertersByIds

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
api_instance = pyTB.ConverterControllerApi(pyTB.ApiClient(configuration))
converter_ids = 'converter_ids_example' # str | converterIds

try:
    # getConvertersByIds
    api_response = api_instance.get_converters_by_ids_using_get(converter_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConverterControllerApi->get_converters_by_ids_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **converter_ids** | **str**| converterIds | 

### Return type

[**list[Converter]**](Converter.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_converters_using_get**
> TextPageDataConverter get_converters_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getConverters

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
api_instance = pyTB.ConverterControllerApi(pyTB.ApiClient(configuration))
limit = 'limit_example' # str | limit
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try:
    # getConverters
    api_response = api_instance.get_converters_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConverterControllerApi->get_converters_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| limit | 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataConverter**](TextPageDataConverter.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_converter_debug_input_using_get**
> str get_latest_converter_debug_input_using_get(converter_id)

getLatestConverterDebugInput

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
api_instance = pyTB.ConverterControllerApi(pyTB.ApiClient(configuration))
converter_id = 'converter_id_example' # str | converterId

try:
    # getLatestConverterDebugInput
    api_response = api_instance.get_latest_converter_debug_input_using_get(converter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConverterControllerApi->get_latest_converter_debug_input_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **converter_id** | **str**| converterId | 

### Return type

**str**

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_converter_using_post**
> Converter save_converter_using_post(body)

saveConverter

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
api_instance = pyTB.ConverterControllerApi(pyTB.ApiClient(configuration))
body = pyTB.Converter() # Converter | converter

try:
    # saveConverter
    api_response = api_instance.save_converter_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConverterControllerApi->save_converter_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Converter**](Converter.md)| converter | 

### Return type

[**Converter**](Converter.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_down_link_converter_using_post**
> str test_down_link_converter_using_post(body)

testDownLinkConverter

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
api_instance = pyTB.ConverterControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | inputParams

try:
    # testDownLinkConverter
    api_response = api_instance.test_down_link_converter_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConverterControllerApi->test_down_link_converter_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| inputParams | 

### Return type

**str**

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_up_link_converter_using_post**
> str test_up_link_converter_using_post(body)

testUpLinkConverter

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
api_instance = pyTB.ConverterControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | inputParams

try:
    # testUpLinkConverter
    api_response = api_instance.test_up_link_converter_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConverterControllerApi->test_up_link_converter_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| inputParams | 

### Return type

**str**

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

