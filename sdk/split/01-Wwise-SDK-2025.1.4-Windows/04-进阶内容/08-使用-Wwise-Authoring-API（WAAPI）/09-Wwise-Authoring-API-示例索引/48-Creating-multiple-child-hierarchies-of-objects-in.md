# Creating multiple child hierarchies of objects in batch

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Creating multiple child hierarchies of objects in batch

在多个对象下一并创建子对象层级结构：#1. 在给定父对象下创建新的 'Boom' Sound 对象。#2. 在 Default Work Unit 下创建新的 'Guns' Virtual Folder。若已存在同名的文件夹，则自动命名为唯一名称。#3. 在 'WAAPI' 虚文件夹下创建 'Play\_SFX' Event，并为 SFX 声音对象添加 Play 动作。#4. 在给定父对象下创建 'Boom' Random Container，并在其中添加 'A' 和 'B' Sound 对象。#5. 按照给定名称和时间（毫秒）在现有 Music Segment 内创建 Custom Cue。参见有关 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 的示例来对比两种架构。

# 函数 URI

[ak.wwise.core.object.set](ak_wwise_core_object_set.html)

# 参数

{

"objects": [

{

"object": "{7A12D08F-B0D9-4403-9EFA-2E6338C197C1}",

"children": [

{

"type": "Sound",

"name": "Boom"

}

]

},

{

"object": "\\Containers\\Default Work Unit",

"children": [

{

"type": "Folder",

"name": "Guns"

}

],

"onNameConflict": "rename"

},

{

"object": "\\Events\\Default Work Unit",

"onNameConflict": "merge",

"children": [

{

"type": "Folder",

"name": "WAAPI",

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

]

},

{

"object": "{7A12D08F-B0D9-4403-9EFA-2E6338C197C1}",

"children": [

{

"type": "RandomSequenceContainer",

"name": "Boom",

"@RandomOrSequence": 1,

"children": [

{

"type": "Sound",

"name": "A"

},

{

"type": "Sound",

"name": "B"

}

]

}

]

},

{

"object": "\\Containers\\Default Work Unit\\My Segment",

"@Cues": [

{

"name": "My Music Cue",

"type": "MusicCue",

"@TimeMs": 1200,

"@CueType": 2

}

]

}

],

"onNameConflict": "fail"

}

# 结果

{

"objects": [

{

"id": "{7A12D08F-B0D9-4403-9EFA-2E6338C197C1}",

"name": "Default Work Unit",

"children": [

{

"id": "{66666666-7777-8888-9999-AAAAAAAAAAAA}",

"name": "Boom"

}

]

},

{

"id": "{7A12D08F-B0D9-4403-9EFA-2E6338C197C1}",

"name": "Default Work Unit",

"children": [

{

"id": "{66666666-7777-8888-9999-AAAAAAAAAAAA}",

"name": "Guns"

}

]

},

{

"id": "{C6C4338E-99E1-44C2-B881-F98612FEDF5F}",

"name": "Default Work Unit",

"children": [

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

]

},

{

"id": "{7A12D08F-B0D9-4403-9EFA-2E6338C197C1}",

"name": "Default Work Unit",

"children": [

{

"id": "{66666666-7777-8888-9999-AAAAAAAAAAAA}",

"name": "Boom",

"children": [

{

"id": "{46813545-2168-3547-8328-681AB678D6F5}",

"name": "A"

},

{

"id": "{68465134-2548-2377-3541-321354318ABD}",

"name": "B"

}

]

}

]

},

{

"id": "{9111F89B-8227-4766-9FEF-BBE6CE5B9F6E}",

"name": "My Segment",

"@Cues": [

{

"id": "{1629938A-24F7-451F-B01F-49F448CED8FF}",

"name": "My Music Cue"

}

]

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。