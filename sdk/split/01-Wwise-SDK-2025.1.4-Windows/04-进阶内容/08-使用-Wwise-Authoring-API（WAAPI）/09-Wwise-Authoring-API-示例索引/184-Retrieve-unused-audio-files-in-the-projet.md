# Retrieve unused audio files in the projet

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Retrieve unused audio files in the projet

Return the path of audio files that are not used by a Wwise object.

# 函数 URI

[ak.wwise.core.sourceControl.getSourceFiles](ak_wwise_core_sourcecontrol_getsourcefiles.html)

# 参数

{

"filter": "unused"

}

# 选项

{

"return": [

"file"

]

}

# 结果

{

"return": [

{

"file": "SFX\\1.wav"

},

{

"file": "SFX\\2.wav"

},

{

"file": "Voices\\English(US)\\3.wav"

},

{

"file": "Voices\\Klingon\\4.wav"

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。