# Importing audio files and creating multiple Sound SFX

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Importing audio files and creating multiple Sound SFX

将由 "audioFile" 指定的文件导入到 "objectPath" 下。

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

"objectPath": "\\Containers\\Default Work Unit\\<Sequence Container>Test 0\\<Sound SFX>My SFX 0"

},

{

"audioFile": "C:\\audio1.wav",

"objectPath": "\\Containers\\Default Work Unit\\<Sequence Container>Test 0\\<Sound SFX>My SFX 1"

}

]

}

# 选项

{

"return": [

"id",

"name",

"path"

]

}

# 结果

{

"log": [],

"files": [

"C:\\Projects\\Example\\Originals\\SFX\\audio0.wav",

"C:\\Projects\\Example\\Originals\\SFX\\audio1.wav"

],

"objects": [

{

"id": "{A5B353C5-ED95-4CFB-B90F-1650BB4E57BA}",

"name": "Test 0",

"path": "\\Containers\\Default Work Unit\\Test 0"

},

{

"id": "{05D7495F-DC8F-4610-B485-91452F1DDC67}",

"name": "audio0",

"path": "\\Containers\\Default Work Unit\\Test 0\\My SFX 0\\audio0"

},

{

"id": "{04E3C1E5-119F-4530-930C-2F5B4095A750}",

"name": "My SFX 0",

"path": "\\Containers\\Default Work Unit\\Test 0\\My SFX 0"

},

{

"id": "{26019629-142E-4B07-A856-EBFE0758C64B}",

"name": "audio1",

"path": "\\Containers\\Default Work Unit\\Test 0\\My SFX 1\\audio1"

},

{

"id": "{1543FE94-E262-4F35-BAB2-F58519976469}",

"name": "My SFX 1",

"path": "\\Containers\\Default Work Unit\\Test 0\\My SFX 1"

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。