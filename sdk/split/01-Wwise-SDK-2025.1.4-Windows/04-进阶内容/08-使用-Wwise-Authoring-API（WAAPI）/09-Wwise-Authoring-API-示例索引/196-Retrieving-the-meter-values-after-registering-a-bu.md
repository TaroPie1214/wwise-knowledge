# Retrieving the meter values after registering a bus for meter

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Retrieving the meter values after registering a bus for meter

Gets the meter values for all registered busses. In this example, one of the busses is configured in 7.1 and is registered with [ak.wwise.core.profiler.registerMeter](ak_wwise_core_profiler_registermeter.html).

# 函数 URI

[ak.wwise.core.profiler.getMeters](ak_wwise_core_profiler_getmeters.html)

# 参数

{

"time": "capture"

}

# 结果

{

"meters": [

{

"object": {

"id": "{1514A4D8-1DA6-412A-A17E-75CA0C2149F3}",

"name": "Main Audio Bus"

},

"source": "Bus",

"channels": [

{

"name": "L",

"value": 0.00794849544763565

},

{

"name": "R",

"value": -764.6162109375

}

],

"configurationType": "Standard",

"configurationMask": 3,

"configurationName": "2.0"

},

{

"object": {

"id": "{0DE372C2-4E96-4096-9E61-781BC76313F3}",

"name": "Bus"

},

"source": "Bus",

"channels": [

{

"name": "L",

"value": 0.00794849544763565

},

{

"name": "R",

"value": -764.6162109375

},

{

"name": "C",

"value": -764.6162109375

},

{

"name": "BL",

"value": -764.6162109375

},

{

"name": "BR",

"value": -764.6162109375

},

{

"name": "SL",

"value": -764.6162109375

},

{

"name": "SR",

"value": -764.6162109375

},

{

"name": "LFE",

"value": -764.6162109375

}

],

"configurationType": "Standard",

"configurationMask": 1599,

"configurationName": "7.1"

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。