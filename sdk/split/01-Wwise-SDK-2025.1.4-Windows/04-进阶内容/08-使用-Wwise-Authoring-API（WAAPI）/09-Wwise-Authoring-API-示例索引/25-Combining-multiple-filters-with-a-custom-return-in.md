# Combining multiple filters with a custom return in the Media Pool

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Combining multiple filters with a custom return in the Media Pool

Searches the 'Project Originals' database for stereo files with 'wind' in the name, and returns their path and channel configuration.

# Function URI

[ak.wwise.core.mediaPool.get](ak_wwise_core_mediapool_get.html)

# Arguments

{

"searchText": "wind",

"databases": [

"\\Databases\\Project Originals"

],

"filters": [

{

"type": "field",

"field": "WAV/Channels",

"operator": "equals",

"value": 2

}

]

}

# Options

{

"return": [

"Path",

"WAV/Channel Configuration"

]

}

# Result

{

"return": [

{

"Path": "C:\\MyProject\\Originals\\SFX\\Ambiance\_Wind\_Stereo.wav",

"WAV/Channel Configuration": "2.0"

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。