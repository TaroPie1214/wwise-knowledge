# Wwise Stereo Delay

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise Stereo Delay

- **Plugin ID**: 135
- **Class ID**: 8847363

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **DryLevel** | Dry Level | Real32 | 0 | [ -96 , 24 ] | true | Additive | false |
| **EnableCrossFeed** | Enable Crossfeed | bool | false | None | true | Boolean | false |
| **EnableFeedback** | Enable Feedback | bool | false | None | true | Boolean | false |
| **FilterFrequency** | Filter Frequency | Real32 | 1000 | [ 20 , 20000 ] | true | Exclusive | false |
| **FilterGain** | Filter Gain | Real32 | 0 | [ -24 , 24 ] | true | Additive | false |
| **FilterQFactor** | Filter Q Factor | Real32 | 1 | [ 0.1 , 20 ] | true | Exclusive | false |
| **FilterType** | Filter Type | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | Low Shelf | | 2 | Peaking | | 3 | High Shelf | | 4 | Low Pass | | 5 | High Pass | | 6 | Band Pass | | 7 | Notch | | true | Exclusive | false |
| **FrontRearBalance** | Front/Rear Balance | Real32 | -100 | [ -100 , 100 ] | true | Additive | false |
| **LeftCrossfeed** | Left Crossfeed | Real32 | -12 | [ -48 , 0 ] | true | Additive | false |
| **LeftDelayTime** | Left Delay Time | Real32 | 0.1 | [ 0.03 , 2 ] | true | None | false |
| **LeftFeedback** | Left Feedback | Real32 | -12 | [ -48 , 0 ] | true | Additive | false |
| **LeftInputType** | Left Input Type | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Left | | 1 | Center | | 2 | Left+Center | | 3 | None | | true | None | false |
| **RightCrossfeed** | Right Crossfeed | Real32 | -12 | [ -48 , 0 ] | true | Additive | false |
| **RightDelayTime** | Right Delay Time | Real32 | 0.1 | [ 0.03 , 2 ] | true | None | false |
| **RightFeedback** | Right Feedback | Real32 | -12 | [ -48 , 0 ] | true | Additive | false |
| **RightInputType** | Right Input Type | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Right | | 1 | Center | | 2 | Right+Center | | 3 | None | | true | None | false |
| **WetLevel** | Wet Level | Real32 | 0 | [ -96 , 24 ] | true | Additive | false |