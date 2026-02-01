# Wwise Multiband Meter

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise Multiband Meter

- **Plugin ID**: 196
- **Class ID**: 12845059

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# Properties, References, Lists

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **ApplyDownstreamVolume** | Apply Downstream Volume | bool | false | None | true | None | false |
| **AttackTime\_Band0** | Full Band Attack Time | Real32 | 0.0 | [ 0 , 10 ] | true | Additive | false |
| **AttackTime\_Band1** | Band 1 Attack Time | Real32 | 0.0 | [ 0 , 10 ] | true | Additive | false |
| **AttackTime\_Band2** | Band 2 Attack Time | Real32 | 0.0 | [ 0 , 10 ] | true | Additive | false |
| **AttackTime\_Band3** | Band 3 Attack Time | Real32 | 0.0 | [ 0 , 10 ] | true | Additive | false |
| **AttackTime\_Band4** | Band 4 Attack Time | Real32 | 0.0 | [ 0 , 10 ] | true | Additive | false |
| **Enabled\_Band1** | Band 1 Enable | bool | true | None | true | None | false |
| **Enabled\_Band2** | Band 2 Enable | bool | true | None | true | None | false |
| **Enabled\_Band3** | Band 3 Enable | bool | true | None | true | None | false |
| **Enabled\_Band4** | Band 4 Enable | bool | true | None | true | None | false |
| **GameParameter\_Band0** | Full Band Game Parameter | Reference |  | **可能的类型：**   |  | | --- | | GameParameter | | true |  |  |
| **GameParameter\_Band1** | Band 1 Game Parameter | Reference |  | **可能的类型：**   |  | | --- | | GameParameter | | true |  |  |
| **GameParameter\_Band2** | Band 2 Game Parameter | Reference |  | **可能的类型：**   |  | | --- | | GameParameter | | true |  |  |
| **GameParameter\_Band3** | Band 3 Game Parameter | Reference |  | **可能的类型：**   |  | | --- | | GameParameter | | true |  |  |
| **GameParameter\_Band4** | Band 4 Game Parameter | Reference |  | **可能的类型：**   |  | | --- | | GameParameter | | true |  |  |
| **HighFrequency\_Band1** | Band 1 High Frequency | Real32 | 200 | [ 20 , 20000 ] | true | Exclusive | false |
| **HighFrequency\_Band2** | Band 2 High Frequency | Real32 | 400 | [ 20 , 20000 ] | true | Exclusive | false |
| **HighFrequency\_Band3** | Band 3 High Frequency | Real32 | 800 | [ 20 , 20000 ] | true | Exclusive | false |
| **HighFrequency\_Band4** | Band 4 High Frequency | Real32 | 16000 | [ 20 , 20000 ] | true | Exclusive | false |
| **HighRolloff\_Band1** | Band 1 High Roll-off | int32 | 2 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Disabled | | 1 | 12 dB/Oct | | 2 | 24 dB/Oct | | 3 | 36 dB/Oct | | 4 | 48 dB/Oct | | true | None | false |
| **HighRolloff\_Band2** | Band 2 High Roll-off | int32 | 2 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Disabled | | 1 | 12 dB/Oct | | 2 | 24 dB/Oct | | 3 | 36 dB/Oct | | 4 | 48 dB/Oct | | true | None | false |
| **HighRolloff\_Band3** | Band 3 High Roll-off | int32 | 2 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Disabled | | 1 | 12 dB/Oct | | 2 | 24 dB/Oct | | 3 | 36 dB/Oct | | 4 | 48 dB/Oct | | true | None | false |
| **HighRolloff\_Band4** | Band 4 High Roll-off | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Disabled | | 1 | 12 dB/Oct | | 2 | 24 dB/Oct | | 3 | 36 dB/Oct | | 4 | 48 dB/Oct | | true | None | false |
| **Hold\_Band0** | Full Band Hold | Real32 | 0 | [ 0 , 10 ] | true | Additive | false |
| **Hold\_Band1** | Band 1 Hold | Real32 | 0 | [ 0 , 10 ] | true | Additive | false |
| **Hold\_Band2** | Band 2 Hold | Real32 | 0 | [ 0 , 10 ] | true | Additive | false |
| **Hold\_Band3** | Band 3 Hold | Real32 | 0 | [ 0 , 10 ] | true | Additive | false |
| **Hold\_Band4** | Band 4 Hold | Real32 | 0 | [ 0 , 10 ] | true | Additive | false |
| **InfiniteHold** | Infinite Hold | bool | false | None | true | Boolean | false |
| **LowFrequency\_Band1** | Band 1 Low Frequency | Real32 | 20 | [ 20 , 20000 ] | true | Exclusive | false |
| **LowFrequency\_Band2** | Band 2 Low Frequency | Real32 | 200 | [ 20 , 20000 ] | true | Exclusive | false |
| **LowFrequency\_Band3** | Band 3 Low Frequency | Real32 | 400 | [ 20 , 20000 ] | true | Exclusive | false |
| **LowFrequency\_Band4** | Band 4 Low Frequency | Real32 | 800 | [ 20 , 20000 ] | true | Exclusive | false |
| **LowRolloff\_Band1** | Band 1 Low Roll-off | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Disabled | | 1 | 12 dB/Oct | | 2 | 24 dB/Oct | | 3 | 36 dB/Oct | | 4 | 48 dB/Oct | | true | None | false |
| **LowRolloff\_Band2** | Band 2 Low Roll-off | int32 | 2 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Disabled | | 1 | 12 dB/Oct | | 2 | 24 dB/Oct | | 3 | 36 dB/Oct | | 4 | 48 dB/Oct | | true | None | false |
| **LowRolloff\_Band3** | Band 3 Low Roll-off | int32 | 2 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Disabled | | 1 | 12 dB/Oct | | 2 | 24 dB/Oct | | 3 | 36 dB/Oct | | 4 | 48 dB/Oct | | true | None | false |
| **LowRolloff\_Band4** | Band 4 Low Roll-off | int32 | 2 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Disabled | | 1 | 12 dB/Oct | | 2 | 24 dB/Oct | | 3 | 36 dB/Oct | | 4 | 48 dB/Oct | | true | None | false |
| **Max\_Band0** | Full Band Max | Real32 | 0 | [ -96.3 , 12 ] | true | Additive | false |
| **Max\_Band1** | Band 1 Max | Real32 | 0 | [ -96.3 , 12 ] | true | Additive | false |
| **Max\_Band2** | Band 2 Max | Real32 | 0 | [ -96.3 , 12 ] | true | Additive | false |
| **Max\_Band3** | Band 3 Max | Real32 | 0 | [ -96.3 , 12 ] | true | Additive | false |
| **Max\_Band4** | Band 4 Max | Real32 | 0 | [ -96.3 , 12 ] | true | Additive | false |
| **MeterMode** | Mode | int32 | 1 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Peak | | 1 | RMS | | true | None | false |
| **MeterScope** | RTPC Scope | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Global | | 1 | Game Object | | true | None | false |
| **Min\_Band0** | Full Band Min | Real32 | -48 | [ -96.3 , 0 ] | true | Additive | false |
| **Min\_Band1** | Band 1 Min | Real32 | -48 | [ -96.3 , 0 ] | true | Additive | false |
| **Min\_Band2** | Band 2 Min | Real32 | -48 | [ -96.3 , 0 ] | true | Additive | false |
| **Min\_Band3** | Band 3 Min | Real32 | -48 | [ -96.3 , 0 ] | true | Additive | false |
| **Min\_Band4** | Band 4 Min | Real32 | -48 | [ -96.3 , 0 ] | true | Additive | false |
| **MixdownCfg** | Mixdown Config | int32 | 16641 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | No Mixdown | | 16641 | Mono | | false | None | false |
| **ReleaseTime\_Band0** | Full Band Release Time | Real32 | 0.1 | [ 0 , 10 ] | true | Additive | false |
| **ReleaseTime\_Band1** | Band 1 Release Time | Real32 | 0.1 | [ 0 , 10 ] | true | Additive | false |
| **ReleaseTime\_Band2** | Band 2 Release Time | Real32 | 0.1 | [ 0 , 10 ] | true | Additive | false |
| **ReleaseTime\_Band3** | Band 3 Release Time | Real32 | 0.1 | [ 0 , 10 ] | true | Additive | false |
| **ReleaseTime\_Band4** | Band 4 Release Time | Real32 | 0.1 | [ 0 , 10 ] | true | Additive | false |
| **SoloMonitor** | Solo Band | Uint32 | 0 | [ 0 , 4 ] | true | None | false |