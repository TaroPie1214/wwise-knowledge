# Querying the Performance Monitor at a point in time.

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Querying the Performance Monitor at a point in time.

Queries the Performance Monitor Counters in the current capture session at the latest capture time. For the purposes of this example only a subset of the returned counters are displayed.

# 函数 URI

[ak.wwise.core.profiler.getPerformanceMonitor](ak_wwise_core_profiler_getperformancemonitor.html)

# 参数

{

"time": "capture"

}

# 结果

{

"return": [

{

"name": "cpuTotal",

"id": "CpuTotal",

"value": 2.21

},

{

"name": "voicesPhysical",

"id": "VoicesPhysical",

"value": 1

},

{

"name": "voicesTotal",

"id": "VoicesTotal",

"value": 2

},

{

"name": "Number of Transitions/Interpolations",

"id": "ActiveTransitions",

"value": 1

},

{

"name": "outputPeak",

"id": "OutputPeak",

"value": -37.5

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。