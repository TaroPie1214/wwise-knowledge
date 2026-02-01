# Adding a Marker to an Audio Source

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Adding a Marker to an Audio Source

In the "Markers" list of an audio source, appends a Marker using the given Time and Label properties.

# 函数 URI

[ak.wwise.core.object.set](ak_wwise_core_object_set.html)

# 参数

{

"objects": [

{

"object": "\\Containers\\Default Work Unit\\MySoundSFX\\MyAudioSource",

"@MarkerInputMode": 2,

"@Markers": [

{

"type": "Marker",

"name": "",

"@Time": 1,

"@Label": "Waapi Generated"

}

],

"listMode": "append"

}

]

}

# 选项

{

"return": [

"id",

"name",

"@Time",

"@Label"

]

}

# 结果

{

"objects": [

{

"id": "{5A1EC9A4-5C47-4555-82EF-50722C168C0C}",

"name": "AudioSource",

"@Markers": [

{

"id": "{DAEC2A58-4605-4553-AA67-1090716691DC}",

"name": "",

"@Time": 1,

"@Label": "Waapi Generated"

}

]

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。