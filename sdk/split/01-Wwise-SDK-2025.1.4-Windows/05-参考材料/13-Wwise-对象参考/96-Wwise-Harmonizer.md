# Wwise Harmonizer

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise Harmonizer

- **Plugin ID**: 138
- **Class ID**: 9043971

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **DryLevel** | Dry Level | Real32 | 0 | [ -96 , 24 ] | true | Additive | false |
| **Input** | Input | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | As Input | | 1 | Mono-Center | | 2 | Stereo | | 3 | L-R-C | | 4 | L-R-LS-RS | | 5 | L-R-C-LS-RS | | 6 | Left Only | | true | None | false |
| **ProcessLFE** | Process LFE | bool | false | None | true | None | false |
| **SyncDry** | Delay Dry | bool | true | None | true | None | false |
| **Voice1Enable** | Voice 1 Enable | bool | true | None | true | None | false |
| **Voice1FilterFrequency** | Voice 1 Filter Frequency | Real32 | 1000 | [ 20 , 20000 ] | true | Exclusive | false |
| **Voice1FilterGain** | Voice 1 Filter Gain | Real32 | 0 | [ -24 , 24 ] | true | Additive | false |
| **Voice1FilterQFactor** | Voice 1 Filter Q Factor | Real32 | 1 | [ 0.1 , 20 ] | true | Exclusive | false |
| **Voice1FilterType** | Voice 1 Filter Type | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | Low Shelf | | 2 | Peaking | | 3 | High Shelf | | 4 | Low Pass | | 5 | High Pass | | 6 | Band Pass | | 7 | Notch | | true | Exclusive | false |
| **Voice1Gain** | Voice 1 Gain | Real32 | 0 | [ -96 , 24 ] | true | Additive | false |
| **Voice1Pitch** | Voice 1 Pitch | Real32 | 0 | [ -2400 , 2400 ] | true | None | false |
| **Voice2Enable** | Voice 2 Enable | bool | false | None | true | None | false |
| **Voice2FilterFrequency** | Voice 2 Filter Frequency | Real32 | 1000 | [ 20 , 20000 ] | true | Exclusive | false |
| **Voice2FilterGain** | Voice 2 Filter Gain | Real32 | 0 | [ -24 , 24 ] | true | Additive | false |
| **Voice2FilterQFactor** | Voice 2 Filter Q Factor | Real32 | 1 | [ 0.1 , 20 ] | true | Exclusive | false |
| **Voice2FilterType** | Voice 2 Filter Type | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | Low Shelf | | 2 | Peaking | | 3 | High Shelf | | 4 | Low Pass | | 5 | High Pass | | 6 | Band Pass | | 7 | Notch | | true | Exclusive | false |
| **Voice2Gain** | Voice 2 Gain | Real32 | 0 | [ -96 , 24 ] | true | Additive | false |
| **Voice2Pitch** | Voice 2 Pitch | Real32 | 0 | [ -2400 , 2400 ] | true | None | false |
| **WetLevel** | Wet Level | Real32 | 0 | [ -96 , 24 ] | true | Additive | false |
| **WindowSize** | Window Size | int32 | 1024 | [ 256 , 4096 ] | true | None | false |