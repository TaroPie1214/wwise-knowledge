# Finding files by audio similarity in the Media Pool

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Finding files by audio similarity in the Media Pool

Searches for audio files that sound similar to a specified file.

# Function URI

[ak.wwise.core.mediaPool.get](ak_wwise_core_mediapool_get.html)

# Arguments

{

"filters": [

{

"type": "audioSimilarity",

"value": "C:\\WAV\\FootStep\\Reference\\Wood\_Creak\_Reference.wav",

"weight": 1.0

}

]

}

# Result

{

"return": [

{

"Path": "C:\\WAV\\Foley\\Wood\_Creak\_01.wav",

"FileId": "{CDEF1234-5678-90AB-CDEF-1234567890AB}",

"Db": {

"id": "{B9A8C7E6-D5F4-A3B2-C1E0-F9A8B7C6D5E4}",

"name": "Foley"

}

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。