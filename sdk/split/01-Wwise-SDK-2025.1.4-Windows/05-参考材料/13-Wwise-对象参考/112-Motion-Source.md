# Motion Source

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Motion Source

- **Plugin ID**: 409
- **Class ID**: 26804226

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Channel1** | **Channel1** | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Driver A | | 1 | Driver B | | 2 | Driver C | | 3 | Driver D | | 4 | Driver E | | 5 | Driver F | | 6 | Driver G | | 7 | Driver H | | true | None | true |
| **Channel2** | **Channel2** | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Driver A | | 1 | Driver B | | 2 | Driver C | | 3 | Driver D | | 4 | Driver E | | 5 | Driver F | | 6 | Driver G | | 7 | Driver H | | true | None | true |
| **Channel3** | **Channel3** | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Driver A | | 1 | Driver B | | 2 | Driver C | | 3 | Driver D | | 4 | Driver E | | 5 | Driver F | | 6 | Driver G | | 7 | Driver H | | true | None | true |
| **Channel4** | **Channel4** | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Driver A | | 1 | Driver B | | 2 | Driver C | | 3 | Driver D | | 4 | Driver E | | 5 | Driver F | | 6 | Driver G | | 7 | Driver H | | true | None | true |
| **ChannelConfig** | **ChannelConfig** | int16 | 6 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Android | | 1 | PlayStation Move | | 2 | DualShock 2-Channel | | 3 | Switch 2-Channel | | 4 | Switch 4-Channel | | 5 | Xbox 4-Channel | | 6 | Generic 1-Channel | | 7 | Generic 2-Channel | | 8 | Generic 4-Channel | | 9 | Generic Haptics 2-Channel | | true | None | true |
| **DriverA** | **DriverA** | Real32 | 0.0 | [ 0 , 1 ] | true | Additive | true |
| **DriverB** | **DriverB** | Real32 | 0.0 | [ 0 , 1 ] | true | Additive | true |
| **DriverC** | **DriverC** | Real32 | 0.0 | [ 0 , 1 ] | true | Additive | true |
| **DriverD** | **DriverD** | Real32 | 0.0 | [ 0 , 1 ] | true | Additive | true |
| **DriverE** | **DriverE** | Real32 | 0.0 | [ 0 , 1 ] | true | Additive | true |
| **DriverF** | **DriverF** | Real32 | 0.0 | [ 0 , 1 ] | true | Additive | true |
| **DriverG** | **DriverG** | Real32 | 0.0 | [ 0 , 1 ] | true | Additive | true |
| **DriverH** | **DriverH** | Real32 | 0.0 | [ 0 , 1 ] | true | Additive | true |
| **High1** | **High1** | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Driver A | | 1 | Driver B | | 2 | Driver C | | 3 | Driver D | | 4 | Driver E | | 5 | Driver F | | 6 | Driver G | | 7 | Driver H | | true | None | true |
| **High2** | **High2** | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Driver A | | 1 | Driver B | | 2 | Driver C | | 3 | Driver D | | 4 | Driver E | | 5 | Driver F | | 6 | Driver G | | 7 | Driver H | | true | None | true |
| **LeftTrigger** | **LeftTrigger** | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Driver A | | 1 | Driver B | | 2 | Driver C | | 3 | Driver D | | 4 | Driver E | | 5 | Driver F | | 6 | Driver G | | 7 | Driver H | | true | None | true |
| **Low1** | **Low1** | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Driver A | | 1 | Driver B | | 2 | Driver C | | 3 | Driver D | | 4 | Driver E | | 5 | Driver F | | 6 | Driver G | | 7 | Driver H | | true | None | true |
| **Low2** | **Low2** | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Driver A | | 1 | Driver B | | 2 | Driver C | | 3 | Driver D | | 4 | Driver E | | 5 | Driver F | | 6 | Driver G | | 7 | Driver H | | true | None | true |
| **RightTrigger** | **RightTrigger** | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Driver A | | 1 | Driver B | | 2 | Driver C | | 3 | Driver D | | 4 | Driver E | | 5 | Driver F | | 6 | Driver G | | 7 | Driver H | | true | None | true |