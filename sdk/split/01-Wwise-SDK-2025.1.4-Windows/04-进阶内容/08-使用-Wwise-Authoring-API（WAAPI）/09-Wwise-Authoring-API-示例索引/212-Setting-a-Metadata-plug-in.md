# Setting a Metadata plug-in

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Setting a Metadata plug-in

Sets the Metadata of a Sound to a newly created Wwise System Output Settings plug-in.

# Function URI

[ak.wwise.core.object.set](ak_wwise_core_object_set.html)

# Arguments

{

"objects": [

{

"object": "\\Containers\\Default Work Unit\\MySound",

"@Metadata": [

{

"type": "MetadataSlot",

"name": "",

"@Metadata": {

"type": "Metadata",

"name": "myCustomMetadata",

"classId": 58982409,

"@Mix": 1

}

}

]

}

]

}

# Options

{}

# Result

{

"objects": [

{

"id": "{5BA74442-2DEC-4370-AD70-97FC17EBF05D}",

"name": "MySound",

"@Metadata": [

{

"id": "{3891F5A9-6DB9-4C26-A84C-03E93121DD76}",

"name": "",

"@Metadata": {

"id": "{5B759989-53F7-4355-944D-C2C604927D18}",

"name": "myCustomMetadata"

}

}

]

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。