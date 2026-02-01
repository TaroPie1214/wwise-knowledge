# Wwise Tone Generator

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise Tone Generator

- **Plugin ID**: 102
- **Class ID**: 6684674

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **AttackTime** | Attack Time | Real32 | 0.0 | [ 0 , 3600 ] | true | None | false |
| **ChannelMask** | Channel | int32 | 4 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 4 | Mono | | 8 | LFE | | true | None | true |
| **DecayTime** | Decay Time | Real32 | 0.0 | [ 0 , 3600 ] | true | None | false |
| **DurMode** | Duration Mode | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Fixed Duration | | 1 | Envelope | | true | None | false |
| **FixDur** | Fixed Duration | Real32 | 1.0 | [ 0.001 , 3600 ] | true | None | false |
| **ReleaseTime** | Release Time | Real32 | 0.0 | [ 0 , 3600 ] | true | None | false |
| **StartFreq** | Start Frequency | Real32 | 1000.0 | [ 20 , 20000 ] | true | Exclusive | false |
| **StartFreqRandMax** | Start Frequency Random Max | Real32 | 0.0 | [ 0 , 12000 ] | true | None | false |
| **StartFreqRandMin** | Start Frequency Random Min | Real32 | 0.0 | [ -12000 , 0 ] | true | None | false |
| **StopFreq** | Stop Frequency | Real32 | 1000.0 | [ 20 , 20000 ] | true | Exclusive | false |
| **StopFreqRandMax** | Start Frequency Random Max | Real32 | 0.0 | [ 0 , 12000 ] | true | None | false |
| **StopFreqRandMin** | Stop Frequency Random Min | Real32 | 0.0 | [ -12000 , 0 ] | true | None | false |
| **SustainLevel** | Sustain Level | Real32 | -12.0 | [ -96.3 , 0 ] | true | None | false |
| **SustainTime** | Sustain Time | Real32 | 1.0 | [ 0 , 3600 ] | true | None | false |
| **SweepFreq** | Sweep Frequency | bool | false | None | true | None | false |
| **SweepFreqType** | Sweep Frequency Type | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Linear | | 1 | Logarithmic | | true | None | false |
| **WaveGain** | Gain | Real32 | -12.0 | [ -96.3 , 0 ] | true | Exclusive | false |
| **WaveType** | Waveform | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Sine | | 1 | Triangular | | 2 | Square | | 3 | Sawtooth | | 4 | White noise | | 5 | Pink noise | | true | None | false |