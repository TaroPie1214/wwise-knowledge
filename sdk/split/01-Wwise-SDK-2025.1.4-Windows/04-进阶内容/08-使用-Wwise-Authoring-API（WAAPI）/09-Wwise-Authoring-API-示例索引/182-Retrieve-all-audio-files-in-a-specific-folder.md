# Retrieve all audio files in a specific folder

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Retrieve all audio files in a specific folder

Returns the absolute path of audio files in a folder.

# 函数 URI

[ak.wwise.core.sourceControl.getSourceFiles](ak_wwise_core_sourcecontrol_getsourcefiles.html)

# 参数

{

"folder": "Voices\\English(US)",

"recursive": false

}

# 选项

{

"return": [

"file",

"isUsed",

"usage"

]

}

# 结果

{

"return": [

{

"file": "Voices\\English(US)\\3.wav",

"isUsed": true,

"usage": [

{

"id": "{97735FC6-A17E-4662-AC77-6E78178D7B03}",

"name": "3"

}

]

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。