# pyTB.RuleEngineControllerApi

All URIs are relative to *//dashboard.digitalconstructionhub.ovh/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**handle_rule_engine_request_using_post**](RuleEngineControllerApi.md#handle_rule_engine_request_using_post) | **POST** /api/rule-engine/ | handleRuleEngineRequest
[**handle_rule_engine_request_using_post1**](RuleEngineControllerApi.md#handle_rule_engine_request_using_post1) | **POST** /api/rule-engine/{entityType}/{entityId}/{timeout} | handleRuleEngineRequest
[**handle_rule_engine_request_using_post2**](RuleEngineControllerApi.md#handle_rule_engine_request_using_post2) | **POST** /api/rule-engine/{entityType}/{entityId} | handleRuleEngineRequest

# **handle_rule_engine_request_using_post**
> DeferredResultResponseEntity handle_rule_engine_request_using_post(body)

handleRuleEngineRequest

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
api_instance = pyTB.RuleEngineControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | requestBody

try:
    # handleRuleEngineRequest
    api_response = api_instance.handle_rule_engine_request_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuleEngineControllerApi->handle_rule_engine_request_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| requestBody | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_rule_engine_request_using_post1**
> DeferredResultResponseEntity handle_rule_engine_request_using_post1(body, entity_type, entity_id, timeout)

handleRuleEngineRequest

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
api_instance = pyTB.RuleEngineControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | requestBody
entity_type = 'entity_type_example' # str | entityType
entity_id = 'entity_id_example' # str | entityId
timeout = 56 # int | timeout

try:
    # handleRuleEngineRequest
    api_response = api_instance.handle_rule_engine_request_using_post1(body, entity_type, entity_id, timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuleEngineControllerApi->handle_rule_engine_request_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| requestBody | 
 **entity_type** | **str**| entityType | 
 **entity_id** | **str**| entityId | 
 **timeout** | **int**| timeout | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_rule_engine_request_using_post2**
> DeferredResultResponseEntity handle_rule_engine_request_using_post2(body, entity_type, entity_id)

handleRuleEngineRequest

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
api_instance = pyTB.RuleEngineControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | requestBody
entity_type = 'entity_type_example' # str | entityType
entity_id = 'entity_id_example' # str | entityId

try:
    # handleRuleEngineRequest
    api_response = api_instance.handle_rule_engine_request_using_post2(body, entity_type, entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuleEngineControllerApi->handle_rule_engine_request_using_post2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| requestBody | 
 **entity_type** | **str**| entityType | 
 **entity_id** | **str**| entityId | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

