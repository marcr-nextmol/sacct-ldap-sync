# openapi_client.SlurmApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slurm_v0040_delete_job**](SlurmApi.md#slurm_v0040_delete_job) | **DELETE** /slurm/v0.0.40/job/{job_id} | cancel or signal job
[**slurm_v0040_delete_jobs**](SlurmApi.md#slurm_v0040_delete_jobs) | **DELETE** /slurm/v0.0.40/jobs/ | send signal to list of jobs
[**slurm_v0040_delete_node**](SlurmApi.md#slurm_v0040_delete_node) | **DELETE** /slurm/v0.0.40/node/{node_name} | delete node
[**slurm_v0040_get_diag**](SlurmApi.md#slurm_v0040_get_diag) | **GET** /slurm/v0.0.40/diag/ | get diagnostics
[**slurm_v0040_get_job**](SlurmApi.md#slurm_v0040_get_job) | **GET** /slurm/v0.0.40/job/{job_id} | get job info
[**slurm_v0040_get_jobs**](SlurmApi.md#slurm_v0040_get_jobs) | **GET** /slurm/v0.0.40/jobs/ | get list of jobs
[**slurm_v0040_get_jobs_state**](SlurmApi.md#slurm_v0040_get_jobs_state) | **GET** /slurm/v0.0.40/jobs/state/ | get list of job states
[**slurm_v0040_get_licenses**](SlurmApi.md#slurm_v0040_get_licenses) | **GET** /slurm/v0.0.40/licenses/ | get all Slurm tracked license info
[**slurm_v0040_get_node**](SlurmApi.md#slurm_v0040_get_node) | **GET** /slurm/v0.0.40/node/{node_name} | get node info
[**slurm_v0040_get_nodes**](SlurmApi.md#slurm_v0040_get_nodes) | **GET** /slurm/v0.0.40/nodes/ | get node(s) info
[**slurm_v0040_get_partition**](SlurmApi.md#slurm_v0040_get_partition) | **GET** /slurm/v0.0.40/partition/{partition_name} | get partition info
[**slurm_v0040_get_partitions**](SlurmApi.md#slurm_v0040_get_partitions) | **GET** /slurm/v0.0.40/partitions/ | get all partition info
[**slurm_v0040_get_ping**](SlurmApi.md#slurm_v0040_get_ping) | **GET** /slurm/v0.0.40/ping/ | ping test
[**slurm_v0040_get_reconfigure**](SlurmApi.md#slurm_v0040_get_reconfigure) | **GET** /slurm/v0.0.40/reconfigure/ | request slurmctld reconfigure
[**slurm_v0040_get_reservation**](SlurmApi.md#slurm_v0040_get_reservation) | **GET** /slurm/v0.0.40/reservation/{reservation_name} | get reservation info
[**slurm_v0040_get_reservations**](SlurmApi.md#slurm_v0040_get_reservations) | **GET** /slurm/v0.0.40/reservations/ | get all reservation info
[**slurm_v0040_get_shares**](SlurmApi.md#slurm_v0040_get_shares) | **GET** /slurm/v0.0.40/shares | get fairshare info
[**slurm_v0040_post_job**](SlurmApi.md#slurm_v0040_post_job) | **POST** /slurm/v0.0.40/job/{job_id} | update job
[**slurm_v0040_post_job_submit**](SlurmApi.md#slurm_v0040_post_job_submit) | **POST** /slurm/v0.0.40/job/submit | submit new job
[**slurm_v0040_post_node**](SlurmApi.md#slurm_v0040_post_node) | **POST** /slurm/v0.0.40/node/{node_name} | update node properties


# **slurm_v0040_delete_job**
> V0040OpenapiResp slurm_v0040_delete_job(job_id, signal=signal, flags=flags)

cancel or signal job

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Job ID
signal = 'signal_example' # str | Signal to send to Job (optional)
flags = 'flags_example' # str | Signalling flags (optional)

    try:
        # cancel or signal job
        api_response = api_instance.slurm_v0040_delete_job(job_id, signal=signal, flags=flags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_delete_job: %s\n" % e)
```

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Job ID
signal = 'signal_example' # str | Signal to send to Job (optional)
flags = 'flags_example' # str | Signalling flags (optional)

    try:
        # cancel or signal job
        api_response = api_instance.slurm_v0040_delete_job(job_id, signal=signal, flags=flags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_delete_job: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Job ID
signal = 'signal_example' # str | Signal to send to Job (optional)
flags = 'flags_example' # str | Signalling flags (optional)

    try:
        # cancel or signal job
        api_response = api_instance.slurm_v0040_delete_job(job_id, signal=signal, flags=flags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_delete_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID | 
 **signal** | **str**| Signal to send to Job | [optional] 
 **flags** | **str**| Signalling flags | [optional] 

### Return type

[**V0040OpenapiResp**](V0040OpenapiResp.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job signal result |  -  |
**0** | job signal result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_delete_jobs**
> V0040OpenapiKillJobsResp slurm_v0040_delete_jobs(v0040_kill_jobs_msg=v0040_kill_jobs_msg)

send signal to list of jobs

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    v0040_kill_jobs_msg = openapi_client.V0040KillJobsMsg() # V0040KillJobsMsg | Signal or cancel jobs (optional)

    try:
        # send signal to list of jobs
        api_response = api_instance.slurm_v0040_delete_jobs(v0040_kill_jobs_msg=v0040_kill_jobs_msg)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_delete_jobs: %s\n" % e)
```

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    v0040_kill_jobs_msg = openapi_client.V0040KillJobsMsg() # V0040KillJobsMsg | Signal or cancel jobs (optional)

    try:
        # send signal to list of jobs
        api_response = api_instance.slurm_v0040_delete_jobs(v0040_kill_jobs_msg=v0040_kill_jobs_msg)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_delete_jobs: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    v0040_kill_jobs_msg = openapi_client.V0040KillJobsMsg() # V0040KillJobsMsg | Signal or cancel jobs (optional)

    try:
        # send signal to list of jobs
        api_response = api_instance.slurm_v0040_delete_jobs(v0040_kill_jobs_msg=v0040_kill_jobs_msg)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_delete_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0040_kill_jobs_msg** | [**V0040KillJobsMsg**](V0040KillJobsMsg.md)| Signal or cancel jobs | [optional] 

### Return type

[**V0040OpenapiKillJobsResp**](V0040OpenapiKillJobsResp.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | description of jobs to signal |  -  |
**0** | description of jobs to signal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_delete_node**
> V0040OpenapiResp slurm_v0040_delete_node(node_name)

delete node

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    node_name = 'node_name_example' # str | Node name

    try:
        # delete node
        api_response = api_instance.slurm_v0040_delete_node(node_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_delete_node: %s\n" % e)
```

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    node_name = 'node_name_example' # str | Node name

    try:
        # delete node
        api_response = api_instance.slurm_v0040_delete_node(node_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_delete_node: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    node_name = 'node_name_example' # str | Node name

    try:
        # delete node
        api_response = api_instance.slurm_v0040_delete_node(node_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_delete_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Node name | 

### Return type

[**V0040OpenapiResp**](V0040OpenapiResp.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node delete request result |  -  |
**0** | node delete request result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_get_diag**
> V0040OpenapiDiagResp slurm_v0040_get_diag()

get diagnostics

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    
    try:
        # get diagnostics
        api_response = api_instance.slurm_v0040_get_diag()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_diag: %s\n" % e)
```

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    
    try:
        # get diagnostics
        api_response = api_instance.slurm_v0040_get_diag()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_diag: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    
    try:
        # get diagnostics
        api_response = api_instance.slurm_v0040_get_diag()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_diag: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V0040OpenapiDiagResp**](V0040OpenapiDiagResp.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | diagnostic results |  -  |
**0** | diagnostic results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_get_job**
> V0040OpenapiJobInfoResp slurm_v0040_get_job(job_id, update_time=update_time, flags=flags)

get job info

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Job ID
update_time = 'update_time_example' # str | Filter jobs since update timestamp (optional)
flags = 'flags_example' # str | Query flags (optional)

    try:
        # get job info
        api_response = api_instance.slurm_v0040_get_job(job_id, update_time=update_time, flags=flags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_job: %s\n" % e)
```

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Job ID
update_time = 'update_time_example' # str | Filter jobs since update timestamp (optional)
flags = 'flags_example' # str | Query flags (optional)

    try:
        # get job info
        api_response = api_instance.slurm_v0040_get_job(job_id, update_time=update_time, flags=flags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_job: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Job ID
update_time = 'update_time_example' # str | Filter jobs since update timestamp (optional)
flags = 'flags_example' # str | Query flags (optional)

    try:
        # get job info
        api_response = api_instance.slurm_v0040_get_job(job_id, update_time=update_time, flags=flags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID | 
 **update_time** | **str**| Filter jobs since update timestamp | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**V0040OpenapiJobInfoResp**](V0040OpenapiJobInfoResp.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job(s) information |  -  |
**0** | job(s) information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_get_jobs**
> V0040OpenapiJobInfoResp slurm_v0040_get_jobs(update_time=update_time, flags=flags)

get list of jobs

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Filter jobs since update timestamp (optional)
flags = 'flags_example' # str | Query flags (optional)

    try:
        # get list of jobs
        api_response = api_instance.slurm_v0040_get_jobs(update_time=update_time, flags=flags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_jobs: %s\n" % e)
```

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Filter jobs since update timestamp (optional)
flags = 'flags_example' # str | Query flags (optional)

    try:
        # get list of jobs
        api_response = api_instance.slurm_v0040_get_jobs(update_time=update_time, flags=flags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_jobs: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Filter jobs since update timestamp (optional)
flags = 'flags_example' # str | Query flags (optional)

    try:
        # get list of jobs
        api_response = api_instance.slurm_v0040_get_jobs(update_time=update_time, flags=flags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Filter jobs since update timestamp | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**V0040OpenapiJobInfoResp**](V0040OpenapiJobInfoResp.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job(s) information |  -  |
**0** | job(s) information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_get_jobs_state**
> V0040OpenapiJobInfoResp slurm_v0040_get_jobs_state(update_time=update_time, flags=flags)

get list of job states

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Filter jobs since update timestamp (optional)
flags = 'flags_example' # str | Query flags (optional)

    try:
        # get list of job states
        api_response = api_instance.slurm_v0040_get_jobs_state(update_time=update_time, flags=flags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_jobs_state: %s\n" % e)
```

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Filter jobs since update timestamp (optional)
flags = 'flags_example' # str | Query flags (optional)

    try:
        # get list of job states
        api_response = api_instance.slurm_v0040_get_jobs_state(update_time=update_time, flags=flags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_jobs_state: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Filter jobs since update timestamp (optional)
flags = 'flags_example' # str | Query flags (optional)

    try:
        # get list of job states
        api_response = api_instance.slurm_v0040_get_jobs_state(update_time=update_time, flags=flags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_jobs_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Filter jobs since update timestamp | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**V0040OpenapiJobInfoResp**](V0040OpenapiJobInfoResp.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job(s) state information |  -  |
**0** | job(s) state information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_get_licenses**
> V0040OpenapiLicensesResp slurm_v0040_get_licenses()

get all Slurm tracked license info

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    
    try:
        # get all Slurm tracked license info
        api_response = api_instance.slurm_v0040_get_licenses()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_licenses: %s\n" % e)
```

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    
    try:
        # get all Slurm tracked license info
        api_response = api_instance.slurm_v0040_get_licenses()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_licenses: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    
    try:
        # get all Slurm tracked license info
        api_response = api_instance.slurm_v0040_get_licenses()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_licenses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V0040OpenapiLicensesResp**](V0040OpenapiLicensesResp.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | results of get all licenses |  -  |
**0** | results of get all licenses |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_get_node**
> V0040OpenapiNodesResp slurm_v0040_get_node(node_name, update_time=update_time, flags=flags)

get node info

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    node_name = 'node_name_example' # str | Node name
update_time = 'update_time_example' # str | Filter jobs since update timestamp (optional)
flags = 'flags_example' # str | Query flags (optional)

    try:
        # get node info
        api_response = api_instance.slurm_v0040_get_node(node_name, update_time=update_time, flags=flags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_node: %s\n" % e)
```

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    node_name = 'node_name_example' # str | Node name
update_time = 'update_time_example' # str | Filter jobs since update timestamp (optional)
flags = 'flags_example' # str | Query flags (optional)

    try:
        # get node info
        api_response = api_instance.slurm_v0040_get_node(node_name, update_time=update_time, flags=flags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_node: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    node_name = 'node_name_example' # str | Node name
update_time = 'update_time_example' # str | Filter jobs since update timestamp (optional)
flags = 'flags_example' # str | Query flags (optional)

    try:
        # get node info
        api_response = api_instance.slurm_v0040_get_node(node_name, update_time=update_time, flags=flags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Node name | 
 **update_time** | **str**| Filter jobs since update timestamp | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**V0040OpenapiNodesResp**](V0040OpenapiNodesResp.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node information |  -  |
**0** | node information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_get_nodes**
> V0040OpenapiNodesResp slurm_v0040_get_nodes(update_time=update_time, flags=flags)

get node(s) info

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Filter jobs since update timestamp (optional)
flags = 'flags_example' # str | Query flags (optional)

    try:
        # get node(s) info
        api_response = api_instance.slurm_v0040_get_nodes(update_time=update_time, flags=flags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_nodes: %s\n" % e)
```

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Filter jobs since update timestamp (optional)
flags = 'flags_example' # str | Query flags (optional)

    try:
        # get node(s) info
        api_response = api_instance.slurm_v0040_get_nodes(update_time=update_time, flags=flags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_nodes: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Filter jobs since update timestamp (optional)
flags = 'flags_example' # str | Query flags (optional)

    try:
        # get node(s) info
        api_response = api_instance.slurm_v0040_get_nodes(update_time=update_time, flags=flags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Filter jobs since update timestamp | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**V0040OpenapiNodesResp**](V0040OpenapiNodesResp.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node(s) information |  -  |
**0** | node(s) information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_get_partition**
> V0040OpenapiPartitionResp slurm_v0040_get_partition(partition_name, update_time=update_time, flags=flags)

get partition info

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    partition_name = 'partition_name_example' # str | Partition name
update_time = 'update_time_example' # str | Filter partitions since update timestamp (optional)
flags = 'flags_example' # str | Query flags (optional)

    try:
        # get partition info
        api_response = api_instance.slurm_v0040_get_partition(partition_name, update_time=update_time, flags=flags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_partition: %s\n" % e)
```

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    partition_name = 'partition_name_example' # str | Partition name
update_time = 'update_time_example' # str | Filter partitions since update timestamp (optional)
flags = 'flags_example' # str | Query flags (optional)

    try:
        # get partition info
        api_response = api_instance.slurm_v0040_get_partition(partition_name, update_time=update_time, flags=flags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_partition: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    partition_name = 'partition_name_example' # str | Partition name
update_time = 'update_time_example' # str | Filter partitions since update timestamp (optional)
flags = 'flags_example' # str | Query flags (optional)

    try:
        # get partition info
        api_response = api_instance.slurm_v0040_get_partition(partition_name, update_time=update_time, flags=flags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_partition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_name** | **str**| Partition name | 
 **update_time** | **str**| Filter partitions since update timestamp | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**V0040OpenapiPartitionResp**](V0040OpenapiPartitionResp.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | partition information |  -  |
**0** | partition information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_get_partitions**
> V0040OpenapiPartitionResp slurm_v0040_get_partitions(update_time=update_time, flags=flags)

get all partition info

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Filter partitions since update timestamp (optional)
flags = 'flags_example' # str | Query flags (optional)

    try:
        # get all partition info
        api_response = api_instance.slurm_v0040_get_partitions(update_time=update_time, flags=flags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_partitions: %s\n" % e)
```

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Filter partitions since update timestamp (optional)
flags = 'flags_example' # str | Query flags (optional)

    try:
        # get all partition info
        api_response = api_instance.slurm_v0040_get_partitions(update_time=update_time, flags=flags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_partitions: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Filter partitions since update timestamp (optional)
flags = 'flags_example' # str | Query flags (optional)

    try:
        # get all partition info
        api_response = api_instance.slurm_v0040_get_partitions(update_time=update_time, flags=flags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_partitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Filter partitions since update timestamp | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**V0040OpenapiPartitionResp**](V0040OpenapiPartitionResp.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | partition information |  -  |
**0** | partition information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_get_ping**
> V0040OpenapiPingArrayResp slurm_v0040_get_ping()

ping test

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    
    try:
        # ping test
        api_response = api_instance.slurm_v0040_get_ping()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_ping: %s\n" % e)
```

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    
    try:
        # ping test
        api_response = api_instance.slurm_v0040_get_ping()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_ping: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    
    try:
        # ping test
        api_response = api_instance.slurm_v0040_get_ping()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_ping: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V0040OpenapiPingArrayResp**](V0040OpenapiPingArrayResp.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | results of ping test |  -  |
**0** | results of ping test |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_get_reconfigure**
> V0040OpenapiResp slurm_v0040_get_reconfigure()

request slurmctld reconfigure

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    
    try:
        # request slurmctld reconfigure
        api_response = api_instance.slurm_v0040_get_reconfigure()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_reconfigure: %s\n" % e)
```

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    
    try:
        # request slurmctld reconfigure
        api_response = api_instance.slurm_v0040_get_reconfigure()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_reconfigure: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    
    try:
        # request slurmctld reconfigure
        api_response = api_instance.slurm_v0040_get_reconfigure()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_reconfigure: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V0040OpenapiResp**](V0040OpenapiResp.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reconfigure request result |  -  |
**0** | reconfigure request result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_get_reservation**
> V0040OpenapiReservationResp slurm_v0040_get_reservation(reservation_name, update_time=update_time)

get reservation info

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    reservation_name = 'reservation_name_example' # str | Reservation name
update_time = 'update_time_example' # str | Filter reservations since update timestamp (optional)

    try:
        # get reservation info
        api_response = api_instance.slurm_v0040_get_reservation(reservation_name, update_time=update_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_reservation: %s\n" % e)
```

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    reservation_name = 'reservation_name_example' # str | Reservation name
update_time = 'update_time_example' # str | Filter reservations since update timestamp (optional)

    try:
        # get reservation info
        api_response = api_instance.slurm_v0040_get_reservation(reservation_name, update_time=update_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_reservation: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    reservation_name = 'reservation_name_example' # str | Reservation name
update_time = 'update_time_example' # str | Filter reservations since update timestamp (optional)

    try:
        # get reservation info
        api_response = api_instance.slurm_v0040_get_reservation(reservation_name, update_time=update_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_reservation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_name** | **str**| Reservation name | 
 **update_time** | **str**| Filter reservations since update timestamp | [optional] 

### Return type

[**V0040OpenapiReservationResp**](V0040OpenapiReservationResp.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reservation information |  -  |
**0** | reservation information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_get_reservations**
> V0040OpenapiReservationResp slurm_v0040_get_reservations(update_time=update_time)

get all reservation info

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Filter reservations since update timestamp (optional)

    try:
        # get all reservation info
        api_response = api_instance.slurm_v0040_get_reservations(update_time=update_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_reservations: %s\n" % e)
```

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Filter reservations since update timestamp (optional)

    try:
        # get all reservation info
        api_response = api_instance.slurm_v0040_get_reservations(update_time=update_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_reservations: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Filter reservations since update timestamp (optional)

    try:
        # get all reservation info
        api_response = api_instance.slurm_v0040_get_reservations(update_time=update_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_reservations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Filter reservations since update timestamp | [optional] 

### Return type

[**V0040OpenapiReservationResp**](V0040OpenapiReservationResp.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reservation information |  -  |
**0** | reservation information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_get_shares**
> V0040OpenapiSharesResp slurm_v0040_get_shares(accounts=accounts, users=users)

get fairshare info

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    accounts = 'accounts_example' # str | Accounts to query (optional)
users = 'users_example' # str | Users to query (optional)

    try:
        # get fairshare info
        api_response = api_instance.slurm_v0040_get_shares(accounts=accounts, users=users)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_shares: %s\n" % e)
```

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    accounts = 'accounts_example' # str | Accounts to query (optional)
users = 'users_example' # str | Users to query (optional)

    try:
        # get fairshare info
        api_response = api_instance.slurm_v0040_get_shares(accounts=accounts, users=users)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_shares: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    accounts = 'accounts_example' # str | Accounts to query (optional)
users = 'users_example' # str | Users to query (optional)

    try:
        # get fairshare info
        api_response = api_instance.slurm_v0040_get_shares(accounts=accounts, users=users)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_get_shares: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accounts** | **str**| Accounts to query | [optional] 
 **users** | **str**| Users to query | [optional] 

### Return type

[**V0040OpenapiSharesResp**](V0040OpenapiSharesResp.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | shares information |  -  |
**0** | shares information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_post_job**
> V0040OpenapiJobPostResponse slurm_v0040_post_job(job_id, v0040_job_desc_msg=v0040_job_desc_msg)

update job

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Job ID
v0040_job_desc_msg = openapi_client.V0040JobDescMsg() # V0040JobDescMsg | Job update description (optional)

    try:
        # update job
        api_response = api_instance.slurm_v0040_post_job(job_id, v0040_job_desc_msg=v0040_job_desc_msg)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_post_job: %s\n" % e)
```

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Job ID
v0040_job_desc_msg = openapi_client.V0040JobDescMsg() # V0040JobDescMsg | Job update description (optional)

    try:
        # update job
        api_response = api_instance.slurm_v0040_post_job(job_id, v0040_job_desc_msg=v0040_job_desc_msg)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_post_job: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Job ID
v0040_job_desc_msg = openapi_client.V0040JobDescMsg() # V0040JobDescMsg | Job update description (optional)

    try:
        # update job
        api_response = api_instance.slurm_v0040_post_job(job_id, v0040_job_desc_msg=v0040_job_desc_msg)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_post_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID | 
 **v0040_job_desc_msg** | [**V0040JobDescMsg**](V0040JobDescMsg.md)| Job update description | [optional] 

### Return type

[**V0040OpenapiJobPostResponse**](V0040OpenapiJobPostResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job update result |  -  |
**0** | job update result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_post_job_submit**
> V0040OpenapiJobSubmitResponse slurm_v0040_post_job_submit(v0040_job_submit_req=v0040_job_submit_req)

submit new job

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    v0040_job_submit_req = openapi_client.V0040JobSubmitReq() # V0040JobSubmitReq | Job description (optional)

    try:
        # submit new job
        api_response = api_instance.slurm_v0040_post_job_submit(v0040_job_submit_req=v0040_job_submit_req)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_post_job_submit: %s\n" % e)
```

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    v0040_job_submit_req = openapi_client.V0040JobSubmitReq() # V0040JobSubmitReq | Job description (optional)

    try:
        # submit new job
        api_response = api_instance.slurm_v0040_post_job_submit(v0040_job_submit_req=v0040_job_submit_req)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_post_job_submit: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    v0040_job_submit_req = openapi_client.V0040JobSubmitReq() # V0040JobSubmitReq | Job description (optional)

    try:
        # submit new job
        api_response = api_instance.slurm_v0040_post_job_submit(v0040_job_submit_req=v0040_job_submit_req)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_post_job_submit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0040_job_submit_req** | [**V0040JobSubmitReq**](V0040JobSubmitReq.md)| Job description | [optional] 

### Return type

[**V0040OpenapiJobSubmitResponse**](V0040OpenapiJobSubmitResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job submission response |  -  |
**0** | job submission response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0040_post_node**
> V0040OpenapiResp slurm_v0040_post_node(node_name, v0040_update_node_msg=v0040_update_node_msg)

update node properties

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    node_name = 'node_name_example' # str | Node name
v0040_update_node_msg = openapi_client.V0040UpdateNodeMsg() # V0040UpdateNodeMsg | Node update description (optional)

    try:
        # update node properties
        api_response = api_instance.slurm_v0040_post_node(node_name, v0040_update_node_msg=v0040_update_node_msg)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_post_node: %s\n" % e)
```

* Api Key Authentication (token):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    node_name = 'node_name_example' # str | Node name
v0040_update_node_msg = openapi_client.V0040UpdateNodeMsg() # V0040UpdateNodeMsg | Node update description (optional)

    try:
        # update node properties
        api_response = api_instance.slurm_v0040_post_node(node_name, v0040_update_node_msg=v0040_update_node_msg)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_post_node: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import openapi_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: token
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-TOKEN': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-TOKEN'] = 'Bearer'

# Configure API key authorization: user
configuration = openapi_client.Configuration(
    host = "http://localhost",
    api_key = {
        'X-SLURM-USER-NAME': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-SLURM-USER-NAME'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    node_name = 'node_name_example' # str | Node name
v0040_update_node_msg = openapi_client.V0040UpdateNodeMsg() # V0040UpdateNodeMsg | Node update description (optional)

    try:
        # update node properties
        api_response = api_instance.slurm_v0040_post_node(node_name, v0040_update_node_msg=v0040_update_node_msg)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlurmApi->slurm_v0040_post_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Node name | 
 **v0040_update_node_msg** | [**V0040UpdateNodeMsg**](V0040UpdateNodeMsg.md)| Node update description | [optional] 

### Return type

[**V0040OpenapiResp**](V0040OpenapiResp.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [token](../README.md#token), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: application/json, application/x-yaml
 - **Accept**: application/json, application/x-yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node update request result |  -  |
**0** | node update request result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

