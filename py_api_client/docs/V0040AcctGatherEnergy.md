# V0040AcctGatherEnergy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_watts** | **int** | Average power consumption, in watts | [optional] 
**base_consumed_energy** | **int** | The energy consumed between when the node was powered on and the last time it was registered by slurmd, in joules | [optional] 
**consumed_energy** | **int** | The energy consumed between the last time the node was registered by the slurmd daemon and the last node energy accounting sample, in joules | [optional] 
**current_watts** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 
**previous_consumed_energy** | **int** | Previous value of consumed_energy | [optional] 
**last_collected** | **int** | Time when energy data was last retrieved (UNIX timestamp) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


