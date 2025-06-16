# openapi_client.AccountsApi

All URIs are relative to *http://localhost:6820/slurm/v0.0.41*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_slurm_accounts**](AccountsApi.md#create_slurm_accounts) | **POST** /accounts | Create Slurm accounts
[**get_all_slurm_accounts**](AccountsApi.md#get_all_slurm_accounts) | **GET** /accounts | Get all Slurm accounts


# **create_slurm_accounts**
> InlineResponse2001 create_slurm_accounts(inline_object1)

Create Slurm accounts

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:6820/slurm/v0.0.41
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:6820/slurm/v0.0.41"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AccountsApi(api_client)
    inline_object1 = openapi_client.InlineObject1() # InlineObject1 | 

    try:
        # Create Slurm accounts
        api_response = api_instance.create_slurm_accounts(inline_object1)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->create_slurm_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accounts created successfully. |  -  |
**400** | Bad request - invalid input data. |  -  |
**401** | Unauthorized - JWT token missing or invalid. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_slurm_accounts**
> InlineResponse2002 get_all_slurm_accounts()

Get all Slurm accounts

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:6820/slurm/v0.0.41
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:6820/slurm/v0.0.41"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AccountsApi(api_client)
    
    try:
        # Get all Slurm accounts
        api_response = api_instance.get_all_slurm_accounts()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->get_all_slurm_accounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Slurm accounts. |  -  |
**401** | Unauthorized - JWT token missing or invalid. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

