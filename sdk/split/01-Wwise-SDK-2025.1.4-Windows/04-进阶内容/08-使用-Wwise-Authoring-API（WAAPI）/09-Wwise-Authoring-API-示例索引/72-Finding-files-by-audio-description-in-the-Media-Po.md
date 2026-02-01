# Finding files by audio description in the Media Pool

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Finding files by audio description in the Media Pool

Searches for files that match the description 'a powerful explosion with debris'.

# Function URI

[ak.wwise.core.mediaPool.get](ak_wwise_core_mediapool_get.html)

# Arguments

{

"filters": [

{

"type": "audioDescription",

"value": "a powerful explosion with debris",

"weight": 0.8

}

]

}

# Result

{

"return": [

{

"Path": "C:\\WAV\\Explosions\\Explosion\_Large\_01.wav",

"FileId": "{98765432-10FE-DCBA-9876-543210FEDCBA}",

"Db": {

"id": "{FEDCBA98-7654-3210-FEDC-BA9876543210}",

"name": "Explosions"

}

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。