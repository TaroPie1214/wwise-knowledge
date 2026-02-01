# Importing two WAV files to create two Sound SFX objects

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Importing two WAV files to create two Sound SFX objects

Creates two Sound SFX objects and two audio file source objects and imports their wave files.

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

"audioFile": "c:\\path\\file1.wav"

},

{

"audioFile": "c:\\path\\file2.wav"

}

]

}

}

]

}

# 结果

{}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。