# Filtering files by duration in the Media Pool

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Filtering files by duration in the Media Pool

Retrieves audio files that are longer than 5 seconds.

# Function URI

[ak.wwise.core.mediaPool.get](ak_wwise_core_mediapool_get.html)

# Arguments

{

"filters": [

{

"type": "field",

"field": "WAV/Duration",

"operator": "greaterThan",

"value": 5

}

]

}

# Result

{

"return": [

{

"Path": "C:\\WAV\\Ambiance\\Ambiance\_Forest\_Long.wav",

"FileId": "{A1B2C3D4-5678-9012-3456-789012345678}",

"Db": {

"id": "{12345678-ABCD-EFGH-IJKL-MNOPQRSTUVWX}",

"name": "Ambiance"

}

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。