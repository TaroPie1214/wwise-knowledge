# 获取所有包含 Sound 对象的对象

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

获取所有包含 Sound 对象的对象

检索至少有一个子对象为 Sound 对象的对象的 ID。可使用 "distinct" 转换来滤掉重复项。

# 函数 URI

[ak.wwise.core.object.get](ak_wwise_core_object_get.html)

# 参数

{

"waql": "from type sound select parent distinct"

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

"return": [

{

"id": "{01181963-13CA-4946-B4C2-7A04BF727596}",

"name": "Folder0"

},

{

"id": "{F9912AA4-7835-4828-99E6-C327840EFE3D}",

"name": "Folder1"

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。