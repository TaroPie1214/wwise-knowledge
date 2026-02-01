# Querying the Loaded Media at a point in time.

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Querying the Loaded Media at a point in time.

Queries the active Loaded Media in the current capture session at the latest capture time.

# 函数 URI

[ak.wwise.core.profiler.getLoadedMedia](ak_wwise_core_profiler_getloadedmedia.html)

# 参数

{

"time": "capture"

}

# 结果

{

"return": [

{

"mediaId": 34223551,

"fileName": "mySound1.wav",

"format": "ptADPCM",

"size": 1745238,

"soundBank": "mySoundBank1"

},

{

"mediaId": 66326472,

"fileName": "mySound2.wav",

"format": "VORBIS",

"size": 36522,

"soundBank": "mySoundBank2"

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。