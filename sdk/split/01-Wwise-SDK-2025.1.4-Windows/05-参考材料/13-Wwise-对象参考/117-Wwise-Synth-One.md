# Wwise Synth One

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise Synth One

- **Plugin ID**: 148
- **Class ID**: 9699330

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **BaseFrequency** | Base Frequency | Real32 | 1000.0 | [ 20 , 20000 ] | true | Exclusive | false |
| **FmAmount** | FM Amount | Real32 | 0 | [ 0 , 100 ] | true | Additive | false |
| **FrequencyMode** | Frequency Mode | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Base Frequency | | 1 | MIDI Note | | true | None | false |
| **NoiseLevel** | Noise Level | Real32 | -96.0 | [ -96.0 , 24.0 ] | true | Additive | false |
| **NoiseShape** | Noise Shape | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | White Noise | | 1 | Pink Noise | | 2 | Red Noise | | 3 | Purple Noise | | true | Exclusive | false |
| **OperationMode** | Operation Mode | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Mix | | 1 | Ring | | true | Exclusive | false |
| **Osc1Invert** | Osc1 Invert | bool | 0 | None | true | Exclusive | false |
| **Osc1Level** | Osc1 Level | Real32 | -6.0 | [ -96.0 , 24.0 ] | true | Additive | false |
| **Osc1Pwm** | Osc1 PWM | Real32 | 50.0 | [ 0.0 , 100.0 ] | true | Exclusive | false |
| **Osc1Transpose** | Osc1 Transpose | int32 | 0 | [ -3600 , 3600 ] | true | Additive | false |
| **Osc1Waveform** | Osc1 Waveform | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Sine | | 1 | Triangle | | 2 | Square | | 3 | Sawtooth | | true | Exclusive | false |
| **Osc2Invert** | Osc2 Invert | bool | 0 | None | true | Exclusive | false |
| **Osc2Level** | Osc2 Level | Real32 | -6.0 | [ -96.0 , 24.0 ] | true | Additive | false |
| **Osc2Pwm** | Osc2 PWM | Real32 | 50 | [ 0.0 , 100.0 ] | true | Exclusive | false |
| **Osc2Transpose** | Osc2 Transpose | int32 | 0 | [ -3600 , 3600 ] | true | Additive | false |
| **Osc2Waveform** | Osc2 Waveform | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Sine | | 1 | Triangle | | 2 | Square | | 3 | Sawtooth | | true | Exclusive | false |
| **OutputLevel** | Output Level | Real32 | 0.0 | [ -96.0 , 24.0 ] | true | Additive | false |
| **OverSampling** | Over-sampling | bool | 1 | None | true | None | false |