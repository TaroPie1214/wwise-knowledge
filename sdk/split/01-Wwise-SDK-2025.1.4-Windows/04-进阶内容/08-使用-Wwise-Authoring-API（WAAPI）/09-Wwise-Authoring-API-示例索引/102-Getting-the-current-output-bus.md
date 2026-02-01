# Getting the current output bus

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Getting the current output bus

Returns the output bus that the object is currently using. The bus returned in the result is either inherited from a parent at a higher level in the hierarchy or is an override (the result does not distinguish between inherited or overridden busses).

# 函数 URI

[ak.wwise.core.object.get](ak_wwise_core_object_get.html)

# 参数

{

"waql": "\"{24979032-B170-43E3-A2E4-469E0193E2C3}\""

}

# 选项

{

"return": [

"OutputBus"

]

}

# 结果

{

"return": [

{

"OutputBus": {

"id": "{1514A4D8-1DA6-412A-A17E-75CA0C2149F3}",

"name": "Main Audio Bus"

}

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。