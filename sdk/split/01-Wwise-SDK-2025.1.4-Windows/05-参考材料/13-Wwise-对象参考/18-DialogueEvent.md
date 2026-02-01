# DialogueEvent

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

DialogueEvent

- **Plugin ID**: 46
- **Class ID**: 3014672

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **参数** | 参数 | List |  | **可能的类型：**   |  | | --- | | ArgumentsSlot | |  |  |  |
| **Color** | Color | int16 | 0 | [ 0 , 26 ] | true | None | false |
| **Entries** | Entries | List |  | **可能的类型：**   |  | | --- | | MultiSwitchEntry | |  |  |  |
| **Mode** | Match Mode | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Best Match | | 1 | Weighted | | true | None | false |
| **OverrideColor** | Override Color | bool | false | None | true | None | false |
| **Probability** | Probability | int32 | 100 | [ 0 , 100 ] | true | None | false |