# Wwise Matrix Reverb

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise Matrix Reverb

- **Plugin ID**: 115
- **Class ID**: 7536643

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **DelayLengthsMode** | Delay Lengths Mode | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Default delay lengths | | 1 | Custom delay lengths | | true | None | false |
| **DelayTime1** | Delay Time 1 | Real32 | 13.62 | [ 1 , 35 ] | true | None | false |
| **DelayTime10** | Delay Time 10 | Real32 | 26.09 | [ 1 , 35 ] | true | None | false |
| **DelayTime11** | Delay Time 11 | Real32 | 26.55 | [ 1 , 35 ] | true | None | false |
| **DelayTime12** | Delay Time 12 | Real32 | 26.91 | [ 1 , 35 ] | true | None | false |
| **DelayTime13** | Delay Time 13 | Real32 | 28.04 | [ 1 , 35 ] | true | None | false |
| **DelayTime14** | Delay Time 14 | Real32 | 29.09 | [ 1 , 35 ] | true | None | false |
| **DelayTime15** | Delay Time 15 | Real32 | 29.90 | [ 1 , 35 ] | true | None | false |
| **DelayTime16** | Delay Time 16 | Real32 | 30.86 | [ 1 , 35 ] | true | None | false |
| **DelayTime2** | Delay Time 2 | Real32 | 15.66 | [ 1 , 35 ] | true | None | false |
| **DelayTime3** | Delay Time 3 | Real32 | 17.52 | [ 1 , 35 ] | true | None | false |
| **DelayTime4** | Delay Time 4 | Real32 | 19.02 | [ 1 , 35 ] | true | None | false |
| **DelayTime5** | Delay Time 5 | Real32 | 20.83 | [ 1 , 35 ] | true | None | false |
| **DelayTime6** | Delay Time 6 | Real32 | 22.60 | [ 1 , 35 ] | true | None | false |
| **DelayTime7** | Delay Time 7 | Real32 | 24.05 | [ 1 , 35 ] | true | None | false |
| **DelayTime8** | Delay Time 8 | Real32 | 24.78 | [ 1 , 35 ] | true | None | false |
| **DelayTime9** | Delay Time 9 | Real32 | 25.60 | [ 1 , 35 ] | true | None | false |
| **DryLevel** | Dry Level | Real32 | -96.3 | [ -96.3 , 0 ] | true | Additive | false |
| **HFRatio** | HF Ratio | Real32 | 2 | [ 0.5 , 10 ] | true | Exclusive | false |
| **NumberOfDelays** | Quality vs. Performance | int32 | 8 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 4 | Favor performance | | 8 | Balance quality and performance | | 12 | Favor quality | | 16 | Maximize quality | | true | None | false |
| **PreDelay** | Pre-delay | Real32 | 0 | [ 0 , 1 ] | true | Exclusive | false |
| **ProcessLFE** | Process LFE | bool | true | None | true | None | false |
| **ReverbTime** | Reverb Time | Real32 | 4 | [ 0.1 , 10 ] | true | Exclusive | false |
| **WetLevel** | Wet Level | Real32 | -35 | [ -96.3 , 0 ] | true | Additive | false |