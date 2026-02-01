# 定义对象的 Attenuation 曲线

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

定义对象的 Attenuation 曲线

通过设置一系列 "points" 来为 "object" 定义 "curveType" 类型的 Attenuation 曲线。

# 函数 URI

[ak.wwise.core.object.setAttenuationCurve](ak_wwise_core_object_setattenuationcurve.html)

# 参数

{

"object": "{A076AA65-B71A-45BB-8841-5A20C52CE727}",

"platform": "{66666666-7777-8888-9999-AAAAAAAAAAAA}",

"curveType": "VolumeDryUsage",

"use": "Custom",

"points": [

{

"x": 0,

"y": 0,

"shape": "Exp1"

},

{

"x": 8,

"y": -1,

"shape": "SCurve"

},

{

"x": 25,

"y": -2,

"shape": "Constant"

}

]

}

# 结果

{}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。