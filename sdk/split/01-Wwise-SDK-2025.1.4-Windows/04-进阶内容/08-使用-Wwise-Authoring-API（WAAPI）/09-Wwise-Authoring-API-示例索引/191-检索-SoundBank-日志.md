# 检索 SoundBank 日志

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

检索 SoundBank 日志

使用 'soundbankGenerate' 通道来检索最新的 SoundBank 生成日志。

# 函数 URI

[ak.wwise.core.log.get](ak_wwise_core_log_get.html)

# 参数

{

"channel": "soundbankGenerate"

}

# 结果

{

"items": [

{

"severity": "Warning",

"time": 1523563779,

"messageId": "ParamControlIntegrityIssue",

"message": "RTPC : object New Audio Bus, property PositioningType cannot be resolved; the RTPC is ignored.",

"platform": {

"id": "{F546017D-201A-49BD-8D4E-0A28F5DBB28D}",

"name": "Windows"

},

"parameters": [

"Init"

]

},

{

"severity": "Message",

"time": 1523563779,

"messageId": "",

"message": "2 message(s), 2 warning(s), 0 error(s), 0 fatal error(s)"

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。