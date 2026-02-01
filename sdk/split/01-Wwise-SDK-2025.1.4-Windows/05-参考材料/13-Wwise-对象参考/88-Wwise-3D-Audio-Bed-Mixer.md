# Wwise 3D Audio Bed Mixer

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise 3D Audio Bed Mixer

- **Plugin ID**: 190
- **Class ID**: 12451843

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **MainMixConfiguration** | Main Mix 配置 | Uint32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Same as Audio Device | | 6549768 | 7.1 | | 761524492 | 7.1.4 | | 516 | Ambisonics 1st order | | 521 | Ambisonics 2nd order | | 528 | Ambisonics 3rd order | | 537 | Ambisonics 4th order | | 548 | Ambisonics 5th order | | true | None | true |
| **PassthroughMixPolicy** | Passthrough Mix | Uint16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | When Audio Device supports it | | 1 | Always | | 2 | Never | | true | Exclusive | true |
| **SystemAudioObjectLimit** | System-Eligible Audio Object Limit | Uint16 | 64 | [ 0 , 512 ] | true | Exclusive | true |
| **SystemAudioObjectsPolicy** | Preserve System-Eligible Audio Objects | Uint16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | When Audio Device supports it | | 1 | Always | | 2 | Never | | true | Exclusive | true |