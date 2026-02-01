# AkExternalSourceArray.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)

[函数](#func-members)

AkExternalSourceArray.h 文件参考

`#include <AK/SoundEngine/Common/AkSoundEngineTypes.h>`

[浏览源代码.](_ak_external_source_array_8h_source.html)

|  |  |
| --- | --- |
| 函数 | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AkExternalSourceArray](_ak_typedefs_8h_a335692278dd11e40d41d21307ca37d34.html#a335692278dd11e40d41d21307ca37d34) | [AK\_ExternalSourceArray\_Create](_ak_external_source_array_8h_af45335a803640fcd6492b02ff5bf042d.html#af45335a803640fcd6492b02ff5bf042d) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) capacity) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AkExternalSourceArray](_ak_typedefs_8h_a335692278dd11e40d41d21307ca37d34.html#a335692278dd11e40d41d21307ca37d34) | [AK\_ExternalSourceArray\_CreateFromData](_ak_external_source_array_8h_af5ecf16d5d53c71b96e7a1bfbbafc8a8.html#af5ecf16d5d53c71b96e7a1bfbbafc8a8) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uNumSrcs, struct [AkExternalSourceInfo](struct_ak_external_source_info.html) \*in\_pSources) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) int | [AK\_ExternalSourceArray\_AddInMemorySource](_ak_external_source_array_8h_a0ddf188e9a33cd31ee4885583e4bb37d.html#a0ddf188e9a33cd31ee4885583e4bb37d) ([AkExternalSourceArray](_ak_typedefs_8h_a335692278dd11e40d41d21307ca37d34.html#a335692278dd11e40d41d21307ca37d34) in\_arSources, [AkCodecID](_ak_typedefs_8h_ae3cd7c34d31c81aa8ac649ac3a0e2206.html#ae3cd7c34d31c81aa8ac649ac3a0e2206) in\_codec, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_cookie, void \*in\_pInMemory, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uiMemorySize) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) int | [AK\_ExternalSourceArray\_AddFileNameSource](_ak_external_source_array_8h_a3c0dfa264df1a93bbd24041d14ca7c4e.html#a3c0dfa264df1a93bbd24041d14ca7c4e) ([AkExternalSourceArray](_ak_typedefs_8h_a335692278dd11e40d41d21307ca37d34.html#a335692278dd11e40d41d21307ca37d34) in\_arSources, [AkCodecID](_ak_typedefs_8h_ae3cd7c34d31c81aa8ac649ac3a0e2206.html#ae3cd7c34d31c81aa8ac649ac3a0e2206) in\_codec, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_cookie, const char \*in\_filename) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) int | [AK\_ExternalSourceArray\_AddFileIDSource](_ak_external_source_array_8h_a4ca5d14e0ec219e91df4e067050aa96a.html#a4ca5d14e0ec219e91df4e067050aa96a) ([AkExternalSourceArray](_ak_typedefs_8h_a335692278dd11e40d41d21307ca37d34.html#a335692278dd11e40d41d21307ca37d34) in\_arSources, [AkCodecID](_ak_typedefs_8h_ae3cd7c34d31c81aa8ac649ac3a0e2206.html#ae3cd7c34d31c81aa8ac649ac3a0e2206) in\_codec, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_cookie, [AkFileID](_ak_typedefs_8h_adff75ad09d4237d128c034afd17f3b35.html#adff75ad09d4237d128c034afd17f3b35) in\_fileID) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AK\_ExternalSourceArray\_Length](_ak_external_source_array_8h_a1fec4a749713e893b4a1b1005086c697.html#a1fec4a749713e893b4a1b1005086c697) ([AkExternalSourceArray](_ak_typedefs_8h_a335692278dd11e40d41d21307ca37d34.html#a335692278dd11e40d41d21307ca37d34) in\_arSources) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [AK\_ExternalSourceArray\_Capacity](_ak_external_source_array_8h_a87df1219b9c322b11b6ecbbee3e1436f.html#a87df1219b9c322b11b6ecbbee3e1436f) ([AkExternalSourceArray](_ak_typedefs_8h_a335692278dd11e40d41d21307ca37d34.html#a335692278dd11e40d41d21307ca37d34) in\_arSources) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) struct [AkExternalSourceInfo](struct_ak_external_source_info.html) \* | [AK\_ExternalSourceArray\_Data](_ak_external_source_array_8h_af0a49e03c2643515a647d9964e93b5ea.html#af0a49e03c2643515a647d9964e93b5ea) ([AkExternalSourceArray](_ak_typedefs_8h_a335692278dd11e40d41d21307ca37d34.html#a335692278dd11e40d41d21307ca37d34) in\_arSources) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AK\_ExternalSourceArray\_Destroy](_ak_external_source_array_8h_afa0bdf3eaf04e9aeda9584c83d32159c.html#afa0bdf3eaf04e9aeda9584c83d32159c) ([AkExternalSourceArray](_ak_typedefs_8h_a335692278dd11e40d41d21307ca37d34.html#a335692278dd11e40d41d21307ca37d34) in\_arSources) |
|  | |