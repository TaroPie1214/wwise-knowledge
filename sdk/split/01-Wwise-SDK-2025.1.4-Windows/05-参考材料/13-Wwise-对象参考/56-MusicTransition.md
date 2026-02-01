# MusicTransition

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

MusicTransition

- **Plugin ID**: 37
- **Class ID**: 2424848

如需了解如何使用 [WAAPI](waapi.html) 设置属性和引用，请参阅 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 、 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。如需了解如何查询属性和引用，请参阅 [查询 Wwise 工程](waapi_query.html) 章节。  
如需了解如何使用 [WAAPI](waapi.html) 向列表添加对象，请参阅 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 章节。

# 属性、引用、列表

| 名称 | 显示名称 | 类型 | 默认 | 限制 | 可见 | 支持的 RTPC 类型 | 支持 Link/Unlink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Color** | Color | int16 | 0 | [ 0 , 26 ] | true | None | false |
| **DestinationContextObject** | Destination Object | Reference |  | **可能的类型：**   |  | | --- | | MusicSegment | | MusicPlaylistContainer | | MusicSwitchContainer | | Folder | | true |  |  |
| **DestinationContextType** | Destination Type | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Any | | 1 | Nothing | | 2 | Object | | true | None | false |
| **DestinationJumpPositionPreset** | Destination Sync To | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Entry Cue | | 1 | Same Time as Playing Segment | | 2 | Random Cue | | 3 | Random Custom Cue | | 4 | Last Exit Position | | true | None | false |
| **DestinationPlaylistJumpTo** | Destination Jump To | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Start of Playlist | | 1 | Specific Playlist Item | | 2 | Last Played Segment | | 3 | Next Segment | | true | None | false |
| **EnableDestinationFadeIn** | Enable Destination Fade-in | bool | false | None | true | None | false |
| **EnableSourceFadeOut** | Enable Source Fade-out | bool | false | None | true | None | false |
| **EnableTransitionFadeIn** | Enable Transition Fade-in | bool | false | None | true | None | false |
| **EnableTransitionFadeOut** | Enable Transition Fade-out | bool | false | None | true | None | false |
| **ExitSourceAt** | Exit Source At | int16 | 7 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Immediate | | 1 | Next Grid | | 2 | Next Bar | | 3 | Next Beat | | 4 | Next Cue | | 5 | Custom Cue | | 7 | Exit Cue | | 8 | Never (only for music tracks) | | true | None | false |
| **ExitSourceCustomCueMatchName** | Exit source at custom cue match name | string |  | None | true | None | false |
| **IsFolder** | Is Folder | bool | false | None | false | None | false |
| **JumpToCustomCueMatchMode** | Jump to custom cue match mode | int16 | 1 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Match source cue name | | 1 | Match specific name | | true | None | false |
| **JumpToCustomCueMatchName** | Jump to custom cue match name | string |  | None | true | None | false |
| **OverrideColor** | Override Color | bool | false | None | true | None | false |
| **PlayDestinationPreEntry** | Play Destination Pre-entry | bool | true | None | true | None | false |
| **PlaySourcePostExit** | Play Source Post-exit | bool | true | None | true | None | false |
| **PlayTransitionPostExit** | Play Transition Post-exit | bool | true | None | true | None | false |
| **PlayTransitionPreEntry** | Play Transition Pre-entry | bool | true | None | true | None | false |
| **SourceContextObject** | Source Object | Reference |  | **可能的类型：**   |  | | --- | | MusicSegment | | MusicPlaylistContainer | | MusicSwitchContainer | | Folder | | true |  |  |
| **SourceContextType** | Source Type | int16 | 0 | **可能的值：**   |  |  | | --- | --- | | 值 | 显示名称 | | 0 | Any | | 1 | Nothing | | 2 | Object | | true | None | false |
| **UseTransitionObject** | Use Transition Object | bool | false | None | true | None | false |