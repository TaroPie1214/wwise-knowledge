# Creating a Music Playlist Container with segment and playlist

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Creating a Music Playlist Container with segment and playlist

Creates a new Music Playlist Container, import a wav file in a Music Segment and create a playlist.

# Function URI

[ak.wwise.core.object.set](ak_wwise_core_object_set.html)

# Arguments

{

"objects": [

{

"object": "\\Containers\\Default Work Unit",

"children": [

{

"type": "MusicPlaylistContainer",

"name": "MySequence",

"children": [

{

"type": "MusicSegment",

"name": "Segment1",

"import": {

"files": [

{

"audioFile": "C:\\wave\\music.wav"

}

]

}

}

],

"@PlaylistRoot": {

"type": "MusicPlaylistItem",

"name": "",

"children": [

{

"type": "MusicPlaylistItem",

"name": "",

"@PlaylistItemType": 1,

"@Segment": "\\Containers\\Default Work Unit\\MySequence\\Segment1"

}

]

}

}

]

}

],

"onNameConflict": "merge",

"listMode": "replaceAll"

}

# Options

{}

# Result

{

"objects": [

{

"id": "{78C8AE0D-6F8F-4FD3-BF65-436C7647C433}",

"name": "Default Work Unit",

"children": [

{

"id": "{8719EFDC-914D-4E95-9017-3DE5A0000E8E}",

"name": "MySequence",

"children": [

{

"id": "{69CA2921-725B-4D1D-BD7E-2674E70B9CA7}",

"name": "Segment1",

"import": {

"objects": [

{

"id": "{C736DC34-45A9-463F-AAD3-80503B1EAD9F}",

"name": "music"

}

],

"logs": [

{

"message": "Finalizing Importation...",

"severity": "Message"

}

]

}

}

],

"@PlaylistRoot": {

"id": "{97E6D2CD-940D-4CF1-9D41-32FC626711B5}",

"name": "",

"children": [

{

"id": "{DA859307-B176-46E8-8A8A-98D359667C49}",

"name": ""

}

]

}

}

]

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。