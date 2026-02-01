# AudioFileSource

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

AudioFileSource

- **Plugin ID**: 0
- **Class ID**: 16

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **ChannelConfigOverride** | Channel Configuration Override | int64 | 0 | None | true | None | false |
| **Color** | Color | int16 | 0 | [ 0 , 26 ] | true | None | false |
| **Conversion** | Conversion Settings | Reference |  | **可能的类型：**   |  | | --- | | Conversion | | true |  |  |
| **CrossfadeDuration** | Crossfade Duration | Real64 | 0 | [ 0 , 60000 ] | true | None | false |
| **CrossfadeShape** | Crossfade Shape | int16 | 1 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Logarithmic (Base 3) | | 1 | Sine | | 2 | Logarithmic (Base 1.41) | | 3 | Inverted S-Curve | | 4 | Linear | | 6 | S-Curve | | 7 | Exponential (Base 1.41) | | 8 | Reciprocal Sine | | 9 | Exponential (Base 3) | | true | None | false |
| **FadeInDuration** | Fade-in Duration | Real64 | 0 | [ 0 , 3600 ] | true | None | false |
| **FadeInShape** | Fade-in Curve | int16 | 1 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Logarithmic (Base 3) | | 1 | Sine | | 2 | Logarithmic (Base 1.41) | | 3 | Inverted S-Curve | | 4 | Linear | | 6 | S-Curve | | 7 | Exponential (Base 1.41) | | 8 | Reciprocal Sine | | 9 | Exponential (Base 3) | | true | None | false |
| **FadeOutDuration** | Fade-out Duration | Real64 | 0 | [ 0 , 3600 ] | true | None | false |
| **FadeOutShape** | Fade-out Curve | int16 | 8 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Logarithmic (Base 3) | | 1 | Sine | | 2 | Logarithmic (Base 1.41) | | 3 | Inverted S-Curve | | 4 | Linear | | 6 | S-Curve | | 7 | Exponential (Base 1.41) | | 8 | Reciprocal Sine | | 9 | Exponential (Base 3) | | true | None | false |
| **HdrEnvelope** | HDR Envelope | Real64 | 0 | [ 0 , 1 ] | false | None | false |
| **LoopBegin** | Loop Start | Real64 | -0.001 | None | true | None | false |
| **LoopEnd** | Loop End | Real64 | -0.001 | None | true | None | false |
| **MarkerDetectionSensitivity** | Marker Detection Sensitivity | Real64 | 0 | [ 0 , 100 ] | true | None | false |
| **MarkerInputMode** | Marker Input Mode | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Import From File | | 1 | Detect From Transients | | 2 | Manual Markers | | true | None | false |
| **Markers** | Markers | List |  | **可能的类型：**   |  | | --- | | Marker | |  |  |  |
| **OverrideColor** | Override Color | bool | false | None | true | None | false |
| **OverrideConversion** | Override Conversion Settings | bool | false | None | true | None | false |
| **OverrideWavLoop** | Override WAV Loop Points | bool | false | None | true | None | false |
| **TrimBegin** | Trim Start | Real64 | -0.001 | None | true | None | false |
| **TrimEnd** | Trim End | Real64 | -0.001 | None | true | None | false |
| **VolumeOffset** | Make-Up Gain | Real64 | 0 | [ -24 , +24 ] | true | None | true |