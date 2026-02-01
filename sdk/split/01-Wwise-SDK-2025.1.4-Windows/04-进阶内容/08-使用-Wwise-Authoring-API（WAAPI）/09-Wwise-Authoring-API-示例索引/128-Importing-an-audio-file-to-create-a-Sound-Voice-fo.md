# Importing an audio file to create a Sound Voice for French

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Importing an audio file to create a Sound Voice for French

Imports files using an absolute objectPath and specifying the French language.

# 函数 URI

[ak.wwise.core.audio.import](ak_wwise_core_audio_import.html)

# 参数

{

"importOperation": "useExisting",

"default": {

"importLanguage": "French"

},

"imports": [

{

"objectPath": "\\Containers\\Default Work Unit\\<Sound Voice>MyVoice",

"audioFile": "C:\\sources\\fr\\Hello.wav"

}

]

}

# 选项

{}

# 结果

{

"log": [],

"files": [

"C:\\Projects\\Example\\Originals\\Voices\\French\\Hello.wav"

],

"objects": [

{

"id": "{7DF60F07-6254-4F05-B36C-C74446FBEEA6}",

"name": "Hello"

},

{

"id": "{BB1BC7DA-92BE-49F5-A27C-CDDEFBF38AAC}",

"name": "MyVoice"

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。