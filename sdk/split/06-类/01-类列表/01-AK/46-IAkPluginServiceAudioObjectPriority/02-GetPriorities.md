# GetPriorities

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkPluginServiceAudioObjectPriority](class_a_k_1_1_i_ak_plugin_service_audio_object_priority.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [GetPriorities](class_a_k_1_1_i_ak_plugin_service_audio_object_priority_a068c7f44bfaf1e61f7953134b2a36f94.html#a068c7f44bfaf1e61f7953134b2a36f94) | | [SetPriorities](class_a_k_1_1_i_ak_plugin_service_audio_object_priority_a0ec7bae4ef2fb785682c98b628ee5101.html#a0ec7bae4ef2fb785682c98b628ee5101) | | [~IAkPluginServiceAudioObjectPriority](class_a_k_1_1_i_ak_plugin_service_audio_object_priority_a75127e603f14310b8151768e060d9f0c.html#a75127e603f14310b8151768e060d9f0c) | | [◆](#a068c7f44bfaf1e61f7953134b2a36f94)GetPriorities() |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  | | --- | --- | --- | --- | | virtual void AK::IAkPluginServiceAudioObjectPriority::GetPriorities | ( | [AkAudioObject](struct_ak_audio_object.html) \*\* | *in\_ppObjects*, | |  |  | [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | *in\_uNumObjects*, | |  |  | [AkPriority](_ak_typedefs_8h_a6fd4ce3da8a0654b665da32c63623433.html#a6fd4ce3da8a0654b665da32c63623433) \* | *out\_pPriorities* | |  | ) |  |  | | pure virtual |  Populates `out_pPriorities` with playback priorities for objects in `in_ppObjects`.  参数  |  |  | | --- | --- | | in\_ppObjects | Array of pointers to audio objects to extract priorites from. | | in\_uNumObjects | The number of audio objects in `in_ppObjects`. Must correspond to the number of priorites in `out_pPriorities`. | | out\_pPriorities | Priorities to fill from `in_ppObjects`. Must be large enough to contain `in_uNumObjects` priorities. | |