# MusicStinger

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

MusicStinger

- **Plugin ID**: 38
- **Class ID**: 2490384

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Color** | Color | int16 | 0 | [ 0 , 26 ] | true | None | false |
| **CustomCueMatchName** | Custom cue match name | string |  | None | true | None | false |
| **DontPlayAgainTime** | Don't Play Again Time | Real64 | 0 | [ 0 , 3600 ] | true | None | false |
| **NumSegmentAdvance** | Allow playing Stinger in next segment | int16 | 1 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | No | | 1 | Yes | | true | None | false |
| **OverrideColor** | Override Color | bool | false | None | true | None | false |
| **PlaySegmentAt** | Play Segment At | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Immediate | | 1 | Next Grid | | 2 | Next Bar | | 3 | Next Beat | | 4 | Next Cue | | 5 | Custom Cue | | 6 | Entry Cue | | 7 | Exit Cue | | true | None | false |
| **Segment** | Segment | Reference |  | **可能的类型：**   |  | | --- | | MusicSegment | | true |  |  |
| **Trigger** | Trigger | Reference |  | **可能的类型：**   |  | | --- | | Trigger | | true |  |  |