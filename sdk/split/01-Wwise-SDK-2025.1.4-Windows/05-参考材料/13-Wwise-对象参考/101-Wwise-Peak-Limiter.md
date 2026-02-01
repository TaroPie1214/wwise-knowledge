# Wwise Peak Limiter

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise Peak Limiter

- **Plugin ID**: 110
- **Class ID**: 7208963

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **ChannelLink** | Channel Link | bool | true | None | true | None | false |
| **LookAhead** | Look Ahead Time | Real32 | 0.01 | [ 0.001 , 0.02 ] | true | None | false |
| **OutputGain** | Output Gain | Real32 | 0 | [ -24 , 24 ] | true | Additive | false |
| **ProcessLFE** | Process LFE | bool | true | None | true | None | false |
| **Ratio** | Ratio | Real32 | 10 | [ 1 , 50 ] | true | Exclusive | false |
| **ReleaseTime** | Release Time | Real32 | 0.1 | [ 0.001 , 0.5 ] | true | Exclusive | false |
| **Threshold** | Threshold | Real32 | 0 | [ -96.3 , 0 ] | true | Additive | false |