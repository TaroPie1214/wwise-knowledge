# Creating a music hierarchy

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Creating a music hierarchy

In one operation, create a Music Switch Container, a Music Playlist Container, a Music Segment, and a Music Track with one imported WAV file.

# 函数 URI

[ak.wwise.core.object.set](ak_wwise_core_object_set.html)

# 参数

{

"objects": [

{

"object": "\\Switches\\Default Work Unit",

"children": [

{

"type": "SwitchGroup",

"name": "MySwitchGroup",

"children": [

{

"type": "Switch",

"name": "Switch1",

"children": []

}

]

}

]

},

{

"object": "\\Containers\\Default Work Unit",

"children": [

{

"type": "MusicSwitchContainer",

"name": "MyMusicSwitchContainer",

"@Arguments": [

{

"type": "MusicArgumentsSlot",

"name": "",

"@Argument": "\\Switches\\Default Work Unit\\MySwitchGroup"

}

],

"@Entries": [

{

"type": "MultiSwitchEntry",

"name": "",

"@EntryPath": [

{

"type": "EntryPathSlot",

"name": "",

"@EntryPathObject": "\\Switches\\Default Work Unit\\MySwitchGroup\\Switch1"

}

],

"@AudioNode": "\\Containers\\Default Work Unit\\MyMusicSwitchContainer\\MyMusicPlaylistContainer",

"children": []

}

],

"children": [

{

"type": "MusicPlaylistContainer",

"name": "MyMusicPlaylistContainer",

"@PlaylistRoot": {

"type": "MusicPlaylistItem",

"name": "",

"@LoopCount": 0,

"children": [

{

"type": "MusicPlaylistItem",

"name": "",

"@Segment": "\\Containers\\Default Work Unit\\MyMusicSwitchContainer\\MyMusicPlaylistContainer\\MySegment",

"@PlaylistItemType": 1,

"children": []

}

]

},

"children": [

{

"type": "MusicSegment",

"name": "MySegment",

"children": [

{

"type": "MusicTrack",

"name": "MyMusicTrack",

"import": {

"files": [

{

"audioFile": "C:\\SFX\_400.wav"

}

]

}

}

]

}

]

}

]

}

]

}

],

"onNameConflict": "merge",

"listMode": "replaceAll"

}

# 结果

{

"objects": [

{

"id": "{6F067572-23CF-4E99-962B-562B441CB4CA}",

"name": "Default Work Unit",

"children": [

{

"id": "{0641A054-EE2C-480B-A25C-71D64FE5D232}",

"name": "MySwitchGroup",

"children": [

{

"id": "{70B9E9D1-D61F-4355-8E95-447C842249CA}",

"name": "Switch1"

}

]

}

]

},

{

"id": "{0E873F51-7FAA-419A-882C-041C140E5498}",

"name": "Default Work Unit",

"children": [

{

"id": "{C49874C1-497D-4A7E-99F1-0B9C959DFDBE}",

"name": "MyMusicSwitchContainer",

"children": [

{

"id": "{7A8F2FA4-6D97-46CA-8F23-ED40C223759B}",

"name": "MyMusicPlaylistContainer",

"children": [

{

"id": "{D4DB8A92-5DAD-43BD-A428-F38DCA0049D3}",

"name": "MySegment",

"children": [

{

"id": "{ED751B21-54C8-43E4-9A10-E7FB2F41E4F4}",

"name": "MyMusicTrack",

"import": {

"objects": [

{

"id": "{0755079B-46C1-4B41-B1EB-BEAE5DB06629}",

"name": "SFX\_400"

}

],

"logs": [

{

"severity": "Message",

"message": "Finalizing Importation..."

}

]

}

}

]

}

],

"@PlaylistRoot": {

"id": "{7F61EF00-6470-4C71-8ABD-7645AA3CF2B0}",

"name": "",

"children": [

{

"id": "{C134EC33-DD74-4C08-B687-9CF9D6C75327}",

"name": ""

}

]

}

}

],

"@Arguments": [

{}

],

"@Entries": [

{

"id": "{06F963DC-169C-464B-92FB-7ABB303852DA}",

"name": "",

"@EntryPath": [

{}

]

}

]

}

]

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。