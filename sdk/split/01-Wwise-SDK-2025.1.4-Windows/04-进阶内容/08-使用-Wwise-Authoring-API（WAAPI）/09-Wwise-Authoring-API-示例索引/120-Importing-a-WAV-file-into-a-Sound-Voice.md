# Importing a WAV file into a Sound Voice

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Importing a WAV file into a Sound Voice

Creates a Sound Voice object and an audio file source object and imports its wave file for English localization.

# 函数 URI

[ak.wwise.core.object.set](ak_wwise_core_object_set.html)

# 参数

{

"objects": [

{

"object": "\\Containers\\Default Work Unit",

"children": [

{

"type": "Sound Voice",

"name": "New Voice",

"import": {

"files": [

{

"audioFile": "c:\\path\\file1.wav",

"language": "English(US)"

}

]

}

}

]

}

]

}

# 结果

{}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。