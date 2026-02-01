# Importing an audio file to create a Sound SFX using a relative object path

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Importing an audio file to create a Sound SFX using a relative object path

Imports files using the importLocation, a relative objectPath, and an objectType.

# 函数 URI

[ak.wwise.core.audio.import](ak_wwise_core_audio_import.html)

# 参数

{

"importOperation": "useExisting",

"default": {

"importLanguage": "SFX",

"importLocation": "\\Containers\\Default Work Unit"

},

"imports": [

{

"audioFile": "C:\\audio0.wav",

"objectPath": "MySound",

"objectType": "Sound SFX"

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

"id": "{5EF24DFF-B9EC-4042-BF49-EC27B1135FB0}",

"name": "audio0"

},

{

"id": "{EB3051A3-5611-4608-AB5C-0EA3F9C3DD6C}",

"name": "MySound"

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。