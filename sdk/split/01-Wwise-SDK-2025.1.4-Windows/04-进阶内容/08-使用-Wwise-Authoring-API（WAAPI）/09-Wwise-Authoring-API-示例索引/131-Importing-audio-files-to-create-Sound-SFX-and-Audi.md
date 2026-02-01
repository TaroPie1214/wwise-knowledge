# Importing audio files to create Sound SFX and Audio File Sources

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Importing audio files to create Sound SFX and Audio File Sources

Imports files using an absolute objectPath that includes the object type for the Sound SFX and the Audio File Source.

# 函数 URI

[ak.wwise.core.audio.import](ak_wwise_core_audio_import.html)

# 参数

{

"importOperation": "replaceExisting",

"default": {

"importLanguage": "SFX"

},

"imports": [

{

"audioFile": "C:\\audio0.wav",

"objectPath": "\\Containers\\Default Work Unit\\<Sound SFX>MySound\\<AudioFileSource>\_MyActiveSource"

},

{

"audioFile": "C:\\audio1.wav",

"objectPath": "\\Containers\\Default Work Unit\\<Sound SFX>MySound\\<AudioFileSource>OtherSource"

}

]

}

# 选项

{}

# 结果

{

"log": [],

"files": [

"C:\\Projects\\Example\\Originals\\SFX\\audio0.wav",

"C:\\Projects\\Example\\Originals\\SFX\\audio1.wav"

],

"objects": [

{

"id": "{FC700D71-5AF1-4B43-A669-6D208591BDFD}",

"name": "MySound"

},

{

"id": "{5F3C304E-6BFF-47E2-9089-B4A17FB229B2}",

"name": "\_MyActiveSource"

},

{

"id": "{281AB61E-2D79-465B-B050-24986AACB2AF}",

"name": "OtherSource"

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。