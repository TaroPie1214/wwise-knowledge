# 为 Sound 对象创建 Play Event

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

为 Sound 对象创建 Play Event

在 'WAAPI' 虚文件夹下创建 'Play\_SFX' Event，并为 SFX 声音对象添加 Play 动作。See [Action](wwiseobject_action.html) for the list of possible event properties and action types.

# 函数 URI

[ak.wwise.core.object.create](ak_wwise_core_object_create.html)

# 参数

{

"parent": "\\Events\\Default Work Unit",

"type": "Folder",

"name": "WAAPI",

"onNameConflict": "merge",

"children": [

{

"type": "Event",

"name": "Play\_SFX",

"children": [

{

"name": "",

"type": "Action",

"@ActionType": 1,

"@Target": "\\Containers\\Default Work Unit\\SFX"

}

]

}

]

}

# 结果

{

"id": "{6114659F-9274-4031-B90E-F369568532E0}",

"name": "WAAPI",

"children": [

{

"id": "{F546017D-201A-49BD-8D4E-0A28F5DBB28D}",

"name": "Play\_SFX",

"children": [

{

"id": "{400D0354-0FDB-48B4-B341-9DFA0B76078D}",

"name": ""

}

]

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。