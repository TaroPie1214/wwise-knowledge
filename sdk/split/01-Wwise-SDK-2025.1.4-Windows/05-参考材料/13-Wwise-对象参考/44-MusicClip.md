# MusicClip

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

MusicClip

- **Plugin ID**: 60
- **Class ID**: 3932176

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **BeginTrimOffset** | Begin Offset | Real64 | 0 | None | true | None | false |
| **Color** | Color | int16 | 0 | [ 0 , 26 ] | true | None | false |
| **EndTrimOffset** | End Offset | Real64 | 0 | None | true | None | false |
| **FadeInDuration** | Fade-in Duration | Real64 | 0 | [ 0 , 3600 ] | true | None | false |
| **FadeInMode** | Clip Fade-in Mode | int16 | 1 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Automatic | | 1 | Manual | | true | None | false |
| **FadeInShape** | Fade-in Curve | int16 | 1 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Logarithmic (Base 3) | | 1 | Sine | | 2 | Logarithmic (Base 1.41) | | 3 | Inverted S-Curve | | 4 | Linear | | 6 | S-Curve | | 7 | Exponential (Base 1.41) | | 8 | Reciprocal Sine | | 9 | Exponential (Base 3) | | true | None | false |
| **FadeOutDuration** | Fade-out Duration | Real64 | 0 | [ 0 , 3600 ] | true | None | false |
| **FadeOutMode** | Clip Fade-out Mode | int16 | 1 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Automatic | | 1 | Manual | | true | None | false |
| **FadeOutShape** | Fade-out Curve | int16 | 8 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Logarithmic (Base 3) | | 1 | Sine | | 2 | Logarithmic (Base 1.41) | | 3 | Inverted S-Curve | | 4 | Linear | | 6 | S-Curve | | 7 | Exponential (Base 1.41) | | 8 | Reciprocal Sine | | 9 | Exponential (Base 3) | | true | None | false |
| **Highpass** | Voice HPF | int16 | 0 | [ 0 , 100 ] | false | Exclusive | false |
| **Lowpass** | Voice LPF | int16 | 0 | [ 0 , 100 ] | false | Exclusive | false |
| **OverrideColor** | Override Color | bool | false | None | true | None | false |
| **PlayAt** | Play Position | Real64 | 0 | [ 0 , 10000000000 ] | true | None | false |
| **Volume** | Voice Volume | Real64 | 0 | [ -96.3 , 0 ] | false | Exclusive | false |