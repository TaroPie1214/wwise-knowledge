# Importing two WAV files into a Music Segment to create two Music Tracks

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Importing two WAV files into a Music Segment to create two Music Tracks

Creates a Music Segment, and imports two WAV files. Two new Music Tracks and two Music Clips are also created.

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

"name": "MultiTrack Segment",

"import": {

"files": [

{

"audioFile": "c:\\path\\track1.wav"

},

{

"audioFile": "c:\\path\\track2.wav"

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

"id": "{7367EE35-EF2E-4EBC-81AC-6B7C23260BF2}",

"import": {

"logs": [

{

"message": "Finalizing Importation...",

"severity": "Message"

}

],

"objects": [

{

"id": "{DB365588-EDE7-4DF3-8473-9DE29F78B077}",

"name": "track1",

"type": "AudioFileSource"

},

{

"id": "{A07D6617-1275-4CC4-BE37-953F97165052}",

"name": "track1",

"type": "MusicClip"

},

{

"id": "{8CE8D07A-F7E0-4A6E-9FD8-1CD2A2B7BBA3}",

"name": "track1",

"type": "MusicTrack"

},

{

"id": "{6D7EE38E-A8B7-4A90-B7B5-EED543C0B396}",

"name": "track2",

"type": "AudioFileSource"

},

{

"id": "{69598206-96C0-48E3-B6D1-01492BDD805F}",

"name": "track2",

"type": "MusicClip"

},

{

"id": "{D9CCB1A3-FAF7-46F8-A14C-18679F78B56E}",

"name": "track2",

"type": "MusicTrack"

}

]

},

"name": "MultiTrack Segment",

"type": "MusicSegment"

}

],

"id": "{6128CF6C-DE55-4E1C-A582-BD27EAD90A13}",

"name": "Default Work Unit"

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。