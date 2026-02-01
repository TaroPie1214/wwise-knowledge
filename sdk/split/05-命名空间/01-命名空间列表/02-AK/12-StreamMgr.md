# StreamMgr

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [StreamMgr](namespace_a_k_1_1_stream_mgr.html)

[类](#nested-classes)

AK::StreamMgr 命名空间参考

Audiokinetic Stream Manager's implementation-specific interfaces of the Low-Level IO submodule.
[更多...](namespace_a_k_1_1_stream_mgr.html#details)

|  |  |
| --- | --- |
| 类 | |
| class | [IAkFileLocationResolver](class_a_k_1_1_stream_mgr_1_1_i_ak_file_location_resolver.html) |
|  | |
| class | [IAkLowLevelIOHook](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook.html) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| Audiokinetic implementation-specific Stream Manager factory. | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [IAkStreamMgr](class_a_k_1_1_i_ak_stream_mgr.html) \* | [Create](namespace_a_k_1_1_stream_mgr_af9d67dd0e502e5603a2921099916e2ab.html#af9d67dd0e502e5603a2921099916e2ab) (const [AkStreamMgrSettings](struct_ak_stream_mgr_settings.html) &in\_settings) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [GetDefaultSettings](namespace_a_k_1_1_stream_mgr_a50fe8111fcb883651390fab6e9dc5ebc.html#a50fe8111fcb883651390fab6e9dc5ebc) ([AkStreamMgrSettings](struct_ak_stream_mgr_settings.html) &out\_settings) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [IAkFileLocationResolver](class_a_k_1_1_stream_mgr_1_1_i_ak_file_location_resolver.html) \* | [GetFileLocationResolver](namespace_a_k_1_1_stream_mgr_a3eaf614a2b462502a3db60de24a5437f.html#a3eaf614a2b462502a3db60de24a5437f) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [SetFileLocationResolver](namespace_a_k_1_1_stream_mgr_ab5c2340963ac5ff81e49969b74ef2520.html#ab5c2340963ac5ff81e49969b74ef2520) ([IAkFileLocationResolver](class_a_k_1_1_stream_mgr_1_1_i_ak_file_location_resolver.html) \*in\_pFileLocationResolver) |
|  | |
| Stream Manager: High-level I/O devices management. | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [CreateDevice](namespace_a_k_1_1_stream_mgr_a64a22d377d25137222fbb66ff21965d5.html#a64a22d377d25137222fbb66ff21965d5) (const [AkDeviceSettings](struct_ak_device_settings.html) &in\_settings, [IAkLowLevelIOHook](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook.html) \*in\_pLowLevelHook, [AkDeviceID](_ak_typedefs_8h_a9fb6f04697979f304a7b2b4f405e8260.html#a9fb6f04697979f304a7b2b4f405e8260) &out\_idDevice) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [DestroyDevice](namespace_a_k_1_1_stream_mgr_a6af0f503def99f59b5ed7c903d919106.html#a6af0f503def99f59b5ed7c903d919106) ([AkDeviceID](_ak_typedefs_8h_a9fb6f04697979f304a7b2b4f405e8260.html#a9fb6f04697979f304a7b2b4f405e8260) in\_deviceID) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [PerformIO](namespace_a_k_1_1_stream_mgr_aa81e51d0e246da5f66cff7a48ee472df.html#aa81e51d0e246da5f66cff7a48ee472df) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [GetDefaultDeviceSettings](namespace_a_k_1_1_stream_mgr_a7d01e09a9bb6b6d34c2bb8f4c8995214.html#a7d01e09a9bb6b6d34c2bb8f4c8995214) ([AkDeviceSettings](struct_ak_device_settings.html) &out\_settings) |
|  | |
| Stream Manager: Cache management. | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [FlushAllCaches](namespace_a_k_1_1_stream_mgr_a21b35b7883d840236c1551b9a3503462.html#a21b35b7883d840236c1551b9a3503462) () |
|  | |

|  |  |
| --- | --- |
| Language management. | |
| typedef void(\* | [AkLanguageChangeHandler](namespace_a_k_1_1_stream_mgr_af6f6b78cad5ec68a1adc59cb5c98b452.html#af6f6b78cad5ec68a1adc59cb5c98b452)) (const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*const in\_pLanguageName, void \*in\_pCookie) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [SetCurrentLanguage](namespace_a_k_1_1_stream_mgr_ae4820886baae734dd90177a49a2be1eb.html#ae4820886baae734dd90177a49a2be1eb) (const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*in\_pszLanguageName) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \* | [GetCurrentLanguage](namespace_a_k_1_1_stream_mgr_ae24e1f8b35b501eaa97599d5d6e48cc1.html#ae24e1f8b35b501eaa97599d5d6e48cc1) () |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [AddLanguageChangeObserver](namespace_a_k_1_1_stream_mgr_af547235acd8c151e6bf461f59e5a8eb7.html#af547235acd8c151e6bf461f59e5a8eb7) ([AkLanguageChangeHandler](namespace_a_k_1_1_stream_mgr_af6f6b78cad5ec68a1adc59cb5c98b452.html#af6f6b78cad5ec68a1adc59cb5c98b452) in\_handler, void \*in\_pCookie) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [RemoveLanguageChangeObserver](namespace_a_k_1_1_stream_mgr_a3663c4a818dbe536665a4e216b8e8424.html#a3663c4a818dbe536665a4e216b8e8424) (void \*in\_pCookie) |
|  | |

## 详细描述

Audiokinetic Stream Manager's implementation-specific interfaces of the Low-Level IO submodule.