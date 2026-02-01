# Wwise Time Stretch

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise Time Stretch

- **Plugin ID**: 130
- **Class ID**: 8519683

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **OutputGain** | Output Gain | Real32 | 0 | [ -24 , 24 ] | true | Additive | false |
| **PitchShift** | Pitch Shift | Real32 | 0 | [ -4800 , 4800 ] | true | Exclusive | false |
| **PitchShiftRandom** | Pitch Shift Random | Real32 | 0 | [ 0 , 4800 ] | true | Exclusive | false |
| **Quality** | Quality Level | Real32 | 100 | [ 0 , 100 ] | true | None | false |
| **QualityEnable** | Stretch Mode | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Classic | | 1 | Transient Preserving | | true | None | false |
| **StereoProcessing** | Stereo Processing | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Left Right | | 1 | Center Cut | | true | None | false |
| **TimeStretch** | Time Stretch | Real32 | 100 | [ 25 , 1600 ] | true | Exclusive | false |
| **TimeStretchRandom** | Time Stretch Random | Real32 | 0 | [ 0 , 200 ] | true | Exclusive | false |
| **WindowSize** | Window Size | int32 | 2048 | [ 256 , 8192 ] | true | None | false |