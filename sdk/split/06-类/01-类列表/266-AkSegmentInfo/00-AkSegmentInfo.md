# AkSegmentInfo

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_segment_info-members.html) |
[Public 属性](#pub-attribs)

AkSegmentInfo结构体 参考

Structure used to query info on active playing segments.
[更多...](struct_ak_segment_info.html#details)

`#include <AkCallbackTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkTimeMs](_ak_typedefs_8h_a8a4d0aa5dba6f9922d6b7b3e48958b24.html#a8a4d0aa5dba6f9922d6b7b3e48958b24) | [iCurrentPosition](struct_ak_segment_info_abd153aaf7f8b8051edd4ae77eaef5f0a.html#abd153aaf7f8b8051edd4ae77eaef5f0a) |
|  | Current position of the segment, relative to the Entry Cue, in milliseconds. Range is [-iPreEntryDuration, iActiveDuration+iPostExitDuration]. [更多...](struct_ak_segment_info_abd153aaf7f8b8051edd4ae77eaef5f0a.html#abd153aaf7f8b8051edd4ae77eaef5f0a) |
|  | |
| [AkTimeMs](_ak_typedefs_8h_a8a4d0aa5dba6f9922d6b7b3e48958b24.html#a8a4d0aa5dba6f9922d6b7b3e48958b24) | [iPreEntryDuration](struct_ak_segment_info_a00e9ffef0699192566eef35bd71fe8c0.html#a00e9ffef0699192566eef35bd71fe8c0) |
|  | Duration of the pre-entry region of the segment, in milliseconds. [更多...](struct_ak_segment_info_a00e9ffef0699192566eef35bd71fe8c0.html#a00e9ffef0699192566eef35bd71fe8c0) |
|  | |
| [AkTimeMs](_ak_typedefs_8h_a8a4d0aa5dba6f9922d6b7b3e48958b24.html#a8a4d0aa5dba6f9922d6b7b3e48958b24) | [iActiveDuration](struct_ak_segment_info_a87524e4b8057eed861cb5cf28daa191f.html#a87524e4b8057eed861cb5cf28daa191f) |
|  | Duration of the active region of the segment (between the Entry and Exit Cues), in milliseconds. [更多...](struct_ak_segment_info_a87524e4b8057eed861cb5cf28daa191f.html#a87524e4b8057eed861cb5cf28daa191f) |
|  | |
| [AkTimeMs](_ak_typedefs_8h_a8a4d0aa5dba6f9922d6b7b3e48958b24.html#a8a4d0aa5dba6f9922d6b7b3e48958b24) | [iPostExitDuration](struct_ak_segment_info_aca30811b8d8a98014c29af8dc8ee0fd5.html#aca30811b8d8a98014c29af8dc8ee0fd5) |
|  | Duration of the post-exit region of the segment, in milliseconds. [更多...](struct_ak_segment_info_aca30811b8d8a98014c29af8dc8ee0fd5.html#aca30811b8d8a98014c29af8dc8ee0fd5) |
|  | |
| [AkTimeMs](_ak_typedefs_8h_a8a4d0aa5dba6f9922d6b7b3e48958b24.html#a8a4d0aa5dba6f9922d6b7b3e48958b24) | [iRemainingLookAheadTime](struct_ak_segment_info_aa8a045be6bea052ee47a4e858da249f8.html#aa8a045be6bea052ee47a4e858da249f8) |
|  | Number of milliseconds remaining in the "looking-ahead" state of the segment, when it is silent but streamed tracks are being prefetched. [更多...](struct_ak_segment_info_aa8a045be6bea052ee47a4e858da249f8.html#aa8a045be6bea052ee47a4e858da249f8) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fBeatDuration](struct_ak_segment_info_ac0bea178854d658f960cf56f457ec5f0.html#ac0bea178854d658f960cf56f457ec5f0) |
|  | Beat Duration in seconds. [更多...](struct_ak_segment_info_ac0bea178854d658f960cf56f457ec5f0.html#ac0bea178854d658f960cf56f457ec5f0) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fBarDuration](struct_ak_segment_info_a2c3fcde1ce2e98ab906f6644550168e4.html#a2c3fcde1ce2e98ab906f6644550168e4) |
|  | Bar Duration in seconds. [更多...](struct_ak_segment_info_a2c3fcde1ce2e98ab906f6644550168e4.html#a2c3fcde1ce2e98ab906f6644550168e4) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fGridDuration](struct_ak_segment_info_a37334524bf8eca39e946714821d9b997.html#a37334524bf8eca39e946714821d9b997) |
|  | Grid duration in seconds. [更多...](struct_ak_segment_info_a37334524bf8eca39e946714821d9b997.html#a37334524bf8eca39e946714821d9b997) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [fGridOffset](struct_ak_segment_info_a5e998af5b9a0c9742a84f6c060e9f9bd.html#a5e998af5b9a0c9742a84f6c060e9f9bd) |
|  | Grid offset in seconds. [更多...](struct_ak_segment_info_a5e998af5b9a0c9742a84f6c060e9f9bd.html#a5e998af5b9a0c9742a84f6c060e9f9bd) |
|  | |

## 详细描述

Structure used to query info on active playing segments.

在文件 [AkCallbackTypes.h](_ak_callback_types_8h_source.html) 第 [141](_ak_callback_types_8h_source.html#l00141) 行定义.