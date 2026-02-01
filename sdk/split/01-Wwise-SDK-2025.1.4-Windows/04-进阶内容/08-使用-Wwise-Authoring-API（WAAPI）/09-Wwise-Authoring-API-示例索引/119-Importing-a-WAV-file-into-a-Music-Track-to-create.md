# Importing a WAV file into a Music Track to create a Music Clip

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Importing a WAV file into a Music Track to create a Music Clip

Creates a Music Segment, a Music Track, and imports its WAV file. A Music Track is also created.

# 函数 URI

[ak.wwise.core.object.set](ak_wwise_core_object_set.html)

# 参数

{

"objects": [

{

"object": "\\Containers\\Default Work Unit",

"children": [

{

"type": "MusicSegment",

"name": "New Segment",

"children": [

{

"type": "MusicTrack",

"name": "New Track",

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

# Options

{

"return": [

"id",

"name",

"type"

]

}

# 结果

{

"objects": [

{

"children": [

{

"children": [

{

"id": "{70E2785C-0AE2-4C66-9B79-97C48F487C31}",

"import": {

"logs": [

{

"message": "Finalizing Importation...",

"severity": "Message"

}

],

"objects": [

{

"id": "{23B912A7-E2E2-4F22-B276-E7259BC7BF6D}",

"name": "file1",

"type": "AudioFileSource"

}

]

},

"name": "New Track",

"type": "MusicTrack"

}

],

"id": "{610325D4-33C9-4957-B663-AA9E3D797146}",

"name": "New Segment",

"type": "MusicSegment"

}

],

"id": "{6128CF6C-DE55-4E1C-A582-BD27EAD90A13}",

"name": "Default Work Unit"

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。