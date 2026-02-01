# Adding an RTPC with curve to an object

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Adding an RTPC with curve to an object

In an object's "RTPC" list, this function creates an RTPC on a property using the specified `ControlInput` and curve points. The `ControlInput` is the game parameter, Modulator, or MIDI object assigned to the x axis of the RTPC. If you use a game parameter, you are passing a reference, and therefore the game parameter that you want to link to `ControlInput` must be created before you pass it to the parameter.

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

"@ControlInput": "{E31BAE21-CFA6-4655-81F6-E6FBDC802E9D}"

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

}

}

]

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。