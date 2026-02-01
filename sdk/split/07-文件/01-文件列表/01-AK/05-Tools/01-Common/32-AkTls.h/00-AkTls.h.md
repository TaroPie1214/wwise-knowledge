# AkTls.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Tools](dir_044f82abbf9804de57b7455f5736f74d.html)
- [Common](dir_3473269f4f57a4c2151a78abe7278350.html)

[宏定义](#define-members) |
[类型定义](#typedef-members) |
[函数](#func-members)

AkTls.h 文件参考

`#include <AK/AkPlatforms.h>`  
`#include <AK/SoundEngine/Common/AkSoundEngineExport.h>`

[浏览源代码.](_ak_tls_8h_source.html)

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AKTLS\_NULL](_ak_tls_8h_aa3718756cd2075630fe1fd3ce724ebad.html#aa3718756cd2075630fe1fd3ce724ebad)   (0) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| typedef [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) | [AkTlsSlot](_ak_tls_8h_a676179a8fb3082e49d37d454ef180089.html#a676179a8fb3082e49d37d454ef180089) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) int | [AkTlsAllocateSlot](_ak_tls_8h_ab9f53556c971540f784b9309048fe9d5.html#ab9f53556c971540f784b9309048fe9d5) ([AkTlsSlot](_ak_tls_8h_a676179a8fb3082e49d37d454ef180089.html#a676179a8fb3082e49d37d454ef180089) \*out\_pSlot) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AkTlsFreeSlot](_ak_tls_8h_ac654970187551ad768f544f655da238d.html#ac654970187551ad768f544f655da238d) ([AkTlsSlot](_ak_tls_8h_a676179a8fb3082e49d37d454ef180089.html#a676179a8fb3082e49d37d454ef180089) in\_slot) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) [AkUIntPtr](_ak_numeral_types_8h_aba972f179e9ca267106fac77b6d3c78b.html#aba972f179e9ca267106fac77b6d3c78b) | [AkTlsGetValue](_ak_tls_8h_a020a73f74097415228f38e136d9f1c56.html#a020a73f74097415228f38e136d9f1c56) ([AkTlsSlot](_ak_tls_8h_a676179a8fb3082e49d37d454ef180089.html#a676179a8fb3082e49d37d454ef180089) in\_slot) |
|  | |
| [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) void | [AkTlsSetValue](_ak_tls_8h_aa02d55e066749853627b85635fa97dc6.html#aa02d55e066749853627b85635fa97dc6) ([AkTlsSlot](_ak_tls_8h_a676179a8fb3082e49d37d454ef180089.html#a676179a8fb3082e49d37d454ef180089) in\_slot, [AkUIntPtr](_ak_numeral_types_8h_aba972f179e9ca267106fac77b6d3c78b.html#aba972f179e9ca267106fac77b6d3c78b) in\_value) |
|  | |