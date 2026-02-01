# Importing a WAV file into a new Sound SFX and creating the associated Event

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Importing a WAV file into a new Sound SFX and creating the associated Event

Creates a new Sound object, imports a WAV file into it, and then creates an Event with a Play action on the Sound.

# 函数 URI

[ak.wwise.core.object.set](ak_wwise_core_object_set.html)

# 参数

{

"objects": [

{

"object": "\\Containers\\Import",

"children": [

{

"type": "Sound",

"name": "MySound",

"import": {

"files": [

{

"audioFile": "C:\\MySound.wav",

"originalsSubFolder": "SUB"

}

]

}

}

]

},

{

"object": "\\Events\\Default Work Unit",

"onNameConflict": "merge",

"children": [

{

"type": "Event",

"name": "Play\_MySound",

"children": [

{

"name": "",

"type": "Action",

"@ActionType": 1,

"@Target": "\\Containers\\Import\\MySound"

}

]

}

]

}

],

"onNameConflict": "merge",

"listMode": "replaceAll"

}

# 选项

{}

# 结果

{

"objects": [

{

"children": [

{

"id": "{4314DDF5-F4EB-477B-A414-DB724A3FC0CC}",

"import": {

"logs": [

{

"message": "Finalizing Importation...",

"severity": "Message"

}

],

"objects": [

{

"id": "{F72DD400-91D1-4305-B14E-31113A28FF1C}",

"name": "MySound"

}

]

},

"name": "MySound"

}

],

"id": "{64EE1D88-F322-4BD8-AA18-21852859CBCF}",

"name": "Import"

},

{

"children": [

{

"children": [

{

"id": "{8A8A7BC0-C62B-4986-BCCF-F98EFB92A697}",

"name": ""

}

],

"id": "{CAA381F1-A9C7-4846-AAFB-696C1C9F00F5}",

"name": "Play\_MySound"

}

],

"id": "{C1F6AE1D-03CF-448A-8DE9-EE25FC6F459C}",

"name": "Default Work Unit"

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。