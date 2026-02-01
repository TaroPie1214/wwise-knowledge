# 将对象添加到 Inclusion 列表

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

将对象添加到 Inclusion 列表

将对象添加到 SoundBank 的 Inclusion 列表。未考虑 'media' 筛选器。

# 函数 URI

[ak.wwise.core.soundbank.setInclusions](ak_wwise_core_soundbank_setinclusions.html)

# 参数

{

"soundbank": "{A076AA65-B71A-45BB-8841-5A20C52CE727}",

"operation": "add",

"inclusions": [

{

"object": "{AAAAAAAA-BBBB-CCCC-DDDD-EEEEEEEEEEEE}",

"filter": [

"events",

"structures"

]

}

]

}

# 结果

{}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。