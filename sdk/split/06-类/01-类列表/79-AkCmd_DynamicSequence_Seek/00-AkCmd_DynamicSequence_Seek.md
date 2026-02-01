# AkCmd_DynamicSequence_Seek

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___dynamic_sequence___seek-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_DynamicSequence\_Seek结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) | [playingID](struct_ak_cmd___dynamic_sequence___seek_ad7fb5aa96e4f6ecbf499203b3c8b0300.html#ad7fb5aa96e4f6ecbf499203b3c8b0300) |
|  | Playing ID that was used to open the dynamic sequence [更多...](struct_ak_cmd___dynamic_sequence___seek_ad7fb5aa96e4f6ecbf499203b3c8b0300.html#ad7fb5aa96e4f6ecbf499203b3c8b0300) |
|  | |
| union { |
| [AkTimeMs](_ak_typedefs_8h_a8a4d0aa5dba6f9922d6b7b3e48958b24.html#a8a4d0aa5dba6f9922d6b7b3e48958b24)   [absolute](struct_ak_cmd___dynamic_sequence___seek_abd24c938411bfe8b573cee9c728566df.html#abd24c938411bfe8b573cee9c728566df) |
|  | Desired position where playback should restart, in milliseconds [更多...](union_ak_cmd___dynamic_sequence___seek_1_1_0d1_a9a95502b60f6a10d6f17fda733a741ad.html#a9a95502b60f6a10d6f17fda733a741ad) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98)   [relative](struct_ak_cmd___dynamic_sequence___seek_a1d6c6b45f79c815350fba070ff58df16.html#a1d6c6b45f79c815350fba070ff58df16) |
|  | Desired position where playback should restart, expressed in a percentage of the file's total duration, between 0 and 1.f (see note above about infinite looping sounds) [更多...](union_ak_cmd___dynamic_sequence___seek_1_1_0d1_ac3d32dacdea1c413776c9c1cf61992d7.html#ac3d32dacdea1c413776c9c1cf61992d7) |
|  | |
| } | [position](struct_ak_cmd___dynamic_sequence___seek_aa44976d165621300a16b28de5950a9fa.html#aa44976d165621300a16b28de5950a9fa) |
|  | |
| [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) | [isPositionRelative](struct_ak_cmd___dynamic_sequence___seek_ac00f6686f15d13eac0ef9f230f0672aa.html#ac00f6686f15d13eac0ef9f230f0672aa) |
|  | Determines whether the position should be interpreted as absolute (milliseconds) or relative (%). [更多...](struct_ak_cmd___dynamic_sequence___seek_ac00f6686f15d13eac0ef9f230f0672aa.html#ac00f6686f15d13eac0ef9f230f0672aa) |
|  | |
| [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) | [seekToNearestMarker](struct_ak_cmd___dynamic_sequence___seek_a9bad1bde79e717116420d02f2a2c3a6c.html#a9bad1bde79e717116420d02f2a2c3a6c) |
|  | If non-zero, the final seeking position will be made equal to the nearest marker (see note above) [更多...](struct_ak_cmd___dynamic_sequence___seek_a9bad1bde79e717116420d02f2a2c3a6c.html#a9bad1bde79e717116420d02f2a2c3a6c) |
|  | |

## 详细描述

Seek inside specified Dynamic Sequence. It is only possible to seek in the first item of the sequence. If you seek past the duration of the first item, it will be skipped and an error will reported in the Capture Log and debug output. All the other items in the sequence will continue to play normally.

This command can fail for the following reasons:

- AK\_InvalidParameter: `playingID` is an invalid ID.
- AK\_IDNotFound: `playingID` is valid but does not refer to an active dynamic sequence.

参见
:   - [AkCommand\_DynamicSequence\_Seek](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda063663ffa99f8efc9e4762af684c329a "See AkCmd_DynamicSequence_Seek")
    - [AkCmd\_DynamicSequence\_Open](struct_ak_cmd___dynamic_sequence___open.html)
    - [AK::SoundEngine::DynamicSequence::Seek](namespace_a_k_1_1_sound_engine_1_1_dynamic_sequence_a46c6c751e936d15f1c75434d3319395f.html#a46c6c751e936d15f1c75434d3319395f)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [840](_ak_command_types_8h_source.html#l00840) 行定义.