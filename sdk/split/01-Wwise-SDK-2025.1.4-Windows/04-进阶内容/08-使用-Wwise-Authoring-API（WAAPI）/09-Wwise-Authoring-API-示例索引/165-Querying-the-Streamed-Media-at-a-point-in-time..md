# Querying the Streamed Media at a point in time.

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Querying the Streamed Media at a point in time.

Queries the active Streamed Media in the current capture session at the latest capture time.

# 函数 URI

[ak.wwise.core.profiler.getStreamedMedia](ak_wwise_core_profiler_getstreamedmedia.html)

# 参数

{

"time": "capture"

}

# 结果

{

"return": [

{

"active": true,

"bandwidthLowLevel": 235177,

"bandwidthTotal": 235177,

"bufferStatusBuffered": 92.05678,

"deviceName": "Win32 Deferred",

"estimatedThroughput": 192000,

"filePosition": 34.843780517578125,

"fileSize": 2304044,

"priority": 50,

"referencedMemory": 65536,

"streamName": "1517878592",

"targetBufferSize": 38400

},

{

"active": true,

"bandwidthLowLevel": 235177,

"bandwidthTotal": 235177,

"bufferStatusBuffered": 100.0,

"deviceName": "Win32 Deferred",

"estimatedThroughput": 192000,

"filePosition": 12.670619010925293,

"fileSize": 6336044,

"priority": 50,

"referencedMemory": 65536,

"streamName": "1517868960",

"targetBufferSize": 38400

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。