# Wwise Meter

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise Meter

- **Plugin ID**: 129
- **Class ID**: 8454147

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **ApplyDownstreamVolume** | Apply Downstream Volume | bool | false | None | true | None | false |
| **AttackTime** | Attack Time | Real32 | 0.0 | [ 0 , 10 ] | true | Additive | false |
| **GameParameter** | Target Game Parameter | Reference |  | **可能的类型：**   |  | | --- | | GameParameter | | true |  |  |
| **Hold** | Hold | Real32 | 0 | [ 0 , 10 ] | true | Additive | false |
| **InfiniteHold** | Infinite Hold | bool | false | None | true | Boolean | false |
| **Max** | Max | Real32 | 0 | [ -96.3 , 12 ] | true | Additive | false |
| **MeterMode** | Mode | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Peak | | 1 | RMS | | true | None | false |
| **MeterScope** | RTPC Scope | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Global | | 1 | Game Object | | true | None | false |
| **Min** | Min | Real32 | -48 | [ -96.3 , 0 ] | true | Additive | false |
| **MixdownCfg** | Mixdown Config | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | No Mixdown | | 16641 | Mono | | false | None | false |
| **ReleaseTime** | Release Time | Real32 | 0.1 | [ 0 , 10 ] | true | Additive | false |