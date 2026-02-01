# Importing a MIDI file into a Music Segment to create a Music Track

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Importing a MIDI file into a Music Segment to create a Music Track

Creates a Music Segment from the imported MIDI file. A Music Track and a Music Clip are also created.

# 函数 URI

[ak.wwise.core.object.set](ak_wwise_core_object_set.html)

# 参数

{

"objects": [

{

"object": "\\Containers\\Default Work Unit",

"children": [

{

"type": "MusicSegment",

"name": "New Segment",

"import": {

"files": [

{

"audioFile": "c:\\path\\music.mid"

}

]

}

}

]

}

],

"onNameConflict": "merge"

}

# Options

{

"return": [

"id",

"name",

"type"

]

}

# 结果

{

"objects": [

{

"children": [

{

"id": "{3B6C9C17-1F33-40DB-80EF-9509C5358334}",

"import": {

"logs": [

{

"message": "Finalizing Importation...",

"severity": "Message"

}

],

"objects": [

{

"id": "{E69EBE64-BE37-4E37-90A1-5B3FBE6BDA8C}",

"name": "music",

"type": "MidiFileSource"

},

{

"id": "{9E1729C9-AAD9-4B07-8640-8B4C9CB6CEA3}",

"name": "music",

"type": "MusicClipMidi"

},

{

"id": "{A114365D-1393-4429-9823-12B11A7755DC}",

"name": "music",

"type": "MusicTrack"

}

]

},

"name": "New Segment",

"type": "MusicSegment"

}

],

"id": "{6128CF6C-DE55-4E1C-A582-BD27EAD90A13}",

"name": "Default Work Unit"

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。