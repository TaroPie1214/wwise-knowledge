# AkSourcePosition

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_source_position-members.html) |
[Public 属性](#pub-attribs)

AkSourcePosition结构体 参考

Return values for GetSourcePlayPositions.
[更多...](struct_ak_source_position.html#details)

`#include <AkSoundEngine.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [audioNodeID](struct_ak_source_position_ad3dd64472f42b8e642a0db79875f6df8.html#ad3dd64472f42b8e642a0db79875f6df8) |
|  | Audio Node ID of playing item [更多...](struct_ak_source_position_ad3dd64472f42b8e642a0db79875f6df8.html#ad3dd64472f42b8e642a0db79875f6df8) |
|  | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [mediaID](struct_ak_source_position_ad63dd5872cfc571382ac735c004ffe6d.html#ad63dd5872cfc571382ac735c004ffe6d) |
|  | Media ID of playing item. (corresponds to 'ID' attribute of 'File' element in SoundBank metadata file) [更多...](struct_ak_source_position_ad63dd5872cfc571382ac735c004ffe6d.html#ad63dd5872cfc571382ac735c004ffe6d) |
|  | |
| [AkTimeMs](_ak_typedefs_8h_a8a4d0aa5dba6f9922d6b7b3e48958b24.html#a8a4d0aa5dba6f9922d6b7b3e48958b24) | [msTime](struct_ak_source_position_a30235ea47138745532b6f047e414264a.html#a30235ea47138745532b6f047e414264a) |
|  | Position of the source (in ms) associated with that playing item [更多...](struct_ak_source_position_a30235ea47138745532b6f047e414264a.html#a30235ea47138745532b6f047e414264a) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [samplePosition](struct_ak_source_position_a3bf9a03fb61a1fdf7e63188a7e81d2f8.html#a3bf9a03fb61a1fdf7e63188a7e81d2f8) |
|  | Position of the source (in samples) associated with that playing item [更多...](struct_ak_source_position_a3bf9a03fb61a1fdf7e63188a7e81d2f8.html#a3bf9a03fb61a1fdf7e63188a7e81d2f8) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [updateBufferTick](struct_ak_source_position_aebb6afab5d0bc5d05f3ab7fd10ec7a5e.html#aebb6afab5d0bc5d05f3ab7fd10ec7a5e) |
|  | Value of [GetBufferTick()](namespace_a_k_1_1_sound_engine_a8d4ce557eb5262a36140c26ccfb93fde.html#a8d4ce557eb5262a36140c26ccfb93fde) at the time the position was updated [更多...](struct_ak_source_position_aebb6afab5d0bc5d05f3ab7fd10ec7a5e.html#aebb6afab5d0bc5d05f3ab7fd10ec7a5e) |
|  | |

## 详细描述

Return values for GetSourcePlayPositions.

在文件 [AkSoundEngine.h](_ak_sound_engine_8h_source.html) 第 [251](_ak_sound_engine_8h_source.html#l00251) 行定义.