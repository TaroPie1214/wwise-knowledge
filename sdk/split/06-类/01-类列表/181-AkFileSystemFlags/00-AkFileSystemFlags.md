# AkFileSystemFlags

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_file_system_flags-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AkFileSystemFlags结构体 参考

File system flags for file descriptors mapping.
[更多...](struct_ak_file_system_flags.html#details)

`#include <AkFileSystemFlags.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkFileSystemFlags](struct_ak_file_system_flags_a0998d8f5b5f4ebee5484c8aedce6d3c8.html#a0998d8f5b5f4ebee5484c8aedce6d3c8) () |
|  | |
|  | [AkFileSystemFlags](struct_ak_file_system_flags_a7858a47215fe4b11bdd950ee77c4bb60.html#a7858a47215fe4b11bdd950ee77c4bb60) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uCompanyID, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uCodecID, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uCustomParamSize, void \*in\_pCustomParam, bool in\_bIsLanguageSpecific, [AkCacheID](_ak_typedefs_8h_a5acf1fe33348412dca7d40b4fd007d98.html#a5acf1fe33348412dca7d40b4fd007d98) in\_uCacheID) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uCompanyID](struct_ak_file_system_flags_a3afa1ed5022d0c225e3b9eddb92a1a9a.html#a3afa1ed5022d0c225e3b9eddb92a1a9a) |
|  | Company ID (Wwise uses AKCOMPANYID\_AUDIOKINETIC, defined in AkTypes.h, for soundbanks and standard streaming files, and AKCOMPANYID\_AUDIOKINETIC\_EXTERNAL for streaming external sources). [更多...](struct_ak_file_system_flags_a3afa1ed5022d0c225e3b9eddb92a1a9a.html#a3afa1ed5022d0c225e3b9eddb92a1a9a) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uCodecID](struct_ak_file_system_flags_a10e070636834a71e86006eb966ecc77d.html#a10e070636834a71e86006eb966ecc77d) |
|  | File/codec type ID (defined in AkTypes.h) [更多...](struct_ak_file_system_flags_a10e070636834a71e86006eb966ecc77d.html#a10e070636834a71e86006eb966ecc77d) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uCustomParamSize](struct_ak_file_system_flags_a711de4f3e8f3e7cce7abd72362ca3aa7.html#a711de4f3e8f3e7cce7abd72362ca3aa7) |
|  | Size of the custom parameter [更多...](struct_ak_file_system_flags_a711de4f3e8f3e7cce7abd72362ca3aa7.html#a711de4f3e8f3e7cce7abd72362ca3aa7) |
|  | |
| void \* | [pCustomParam](struct_ak_file_system_flags_a23007119f2b9d630d97ac5e2c95d9ac5.html#a23007119f2b9d630d97ac5e2c95d9ac5) |
|  | Custom parameter [更多...](struct_ak_file_system_flags_a23007119f2b9d630d97ac5e2c95d9ac5.html#a23007119f2b9d630d97ac5e2c95d9ac5) |
|  | |
| bool | [bIsLanguageSpecific](struct_ak_file_system_flags_a6fc45a77ef8411269da43d3d63b669db.html#a6fc45a77ef8411269da43d3d63b669db) |
|  | True when the file location depends on language [更多...](struct_ak_file_system_flags_a6fc45a77ef8411269da43d3d63b669db.html#a6fc45a77ef8411269da43d3d63b669db) |
|  | |
| bool | [bIsAutomaticStream](struct_ak_file_system_flags_aaacd04936e1cbb575cf187470cefe0d6.html#aaacd04936e1cbb575cf187470cefe0d6) |
|  | |
| [AkCacheID](_ak_typedefs_8h_a5acf1fe33348412dca7d40b4fd007d98.html#a5acf1fe33348412dca7d40b4fd007d98) | [uCacheID](struct_ak_file_system_flags_a594e4b1e8c2c432221c126d432fd59e0.html#a594e4b1e8c2c432221c126d432fd59e0) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uNumBytesPrefetch](struct_ak_file_system_flags_adf724a85c0041cae4dadd2fa4c64c57e.html#adf724a85c0041cae4dadd2fa4c64c57e) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uDirectoryHash](struct_ak_file_system_flags_aa1d907d209451852d72a1617fba1d42b.html#aa1d907d209451852d72a1617fba1d42b) |
|  | If the implementation uses a hashed directory structure, this is the hash value that should be employed for determining the directory structure [更多...](struct_ak_file_system_flags_aa1d907d209451852d72a1617fba1d42b.html#aa1d907d209451852d72a1617fba1d42b) |
|  | |

## 详细描述

File system flags for file descriptors mapping.

在文件 [AkFileSystemFlags.h](_ak_file_system_flags_8h_source.html) 第 [34](_ak_file_system_flags_8h_source.html#l00034) 行定义.