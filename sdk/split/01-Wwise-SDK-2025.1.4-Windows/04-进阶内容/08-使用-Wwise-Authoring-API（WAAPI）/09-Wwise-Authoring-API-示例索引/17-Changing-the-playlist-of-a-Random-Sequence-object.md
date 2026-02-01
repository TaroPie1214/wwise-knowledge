# Changing the playlist of a Random Sequence object

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Changing the playlist of a Random Sequence object

The playlist added to the Random Sequence object is composed of the '1st number' object followed by two times '2nd Number'.

# 函数 URI

[ak.wwise.core.object.set](ak_wwise_core_object_set.html)

# 参数

{

"objects": [

{

"object": "\\Containers\\External Sources\\Three Numbers in a Row",

"@Playlist": [

{

"type": "PlaylistSlot",

"name": "",

"@PlaylistObject": "\\Containers\\External Sources\\Three Numbers in a Row\\1st Number"

},

{

"type": "PlaylistSlot",

"name": "",

"@PlaylistObject": "\\Containers\\External Sources\\Three Numbers in a Row\\2nd Number"

},

{

"type": "PlaylistSlot",

"name": "",

"@PlaylistObject": "\\Containers\\External Sources\\Three Numbers in a Row\\2nd Number"

}

]

}

],

"onNameConflict": "merge",

"listMode": "replaceAll"

}

# 结果

{}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。