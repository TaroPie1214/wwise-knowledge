# AkStreamMgrModule.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)

[类](#nested-classes) |
[命名空间](#namespaces)

AkStreamMgrModule.h 文件参考

`#include <AK/SoundEngine/Common/IAkStreamMgr.h>`  
`#include <AK/Tools/Common/AkPlatformFuncs.h>`

[浏览源代码.](_ak_stream_mgr_module_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [AkStreamMgrSettings](struct_ak_stream_mgr_settings.html) |
|  | |
| struct | [AkDeviceSettings](struct_ak_device_settings.html) |
|  | |
| struct | [AkFileDesc](struct_ak_file_desc.html) |
|  | |
| struct | [AkIOTransferInfo](struct_ak_i_o_transfer_info.html) |
|  | |
| struct | [AkAsyncIOTransferInfo](struct_ak_async_i_o_transfer_info.html) |
|  | |
| struct | [AkAsyncFileOpenData](struct_ak_async_file_open_data.html) |
|  | |
| struct | [AkIoHeuristics](struct_ak_io_heuristics.html) |
|  | |
| class | [AK::StreamMgr::IAkLowLevelIOHook](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook.html) |
|  | |
| struct | [AK::StreamMgr::IAkLowLevelIOHook::BatchIoTransferItem](struct_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_1_1_batch_io_transfer_item.html) |
|  | |
| class | [AK::StreamMgr::IAkFileLocationResolver](class_a_k_1_1_stream_mgr_1_1_i_ak_file_location_resolver.html) |
|  | |

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |
|  | [AK::StreamMgr](namespace_a_k_1_1_stream_mgr.html) |
|  | Audiokinetic Stream Manager's implementation-specific interfaces of the Low-Level IO submodule. |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| Audiokinetic Stream Manager's implementation-specific definitions. | |
| typedef void(\* | [AkIOCallback](_ak_stream_mgr_module_8h_a3e66cb4516ec856e0b7d3f6ba45994e0.html#a3e66cb4516ec856e0b7d3f6ba45994e0)) ([AkAsyncIOTransferInfo](struct_ak_async_i_o_transfer_info.html) \*in\_pTransferInfo, [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) in\_eResult) |
|  | |
| typedef void(\* | [AkFileOpenCallback](_ak_stream_mgr_module_8h_ae00967344e3fcd553d8cdf391ec7081e.html#ae00967344e3fcd553d8cdf391ec7081e)) ([AkAsyncFileOpenData](struct_ak_async_file_open_data.html) \*in\_pOpenInfo, [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) in\_eResult) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| Audiokinetic implementation-specific Stream Manager factory. | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) IAkStreamMgr \* | [AK::StreamMgr::Create](namespace_a_k_1_1_stream_mgr_af9d67dd0e502e5603a2921099916e2ab.html#af9d67dd0e502e5603a2921099916e2ab) (const [AkStreamMgrSettings](struct_ak_stream_mgr_settings.html) &in\_settings) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::StreamMgr::GetDefaultSettings](namespace_a_k_1_1_stream_mgr_a50fe8111fcb883651390fab6e9dc5ebc.html#a50fe8111fcb883651390fab6e9dc5ebc) ([AkStreamMgrSettings](struct_ak_stream_mgr_settings.html) &out\_settings) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) IAkFileLocationResolver \* | [AK::StreamMgr::GetFileLocationResolver](namespace_a_k_1_1_stream_mgr_a3eaf614a2b462502a3db60de24a5437f.html#a3eaf614a2b462502a3db60de24a5437f) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::StreamMgr::SetFileLocationResolver](namespace_a_k_1_1_stream_mgr_ab5c2340963ac5ff81e49969b74ef2520.html#ab5c2340963ac5ff81e49969b74ef2520) (IAkFileLocationResolver \*in\_pFileLocationResolver) |
|  | |
| Stream Manager: High-level I/O devices management. | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [AK::StreamMgr::CreateDevice](namespace_a_k_1_1_stream_mgr_a64a22d377d25137222fbb66ff21965d5.html#a64a22d377d25137222fbb66ff21965d5) (const [AkDeviceSettings](struct_ak_device_settings.html) &in\_settings, IAkLowLevelIOHook \*in\_pLowLevelHook, [AkDeviceID](_ak_typedefs_8h_a9fb6f04697979f304a7b2b4f405e8260.html#a9fb6f04697979f304a7b2b4f405e8260) &out\_idDevice) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [AK::StreamMgr::DestroyDevice](namespace_a_k_1_1_stream_mgr_a6af0f503def99f59b5ed7c903d919106.html#a6af0f503def99f59b5ed7c903d919106) ([AkDeviceID](_ak_typedefs_8h_a9fb6f04697979f304a7b2b4f405e8260.html#a9fb6f04697979f304a7b2b4f405e8260) in\_deviceID) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [AK::StreamMgr::PerformIO](namespace_a_k_1_1_stream_mgr_aa81e51d0e246da5f66cff7a48ee472df.html#aa81e51d0e246da5f66cff7a48ee472df) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::StreamMgr::GetDefaultDeviceSettings](namespace_a_k_1_1_stream_mgr_a7d01e09a9bb6b6d34c2bb8f4c8995214.html#a7d01e09a9bb6b6d34c2bb8f4c8995214) ([AkDeviceSettings](struct_ak_device_settings.html) &out\_settings) |
|  | |
| Stream Manager: Cache management. | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::StreamMgr::FlushAllCaches](namespace_a_k_1_1_stream_mgr_a21b35b7883d840236c1551b9a3503462.html#a21b35b7883d840236c1551b9a3503462) () |
|  | |

|  |  |
| --- | --- |
| Language management. | |
| typedef void(\* | [AK::StreamMgr::AkLanguageChangeHandler](namespace_a_k_1_1_stream_mgr_af6f6b78cad5ec68a1adc59cb5c98b452.html#af6f6b78cad5ec68a1adc59cb5c98b452)) (const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*const in\_pLanguageName, void \*in\_pCookie) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [AK::StreamMgr::SetCurrentLanguage](namespace_a_k_1_1_stream_mgr_ae4820886baae734dd90177a49a2be1eb.html#ae4820886baae734dd90177a49a2be1eb) (const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*in\_pszLanguageName) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \* | [AK::StreamMgr::GetCurrentLanguage](namespace_a_k_1_1_stream_mgr_ae24e1f8b35b501eaa97599d5d6e48cc1.html#ae24e1f8b35b501eaa97599d5d6e48cc1) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [AK::StreamMgr::AddLanguageChangeObserver](namespace_a_k_1_1_stream_mgr_af547235acd8c151e6bf461f59e5a8eb7.html#af547235acd8c151e6bf461f59e5a8eb7) (AkLanguageChangeHandler in\_handler, void \*in\_pCookie) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK::StreamMgr::RemoveLanguageChangeObserver](namespace_a_k_1_1_stream_mgr_a3663c4a818dbe536665a4e216b8e8424.html#a3663c4a818dbe536665a4e216b8e8424) (void \*in\_pCookie) |
|  | |

## 详细描述

Audiokinetic's implementation-specific definitions and factory of overridable Stream Manager module. Contains the default Stream Manager's implementation-specific interfaces that altogether constitute the Low-Level I/O submodule. This submodule needs to be implemented by the game. All I/O requests generated by the Stream Manager end up to one of the I/O hooks defined herein. Read [Low-Level I/O](streamingmanager_lowlevel.html) to learn more about the Low-Level I/O.

在文件 [AkStreamMgrModule.h](_ak_stream_mgr_module_8h_source.html) 中定义.