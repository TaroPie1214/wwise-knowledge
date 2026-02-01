# Importing an audio files to create Sound Voices for English and French

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Importing an audio files to create Sound Voices for English and French

Imports files using an absolute objectPath and specifying the language for each entry.

# 函数 URI

[ak.wwise.core.audio.import](ak_wwise_core_audio_import.html)

# 参数

{

"importOperation": "useExisting",

"imports": [

{

"audioFile": "C:\\sources\\hello\_en.wav",

"objectPath": "\\Containers\\Default Work Unit\\<Sound Voice>hello\\<AudioFileSource>hello\_en",

"importLanguage": "EN\_US"

},

{

"audioFile": "C:\\sources\\hello\_fr.wav",

"objectPath": "\\Containers\\Default Work Unit\\<Sound Voice>hello\\<AudioFileSource>hello\_fr",

"importLanguage": "FR\_CA"

}

]

}

# 选项

{}

# 结果

{

"log": [],

"files": [

"C:\\Projects\\Example\\Originals\\Voices\\EN\_US\\hello\_en.wav",

"C:\\Projects\\Example\\Originals\\Voices\\FR\_CA\\hello\_fr.wav"

],

"objects": [

{

"id": "{1F2EDC6F-416D-4FDF-98E9-8359C63E6CFC}",

"name": "hello"

},

{

"id": "{F54A8C00-4777-4E71-BD1B-5E2E4E6504A1}",

"name": "hello\_en"

},

{

"id": "{308B215B-DDF3-4E42-8646-33A6FB485093}",

"name": "hello\_fr"

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。