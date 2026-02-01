# AkMusicPlaylistCallbackInfo

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_music_playlist_callback_info-members.html) |
[Public 属性](#pub-attribs)

AkMusicPlaylistCallbackInfo结构体 参考

`#include <AkCallbackTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [playlistID](struct_ak_music_playlist_callback_info_a4015338108567c652d091d526a694775.html#a4015338108567c652d091d526a694775) |
|  | ID of playlist node [更多...](struct_ak_music_playlist_callback_info_a4015338108567c652d091d526a694775.html#a4015338108567c652d091d526a694775) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uNumPlaylistItems](struct_ak_music_playlist_callback_info_adef75376a27daf80e948ecc7d2c20eb8.html#adef75376a27daf80e948ecc7d2c20eb8) |
|  | Number of items in playlist node (may be segments or other playlists) [更多...](struct_ak_music_playlist_callback_info_adef75376a27daf80e948ecc7d2c20eb8.html#adef75376a27daf80e948ecc7d2c20eb8) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uPlaylistSelection](struct_ak_music_playlist_callback_info_a21553360a102b37444487bfe6b7f8f90.html#a21553360a102b37444487bfe6b7f8f90) |
|  | Selection: set by sound engine, modified by callback function (if not in range 0 <= uPlaylistSelection < uNumPlaylistItems then ignored). [更多...](struct_ak_music_playlist_callback_info_a21553360a102b37444487bfe6b7f8f90.html#a21553360a102b37444487bfe6b7f8f90) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uPlaylistItemDone](struct_ak_music_playlist_callback_info_a2d245ddc4450970aa843904cf5faf474.html#a2d245ddc4450970aa843904cf5faf474) |
|  | Playlist node done: set by sound engine, modified by callback function (if set to anything but 0 then the current playlist item is done, and uPlaylistSelection is ignored) [更多...](struct_ak_music_playlist_callback_info_a2d245ddc4450970aa843904cf5faf474.html#a2d245ddc4450970aa843904cf5faf474) |
|  | |

## 详细描述

Callback information structure corresponding to [AK\_MusicPlaylistSelect](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732aec46a37d9cfdef25777042feaf56e265). Called when a music playlist container must select its next item to play. The members uPlaylistSelection and uPlaylistItemDone are set by the sound engine before the callback function call. They are set to the next item selected by the sound engine. They are to be modified by the callback function if the selection is to be changed.

参见
:   - [集成详情——事件](soundengine_events.html)
    - [AK::SoundEngine::PostEvent()](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e)
    - [集成详情——音乐回调](soundengine_music_callbacks.html)

在文件 [AkCallbackTypes.h](_ak_callback_types_8h_source.html) 第 [248](_ak_callback_types_8h_source.html#l00248) 行定义.