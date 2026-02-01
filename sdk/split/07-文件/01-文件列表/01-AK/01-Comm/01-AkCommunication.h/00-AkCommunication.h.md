# AkCommunication.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Comm](dir_5e37e7a1868355c42d827f3b46c71c5e.html)

[类](#nested-classes) |
[命名空间](#namespaces) |
[宏定义](#define-members)

AkCommunication.h 文件参考

`#include <AK/SoundEngine/Common/AkTypes.h>`

[浏览源代码.](_ak_communication_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [AkCommSettings](struct_ak_comm_settings.html) |
|  | |
| struct | [AkCommSettings::Ports](struct_ak_comm_settings_1_1_ports.html) |
|  | |

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |
|  | [AK::Comm](namespace_a_k_1_1_comm.html) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AK\_COMM\_SETTINGS\_MAX\_STRING\_SIZE](_ak_communication_8h_a3e84d6265701ceaef4eac64092bec3d6.html#a3e84d6265701ceaef4eac64092bec3d6)   64 |
|  | |
| #define | [AK\_COMM\_SETTINGS\_MAX\_URL\_SIZE](_ak_communication_8h_a30507c06e3bdb32252d90713f50f5ab4.html#a30507c06e3bdb32252d90713f50f5ab4)   128 |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| Initialization | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [AK::Comm::Init](namespace_a_k_1_1_comm_a596691b552b507c26b4df958ee1c6de8.html#a596691b552b507c26b4df958ee1c6de8) (const [AkCommSettings](struct_ak_comm_settings.html) &in\_settings) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [AK::Comm::GetLastError](namespace_a_k_1_1_comm_ab257079d30e10185e37ca7e146b386b2.html#ab257079d30e10185e37ca7e146b386b2) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::Comm::GetDefaultInitSettings](namespace_a_k_1_1_comm_a3280f8b7ad6261d8b2a4bdf39c234fa7.html#a3280f8b7ad6261d8b2a4bdf39c234fa7) ([AkCommSettings](struct_ak_comm_settings.html) &out\_settings) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::Comm::Term](namespace_a_k_1_1_comm_a94e307d2974b89cc4fbc8ab0fef20d2f.html#a94e307d2974b89cc4fbc8ab0fef20d2f) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [AK::Comm::Reset](namespace_a_k_1_1_comm_af3d99fab833c0b3c4bc7ce7b78d7b4bf.html#af3d99fab833c0b3c4bc7ce7b78d7b4bf) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) const [AkCommSettings](struct_ak_comm_settings.html) & | [AK::Comm::GetCurrentSettings](namespace_a_k_1_1_comm_a77e4ce372728d84cceda483823c301d0.html#a77e4ce372728d84cceda483823c301d0) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AkUInt16](_ak_numeral_types_8h_a7100a9b0a3b01df7639c1dc512678219.html#a7100a9b0a3b01df7639c1dc512678219) | [AK::Comm::GetCommandPort](namespace_a_k_1_1_comm_a3dfcb1cbf75b7edd87277ea333893b44.html#a3dfcb1cbf75b7edd87277ea333893b44) () |
|  | |

## 详细描述

The main communication interface (between the in-game sound engine and authoring tool).

参见
:   - [通信初始化](workingwithsdks_initialization.html#initialization_comm)
    - [终止通信模块](workingwithsdks_termination.html#termination_comm)

在文件 [AkCommunication.h](_ak_communication_8h_source.html) 中定义.