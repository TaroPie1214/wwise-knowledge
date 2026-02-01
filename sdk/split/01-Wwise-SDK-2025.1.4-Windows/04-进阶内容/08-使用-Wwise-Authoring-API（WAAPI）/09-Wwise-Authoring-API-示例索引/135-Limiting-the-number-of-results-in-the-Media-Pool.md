# Limiting the number of results in the Media Pool

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Limiting the number of results in the Media Pool

Searches for 'footstep' but limits the returned results to the first 3 matches.

# Function URI

[ak.wwise.core.mediaPool.get](ak_wwise_core_mediapool_get.html)

# Arguments

{

"searchText": "footstep",

"maxResults": 3

}

# Result

{

"return": [

{

"Path": "C:\\WAV\\FootStep\\Concrete\\Concrete\_Footstep\_01.wav",

"FileId": "{E7A5D7C1-3B8F-4B7B-8E2E-1A2B3C4D5E6F}",

"Db": {

"id": "{D8CFE25E-5600-4120-86BD-9079EFA32F98}",

"name": "FootStep"

}

},

{

"Path": "C:\\WAV\\FootStep\\Concrete\\Concrete\_Footstep\_02.wav",

"FileId": "{32A1B2C3-4D5E-6F7A-8B9C-D0E1F2A3B4C5}",

"Db": {

"id": "{D8CFE25E-5600-4120-86BD-9079EFA32F98}",

"name": "FootStep"

}

},

{

"Path": "C:\\WAV\\FootStep\\Concrete\\Concrete\_Footstep\_03.wav",

"FileId": "{F3B9A1C5-8A7D-4C6E-9F3A-2B1C8D7E6F5A}",

"Db": {

"id": "{D8CFE25E-5600-4120-86BD-9079EFA32F98}",

"name": "FootStep"

}

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。