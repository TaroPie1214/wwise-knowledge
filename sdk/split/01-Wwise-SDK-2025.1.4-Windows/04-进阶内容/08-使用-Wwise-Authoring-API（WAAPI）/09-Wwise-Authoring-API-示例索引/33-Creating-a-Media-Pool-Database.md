# Creating a Media Pool Database

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Creating a Media Pool Database

Creates a Media Pool Database with the specified name and path to an audio file directory. The GUID for the `'User` Databases' folder is always `'{8452BD49-9264-4A56-A3BB-047FA7F119BE}'`.

# Function URI

[ak.wwise.core.object.set](ak_wwise_core_object_set.html)

# Arguments

{

"objects": [

{

"object": "\\Databases\\User Databases",

"children": [

{

"type": "MediaPoolDatabase",

"name": "FootSteps",

"@Paths": [

{

"type": "MediaPoolDatabasePath",

"name": "",

"@Path": "C:\\WAV\\FootSteps"

}

]

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

"id": "{8452BD49-9264-4A56-A3BB-047FA7F119BE}",

"name": "User Databases",

"children": [

{

"id": "{27497F4A-C9C9-4B68-A109-D54CC182D69A}",

"name": "FootSteps",

"@Paths": [

{

"id": "{7A5EE645-BE71-44E9-B535-5BAE8E027388}",

"name": ""

}

]

}

]

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。