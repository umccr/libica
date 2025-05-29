# libica.openapi.v3.EventLogApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event_logs**](EventLogApi.md#get_event_logs) | **GET** /api/eventLog | Retrieve a list of event logs.
[**search_event_logs**](EventLogApi.md#search_event_logs) | **POST** /api/eventLog:search | Search event logs.


# **get_event_logs**
> EventLogListV3 get_event_logs(code=code, code_filter_type=code_filter_type, category=category, date_from=date_from, date_until=date_until, rows=rows)

Retrieve a list of event logs.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.event_log_list_v3 import EventLogListV3
from libica.openapi.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /ica/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.v3.Configuration(
    host = "/ica/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JwtAuth
configuration = libica.openapi.v3.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with libica.openapi.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libica.openapi.v3.EventLogApi(api_client)
    code = 'code_example' # str | Code (optional)
    code_filter_type = 'code_filter_type_example' # str | Code filter type (optional)
    category = 'category_example' # str | Category (optional)
    date_from = 'date_from_example' # str | Date from. Format: yyyy-MM-dd'T'HH:mm:ss.SSS'Z' eg: 2017-01-10T10:47:56.039Z (optional)
    date_until = 'date_until_example' # str | Date until. Format: yyyy-MM-dd'T'HH:mm:ss.SSS'Z' eg: 2017-01-10T10:47:56.039Z (optional)
    rows = 250 # int | Amount of rows to fetch (chronologically oldest first). Maximum 250. Defaults to 250 (optional) (default to 250)

    try:
        # Retrieve a list of event logs.
        api_response = api_instance.get_event_logs(code=code, code_filter_type=code_filter_type, category=category, date_from=date_from, date_until=date_until, rows=rows)
        print("The response of EventLogApi->get_event_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventLogApi->get_event_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Code | [optional] 
 **code_filter_type** | **str**| Code filter type | [optional] 
 **category** | **str**| Category | [optional] 
 **date_from** | **str**| Date from. Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39; eg: 2017-01-10T10:47:56.039Z | [optional] 
 **date_until** | **str**| Date until. Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39; eg: 2017-01-10T10:47:56.039Z | [optional] 
 **rows** | **int**| Amount of rows to fetch (chronologically oldest first). Maximum 250. Defaults to 250 | [optional] [default to 250]

### Return type

[**EventLogListV3**](EventLogListV3.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of event logs is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_event_logs**
> EventLogPagedListV4 search_event_logs(page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort, event_log_query_parameters_v4=event_log_query_parameters_v4)

Search event logs.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import libica.openapi.v3
from libica.openapi.v3.models.event_log_paged_list_v4 import EventLogPagedListV4
from libica.openapi.v3.models.event_log_query_parameters_v4 import EventLogQueryParametersV4
from libica.openapi.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /ica/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.v3.Configuration(
    host = "/ica/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JwtAuth
configuration = libica.openapi.v3.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with libica.openapi.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = libica.openapi.v3.EventLogApi(api_client)
    page_offset = 'page_offset_example' # str | [only use with offset-based paging]<br>The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = 'page_token_example' # str | [only use with cursor-based paging]<br>The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = 'page_size_example' # str | [can be used with both offset- and cursor-based paging]<br>The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results (optional)
    sort = 'sort_example' # str | [only use with offset-based paging]<br>Which field to order the results by. The default order is ascending, suffix with ' desc' to sort descending (suffix ' asc' also works for ascending). Multiple values should be separated with commas. An example: \"?sort=sortAttribute1, sortAttribute2 desc\"  The attributes for which sorting is supported: - timeCreated  (optional)
    event_log_query_parameters_v4 = libica.openapi.v3.EventLogQueryParametersV4() # EventLogQueryParametersV4 |  (optional)

    try:
        # Search event logs.
        api_response = api_instance.search_event_logs(page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort, event_log_query_parameters_v4=event_log_query_parameters_v4)
        print("The response of EventLogApi->search_event_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventLogApi->search_event_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_offset** | **str**| [only use with offset-based paging]&lt;br&gt;The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages | [optional] 
 **page_token** | **str**| [only use with cursor-based paging]&lt;br&gt;The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. | [optional] 
 **page_size** | **str**| [can be used with both offset- and cursor-based paging]&lt;br&gt;The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results | [optional] 
 **sort** | **str**| [only use with offset-based paging]&lt;br&gt;Which field to order the results by. The default order is ascending, suffix with &#39; desc&#39; to sort descending (suffix &#39; asc&#39; also works for ascending). Multiple values should be separated with commas. An example: \&quot;?sort&#x3D;sortAttribute1, sortAttribute2 desc\&quot;  The attributes for which sorting is supported: - timeCreated  | [optional] 
 **event_log_query_parameters_v4** | [**EventLogQueryParametersV4**](EventLogQueryParametersV4.md)|  | [optional] 

### Return type

[**EventLogPagedListV4**](EventLogPagedListV4.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v4+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v4+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of event logs is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

