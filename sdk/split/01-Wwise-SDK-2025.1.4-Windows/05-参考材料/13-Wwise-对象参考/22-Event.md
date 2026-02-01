# Event

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Event

- **Plugin ID**: 4
- **Class ID**: 262160

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Color** | Color | int16 | 0 | [ 0 , 26 ] | true | None | false |
| **CooldownTime** | Cooldown Time | Real32 | 0 | [ 0 , 3600 ] | true | None | true |
| **Inclusion** | Inclusion | bool | true | None | true | None | false |
| **InstanceLimit** | Limit | int16 | 0 | [ 0 , 10000 ] | true | None | true |
| **LimitScope** | Scope | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Global | | 1 | Game Object | | true | None | true |
| **OverrideColor** | Override Color | bool | false | None | true | None | false |