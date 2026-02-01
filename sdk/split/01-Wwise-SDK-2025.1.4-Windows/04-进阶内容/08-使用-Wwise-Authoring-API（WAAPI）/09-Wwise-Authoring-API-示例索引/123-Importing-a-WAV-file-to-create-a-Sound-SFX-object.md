# Importing a WAV file to create a Sound SFX object

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Importing a WAV file to create a Sound SFX object

Creates a Source SFX object and an audio file source object and imports its wave file.

# 函数 URI

[ak.wwise.core.object.set](ak_wwise_core_object_set.html)

# 参数

{

"objects": [

{

"object": "\\Containers\\Default Work Unit",

"import": {

"files": [

{

"audioFile": "c:\\path\\file.wav"

}

]

}

}

],

"onNameConflict": "merge"

}

# 结果

{}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。