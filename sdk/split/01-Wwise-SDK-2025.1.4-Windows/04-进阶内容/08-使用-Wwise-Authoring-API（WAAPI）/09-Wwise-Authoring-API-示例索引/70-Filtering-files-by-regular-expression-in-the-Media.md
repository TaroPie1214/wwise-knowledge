# Filtering files by regular expression in the Media Pool

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Filtering files by regular expression in the Media Pool

Retrieves all files ending with '\_01.wav' or '\_02.wav' using a regex filter on the filename.

# Function URI

[ak.wwise.core.mediaPool.get](ak_wwise_core_mediapool_get.html)

# Arguments

{

"filters": [

{

"type": "field",

"field": "Filename",

"operator": "matchesRegex",

"value": ".\*\_0[12]\\.wav$"

}

]

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

"Path": "C:\\WAV\\Weapons\\Gun\_Shot\_02.wav",

"FileId": "{B2C3D4E5-F6A7-B8C9-D0E1-F2A3B4C5D6E7}",

"Db": {

"id": "{ABCDEF12-3456-7890-ABCD-EF1234567890}",

"name": "Weapons"

}

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。