# Getting all files from a specific database in the Media Pool

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Getting all files from a specific database in the Media Pool

Query the media with FootStep database id.

# Function URI

[ak.wwise.core.mediaPool.get](ak_wwise_core_mediapool_get.html)

# Arguments

{

"databases": [

"{4BAA7169-B669-4FDC-8711-4E80202396EC}"

]

}

# Result

{

"return": [

{

"Path": "C:\\WAV\\FootStep\\Concrete\\Concrete\_Footstep\_01.wav",

"FileId": "{06E33651-DBB1-414E-9771-4969C3A9EF6E}",

"Db": {

"id": "{4BAA7169-B669-4FDC-8711-4E80202396EC}",

"name": "FootStep"

}

},

{

"Path": "C:\\WAV\\FootStep\\Concrete\\Concrete\_Footstep\_02.wav",

"FileId": "{72FDEC4C-5E71-4551-8D74-C306E7BBF4B4}",

"Db": {

"id": "{4BAA7169-B669-4FDC-8711-4E80202396EC}",

"name": "FootStep"

}

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。