# Adding a Metadata shareset to an existing Sound SFX

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Adding a Metadata shareset to an existing Sound SFX

Creates a Metadata entry in the Metadata object list inside an existing Sound SFX. The Metadata is a shareset with the specified GUID.

# Function URI

[ak.wwise.core.object.create](ak_wwise_core_object_create.html)

# Arguments

{

"name": "",

"parent": "\\Containers\\Default Work Unit\\MySound",

"type": "MetadataSlot",

"list": "Metadata",

"@Metadata": "{F3FCCECA-170B-4958-9CDF-14CE25C58EBC}"

}

# Result

{

"id": "{8E795E58-95F9-42F1-BB24-1D36283362A2}",

"name": ""

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。