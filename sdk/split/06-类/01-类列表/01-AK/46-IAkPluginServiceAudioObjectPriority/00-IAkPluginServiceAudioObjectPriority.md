# IAkPluginServiceAudioObjectPriority

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkPluginServiceAudioObjectPriority](class_a_k_1_1_i_ak_plugin_service_audio_object_priority.html)

[所有成员列表](class_a_k_1_1_i_ak_plugin_service_audio_object_priority-members.html) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods)

AK::IAkPluginServiceAudioObjectPriority类 参考abstract

`#include <IAkPlugin.h>`

类 AK::IAkPluginServiceAudioObjectPriority 继承关系图:

![](../../../../images/class_a_k_1_1_i_ak_plugin_service_audio_object_priority.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual void | [GetPriorities](class_a_k_1_1_i_ak_plugin_service_audio_object_priority_a068c7f44bfaf1e61f7953134b2a36f94.html#a068c7f44bfaf1e61f7953134b2a36f94) ([AkAudioObject](struct_ak_audio_object.html) \*\*in\_ppObjects, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumObjects, [AkPriority](_ak_typedefs_8h_a6fd4ce3da8a0654b665da32c63623433.html#a6fd4ce3da8a0654b665da32c63623433) \*out\_pPriorities)=0 |
|  | Populates `out_pPriorities` with playback priorities for objects in `in_ppObjects`. [更多...](class_a_k_1_1_i_ak_plugin_service_audio_object_priority_a068c7f44bfaf1e61f7953134b2a36f94.html#a068c7f44bfaf1e61f7953134b2a36f94) |
|  | |
| virtual void | [SetPriorities](class_a_k_1_1_i_ak_plugin_service_audio_object_priority_a0ec7bae4ef2fb785682c98b628ee5101.html#a0ec7bae4ef2fb785682c98b628ee5101) ([AkAudioObject](struct_ak_audio_object.html) \*\*io\_ppObjects, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumObjects, [AkPriority](_ak_typedefs_8h_a6fd4ce3da8a0654b665da32c63623433.html#a6fd4ce3da8a0654b665da32c63623433) \*in\_pPriorities)=0 |
|  | Sets the playback priority of each of the `in_uNumObjects` audio objects in `io_ppObjects` from `in_pPriorities`. [更多...](class_a_k_1_1_i_ak_plugin_service_audio_object_priority_a0ec7bae4ef2fb785682c98b628ee5101.html#a0ec7bae4ef2fb785682c98b628ee5101) |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| virtual | [~IAkPluginServiceAudioObjectPriority](class_a_k_1_1_i_ak_plugin_service_audio_object_priority_a75127e603f14310b8151768e060d9f0c.html#a75127e603f14310b8151768e060d9f0c) () |
|  | |
| - Protected 成员函数 继承自 [AK::IAkPluginService](class_a_k_1_1_i_ak_plugin_service.html) | |
| virtual | [~IAkPluginService](class_a_k_1_1_i_ak_plugin_service_af880be6eab8f4f3cd124ec8db8b562de.html#af880be6eab8f4f3cd124ec8db8b562de) () |
|  | |

## 详细描述

Interface for the audio object priority service, to retrieve and update playback priority on audio objects. Playback priority of the audio object may be used by the audio endpoint when there are more audio objects than the available hardware objects to determine which audio objects should be mixed as hardware objects in priority and which can be mixed to a lower resolution 3D bed.

参见
:   - [Defining Playback Priority](https://www.audiokinetic.com/library/edge/?source=Help&id=defining_playback_priority)
    - `AkAudioObject`
    - `AkPriority`

在文件 [IAkPlugin.h](_i_ak_plugin_8h_source.html) 第 [1928](_i_ak_plugin_8h_source.html#l01928) 行定义.