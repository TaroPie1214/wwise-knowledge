# Importing WAV files into Impacter source plug-in

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Importing WAV files into Impacter source plug-in

Creates a Sound and an Impacter source plug-in, then imports WAV files.

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

"name": "Impacter",

"children": [

{

"type": "SourcePlugin",

"name": "Impacter",

"classId": 12058626,

"import": {

"files": [

{

"audioFile": "C:\\Sound1.wav"

},

{

"audioFile": "C:\\Sound2.wav"

},

{

"audioFile": "C:\\Sound3.wav"

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

"id": "{5EB1DA04-E70C-450A-87C1-EFA673466B6E}",

"name": "Impacter",

"children": [

{

"id": "{0DF0AE5B-48E0-44B9-A9BB-23296814AE78}",

"name": "Impacter",

"import": {}

}

]

}

]

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。