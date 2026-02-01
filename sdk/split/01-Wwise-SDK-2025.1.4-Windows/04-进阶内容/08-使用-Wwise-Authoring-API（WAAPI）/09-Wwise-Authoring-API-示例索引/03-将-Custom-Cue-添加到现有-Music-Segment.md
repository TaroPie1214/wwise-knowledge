# 将 Custom Cue 添加到现有 Music Segment

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

将 Custom Cue 添加到现有 Music Segment

按照给定名称和时间（毫秒）在现有 Music Segment 内创建 Custom Cue。

# 函数 URI

[ak.wwise.core.object.create](ak_wwise_core_object_create.html)

# 参数

{

"name": "My Music Cue",

"parent": "\\Containers\\Default Work Unit\\My Segment",

"type": "MusicCue",

"list": "Cues",

"@TimeMs": 1200,

"@CueType": 2

}

# 结果

{

"id": "{1629938A-24F7-451F-B01F-49F448CED8FF}",

"name": "My Music Cue"

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。