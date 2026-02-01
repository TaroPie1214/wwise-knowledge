# 获取有关 RTPC 的信息

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

获取有关 RTPC 的信息

使用属性/引用访问器 @ 获取 RTPC 的 "PropertyName" 属性及 "ControlInput" 和 "Curve" 引用。

# 函数 URI

[ak.wwise.core.object.get](ak_wwise_core_object_get.html)

# 参数

{

"waql": "\"{67A2C1B5-4FBF-4938-A86C-4AEE7E84822A}\""

}

# 选项

{

"return": [

"type",

"path",

"@PropertyName",

"@ControlInput",

"@Curve"

]

}

# 结果

{

"return": [

{

"@ControlInput": {

"id": "{4CCB066B-FB7D-4894-9D07-1C42D28E3256}",

"name": "Modulator Time (Custom)"

},

"@Curve": {

"id": "{AFECA9AF-21D9-4CC0-81E4-19A7264934EF}",

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

},

"@PropertyName": "MidiVelocityOffset",

"path": "\\Containers\\Default Work Unit\\RTPC\_TEST\\[RTPC: Velocity Offset, Modulator Time (Custom)]",

"type": "RTPC"

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。