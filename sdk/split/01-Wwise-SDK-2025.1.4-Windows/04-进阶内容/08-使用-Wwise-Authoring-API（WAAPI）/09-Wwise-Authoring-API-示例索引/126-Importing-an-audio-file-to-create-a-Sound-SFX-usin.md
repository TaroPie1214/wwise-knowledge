# Importing an audio file to create a Sound SFX using an absolute object path

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Importing an audio file to create a Sound SFX using an absolute object path

Imports files using an absolute objectPath that includes the object type.

# 函数 URI

[ak.wwise.core.audio.import](ak_wwise_core_audio_import.html)

# 参数

{

"importOperation": "useExisting",

"default": {

"importLanguage": "SFX"

},

"imports": [

{

"audioFile": "C:\\audio0.wav",

"objectPath": "\\Containers\\Default Work Unit\\<Sound SFX>MySound"

}

]

}

# 选项

{}

# 结果

{

"log": [],

"files": [

"C:\\Projects\\Example\\Originals\\SFX\\audio0.wav"

],

"objects": [

{

"id": "{FAF8DDCD-D1B2-4EC6-997F-CB9BE9703544}",

"name": "audio0"

},

{

"id": "{5F444FD2-1203-4205-B8FA-F9DAB3F5F74C}",

"name": "MySound"

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。