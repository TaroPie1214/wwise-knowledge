# Importing a WAV file into a Convolution Reverb effect plug-in

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Importing a WAV file into a Convolution Reverb effect plug-in

Creates a Sound and a Convolution Reverb effect plug-in, then imports a WAV file as an impulse response.

# 函数 URI

[ak.wwise.core.object.set](ak_wwise_core_object_set.html)

# 参数

{

"objects": [

{

"object": "\\Containers\\Default Work Unit",

"children": [

{

"type": "Sound",

"name": "Reverb",

"@Effects": [

{

"type": "EffectSlot",

"name": "",

"@Effect": {

"type": "Effect",

"name": "Reverb",

"classId": 8323075,

"import": {

"files": [

{

"audioFile": "C:\\ImpulseResponse.wav"

}

]

}

}

}

],

"import": {

"files": [

{

"audioFile": "C:\\wave\\cues\\30.wav"

}

]

}

}

]

}

],

"onNameConflict": "merge"

}

# 结果

{

"objects": [

{

"id": "{88012962-D6A8-4400-BC86-DF1A5980EDFA}",

"name": "Default Work Unit",

"children": [

{

"id": "{2DF8A2CA-E676-4A66-B7D4-EEA3CEC818D7}",

"name": "Reverb",

"import": {

"objects": [

{

"id": "{B0110790-DB1A-4AFA-A0C2-A90E7350D441}",

"name": "30"

}

],

"logs": [

{

"severity": "Message",

"message": "Finalizing Importation..."

}

]

},

"@Effects": [

{

"id": "{494D2556-01CF-4E46-BC4E-5DA41CA1FF0D}",

"name": "",

"@Effect": {

"id": "{4349C021-EE84-4AA7-8D28-617B48DF1065}",

"name": "Reverb",

"import": {}

}

}

]

}

]

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。