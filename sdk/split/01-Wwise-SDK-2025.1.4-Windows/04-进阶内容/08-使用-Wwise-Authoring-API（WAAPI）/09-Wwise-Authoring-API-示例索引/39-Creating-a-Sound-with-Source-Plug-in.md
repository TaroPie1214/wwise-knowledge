# Creating a Sound with Source Plug-in

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Creating a Sound with Source Plug-in

Creates a new Sound with a Synth One Source Plug-in.

# Function URI

[ak.wwise.core.object.set](ak_wwise_core_object_set.html)

# Arguments

{

"objects": [

{

"object": "\\Containers\\Default Work Unit",

"children": [

{

"type": "Sound",

"name": "MySynthOne",

"children": [

{

"type": "SourcePlugin",

"name": "SynthOne",

"classId": 9699330,

"@BaseFrequency": 100,

"@Osc1Waveform": 0,

"@Osc2Waveform": 1

}

]

}

]

}

],

"onNameConflict": "merge"

}

# Options

{}

# Result

{

"objects": [

{

"id": "{8D358F4E-6BF1-4C72-9EE7-5B1A53C69E1B}",

"name": "Default Work Unit",

"children": [

{

"id": "{32E53900-803E-4067-8F65-E32D8B32CCDB}",

"name": "MySynthOne",

"children": [

{

"id": "{0B743757-7744-4393-8E2A-D65793CDDD6D}",

"name": "SynthOne"

}

]

}

]

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。