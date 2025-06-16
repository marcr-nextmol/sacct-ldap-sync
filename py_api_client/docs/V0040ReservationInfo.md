# V0040ReservationInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | **str** | Comma separated list of permitted accounts | [optional] 
**burst_buffer** | **str** | BurstBuffer | [optional] 
**core_count** | **int** | CoreCnt | [optional] 
**core_specializations** | [**list[V0040ReservationCoreSpec]**](V0040ReservationCoreSpec.md) |  | [optional] 
**end_time** | [**V0040Uint64NoVal**](V0040Uint64NoVal.md) |  | [optional] 
**features** | **str** | Features | [optional] 
**flags** | **list[str]** | Flags associated with the reservation | [optional] 
**groups** | **str** | Groups | [optional] 
**licenses** | **str** | Licenses | [optional] 
**max_start_delay** | **int** | MaxStartDelay in seconds | [optional] 
**name** | **str** | ReservationName | [optional] 
**node_count** | **int** | NodeCnt | [optional] 
**node_list** | **str** | Nodes | [optional] 
**partition** | **str** | PartitionName | [optional] 
**purge_completed** | [**V0040ReservationInfoPurgeCompleted**](V0040ReservationInfoPurgeCompleted.md) |  | [optional] 
**start_time** | [**V0040Uint64NoVal**](V0040Uint64NoVal.md) |  | [optional] 
**watts** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 
**tres** | **str** | Comma separated list of required TRES | [optional] 
**users** | **str** | Comma separated list of permitted users | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


