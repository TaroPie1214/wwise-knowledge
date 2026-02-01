# GameParameter

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

GameParameter

- **Plugin ID**: 23
- **Class ID**: 1507344

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **BindToBuiltInParam** | Use Built-In Parameter | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | Distance | | 2 | Azimuth | | 3 | Elevation | | 4 | Emitter Cone | | 5 | Obstruction | | 6 | Occlusion | | 7 | Listener Cone | | 8 | Diffraction | | 9 | Transmission Loss | | true | None | false |
| **Color** | Color | int16 | 0 | [ 0 , 26 ] | true | None | false |
| **FilterTimeDown** | Release | Real64 | 0 | [ 0 , 100000 ] | true | None | false |
| **FilterTimeUp** | Attack | Real64 | 0 | [ 0 , 100000 ] | true | None | false |
| **InitialValue** | Default Value | Real64 | 50 | None | true | None | false |
| **Max** | Max | Real64 | 100 | None | true | None | false |
| **Min** | Min | Real64 | 0 | None | true | None | false |
| **OverrideColor** | Override Color | bool | false | None | true | None | false |
| **RTPCRamping** | Interpolation Mode | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | None | | 1 | Slew Rate | | 2 | Filtering over time | | true | None | false |
| **SimulationValue** | Simulation Value | Real64 | 50 | None | true | None | false |
| **SlewRateDown** | Release | Real64 | 50 | [ 0 , 1000000 ] | true | None | false |
| **SlewRateUp** | Attack | Real64 | 50 | [ 0 , 1000000 ] | true | None | false |