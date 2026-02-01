# 获取对象的 Attenuation 曲线

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

获取对象的 Attenuation 曲线

从由 "object" 指定的对象获取 "curve"。

# 函数 URI

[ak.wwise.core.object.getAttenuationCurve](ak_wwise_core_object_getattenuationcurve.html)

# 参数

{

"object": "{A076AA65-B71A-45BB-8841-5A20C52CE727}",

"platform": "{66666666-7777-8888-9999-AAAAAAAAAAAA}",

"curveType": "VolumeDryUsage"

}

# 结果

{

"curveType": "VolumeDryUsage",

"points": [

{

"shape": "Exp3",

"x": 0,

"y": 0

},

{

"shape": "SCurve",

"x": 30,

"y": -3

},

{

"shape": "Log1",

"x": 60,

"y": -5

},

{

"shape": "Linear",

"x": 100,

"y": -200

}

],

"use": "Custom"

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。