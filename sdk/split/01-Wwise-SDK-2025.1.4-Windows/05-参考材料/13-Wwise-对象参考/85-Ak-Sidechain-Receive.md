# Ak Sidechain Receive

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Ak Sidechain Receive

- **Plugin ID**: 194
- **Class ID**: 12713987

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# Properties, References, Lists

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **HPF** | HPF | int16 | 0 | [ 0 , 100 ] | false | Additive | true |
| **LPF** | LPF | int16 | 0 | [ 0 , 100 ] | false | Additive | true |
| **SidechainRef** | Sidechain Mix Source | Reference |  | **可能的类型：**   |  | | --- | | SidechainMix | | true |  |  |
| **SidechainScope** | Sidechain Scope | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Global | | 1 | Game Object | | true | None | false |
| **Volume** | Volume | Real32 | 0 | [ -200 , 200 ] | true | Additive | true |