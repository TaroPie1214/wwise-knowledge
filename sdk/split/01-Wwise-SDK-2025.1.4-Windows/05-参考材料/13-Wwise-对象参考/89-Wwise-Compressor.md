# Wwise Compressor

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise Compressor

- **Plugin ID**: 108
- **Class ID**: 7077891

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **AttackTime** | Attack Time | Real32 | 0.1 | [ 0 , 2 ] | true | Additive | false |
| **ChannelLink** | Channel Link | bool | true | None | true | None | false |
| **ChannelLinkPercentage** | Channel Link Percentage | Real32 | 0 | [ 0 , 100 ] | true | None | false |
| **GainMeterRange** | **GainMeterRange** | Real32 | -24 | None | false | None | false |
| **OutputGain** | Output Gain | Real32 | 0 | [ -24 , 24 ] | true | Additive | false |
| **ProcessLFE** | Process LFE | bool | true | None | true | None | false |
| **Ratio** | Ratio | Real32 | 1.5 | [ 1 , 50 ] | true | Exclusive | false |
| **ReleaseTime** | Release Time | Real32 | 0.1 | [ 0 , 2 ] | true | Additive | false |
| **SidechainRef** | Sidechain Mix Source | Reference |  | **可能的类型：**   |  | | --- | | SidechainMix | | true |  |  |
| **SidechainScope** | Sidechain Scope | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Global | | 1 | Game Object | | true | None | false |
| **Threshold** | Threshold | Real32 | 0 | [ -96.3 , 0 ] | true | Additive | false |