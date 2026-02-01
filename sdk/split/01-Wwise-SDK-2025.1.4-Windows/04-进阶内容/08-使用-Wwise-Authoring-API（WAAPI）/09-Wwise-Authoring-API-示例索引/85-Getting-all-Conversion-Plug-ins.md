# Getting all Conversion Plug-ins

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Getting all Conversion Plug-ins

Using a WAQL query in order to retrieve all Conversion Plug-ins.

# 函数 URI

[ak.wwise.core.object.get](ak_wwise_core_object_get.html)

# 参数

{

"waql": "from type conversionplugin"

}

# 选项

{

"return": [

"pluginname",

"id",

"owner.name",

"classid"

]

}

# 结果

{

"return": [

{

"classid": 65537,

"id": "{F8FB3A88-AC84-4304-AD93-079C918B19F8}",

"owner.name": "",

"pluginname": "PCM"

},

{

"classid": 262145,

"id": "{D8F1A7CC-D727-4721-97C3-8911E3D0E979}",

"owner.name": "Vorbis Auto Detect Low",

"pluginname": "Vorbis"

},

{

"classid": 131073,

"id": "{6E4343A8-57F1-4E5C-8469-81424F6D8A44}",

"owner.name": "ADPCM Auto Detect Low",

"pluginname": "ADPCM"

},

{

"classid": 65537,

"id": "{58BB40C6-EA49-491A-AE33-F2B0675EEC25}",

"owner.name": "Default Conversion Settings",

"pluginname": "PCM"

},

{

"classid": 262145,

"id": "{EDA4F59A-7772-4880-ABB9-EBF5F02E62B8}",

"owner.name": "Vorbis Quality High",

"pluginname": "Vorbis"

},

{

"classid": 65537,

"id": "{AA79CD6E-0D44-46FC-B065-15F2D578473B}",

"owner.name": "PCM Auto Detect Low",

"pluginname": "PCM"

},

{

"classid": 65537,

"id": "{DFBA6F29-71B3-4AA9-B7F8-03CBF7D68F6A}",

"owner.name": "PCM Auto Detect High",

"pluginname": "PCM"

},

{

"classid": 131073,

"id": "{5162E037-D428-4CDF-B8BB-A5358EA69C5B}",

"owner.name": "ADPCM Auto Detect High",

"pluginname": "ADPCM"

},

{

"classid": 262145,

"id": "{84223C4C-D68C-4EC5-9C1D-A9B2594723F2}",

"owner.name": "Vorbis Quality Medium",

"pluginname": "Vorbis"

},

{

"classid": 262145,

"id": "{55B19A63-7CF0-49F3-A2A5-D8CC03866522}",

"owner.name": "Vorbis Quality Low",

"pluginname": "Vorbis"

},

{

"classid": 131073,

"id": "{341B0DE3-6BFD-4BDF-AB49-10B8EA37C99C}",

"owner.name": "ADPCM Auto Detect Medium",

"pluginname": "ADPCM"

},

{

"classid": 65537,

"id": "{8360D0D4-C19C-45FE-8A6E-48FBECA49488}",

"owner.name": "Conversion Settings",

"pluginname": "PCM"

},

{

"classid": 65537,

"id": "{603785B6-A9C6-42CC-911D-3B685E1B375C}",

"owner.name": "PCM As Input",

"pluginname": "PCM"

},

{

"classid": 131073,

"id": "{56CDDB68-9926-496A-80E6-4331F7C21FA9}",

"owner.name": "ADPCM As Input",

"pluginname": "ADPCM"

},

{

"classid": 262145,

"id": "{6AC8D0D1-B3A5-4A5E-B4BC-05B402BBD80C}",

"owner.name": "Vorbis Auto Detect Medium",

"pluginname": "Vorbis"

},

{

"classid": 262145,

"id": "{59A7F590-6819-4936-B63C-9A65C7A1444A}",

"owner.name": "Vorbis Auto Detect High",

"pluginname": "Vorbis"

},

{

"classid": 65537,

"id": "{53FF3BEB-600B-4FC4-88B2-0C527028B050}",

"owner.name": "PCM Auto Detect Medium",

"pluginname": "PCM"

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。