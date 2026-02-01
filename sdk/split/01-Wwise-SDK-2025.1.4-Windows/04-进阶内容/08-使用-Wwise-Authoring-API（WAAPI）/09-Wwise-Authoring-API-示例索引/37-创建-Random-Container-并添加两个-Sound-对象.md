# 创建 Random Container 并添加两个 Sound 对象

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

创建 Random Container 并添加两个 Sound 对象

在给定父对象下创建 'Boom' Random Container，并在其中添加 'A' 和 'B' Sound 对象。

# 函数 URI

[ak.wwise.core.object.create](ak_wwise_core_object_create.html)

# 参数

{

"parent": "{7A12D08F-B0D9-4403-9EFA-2E6338C197C1}",

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

# 结果

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

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。