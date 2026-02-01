# Query

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Query

- **Plugin ID**: 32
- **Class ID**: 2097168

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Color** | Color | int16 | 0 | [ 0 , 26 ] | true | None | false |
| **LogicalOperator** | Logical Operator | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 |  | | 1 |  | | false | None | false |
| **ObjectType** | Object Type | int32 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | All Objects | | 10 | WAQL Query | | 100 | Property Container | | 205 | Containers - All | | 200 | Containers - No Music | | 620 | Containers - All Music | | 621 | Containers - Music Containers | | 2200 | Acoustic Texture | | 1300 | Argument | | 1400 | Argument Value | | 250 | Attenuation | | 500 | Audio Bus | | 740 | Audio Device | | 502 | Auxiliary Bus | | 300 | Audio Source | | 400 | Blend Container | | 1500 | Conversion Settings | | 1200 | Dialogue Event | | 550 | Effect | | 600 | Event | | 1600 | External Source | | 1700 | Virtual Folder | | 2400 | Metadata | | 1900 | Modulator Envelope | | 2000 | Modulator LFO | | 2300 | Modulator Time | | 2100 | Modulators | | 667 | Music Clip | | 669 | Music Clip MIDI | | 668 | Music Cue | | 671 | Music Event Cue | | 630 | Music Fade | | 640 | Music Playlist Item | | 645 | Music Playlist Container | | 650 | Music Segment | | 655 | Music Stinger | | 660 | Music Switch Container | | 665 | Music Track | | 666 | Music Track Sequence | | 670 | Music Transition | | 700 | Random-Sequence Container | | 770 | Sidechain Mix | | 800 | Sound | | 900 | SoundBank | | 1000 | Switch Container | | 1010 | Switch Group | | 1100 | Trigger | | 1800 | Work Unit-Physical Folder | | true | None | false |
| **OverrideColor** | Override Color | bool | false | None | true | None | false |
| **Platform** | Platform | int16 | 1 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 |  | | 1 |  | | false | None | false |
| **StartObject** | Starting Object | Reference |  | None | true |  |  |
| **WAQL** | WAQL Query | string |  | None | true | None | false |