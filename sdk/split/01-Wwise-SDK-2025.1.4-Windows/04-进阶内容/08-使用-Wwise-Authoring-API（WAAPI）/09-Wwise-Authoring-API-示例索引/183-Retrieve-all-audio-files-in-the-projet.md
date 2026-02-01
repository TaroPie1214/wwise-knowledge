# Retrieve all audio files in the projet

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Retrieve all audio files in the projet

Return the absolute path of audio files that are not used by a Wwise object and all folders under the Originals folder.

# 函数 URI

[ak.wwise.core.sourceControl.getSourceFiles](ak_wwise_core_sourcecontrol_getsourcefiles.html)

# 参数

{}

# 选项

{}

# 结果

{

"return": [

{

"folder": "SFX"

},

{

"file": "SFX\\1.wav",

"isUsed": true,

"isMissing": false,

"usage": [

{

"id": "{80BD7970-696A-4358-8D8C-22F3CF8AAAEE}",

"name": "1"

}

]

},

{

"file": "SFX\\2.wav",

"isUsed": true,

"isMissing": false,

"usage": [

{

"id": "{68D8CE8A-6DA9-4271-ACA2-63115C14E065}",

"name": "2"

}

]

},

{

"file": "SFX\\A.wav",

"isUsed": false,

"isMissing": false

},

{

"folder": "Voices"

},

{

"folder": "Voices\\English(US)"

},

{

"file": "Voices\\English(US)\\3.wav",

"isUsed": true,

"isMissing": false,

"usage": [

{

"id": "{97735FC6-A17E-4662-AC77-6E78178D7B03}",

"name": "3"

}

]

},

{

"folder": "Voices\\Klingon"

},

{

"file": "Voices\\Klingon\\4.wav",

"isUsed": true,

"isMissing": false,

"usage": [

{

"id": "{B96F7F61-1EE5-468E-9150-075B5B24CF81}",

"name": "4"

}

]

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。