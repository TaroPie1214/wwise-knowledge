# SoundSeed Air Wind

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

SoundSeed Air Wind

- **Plugin ID**: 119
- **Class ID**: 7798786

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **AttenuationRollOff** | **AttenuationRollOff** | Real32 | 1 | [ 0.0 , 4 ] | true | Exclusive | false |
| **AverageVelocity** | **AverageVelocity** | Real32 | 0 | [ -2400 , 2400 ] | true | Exclusive | false |
| **AverageVelocityAutomate** | **AverageVelocityAutomate** | bool | false | None | true | None | false |
| **AverageVelocityRandom** | **AverageVelocityRandom** | Real32 | 0.0 | [ 0 , 2400 ] | true | None | false |
| **ChannelMask** | **ChannelMask** | int16 | 1 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | 1.0 | | 1 | 2.0 | | 2 | 4.0 | | true | None | false |
| **Direction** | **Direction** | Real32 | 0 | [ -180 , 180 ] | true | Exclusive | false |
| **DirectionAutomate** | **DirectionAutomate** | bool | false | None | true | None | false |
| **DirectionRandom** | **DirectionRandom** | Real32 | 0.0 | [ 0 , 180 ] | true | None | false |
| **Duration** | **Duration** | Real64 | 10.0 | [ 0.1 , 3600.0 ] | true | None | false |
| **DurationRandom** | **DurationRandom** | Real32 | 0.0 | [ 0.0 , 3600.0 ] | true | None | false |
| **FrequencyScale** | **FrequencyScale** | Real32 | 0.0 | [ -4.0 , 4.0 ] | true | Exclusive | false |
| **FrequencyScaleAutomate** | **FrequencyScaleAutomate** | bool | false | None | true | None | false |
| **FrequencyScaleRandom** | **FrequencyScaleRandom** | Real32 | 0.0 | [ 0.0 , 4.0 ] | true | None | false |
| **GainOffset** | **GainOffset** | Real32 | 0.0 | [ -96.3 , 24.0 ] | true | Exclusive | false |
| **GainOffsetAutomate** | **GainOffsetAutomate** | bool | false | None | true | None | false |
| **GainOffsetRandom** | **GainOffsetRandom** | Real32 | 0.0 | [ 0 , 48.0 ] | true | None | false |
| **Gustiness** | **Gustiness** | Real32 | 0.5 | [ 0.0 , 1.0 ] | true | Exclusive | false |
| **GustinessAutomate** | **GustinessAutomate** | bool | false | None | true | None | false |
| **GustinessRandom** | **GustinessRandom** | Real32 | 0.0 | [ 0.0 , 0.5 ] | true | None | false |
| **MaxDistance** | **MaxDistance** | Real32 | 10.0 | [ 1.0 , 100.0 ] | true | None | false |
| **MinDistance** | **MinDistance** | Real32 | 5.0 | [ 0.1 , 50 ] | true | Exclusive | false |
| **PlaybackRate** | **PlaybackRate** | Real32 | 1.0 | [ 0.1 , 10.0 ] | true | Exclusive | false |
| **QFactorScale** | **QFactorScale** | Real32 | 0.0 | [ -4.0 , 4.0 ] | true | Exclusive | false |
| **QFactorScaleAutomate** | **QFactorScaleAutomate** | bool | false | None | true | None | false |
| **QFactorScaleRandom** | **QFactorScaleRandom** | Real32 | 0.0 | [ 0.0 , 4.0 ] | true | None | false |
| **Variability** | **Variability** | Real32 | 0.25 | [ 0.0 , 1.0 ] | true | Exclusive | false |
| **VariabilityAutomate** | **VariabilityAutomate** | bool | false | None | true | None | false |
| **VariabilityRandom** | **VariabilityRandom** | Real32 | 0.0 | [ 0.0 , 0.5 ] | true | None | false |
| **VelocityDynamicRange** | **VelocityDynamicRange** | Real32 | 0.5 | [ 0 , 1 ] | true | Exclusive | false |