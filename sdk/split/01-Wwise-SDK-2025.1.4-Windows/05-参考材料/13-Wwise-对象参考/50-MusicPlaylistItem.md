# MusicPlaylistItem

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

MusicPlaylistItem

- **Plugin ID**: 36
- **Class ID**: 2359312

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Color** | Color | int16 | 0 | [ 0 , 26 ] | true | None | false |
| **LoopCount** | No. of Loops | int16 | 1 | [ 0 , 32767 ] | true | None | false |
| **NormalOrShuffle** | Random type | int16 | 1 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Shuffle | | 1 | Standard | | true | None | false |
| **OverrideColor** | Override Color | bool | false | None | true | None | false |
| **PlayMode** | Play Mode | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Sequence Continuous | | 1 | Sequence Step | | 2 | Random Continuous | | 3 | Random Step | | true | None | false |
| **PlaylistItemType** | Playlist Item Type | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Group | | 1 | Segment | | true | None | false |
| **RandomAvoidRepeatingCount** | Limit repetition to | int32 | 1 | [ 0 , 999 ] | true | None | false |
| **Segment** | Segment | Reference |  | **可能的类型：**   |  | | --- | | MusicSegment |     **不得为 Null** | true |  |  |
| **Weight** | Weight | Real64 | 50 | [ 0.001 , 100 ] | true | None | true |