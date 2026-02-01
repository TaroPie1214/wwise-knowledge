# Importing a WAV file into Soundseed Grain source plug-in

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Importing a WAV file into Soundseed Grain source plug-in

Creates a Sound and a Soundseed Grain source plug-in, then imports a WAV file.

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

"name": "Grain",

"children": [

{

"type": "SourcePlugin",

"name": "Grain",

"classId": 11993090,

"import": {

"files": [

{

"audioFile": "C:\\Sound1.wav"

}

]

}

}

]

}

]

}

],

"onNameConflict": "merge"

}

# 结果

{

"objects": [

{

"id": "{FF8CD9E6-627F-4760-B0A9-F9AD3B3EB477}",

"name": "Default Work Unit",

"children": [

{

"id": "{54129975-8649-42C5-B5AE-BE5871C4D373}",

"name": "Grain",

"children": [

{

"id": "{4A8356D6-C925-4945-8C84-9F67D0B774EB}",

"name": "Grain",

"import": {}

}

]

}

]

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。