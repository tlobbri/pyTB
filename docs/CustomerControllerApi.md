# pyTB.CustomerControllerApi

All URIs are relative to *//dashboard.digitalconstructionhub.ovh/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_customer_using_delete**](CustomerControllerApi.md#delete_customer_using_delete) | **DELETE** /api/customer/{customerId} | deleteCustomer
[**get_customer_by_id_using_get**](CustomerControllerApi.md#get_customer_by_id_using_get) | **GET** /api/customer/{customerId} | getCustomerById
[**get_customer_title_by_id_using_get**](CustomerControllerApi.md#get_customer_title_by_id_using_get) | **GET** /api/customer/{customerId}/title | getCustomerTitleById
[**get_customers_by_entity_group_id_using_get**](CustomerControllerApi.md#get_customers_by_entity_group_id_using_get) | **GET** /api/entityGroup/{entityGroupId}/customers{?limit,startTime,endTime,ascOrder,offset} | getCustomersByEntityGroupId
[**get_customers_by_ids_using_get**](CustomerControllerApi.md#get_customers_by_ids_using_get) | **GET** /api/customers{?customerIds} | getCustomersByIds
[**get_customers_using_get**](CustomerControllerApi.md#get_customers_using_get) | **GET** /api/customers{?textSearch,idOffset,textOffset,limit} | getCustomers
[**get_short_customer_info_by_id_using_get**](CustomerControllerApi.md#get_short_customer_info_by_id_using_get) | **GET** /api/customer/{customerId}/shortInfo | getShortCustomerInfoById
[**get_tenant_customer_using_get**](CustomerControllerApi.md#get_tenant_customer_using_get) | **GET** /api/tenant/customers{?customerTitle} | getTenantCustomer
[**get_user_customers_using_get**](CustomerControllerApi.md#get_user_customers_using_get) | **GET** /api/user/customers{?textSearch,idOffset,textOffset,limit} | getUserCustomers
[**save_customer_using_post**](CustomerControllerApi.md#save_customer_using_post) | **POST** /api/customer{?entityGroupId} | saveCustomer

# **delete_customer_using_delete**
> delete_customer_using_delete(customer_id)

deleteCustomer

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
api_instance = pyTB.CustomerControllerApi(pyTB.ApiClient(configuration))
customer_id = 'customer_id_example' # str | customerId

try:
    # deleteCustomer
    api_instance.delete_customer_using_delete(customer_id)
except ApiException as e:
    print("Exception when calling CustomerControllerApi->delete_customer_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| customerId | 

### Return type

void (empty response body)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_by_id_using_get**
> Customer get_customer_by_id_using_get(customer_id)

getCustomerById

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
api_instance = pyTB.CustomerControllerApi(pyTB.ApiClient(configuration))
customer_id = 'customer_id_example' # str | customerId

try:
    # getCustomerById
    api_response = api_instance.get_customer_by_id_using_get(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerControllerApi->get_customer_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| customerId | 

### Return type

[**Customer**](Customer.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_title_by_id_using_get**
> str get_customer_title_by_id_using_get(customer_id)

getCustomerTitleById

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
api_instance = pyTB.CustomerControllerApi(pyTB.ApiClient(configuration))
customer_id = 'customer_id_example' # str | customerId

try:
    # getCustomerTitleById
    api_response = api_instance.get_customer_title_by_id_using_get(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerControllerApi->get_customer_title_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| customerId | 

### Return type

**str**

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customers_by_entity_group_id_using_get**
> TimePageDataCustomer get_customers_by_entity_group_id_using_get(entity_group_id, limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset)

getCustomersByEntityGroupId

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
api_instance = pyTB.CustomerControllerApi(pyTB.ApiClient(configuration))
entity_group_id = 'entity_group_id_example' # str | entityGroupId
limit = 56 # int | Page link limit
start_time = 789 # int | startTime (optional)
end_time = 789 # int | endTime (optional)
asc_order = true # bool | ascOrder (optional)
offset = 'offset_example' # str | offset (optional)

try:
    # getCustomersByEntityGroupId
    api_response = api_instance.get_customers_by_entity_group_id_using_get(entity_group_id, limit, start_time=start_time, end_time=end_time, asc_order=asc_order, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerControllerApi->get_customers_by_entity_group_id_using_get: %s\n" % e)
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

[**TimePageDataCustomer**](TimePageDataCustomer.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customers_by_ids_using_get**
> list[Customer] get_customers_by_ids_using_get(customer_ids)

getCustomersByIds

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
api_instance = pyTB.CustomerControllerApi(pyTB.ApiClient(configuration))
customer_ids = 'customer_ids_example' # str | customerIds

try:
    # getCustomersByIds
    api_response = api_instance.get_customers_by_ids_using_get(customer_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerControllerApi->get_customers_by_ids_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_ids** | **str**| customerIds | 

### Return type

[**list[Customer]**](Customer.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customers_using_get**
> TextPageDataCustomer get_customers_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getCustomers

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
api_instance = pyTB.CustomerControllerApi(pyTB.ApiClient(configuration))
limit = 'limit_example' # str | limit
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try:
    # getCustomers
    api_response = api_instance.get_customers_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerControllerApi->get_customers_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| limit | 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataCustomer**](TextPageDataCustomer.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_short_customer_info_by_id_using_get**
> str get_short_customer_info_by_id_using_get(customer_id)

getShortCustomerInfoById

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
api_instance = pyTB.CustomerControllerApi(pyTB.ApiClient(configuration))
customer_id = 'customer_id_example' # str | customerId

try:
    # getShortCustomerInfoById
    api_response = api_instance.get_short_customer_info_by_id_using_get(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerControllerApi->get_short_customer_info_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| customerId | 

### Return type

**str**

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_customer_using_get**
> Customer get_tenant_customer_using_get(customer_title)

getTenantCustomer

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
api_instance = pyTB.CustomerControllerApi(pyTB.ApiClient(configuration))
customer_title = 'customer_title_example' # str | customerTitle

try:
    # getTenantCustomer
    api_response = api_instance.get_tenant_customer_using_get(customer_title)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerControllerApi->get_tenant_customer_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_title** | **str**| customerTitle | 

### Return type

[**Customer**](Customer.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_customers_using_get**
> TextPageDataCustomer get_user_customers_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)

getUserCustomers

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
api_instance = pyTB.CustomerControllerApi(pyTB.ApiClient(configuration))
limit = 'limit_example' # str | limit
text_search = 'text_search_example' # str | textSearch (optional)
id_offset = 'id_offset_example' # str | idOffset (optional)
text_offset = 'text_offset_example' # str | textOffset (optional)

try:
    # getUserCustomers
    api_response = api_instance.get_user_customers_using_get(limit, text_search=text_search, id_offset=id_offset, text_offset=text_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerControllerApi->get_user_customers_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| limit | 
 **text_search** | **str**| textSearch | [optional] 
 **id_offset** | **str**| idOffset | [optional] 
 **text_offset** | **str**| textOffset | [optional] 

### Return type

[**TextPageDataCustomer**](TextPageDataCustomer.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_customer_using_post**
> Customer save_customer_using_post(body, entity_group_id=entity_group_id)

saveCustomer

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
api_instance = pyTB.CustomerControllerApi(pyTB.ApiClient(configuration))
body = pyTB.Customer() # Customer | customer
entity_group_id = 'entity_group_id_example' # str | entityGroupId (optional)

try:
    # saveCustomer
    api_response = api_instance.save_customer_using_post(body, entity_group_id=entity_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerControllerApi->save_customer_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Customer**](Customer.md)| customer | 
 **entity_group_id** | **str**| entityGroupId | [optional] 

### Return type

[**Customer**](Customer.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

