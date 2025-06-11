# V0040UpdateNodeMsg

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Arbitrary comment | [optional] 
**cpu_bind** | **int** | Default method for binding tasks to allocated CPUs | [optional] 
**extra** | **str** | Arbitrary string used for node filtering if extra constraints are enabled | [optional] 
**features** | **list[str]** |  | [optional] 
**features_act** | **list[str]** |  | [optional] 
**gres** | **str** | Generic resources | [optional] 
**address** | **list[str]** |  | [optional] 
**hostname** | **list[str]** |  | [optional] 
**name** | **list[str]** |  | [optional] 
**state** | **list[str]** | New state to assign to the node | [optional] 
**reason** | **str** | Reason for node being DOWN or DRAINING | [optional] 
**reason_uid** | **str** | User ID to associate with the reason (needed if user root is sending message) | [optional] 
**resume_after** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 
**weight** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


