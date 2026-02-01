# 检索 SoundBank 的 Inclusion 列表

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

检索 SoundBank 的 Inclusion 列表

获取 SoundBank 的 Inclusion 列表。

# 函数 URI

[ak.wwise.core.soundbank.getInclusions](ak_wwise_core_soundbank_getinclusions.html)

# 参数

{

"soundbank": "{A076AA65-B71A-45BB-8841-5A20C52CE727}"

}

# 结果

{

"inclusions": [

{

"object": "{1111AAAA-BBBB-CCCC-DDDD-EEEEEEEEEEEE}",

"filter": [

"events"

]

},

{

"object": "{2222AAAA-BBBB-CCCC-DDDD-EEEEEEEEEEEE}",

"filter": [

"structures",

"media"

]

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。