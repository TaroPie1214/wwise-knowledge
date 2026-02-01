# MusicFade

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

MusicFade

- **Plugin ID**: 39
- **Class ID**: 2555920

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **FadeCurve** | Fade Curve | int16 | 4 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Logarithmic (Base 3) | | 1 | Sine | | 2 | Logarithmic (Base 1.41) | | 3 | Inverted S-Curve | | 4 | Linear | | 5 | S-Curve | | 6 | Exponential (Base 1.41) | | 7 | Reciprocal Sine | | 8 | Exponential (Base 3) | | true | None | false |
| **FadeOffset** | Fade Offset | Real64 | 0 | [ -60 , 60 ] | true | None | false |
| **FadeTime** | Fade Time | Real64 | 0 | [ 0 , 60 ] | true | None | false |
| **FadeType** | Fade Type | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Fade-in | | 1 | Fade-out | | false | None | false |