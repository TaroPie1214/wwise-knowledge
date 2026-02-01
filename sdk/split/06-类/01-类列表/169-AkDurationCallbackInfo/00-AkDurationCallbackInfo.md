# AkDurationCallbackInfo

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_duration_callback_info-members.html) |
[Public 属性](#pub-attribs)

AkDurationCallbackInfo结构体 参考

`#include <AkCallbackTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fDuration](struct_ak_duration_callback_info_aee648dd75586f055e0b8d8244ddf73d7.html#aee648dd75586f055e0b8d8244ddf73d7) |
|  | Duration of the sound (unit: milliseconds) [更多...](struct_ak_duration_callback_info_aee648dd75586f055e0b8d8244ddf73d7.html#aee648dd75586f055e0b8d8244ddf73d7) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fEstimatedDuration](struct_ak_duration_callback_info_aa4f43d5859bed106c8608851a99afc03.html#aa4f43d5859bed106c8608851a99afc03) |
|  | Estimated duration of the sound depending on source settings such as pitch. (unit: milliseconds) [更多...](struct_ak_duration_callback_info_aa4f43d5859bed106c8608851a99afc03.html#aa4f43d5859bed106c8608851a99afc03) |
|  | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [audioNodeID](struct_ak_duration_callback_info_a2ea5c0b437a7d17cb533d28f3fbc2fd1.html#a2ea5c0b437a7d17cb533d28f3fbc2fd1) |
|  | Audio Node ID of playing item [更多...](struct_ak_duration_callback_info_a2ea5c0b437a7d17cb533d28f3fbc2fd1.html#a2ea5c0b437a7d17cb533d28f3fbc2fd1) |
|  | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [mediaID](struct_ak_duration_callback_info_a350e374948d180e8f596f78914907015.html#a350e374948d180e8f596f78914907015) |
|  | Media ID of playing item. (corresponds to 'ID' attribute of 'File' element in SoundBank metadata file) [更多...](struct_ak_duration_callback_info_a350e374948d180e8f596f78914907015.html#a350e374948d180e8f596f78914907015) |
|  | |
| bool | [bStreaming](struct_ak_duration_callback_info_a328183b46b8c5a73b2d764b9e3f94ea9.html#a328183b46b8c5a73b2d764b9e3f94ea9) |
|  | True if source is streaming, false otherwise. [更多...](struct_ak_duration_callback_info_a328183b46b8c5a73b2d764b9e3f94ea9.html#a328183b46b8c5a73b2d764b9e3f94ea9) |
|  | |

## 详细描述

Callback information structure corresponding to [AK\_Duration](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732ac258a8d8f9d67963d0ad37ecf2b989ad).

参见
:   - [AK::SoundEngine::PostEvent()](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e)
    - [集成详情——事件](soundengine_events.html)

在文件 [AkCallbackTypes.h](_ak_callback_types_8h_source.html) 第 [191](_ak_callback_types_8h_source.html#l00191) 行定义.