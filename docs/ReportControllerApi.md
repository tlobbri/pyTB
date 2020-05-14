# pyTB.ReportControllerApi

All URIs are relative to *//dashboard.digitalconstructionhub.ovh/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_dashboard_report_using_post**](ReportControllerApi.md#download_dashboard_report_using_post) | **POST** /api/report/{dashboardId}/download | downloadDashboardReport
[**download_test_report_using_post**](ReportControllerApi.md#download_test_report_using_post) | **POST** /api/report/test{?reportsServerEndpointUrl} | downloadTestReport

# **download_dashboard_report_using_post**
> DeferredResultResponseEntity download_dashboard_report_using_post(body, dashboard_id)

downloadDashboardReport

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
api_instance = pyTB.ReportControllerApi(pyTB.ApiClient(configuration))
body = 'body_example' # str | reportParams
dashboard_id = 'dashboard_id_example' # str | dashboardId

try:
    # downloadDashboardReport
    api_response = api_instance.download_dashboard_report_using_post(body, dashboard_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportControllerApi->download_dashboard_report_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| reportParams | 
 **dashboard_id** | **str**| dashboardId | 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_test_report_using_post**
> DeferredResultResponseEntity download_test_report_using_post(body, reports_server_endpoint_url=reports_server_endpoint_url)

downloadTestReport

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
api_instance = pyTB.ReportControllerApi(pyTB.ApiClient(configuration))
body = pyTB.ReportConfig() # ReportConfig | reportConfig
reports_server_endpoint_url = 'reports_server_endpoint_url_example' # str | reportsServerEndpointUrl (optional)

try:
    # downloadTestReport
    api_response = api_instance.download_test_report_using_post(body, reports_server_endpoint_url=reports_server_endpoint_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportControllerApi->download_test_report_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportConfig**](ReportConfig.md)| reportConfig | 
 **reports_server_endpoint_url** | **str**| reportsServerEndpointUrl | [optional] 

### Return type

[**DeferredResultResponseEntity**](DeferredResultResponseEntity.md)

### Authorization

[X-Authorization](../README.md#X-Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

