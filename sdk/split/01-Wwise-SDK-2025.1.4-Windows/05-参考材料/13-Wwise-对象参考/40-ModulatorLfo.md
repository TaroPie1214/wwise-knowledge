# ModulatorLfo

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

ModulatorLfo

- **Plugin ID**: 64
- **Class ID**: 4194320

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Color** | Color | int16 | 0 | [ 0 , 26 ] | true | None | false |
| **LfoAttack** | Attack | Real64 | 0 | [ 0 , 100000 ] | true | Exclusive | false |
| **LfoDepth** | Depth | Real64 | 100 | [ 0 , 100 ] | true | Exclusive | false |
| **LfoFrequency** | Frequency | Real64 | 1 | [ 0 , 20000 ] | true | Exclusive | false |
| **LfoInitialPhase** | Initial Phase Offset | Real64 | 0 | [ -180 , 180 ] | true | Exclusive | false |
| **LfoPWM** | PWM | Real64 | 50 | [ 0 , 100 ] | true | Exclusive | false |
| **LfoSmoothing** | Smoothing | Real64 | 0 | [ 0 , 100 ] | true | Exclusive | false |
| **LfoWaveform** | Waveform | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Sine | | 1 | Triangle | | 2 | Square | | 3 | Saw up | | 4 | Saw down | | 5 | Random | | true | Exclusive | false |
| **ModulatorScope** | Scope | int32 | 1 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Voice | | 1 | Note or Event | | 2 | Game Object | | 3 | Global | | true | None | false |
| **OverrideColor** | Override Color | bool | false | None | true | None | false |
| **RTPC** | RTPC | List |  | **可能的类型：**   |  | | --- | | RTPC | |  |  |  |