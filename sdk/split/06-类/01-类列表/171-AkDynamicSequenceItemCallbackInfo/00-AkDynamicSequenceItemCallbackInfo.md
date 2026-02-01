# AkDynamicSequenceItemCallbackInfo

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_dynamic_sequence_item_callback_info-members.html) |
[Public 属性](#pub-attribs)

AkDynamicSequenceItemCallbackInfo结构体 参考

`#include <AkCallbackTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [audioNodeID](struct_ak_dynamic_sequence_item_callback_info_a83f3078c787ea6add02ab82cc938ad0d.html#a83f3078c787ea6add02ab82cc938ad0d) |
|  | Audio Node ID of finished item [更多...](struct_ak_dynamic_sequence_item_callback_info_a83f3078c787ea6add02ab82cc938ad0d.html#a83f3078c787ea6add02ab82cc938ad0d) |
|  | |
| void \* | [pCustomInfo](struct_ak_dynamic_sequence_item_callback_info_accc1b5efdf7fb8e6d6dae5906945ddbb.html#accc1b5efdf7fb8e6d6dae5906945ddbb) |
|  | Custom info passed to the DynamicSequence::Open function [更多...](struct_ak_dynamic_sequence_item_callback_info_accc1b5efdf7fb8e6d6dae5906945ddbb.html#accc1b5efdf7fb8e6d6dae5906945ddbb) |
|  | |

## 详细描述

Callback information structure corresponding to [AK\_EndOfDynamicSequenceItem](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732a1f3c7ae3783296ae95315c97c9b59f75).

参见
:   - [AK::SoundEngine::PostEvent()](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e)
    - [AK::SoundEngine::DynamicSequence::Open()](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_ab6daddd96e109dc7669889733ce4f2cc.html#ab6daddd96e109dc7669889733ce4f2cc)
    - [集成详情——事件](soundengine_events.html)

在文件 [AkCallbackTypes.h](_ak_callback_types_8h_source.html) 第 [205](_ak_callback_types_8h_source.html#l00205) 行定义.