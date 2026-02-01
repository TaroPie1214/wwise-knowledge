# Setting an effect plug-in

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Setting an effect plug-in

Sets the effects of a Sound to a newly created Custom RoomVerb Effect plug-in.

# 函数 URI

[ak.wwise.core.object.set](ak_wwise_core_object_set.html)

# 参数

{

"objects": [

{

"object": "\\Containers\\Default Work Unit\\MySound",

"@Effects": [

{

"type": "EffectSlot",

"name": "",

"@Effect": {

"type": "Effect",

"name": "myCustomEffect",

"classId": 7733251,

"@PreDelay": 24,

"@RoomShape": 99

}

}

]

}

]

}

# 选项

{}

# 结果

{

"objects": [

{

"id": "{5BA74442-2DEC-4370-AD70-97FC17EBF05D}",

"name": "MySound",

"@Effects": [

{

"id": "{3891F5A9-6DB9-4C26-A84C-03E93121DD76}",

"name": "",

"@Effect": {

"id": "{5B759989-53F7-4355-944D-C2C604927D18}",

"name": "myCustomEffect"

}

}

]

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。