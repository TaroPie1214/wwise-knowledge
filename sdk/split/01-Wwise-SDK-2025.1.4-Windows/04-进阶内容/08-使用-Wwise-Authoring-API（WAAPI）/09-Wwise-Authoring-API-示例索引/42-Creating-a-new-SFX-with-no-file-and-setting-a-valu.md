# Creating a new SFX with no file and setting a value to a property

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Creating a new SFX with no file and setting a value to a property

在 "objectPath" 下创建新的 SFX，将其音量属性设为 1。

# 函数 URI

[ak.wwise.core.audio.import](ak_wwise_core_audio_import.html)

# 参数

{

"importOperation": "createNew",

"default": {},

"imports": [

{

"importLanguage": "SFX",

"@Volume": "1",

"objectPath": "\\Containers\\Default Work Unit\\<Property Container>Test 0\\<Sequence Container>Container 0\\<Sound SFX>Sound 0"

}

]

}

# 结果

{

"log": [],

"files": [],

"objects": [

{

"name": "Test 0",

"id": "{47EF0874-4C86-4DB6-A63B-4411A1EA766E}"

},

{

"name": "Container 0",

"id": "{E9AD319F-BCC3-43C0-9645-851B758A86FD}"

},

{

"name": "Sound 0",

"id": "{692C77EB-7542-4AE9-A56A-ADB9D4CE0008}"

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。