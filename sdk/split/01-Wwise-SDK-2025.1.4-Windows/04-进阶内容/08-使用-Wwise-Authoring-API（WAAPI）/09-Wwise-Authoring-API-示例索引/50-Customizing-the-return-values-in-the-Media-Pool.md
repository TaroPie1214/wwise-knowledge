# Customizing the return values in the Media Pool

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Customizing the return values in the Media Pool

Searches for files and returns only their filename, duration, and sample rate.

# Function URI

[ak.wwise.core.mediaPool.get](ak_wwise_core_mediapool_get.html)

# Arguments

{

"searchText": "Gun"

}

# Options

{

"return": [

"Filename",

"WAV/Duration",

"WAV/Sample Rate"

]

}

# Result

{

"return": [

{

"Filename": "Gun\_Shot\_01.wav",

"WAV/Duration": 0.85,

"WAV/Sample Rate": 48000

},

{

"Filename": "Gun\_Shot\_02.wav",

"WAV/Duration": 0.92,

"WAV/Sample Rate": 48000

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。