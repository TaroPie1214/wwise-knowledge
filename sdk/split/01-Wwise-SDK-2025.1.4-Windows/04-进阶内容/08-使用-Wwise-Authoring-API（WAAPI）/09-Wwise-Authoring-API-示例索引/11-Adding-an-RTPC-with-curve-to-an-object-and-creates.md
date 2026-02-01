# Adding an RTPC with curve to an object and creates a new Custom ControlInput

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Adding an RTPC with curve to an object and creates a new Custom ControlInput

在对象的 "RTPC" 列表中，使用给定 ControlInput 和曲线控制点在属性上创建 RTPC。

# 函数 URI

[ak.wwise.core.object.set](ak_wwise_core_object_set.html)

# 参数

{

"objects": [

{

"object": "{BAE891BA-E025-43ED-A4D1-4DC55C68E7CA}",

"@RTPC": [

{

"type": "RTPC",

"name": "",

"@Curve": {

"type": "Curve",

"points": [

{

"x": 0,

"y": -20.82785,

"shape": "Linear"

},

{

"x": 1000,

"y": 21.8509,

"shape": "Linear"

}

]

},

"notes": "a new rtpc",

"@PropertyName": "OutputBusVolume",

"@ControlInput": {

"type": "ModulatorTime",

"name": "TimeMod",

"@TimeModDuration": 5,

"@EnvelopeStopPlayback": false

}

}

]

}

]

}

# 选项

{

"return": [

"id",

"name",

"type",

"@Curve"

]

}

# 结果

{

"objects": [

{

"id": "{BAE891BA-E025-43ED-A4D1-4DC55C68E7CA}",

"name": "Sound",

"@RTPC": [

{

"id": "{31DA7AE1-B215-4689-A5F7-67A9C5B3DFDC}",

"name": "",

"type": "RTPC",

"@Curve": {

"id": "{676ECEEC-9FF5-46CD-B2C7-A6D5C9370620}",

"points": [

{

"x": 0,

"y": -20.82785,

"shape": "Linear"

},

{

"x": 1000,

"y": 21.8509,

"shape": "Linear"

}

]

},

"@ControlInput": {

"id": "{2D7084B6-2AA7-45B0-94B4-4976E886627A}",

"name": "TimeMod"

}

}

]

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。