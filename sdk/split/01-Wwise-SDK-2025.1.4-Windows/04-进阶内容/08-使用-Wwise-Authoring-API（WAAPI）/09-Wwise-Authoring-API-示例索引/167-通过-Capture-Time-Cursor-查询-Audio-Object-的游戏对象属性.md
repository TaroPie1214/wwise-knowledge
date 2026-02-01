# 通过 Capture Time Cursor 查询 Audio Object 的游戏对象属性

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

通过 Capture Time Cursor 查询 Audio Object 的游戏对象属性

指定 Capture Time Cursor 作为处理调用时捕获会话的最新时间来查询 Audio Object。

# 函数 URI

[ak.wwise.core.profiler.getAudioObjects](ak_wwise_core_profiler_getaudioobjects.html)

# 参数

{

"time": "capture"

}

# 选项

{

"return": [

"gameObjectID",

"gameObjectName"

]

}

# 结果

{

"return": [

{

"gameObjectID": 18446744073709551614,

"gameObjectName": "Transport/Soundcaster"

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。