# AK_ExternalSourceArray_Data

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)
- [AkExternalSourceArray.h](_ak_external_source_array_8h.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [AK\_ExternalSourceArray\_AddFileIDSource](_ak_external_source_array_8h_a4ca5d14e0ec219e91df4e067050aa96a.html#a4ca5d14e0ec219e91df4e067050aa96a) | | [AK\_ExternalSourceArray\_AddFileNameSource](_ak_external_source_array_8h_a3c0dfa264df1a93bbd24041d14ca7c4e.html#a3c0dfa264df1a93bbd24041d14ca7c4e) | | [AK\_ExternalSourceArray\_AddInMemorySource](_ak_external_source_array_8h_a0ddf188e9a33cd31ee4885583e4bb37d.html#a0ddf188e9a33cd31ee4885583e4bb37d) | | [AK\_ExternalSourceArray\_Capacity](_ak_external_source_array_8h_a87df1219b9c322b11b6ecbbee3e1436f.html#a87df1219b9c322b11b6ecbbee3e1436f) | | [AK\_ExternalSourceArray\_Create](_ak_external_source_array_8h_af45335a803640fcd6492b02ff5bf042d.html#af45335a803640fcd6492b02ff5bf042d) | | [AK\_ExternalSourceArray\_CreateFromData](_ak_external_source_array_8h_af5ecf16d5d53c71b96e7a1bfbbafc8a8.html#af5ecf16d5d53c71b96e7a1bfbbafc8a8) | | [AK\_ExternalSourceArray\_Data](_ak_external_source_array_8h_af0a49e03c2643515a647d9964e93b5ea.html#af0a49e03c2643515a647d9964e93b5ea) | | [AK\_ExternalSourceArray\_Destroy](_ak_external_source_array_8h_afa0bdf3eaf04e9aeda9584c83d32159c.html#afa0bdf3eaf04e9aeda9584c83d32159c) | | [AK\_ExternalSourceArray\_Length](_ak_external_source_array_8h_a1fec4a749713e893b4a1b1005086c697.html#a1fec4a749713e893b4a1b1005086c697) | | [◆](#af0a49e03c2643515a647d9964e93b5ea)AK\_ExternalSourceArray\_Data() |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) struct [AkExternalSourceInfo](struct_ak_external_source_info.html)\* AK\_ExternalSourceArray\_Data | ( | [AkExternalSourceArray](_ak_typedefs_8h_a335692278dd11e40d41d21307ca37d34.html#a335692278dd11e40d41d21307ca37d34) | *in\_arSources* | ) |  |  Returns the raw data of the array.  This raw data can be passed to other functions like AK\_CommandBuffer\_AddExternalSources.  参数  |  |  |  | | --- | --- | --- | | [in] | in\_arSources | The array |  返回  Pointer to the raw data of the array. |