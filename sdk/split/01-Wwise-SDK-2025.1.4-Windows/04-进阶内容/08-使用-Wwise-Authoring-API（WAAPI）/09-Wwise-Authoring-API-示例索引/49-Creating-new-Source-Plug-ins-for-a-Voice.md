# Creating new Source Plug-ins for a Voice

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Creating new Source Plug-ins for a Voice

针对 "English(US)" 和 "French" 语言为使用 Silence 和 SoundSeed Grain 插件的 Voice 创建两个新的 Source 对象。

# 函数 URI

[ak.wwise.core.object.set](ak_wwise_core_object_set.html)

# 参数

{

"objects": [

{

"object": "\\Containers\\Default Work Unit\\MyVoice",

"children": [

{

"type": "Source",

"name": "source1",

"language": "English(US)",

"classId": 6619138

},

{

"type": "Source",

"name": "source2",

"language": "French",

"classId": 11993090

}

]

}

]

}

# 选项

{

"return": [

"id",

"name"

]

}

# 结果

{

"objects": [

{

"id": "{7ACD763F-2E44-4D07-AA7F-E6C9C60B2DDC}",

"name": "VO",

"children": [

{

"id": "{DAEC2A58-4605-4553-AA67-1090716691DC}",

"name": "source1"

},

{

"id": "{92A79310-38E6-4C89-9A06-DA59668E79A4}",

"name": "source2"

}

]

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。