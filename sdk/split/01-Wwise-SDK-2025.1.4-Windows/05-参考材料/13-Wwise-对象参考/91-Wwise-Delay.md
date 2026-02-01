# Wwise Delay

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise Delay

- **Plugin ID**: 106
- **Class ID**: 6946819

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **DelayTime** | Delay Time | Real32 | 0.5 | [ 0.001 , 1 ] | true | None | false |
| **Feedback** | Feedback | Real32 | 15 | [ 0 , 100 ] | true | Additive | false |
| **FeedbackEnabled** | Feedback Enable | bool | true | None | true | Boolean | false |
| **OutputLevel** | Output Level | Real32 | 0 | [ -96.3 , 0 ] | true | Additive | false |
| **ProcessLFE** | Process LFE | bool | true | None | true | None | false |
| **WetDryMix** | Wet/Dry Mix | Real32 | 25 | [ 0 , 100 ] | true | Additive | false |