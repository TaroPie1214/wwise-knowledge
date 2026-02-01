# 获取有关 Curve 的信息

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

获取有关 Curve 的信息

使用 "points" 访问器获取曲线的控制点。

# 函数 URI

[ak.wwise.core.object.get](ak_wwise_core_object_get.html)

# 参数

{

"waql": "\"{AFECA9AF-21D9-4CC0-81E4-19A7264934EF}\""

}

# 选项

{

"return": [

"id",

"name",

"points"

]

}

# 结果

{

"return": [

{

"id": "{AFECA9AF-21D9-4CC0-81E4-19A7264934EF}",

"name": "",

"points": [

{

"shape": "Linear",

"x": 0,

"y": -40

},

{

"shape": "Linear",

"x": 0.138,

"y": 114

},

{

"shape": "Linear",

"x": 0.40673,

"y": -148

},

{

"shape": "Linear",

"x": 0.77829,

"y": 162

},

{

"shape": "Linear",

"x": 1,

"y": -71

}

]

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。