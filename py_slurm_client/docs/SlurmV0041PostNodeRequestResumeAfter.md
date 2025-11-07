# SlurmV0041PostNodeRequestResumeAfter

Number of seconds after which to automatically resume DOWN or DRAINED node

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from openapi_client.models.slurm_v0041_post_node_request_resume_after import SlurmV0041PostNodeRequestResumeAfter

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041PostNodeRequestResumeAfter from a JSON string
slurm_v0041_post_node_request_resume_after_instance = SlurmV0041PostNodeRequestResumeAfter.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041PostNodeRequestResumeAfter.to_json())

# convert the object into a dict
slurm_v0041_post_node_request_resume_after_dict = slurm_v0041_post_node_request_resume_after_instance.to_dict()
# create an instance of SlurmV0041PostNodeRequestResumeAfter from a dict
slurm_v0041_post_node_request_resume_after_from_dict = SlurmV0041PostNodeRequestResumeAfter.from_dict(slurm_v0041_post_node_request_resume_after_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


