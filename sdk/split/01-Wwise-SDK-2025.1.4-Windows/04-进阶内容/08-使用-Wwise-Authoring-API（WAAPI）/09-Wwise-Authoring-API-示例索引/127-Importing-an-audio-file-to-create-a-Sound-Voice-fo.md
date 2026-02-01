# Importing an audio file to create a Sound Voice for English

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Importing an audio file to create a Sound Voice for English

Imports files using an absolute objectPath and specifying the English language.

# 函数 URI

[ak.wwise.core.audio.import](ak_wwise_core_audio_import.html)

# 参数

{

"importOperation": "useExisting",

"default": {

"importLanguage": "English(US)"

},

"imports": [

{

"objectPath": "\\Containers\\Default Work Unit\\<Sound Voice>MyVoice",

"audioFile": "C:\\sources\\en\\Hello.wav"

}

]

}

# 选项

{}

# 结果

{

"log": [],

"files": [

"C:\\Projects\\Example\\Originals\\Voices\\English(US)\\Hello.wav"

],

"objects": [

{

"id": "{AFEC4890-A037-4AB6-A96B-F4C7C4B7FAA0}",

"name": "Hello"

},

{

"id": "{C624F4A4-305A-462F-8FFE-C234FDB0771B}",

"name": "MyVoice"

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。