# openapi_client.UsersApi

All URIs are relative to *http://localhost:6820/slurm/v0.0.41*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_slurm_users**](UsersApi.md#create_slurm_users) | **POST** /users | Create Slurm users
[**get_all_slurm_users**](UsersApi.md#get_all_slurm_users) | **GET** /users | Get all Slurm users


# **create_slurm_users**
> InlineResponse2001 create_slurm_users(inline_object)

Create Slurm users

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
    api_instance = openapi_client.UsersApi(api_client)
    inline_object = openapi_client.InlineObject() # InlineObject | 

    try:
        # Create Slurm users
        api_response = api_instance.create_slurm_users(inline_object)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->create_slurm_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object** | [**InlineObject**](InlineObject.md)|  | 

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
**200** | Users created successfully. |  -  |
**400** | Bad request - invalid input data. |  -  |
**401** | Unauthorized - JWT token missing or invalid. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_slurm_users**
> InlineResponse200 get_all_slurm_users()

Get all Slurm users

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
    api_instance = openapi_client.UsersApi(api_client)
    
    try:
        # Get all Slurm users
        api_response = api_instance.get_all_slurm_users()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->get_all_slurm_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Slurm users. |  -  |
**401** | Unauthorized - JWT token missing or invalid. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

