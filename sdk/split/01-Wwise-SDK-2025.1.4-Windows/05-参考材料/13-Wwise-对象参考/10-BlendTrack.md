# BlendTrack

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

BlendTrack

- **Plugin ID**: 30
- **Class ID**: 1966096

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **EnableCrossFading** | Enable Crossfade | bool | false | None | false | None | false |
| **Highpass** | Voice HPF | int16 | 0 | [ 0 , 100 ] | true | Additive | false |
| **LayerCrossFadeControlInput** | Crossfade Control Input | Reference |  | None | true |  |  |
| **Lowpass** | Voice LPF | int16 | 0 | [ 0 , 100 ] | true | Additive | false |
| **MakeUpGain** | Make-Up Gain | Real64 | 0 | [ -200 , 200 ] | true | Additive | false |
| **Pitch** | Voice Pitch | int32 | 0 | [ -2400 , 2400 ] | true | Additive | false |
| **RTPC** | RTPC | List |  | **可能的类型：**   |  | | --- | | RTPC | |  |  |  |
| **Volume** | Voice Volume | Real64 | 0 | [ -200 , 200 ] | true | Additive | false |