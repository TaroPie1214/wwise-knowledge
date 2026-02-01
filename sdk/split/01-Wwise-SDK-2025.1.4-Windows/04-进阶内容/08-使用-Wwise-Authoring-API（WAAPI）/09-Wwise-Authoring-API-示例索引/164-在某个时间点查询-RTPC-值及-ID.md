# 在某个时间点查询 RTPC 值及 ID

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

在某个时间点查询 RTPC 值及 ID

在当前捕获会话的 30 秒（30,000 毫秒）位置查询活跃的 RTPC。

# 函数 URI

[ak.wwise.core.profiler.getRTPCs](ak_wwise_core_profiler_getrtpcs.html)

# 参数

{

"time": 30000

}

# 结果

{

"return": [

{

"id": "{8CCB75BA-256A-4C7B-907F-9BEB03689F56}",

"name": "Footstep\_weight",

"gameObjectId": 10,

"value": 50

},

{

"id": "{1FEAF6CE-113A-49F2-BCAA-9AFDDE35ADA5}",

"name": "Footstep\_speed",

"gameObjectId": 11,

"value": 5

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。