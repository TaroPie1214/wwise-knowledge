# Getting the objects using an effect

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Getting the objects using an effect

Uses the referencesTo and owner accessors to get the list of objects using the effect ShareSet.

# 函数 URI

[ak.wwise.core.object.get](ak_wwise_core_object_get.html)

# 参数

{

"waql": "\"\\Effects\\Factory Effects\\Flanger\\Chorus\\Chorus\_Like\" select referencesTo.owner"

}

# 选项

{

"return": [

"path",

"name"

]

}

# 结果

{

"return": [

{

"id": "{F72DD400-91D1-4305-B14E-31113A28FF1C}",

"name": "MySound"

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。