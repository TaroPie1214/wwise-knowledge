# 在某个时间点查询 Audio Object 的 Instigator ID (Pipeline ID)

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

在某个时间点查询 Audio Object 的 Instigator ID (Pipeline ID)

在当前捕获会话的 30 秒（30,000 毫秒）位置查询 Audio Object 的 Instigator ID (Pipeline ID)。

# 函数 URI

[ak.wwise.core.profiler.getAudioObjects](ak_wwise_core_profiler_getaudioobjects.html)

# 参数

{

"time": 30000

}

# 选项

{

"return": [

"audioObjectName"

]

}

# 结果

{

"return": [

{

"audioObjectName": "MyObject"

},

{

"audioObjectName": "MyOtherObject"

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。