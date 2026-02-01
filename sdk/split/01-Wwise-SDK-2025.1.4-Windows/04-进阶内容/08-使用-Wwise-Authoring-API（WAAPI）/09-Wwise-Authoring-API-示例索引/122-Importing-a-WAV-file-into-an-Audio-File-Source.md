# Importing a WAV file into an Audio File Source

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Importing a WAV file into an Audio File Source

Creates a Sound SFX object and its audio source. The property field Sound object is also set.

# 函数 URI

[ak.wwise.core.object.set](ak_wwise_core_object_set.html)

# 参数

{

"objects": [

{

"object": "\\Containers\\Default Work Unit",

"children": [

{

"type": "Sound",

"name": "New Sound",

"children": [

{

"name": "mySource",

"type": "AudioFileSource",

"notes": "newNotes",

"import": {

"files": [

{

"audioFile": "c:\\path\\file1.wav"

}

]

}

}

]

}

]

}

]

}

# 结果

{}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。