# openapi_client.SlurmApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slurm_v0041_delete_job**](SlurmApi.md#slurm_v0041_delete_job) | **DELETE** /slurm/v0.0.41/job/{job_id} | cancel or signal job
[**slurm_v0041_delete_jobs**](SlurmApi.md#slurm_v0041_delete_jobs) | **DELETE** /slurm/v0.0.41/jobs/ | send signal to list of jobs
[**slurm_v0041_delete_node**](SlurmApi.md#slurm_v0041_delete_node) | **DELETE** /slurm/v0.0.41/node/{node_name} | delete node
[**slurm_v0041_get_diag**](SlurmApi.md#slurm_v0041_get_diag) | **GET** /slurm/v0.0.41/diag/ | get diagnostics
[**slurm_v0041_get_job**](SlurmApi.md#slurm_v0041_get_job) | **GET** /slurm/v0.0.41/job/{job_id} | get job info
[**slurm_v0041_get_jobs**](SlurmApi.md#slurm_v0041_get_jobs) | **GET** /slurm/v0.0.41/jobs/ | get list of jobs
[**slurm_v0041_get_jobs_state**](SlurmApi.md#slurm_v0041_get_jobs_state) | **GET** /slurm/v0.0.41/jobs/state/ | get list of job states
[**slurm_v0041_get_licenses**](SlurmApi.md#slurm_v0041_get_licenses) | **GET** /slurm/v0.0.41/licenses/ | get all Slurm tracked license info
[**slurm_v0041_get_node**](SlurmApi.md#slurm_v0041_get_node) | **GET** /slurm/v0.0.41/node/{node_name} | get node info
[**slurm_v0041_get_nodes**](SlurmApi.md#slurm_v0041_get_nodes) | **GET** /slurm/v0.0.41/nodes/ | get node(s) info
[**slurm_v0041_get_partition**](SlurmApi.md#slurm_v0041_get_partition) | **GET** /slurm/v0.0.41/partition/{partition_name} | get partition info
[**slurm_v0041_get_partitions**](SlurmApi.md#slurm_v0041_get_partitions) | **GET** /slurm/v0.0.41/partitions/ | get all partition info
[**slurm_v0041_get_ping**](SlurmApi.md#slurm_v0041_get_ping) | **GET** /slurm/v0.0.41/ping/ | ping test
[**slurm_v0041_get_reconfigure**](SlurmApi.md#slurm_v0041_get_reconfigure) | **GET** /slurm/v0.0.41/reconfigure/ | request slurmctld reconfigure
[**slurm_v0041_get_reservation**](SlurmApi.md#slurm_v0041_get_reservation) | **GET** /slurm/v0.0.41/reservation/{reservation_name} | get reservation info
[**slurm_v0041_get_reservations**](SlurmApi.md#slurm_v0041_get_reservations) | **GET** /slurm/v0.0.41/reservations/ | get all reservation info
[**slurm_v0041_get_shares**](SlurmApi.md#slurm_v0041_get_shares) | **GET** /slurm/v0.0.41/shares | get fairshare info
[**slurm_v0041_post_job**](SlurmApi.md#slurm_v0041_post_job) | **POST** /slurm/v0.0.41/job/{job_id} | update job
[**slurm_v0041_post_job_allocate**](SlurmApi.md#slurm_v0041_post_job_allocate) | **POST** /slurm/v0.0.41/job/allocate | submit new job allocation without any steps that must be signaled to stop
[**slurm_v0041_post_job_submit**](SlurmApi.md#slurm_v0041_post_job_submit) | **POST** /slurm/v0.0.41/job/submit | submit new job
[**slurm_v0041_post_node**](SlurmApi.md#slurm_v0041_post_node) | **POST** /slurm/v0.0.41/node/{node_name} | update node properties


# **slurm_v0041_delete_job**
> V0041OpenapiResp slurm_v0041_delete_job(job_id, signal=signal, flags=flags)

cancel or signal job

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0041_openapi_resp import V0041OpenapiResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Job ID
    signal = 'signal_example' # str | Signal to send to Job (optional)
    flags = 'flags_example' # str | Signalling flags (optional)

    try:
        # cancel or signal job
        api_response = api_instance.slurm_v0041_delete_job(job_id, signal=signal, flags=flags)
        print("The response of SlurmApi->slurm_v0041_delete_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_delete_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID | 
 **signal** | **str**| Signal to send to Job | [optional] 
 **flags** | **str**| Signalling flags | [optional] 

### Return type

[**V0041OpenapiResp**](V0041OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job signal result |  -  |
**0** | job signal result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_delete_jobs**
> SlurmV0041DeleteJobs200Response slurm_v0041_delete_jobs(slurm_v0041_delete_jobs_request=slurm_v0041_delete_jobs_request)

send signal to list of jobs

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.slurm_v0041_delete_jobs200_response import SlurmV0041DeleteJobs200Response
from openapi_client.models.slurm_v0041_delete_jobs_request import SlurmV0041DeleteJobsRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    slurm_v0041_delete_jobs_request = openapi_client.SlurmV0041DeleteJobsRequest() # SlurmV0041DeleteJobsRequest | Signal or cancel jobs (optional)

    try:
        # send signal to list of jobs
        api_response = api_instance.slurm_v0041_delete_jobs(slurm_v0041_delete_jobs_request=slurm_v0041_delete_jobs_request)
        print("The response of SlurmApi->slurm_v0041_delete_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_delete_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slurm_v0041_delete_jobs_request** | [**SlurmV0041DeleteJobsRequest**](SlurmV0041DeleteJobsRequest.md)| Signal or cancel jobs | [optional] 

### Return type

[**SlurmV0041DeleteJobs200Response**](SlurmV0041DeleteJobs200Response.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | description of jobs to signal |  -  |
**0** | description of jobs to signal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_delete_node**
> V0041OpenapiResp slurm_v0041_delete_node(node_name)

delete node

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0041_openapi_resp import V0041OpenapiResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    node_name = 'node_name_example' # str | Node name

    try:
        # delete node
        api_response = api_instance.slurm_v0041_delete_node(node_name)
        print("The response of SlurmApi->slurm_v0041_delete_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_delete_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Node name | 

### Return type

[**V0041OpenapiResp**](V0041OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node delete request result |  -  |
**0** | node delete request result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_get_diag**
> SlurmV0041GetDiag200Response slurm_v0041_get_diag()

get diagnostics

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.slurm_v0041_get_diag200_response import SlurmV0041GetDiag200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)

    try:
        # get diagnostics
        api_response = api_instance.slurm_v0041_get_diag()
        print("The response of SlurmApi->slurm_v0041_get_diag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_get_diag: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SlurmV0041GetDiag200Response**](SlurmV0041GetDiag200Response.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | diagnostic results |  -  |
**0** | diagnostic results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_get_job**
> V0041OpenapiJobInfoResp slurm_v0041_get_job(job_id, update_time=update_time, flags=flags)

get job info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0041_openapi_job_info_resp import V0041OpenapiJobInfoResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Job ID
    update_time = 'update_time_example' # str | Filter jobs since update timestamp (optional)
    flags = 'flags_example' # str | Query flags (optional)

    try:
        # get job info
        api_response = api_instance.slurm_v0041_get_job(job_id, update_time=update_time, flags=flags)
        print("The response of SlurmApi->slurm_v0041_get_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_get_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID | 
 **update_time** | **str**| Filter jobs since update timestamp | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**V0041OpenapiJobInfoResp**](V0041OpenapiJobInfoResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job(s) information |  -  |
**0** | job(s) information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_get_jobs**
> V0041OpenapiJobInfoResp slurm_v0041_get_jobs(update_time=update_time, flags=flags)

get list of jobs

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0041_openapi_job_info_resp import V0041OpenapiJobInfoResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Filter jobs since update timestamp (optional)
    flags = 'flags_example' # str | Query flags (optional)

    try:
        # get list of jobs
        api_response = api_instance.slurm_v0041_get_jobs(update_time=update_time, flags=flags)
        print("The response of SlurmApi->slurm_v0041_get_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_get_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Filter jobs since update timestamp | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**V0041OpenapiJobInfoResp**](V0041OpenapiJobInfoResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job(s) information |  -  |
**0** | job(s) information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_get_jobs_state**
> V0041OpenapiJobInfoResp slurm_v0041_get_jobs_state(update_time=update_time, flags=flags)

get list of job states

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0041_openapi_job_info_resp import V0041OpenapiJobInfoResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Filter jobs since update timestamp (optional)
    flags = 'flags_example' # str | Query flags (optional)

    try:
        # get list of job states
        api_response = api_instance.slurm_v0041_get_jobs_state(update_time=update_time, flags=flags)
        print("The response of SlurmApi->slurm_v0041_get_jobs_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_get_jobs_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Filter jobs since update timestamp | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**V0041OpenapiJobInfoResp**](V0041OpenapiJobInfoResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job(s) state information |  -  |
**0** | job(s) state information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_get_licenses**
> SlurmV0041GetLicenses200Response slurm_v0041_get_licenses()

get all Slurm tracked license info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.slurm_v0041_get_licenses200_response import SlurmV0041GetLicenses200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)

    try:
        # get all Slurm tracked license info
        api_response = api_instance.slurm_v0041_get_licenses()
        print("The response of SlurmApi->slurm_v0041_get_licenses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_get_licenses: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SlurmV0041GetLicenses200Response**](SlurmV0041GetLicenses200Response.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | results of get all licenses |  -  |
**0** | results of get all licenses |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_get_node**
> V0041OpenapiNodesResp slurm_v0041_get_node(node_name, update_time=update_time, flags=flags)

get node info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0041_openapi_nodes_resp import V0041OpenapiNodesResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    node_name = 'node_name_example' # str | Node name
    update_time = 'update_time_example' # str | Filter jobs since update timestamp (optional)
    flags = 'flags_example' # str | Query flags (optional)

    try:
        # get node info
        api_response = api_instance.slurm_v0041_get_node(node_name, update_time=update_time, flags=flags)
        print("The response of SlurmApi->slurm_v0041_get_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_get_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Node name | 
 **update_time** | **str**| Filter jobs since update timestamp | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**V0041OpenapiNodesResp**](V0041OpenapiNodesResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node information |  -  |
**0** | node information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_get_nodes**
> V0041OpenapiNodesResp slurm_v0041_get_nodes(update_time=update_time, flags=flags)

get node(s) info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0041_openapi_nodes_resp import V0041OpenapiNodesResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Filter jobs since update timestamp (optional)
    flags = 'flags_example' # str | Query flags (optional)

    try:
        # get node(s) info
        api_response = api_instance.slurm_v0041_get_nodes(update_time=update_time, flags=flags)
        print("The response of SlurmApi->slurm_v0041_get_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_get_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Filter jobs since update timestamp | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**V0041OpenapiNodesResp**](V0041OpenapiNodesResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node(s) information |  -  |
**0** | node(s) information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_get_partition**
> V0041OpenapiPartitionResp slurm_v0041_get_partition(partition_name, update_time=update_time, flags=flags)

get partition info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0041_openapi_partition_resp import V0041OpenapiPartitionResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    partition_name = 'partition_name_example' # str | Partition name
    update_time = 'update_time_example' # str | Filter partitions since update timestamp (optional)
    flags = 'flags_example' # str | Query flags (optional)

    try:
        # get partition info
        api_response = api_instance.slurm_v0041_get_partition(partition_name, update_time=update_time, flags=flags)
        print("The response of SlurmApi->slurm_v0041_get_partition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_get_partition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_name** | **str**| Partition name | 
 **update_time** | **str**| Filter partitions since update timestamp | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**V0041OpenapiPartitionResp**](V0041OpenapiPartitionResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | partition information |  -  |
**0** | partition information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_get_partitions**
> V0041OpenapiPartitionResp slurm_v0041_get_partitions(update_time=update_time, flags=flags)

get all partition info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0041_openapi_partition_resp import V0041OpenapiPartitionResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Filter partitions since update timestamp (optional)
    flags = 'flags_example' # str | Query flags (optional)

    try:
        # get all partition info
        api_response = api_instance.slurm_v0041_get_partitions(update_time=update_time, flags=flags)
        print("The response of SlurmApi->slurm_v0041_get_partitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_get_partitions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Filter partitions since update timestamp | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**V0041OpenapiPartitionResp**](V0041OpenapiPartitionResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | partition information |  -  |
**0** | partition information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_get_ping**
> SlurmV0041GetPing200Response slurm_v0041_get_ping()

ping test

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.slurm_v0041_get_ping200_response import SlurmV0041GetPing200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)

    try:
        # ping test
        api_response = api_instance.slurm_v0041_get_ping()
        print("The response of SlurmApi->slurm_v0041_get_ping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_get_ping: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SlurmV0041GetPing200Response**](SlurmV0041GetPing200Response.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | results of ping test |  -  |
**0** | results of ping test |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_get_reconfigure**
> V0041OpenapiResp slurm_v0041_get_reconfigure()

request slurmctld reconfigure

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0041_openapi_resp import V0041OpenapiResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)

    try:
        # request slurmctld reconfigure
        api_response = api_instance.slurm_v0041_get_reconfigure()
        print("The response of SlurmApi->slurm_v0041_get_reconfigure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_get_reconfigure: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0041OpenapiResp**](V0041OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reconfigure request result |  -  |
**0** | reconfigure request result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_get_reservation**
> V0041OpenapiReservationResp slurm_v0041_get_reservation(reservation_name, update_time=update_time)

get reservation info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0041_openapi_reservation_resp import V0041OpenapiReservationResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    reservation_name = 'reservation_name_example' # str | Reservation name
    update_time = 'update_time_example' # str | Filter reservations since update timestamp (optional)

    try:
        # get reservation info
        api_response = api_instance.slurm_v0041_get_reservation(reservation_name, update_time=update_time)
        print("The response of SlurmApi->slurm_v0041_get_reservation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_get_reservation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_name** | **str**| Reservation name | 
 **update_time** | **str**| Filter reservations since update timestamp | [optional] 

### Return type

[**V0041OpenapiReservationResp**](V0041OpenapiReservationResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reservation information |  -  |
**0** | reservation information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_get_reservations**
> V0041OpenapiReservationResp slurm_v0041_get_reservations(update_time=update_time)

get all reservation info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0041_openapi_reservation_resp import V0041OpenapiReservationResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Filter reservations since update timestamp (optional)

    try:
        # get all reservation info
        api_response = api_instance.slurm_v0041_get_reservations(update_time=update_time)
        print("The response of SlurmApi->slurm_v0041_get_reservations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_get_reservations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Filter reservations since update timestamp | [optional] 

### Return type

[**V0041OpenapiReservationResp**](V0041OpenapiReservationResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reservation information |  -  |
**0** | reservation information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_get_shares**
> SlurmV0041GetShares200Response slurm_v0041_get_shares(accounts=accounts, users=users)

get fairshare info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.slurm_v0041_get_shares200_response import SlurmV0041GetShares200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    accounts = 'accounts_example' # str | Accounts to query (optional)
    users = 'users_example' # str | Users to query (optional)

    try:
        # get fairshare info
        api_response = api_instance.slurm_v0041_get_shares(accounts=accounts, users=users)
        print("The response of SlurmApi->slurm_v0041_get_shares:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_get_shares: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accounts** | **str**| Accounts to query | [optional] 
 **users** | **str**| Users to query | [optional] 

### Return type

[**SlurmV0041GetShares200Response**](SlurmV0041GetShares200Response.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | shares information |  -  |
**0** | shares information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_post_job**
> SlurmV0041PostJob200Response slurm_v0041_post_job(job_id, slurm_v0041_post_job_submit_request_jobs_inner=slurm_v0041_post_job_submit_request_jobs_inner)

update job

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.slurm_v0041_post_job200_response import SlurmV0041PostJob200Response
from openapi_client.models.slurm_v0041_post_job_submit_request_jobs_inner import SlurmV0041PostJobSubmitRequestJobsInner
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Job ID
    slurm_v0041_post_job_submit_request_jobs_inner = openapi_client.SlurmV0041PostJobSubmitRequestJobsInner() # SlurmV0041PostJobSubmitRequestJobsInner | Job update description (optional)

    try:
        # update job
        api_response = api_instance.slurm_v0041_post_job(job_id, slurm_v0041_post_job_submit_request_jobs_inner=slurm_v0041_post_job_submit_request_jobs_inner)
        print("The response of SlurmApi->slurm_v0041_post_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_post_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID | 
 **slurm_v0041_post_job_submit_request_jobs_inner** | [**SlurmV0041PostJobSubmitRequestJobsInner**](SlurmV0041PostJobSubmitRequestJobsInner.md)| Job update description | [optional] 

### Return type

[**SlurmV0041PostJob200Response**](SlurmV0041PostJob200Response.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job update result |  -  |
**0** | job update result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_post_job_allocate**
> SlurmV0041PostJobAllocate200Response slurm_v0041_post_job_allocate(slurm_v0041_post_job_allocate_request=slurm_v0041_post_job_allocate_request)

submit new job allocation without any steps that must be signaled to stop

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.slurm_v0041_post_job_allocate200_response import SlurmV0041PostJobAllocate200Response
from openapi_client.models.slurm_v0041_post_job_allocate_request import SlurmV0041PostJobAllocateRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    slurm_v0041_post_job_allocate_request = openapi_client.SlurmV0041PostJobAllocateRequest() # SlurmV0041PostJobAllocateRequest | Job allocation description (optional)

    try:
        # submit new job allocation without any steps that must be signaled to stop
        api_response = api_instance.slurm_v0041_post_job_allocate(slurm_v0041_post_job_allocate_request=slurm_v0041_post_job_allocate_request)
        print("The response of SlurmApi->slurm_v0041_post_job_allocate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_post_job_allocate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slurm_v0041_post_job_allocate_request** | [**SlurmV0041PostJobAllocateRequest**](SlurmV0041PostJobAllocateRequest.md)| Job allocation description | [optional] 

### Return type

[**SlurmV0041PostJobAllocate200Response**](SlurmV0041PostJobAllocate200Response.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job allocation response |  -  |
**0** | job allocation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_post_job_submit**
> SlurmV0041PostJobSubmit200Response slurm_v0041_post_job_submit(slurm_v0041_post_job_submit_request=slurm_v0041_post_job_submit_request)

submit new job

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.slurm_v0041_post_job_submit200_response import SlurmV0041PostJobSubmit200Response
from openapi_client.models.slurm_v0041_post_job_submit_request import SlurmV0041PostJobSubmitRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    slurm_v0041_post_job_submit_request = openapi_client.SlurmV0041PostJobSubmitRequest() # SlurmV0041PostJobSubmitRequest | Job description (optional)

    try:
        # submit new job
        api_response = api_instance.slurm_v0041_post_job_submit(slurm_v0041_post_job_submit_request=slurm_v0041_post_job_submit_request)
        print("The response of SlurmApi->slurm_v0041_post_job_submit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_post_job_submit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slurm_v0041_post_job_submit_request** | [**SlurmV0041PostJobSubmitRequest**](SlurmV0041PostJobSubmitRequest.md)| Job description | [optional] 

### Return type

[**SlurmV0041PostJobSubmit200Response**](SlurmV0041PostJobSubmit200Response.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job submission response |  -  |
**0** | job submission response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_post_node**
> V0041OpenapiResp slurm_v0041_post_node(node_name, slurm_v0041_post_node_request=slurm_v0041_post_node_request)

update node properties

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.slurm_v0041_post_node_request import SlurmV0041PostNodeRequest
from openapi_client.models.v0041_openapi_resp import V0041OpenapiResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    node_name = 'node_name_example' # str | Node name
    slurm_v0041_post_node_request = openapi_client.SlurmV0041PostNodeRequest() # SlurmV0041PostNodeRequest | Node update description (optional)

    try:
        # update node properties
        api_response = api_instance.slurm_v0041_post_node(node_name, slurm_v0041_post_node_request=slurm_v0041_post_node_request)
        print("The response of SlurmApi->slurm_v0041_post_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_post_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Node name | 
 **slurm_v0041_post_node_request** | [**SlurmV0041PostNodeRequest**](SlurmV0041PostNodeRequest.md)| Node update description | [optional] 

### Return type

[**V0041OpenapiResp**](V0041OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node update request result |  -  |
**0** | node update request result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

