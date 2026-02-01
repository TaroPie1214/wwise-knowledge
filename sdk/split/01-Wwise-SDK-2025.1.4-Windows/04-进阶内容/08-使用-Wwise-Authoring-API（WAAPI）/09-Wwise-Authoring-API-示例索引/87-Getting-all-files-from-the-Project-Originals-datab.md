# Getting all files from the Project Originals database

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Getting all files from the Project Originals database

Query the media with Project Originals database id.

# Function URI

[ak.wwise.core.mediaPool.get](ak_wwise_core_mediapool_get.html)

# Arguments

{

"databases": [

"\\Databases\\Project Originals"

]

}

# Result

{

"return": [

{

"Path": "C:\\MyProject\\Originals\\SFX\\Concrete\_Footstep\_01.wav",

"FileId": "{2392B2A9-D4A0-4395-A867-57AE8901BC13}",

"Db": {

"id": "{D8CFE25E-5600-4120-86BD-9079EFA32F98}",

"name": "Project Originals"

}

},

{

"Path": "C:\\MyProject\\Originals\\SFX\\Concrete\_Footstep\_02.wav",

"FileId": "{A460921E-24BF-45E1-A934-2336419AF936}",

"Db": {

"id": "{D8CFE25E-5600-4120-86BD-9079EFA32F98}",

"name": "Project Originals"

}

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。