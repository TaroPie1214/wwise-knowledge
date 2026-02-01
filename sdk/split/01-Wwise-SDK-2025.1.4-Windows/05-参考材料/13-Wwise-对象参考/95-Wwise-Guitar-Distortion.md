# Wwise Guitar Distortion

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise Guitar Distortion

- **Plugin ID**: 126
- **Class ID**: 8257539

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **DistortionDrive** | Distortion Drive | Real32 | 50 | [ 0 , 100 ] | true | Additive | false |
| **DistortionTone** | Distortion Tone | Real32 | 50 | [ 0 , 100 ] | true | Additive | false |
| **DistortionType** | Distortion Type | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | Overdrive | | 2 | Heavy | | 3 | Fuzz | | 4 | Clip | | true | Exclusive | false |
| **OutputLevel** | Output Gain | Real32 | 0 | [ -24 , 24 ] | true | Additive | false |
| **PostEQBand1Enable** | Post-Distortion EQ Band 1 Enable | bool | false | None | true | Boolean | false |
| **PostEQBand1FilterType** | Post-Distortion EQ Band 1 Filter Type | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Low Shelf | | 1 | Peaking | | 2 | High Shelf | | 3 | Low Pass | | 4 | High Pass | | 5 | Band Pass | | 6 | Notch | | true | Exclusive | false |
| **PostEQBand1Frequency** | Post-Distortion EQ Band 1 Frequency | Real32 | 1000 | [ 20 , 20000 ] | true | Exclusive | false |
| **PostEQBand1Gain** | Post-Distortion EQ Band 1 Gain | Real32 | 0 | [ -48 , 48 ] | true | Additive | false |
| **PostEQBand1QFactor** | Post-Distortion EQ Band 1 Quality Factor | Real32 | 1 | [ 0.1 , 20 ] | true | Exclusive | false |
| **PostEQBand2Enable** | Post-Distortion EQ Band 2 Enable | bool | false | None | true | Boolean | false |
| **PostEQBand2FilterType** | Post-Distortion EQ Band 2 Filter Type | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Low Shelf | | 1 | Peaking | | 2 | High Shelf | | 3 | Low Pass | | 4 | High Pass | | 5 | Band Pass | | 6 | Notch | | true | Exclusive | false |
| **PostEQBand2Frequency** | Post-Distortion EQ Band 2 Frequency | Real32 | 1000 | [ 20 , 20000 ] | true | Exclusive | false |
| **PostEQBand2Gain** | Post-Distortion EQ Band 2 Gain | Real32 | 0 | [ -48 , 48 ] | true | Additive | false |
| **PostEQBand2QFactor** | Post-Distortion EQ Band 2 Quality Factor | Real32 | 1 | [ 0.1 , 20 ] | true | Exclusive | false |
| **PostEQBand3Enable** | Post-Distortion EQ Band 3 Enable | bool | false | None | true | Boolean | false |
| **PostEQBand3FilterType** | Post-Distortion EQ Band 3 Filter Type | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Low Shelf | | 1 | Peaking | | 2 | High Shelf | | 3 | Low Pass | | 4 | High Pass | | 5 | Band Pass | | 6 | Notch | | true | Exclusive | false |
| **PostEQBand3Frequency** | Post-Distortion EQ Band 3 Frequency | Real32 | 1000 | [ 20 , 20000 ] | true | Exclusive | false |
| **PostEQBand3Gain** | Post-Distortion EQ Band 3 Gain | Real32 | 0 | [ -48 , 48 ] | true | Additive | false |
| **PostEQBand3QFactor** | Post-Distortion EQ Band 3 Quality Factor | Real32 | 1 | [ 0.1 , 20 ] | true | Exclusive | false |
| **PreEQBand1Enable** | Pre-Distortion EQ Band 1 Enable | bool | false | None | true | Boolean | false |
| **PreEQBand1FilterType** | Pre-Distortion EQ Band 1 Filter Type | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Low Shelf | | 1 | Peaking | | 2 | High Shelf | | 3 | Low Pass | | 4 | High Pass | | 5 | Band Pass | | 6 | Notch | | true | Exclusive | false |
| **PreEQBand1Frequency** | Pre-Distortion EQ Band 1 Frequency | Real32 | 1000 | [ 20 , 20000 ] | true | Exclusive | false |
| **PreEQBand1Gain** | Pre-Distortion EQ Band 1 Gain | Real32 | 0 | [ -48 , 48 ] | true | Additive | false |
| **PreEQBand1QFactor** | Pre-Distortion EQ Band 1 Quality Factor | Real32 | 1 | [ 0.1 , 20 ] | true | Exclusive | false |
| **PreEQBand2Enable** | Pre-Distortion EQ Band 2 Enable | bool | false | None | true | Boolean | false |
| **PreEQBand2FilterType** | Pre-Distortion EQ Band 2 Filter Type | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Low Shelf | | 1 | Peaking | | 2 | High Shelf | | 3 | Low Pass | | 4 | High Pass | | 5 | Band Pass | | 6 | Notch | | true | Exclusive | false |
| **PreEQBand2Frequency** | Pre-Distortion EQ Band 2 Frequency | Real32 | 1000 | [ 20 , 20000 ] | true | Exclusive | false |
| **PreEQBand2Gain** | Pre-Distortion EQ Band 2 Gain | Real32 | 0 | [ -48 , 48 ] | true | Additive | false |
| **PreEQBand2QFactor** | Pre-Distortion EQ Band 2 Quality Factor | Real32 | 1 | [ 0.1 , 20 ] | true | Exclusive | false |
| **PreEQBand3Enable** | Pre-Distortion EQ Band 3 Enable | bool | false | None | true | Boolean | false |
| **PreEQBand3FilterType** | Pre-Distortion EQ Band 3 Filter Type | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Low Shelf | | 1 | Peaking | | 2 | High Shelf | | 3 | Low Pass | | 4 | High Pass | | 5 | Band Pass | | 6 | Notch | | true | Exclusive | false |
| **PreEQBand3Frequency** | Pre-Distortion EQ Band 3 Frequency | Real32 | 1000 | [ 20 , 20000 ] | true | Exclusive | false |
| **PreEQBand3Gain** | Pre-Distortion EQ Band 3 Gain | Real32 | 0 | [ -48 , 48 ] | true | Additive | false |
| **PreEQBand3QFactor** | Pre-Distortion EQ Band 3 Quality Factor | Real32 | 1 | [ 0.1 , 20 ] | true | Exclusive | false |
| **Rectification** | Distortion Rectification | Real32 | 0 | [ 0 , 100 ] | true | Additive | false |
| **WetDryMix** | Wet/Dry Mix | Real32 | 100 | [ 0 , 100 ] | true | Additive | false |