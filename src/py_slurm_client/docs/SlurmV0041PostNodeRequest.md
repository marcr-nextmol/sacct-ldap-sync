# SlurmV0041PostNodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Arbitrary comment | [optional] 
**cpu_bind** | **int** | Default method for binding tasks to allocated CPUs | [optional] 
**extra** | **str** | Arbitrary string used for node filtering if extra constraints are enabled | [optional] 
**features** | **List[str]** | Available features | [optional] 
**features_act** | **List[str]** | Currently active features | [optional] 
**gres** | **str** | Generic resources | [optional] 
**address** | **List[str]** | NodeAddr, used to establish a communication path | [optional] 
**hostname** | **List[str]** | NodeHostname | [optional] 
**name** | **List[str]** | NodeName | [optional] 
**state** | **List[str]** | New state to assign to the node | [optional] 
**reason** | **str** | Reason for node being DOWN or DRAINING | [optional] 
**reason_uid** | **str** | User ID to associate with the reason (needed if user root is sending message) | [optional] 
**resume_after** | [**SlurmV0041PostNodeRequestResumeAfter**](SlurmV0041PostNodeRequestResumeAfter.md) |  | [optional] 
**weight** | [**SlurmV0041PostNodeRequestWeight**](SlurmV0041PostNodeRequestWeight.md) |  | [optional] 

## Example

```python
from openapi_client.models.slurm_v0041_post_node_request import SlurmV0041PostNodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SlurmV0041PostNodeRequest from a JSON string
slurm_v0041_post_node_request_instance = SlurmV0041PostNodeRequest.from_json(json)
# print the JSON string representation of the object
print(SlurmV0041PostNodeRequest.to_json())

# convert the object into a dict
slurm_v0041_post_node_request_dict = slurm_v0041_post_node_request_instance.to_dict()
# create an instance of SlurmV0041PostNodeRequest from a dict
slurm_v0041_post_node_request_from_dict = SlurmV0041PostNodeRequest.from_dict(slurm_v0041_post_node_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


