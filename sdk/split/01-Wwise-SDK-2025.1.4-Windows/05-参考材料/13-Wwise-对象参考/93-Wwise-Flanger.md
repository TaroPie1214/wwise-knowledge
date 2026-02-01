# Wwise Flanger

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise Flanger

- **Plugin ID**: 125
- **Class ID**: 8192003

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **DelayTime** | Delay Time | Real32 | 5 | [ 0.2 , 100 ] | true | None | false |
| **DryLevel** | Blend | Real32 | 1.0 | [ 0 , 1 ] | true | Additive | false |
| **EnableLFO** | LFO Enable | bool | true | None | true | None | false |
| **FeedBackLevel** | Feedback | Real32 | 0 | [ -1 , 1 ] | true | Additive | false |
| **FeedForwardLevel** | Feedforward | Real32 | 1 | [ -1 , 1 ] | true | Additive | false |
| **ModDepth** | LFO Depth | Real32 | 50 | [ 0 , 100 ] | true | Additive | false |
| **ModFrequency** | LFO Frequency | Real32 | 1 | [ 0.002 , 20 ] | true | Exclusive | false |
| **ModPWM** | LFO PWM | Real32 | 50 | [ 0 , 100 ] | true | Additive | false |
| **ModPhaseMode** | LFO Spread Mode | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Left-Right | | 1 | Front-Rear | | 2 | Circular | | 3 | Random | | true | Exclusive | false |
| **ModPhaseOffset** | LFO Phase Offset | Real32 | 0 | [ -180 , 180 ] | true | Additive | false |
| **ModPhaseSpread** | LFO Phase Spread | Real32 | 0 | [ 0 , 180 ] | true | Additive | false |
| **ModSmoothing** | LFO Smoothing | Real32 | 0 | [ 0 , 100 ] | true | Additive | false |
| **ModWaveform** | LFO Waveform | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Sine | | 1 | Triangle | | 2 | Square | | 3 | Saw up | | 4 | Saw down | | true | Exclusive | false |
| **OutputLevel** | Output Gain | Real32 | 0 | [ -24 , 24 ] | true | Additive | false |
| **ProcessCenter** | Process Center | bool | false | None | true | None | false |
| **ProcessLFE** | Process LFE | bool | false | None | true | None | false |
| **WetDryMix** | Wet/Dry Mix | Real32 | 100 | [ 0 , 100 ] | true | Additive | false |