# Querying the CPU usage at a point in time.

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Querying the CPU usage at a point in time.

Queries the CPU usage in the current capture session at the latest capture time.

# 函数 URI

[ak.wwise.core.profiler.getCpuUsage](ak_wwise_core_profiler_getcpuusage.html)

# 参数

{

"time": "capture"

}

# 结果

{

"return": [

{

"elementName": "Interactive Music",

"id": 52494344,

"instances": 1,

"percentInclusive": 0.1809375137090683,

"percentExclusive": 0.001875000074505806,

"millisecondsInclusive": 0.019300000742077827,

"millisecondsExclusive": 0.00019999999494757503,

"type": "Global Extension"

},

{

"elementName": "Meter",

"id": 8454147,

"instances": 3,

"percentInclusive": 0.1678125113248825,

"percentExclusive": 0.1678125113248825,

"millisecondsInclusive": 0.017899999395012856,

"millisecondsExclusive": 0.017899999395012856,

"type": "Effect"

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。