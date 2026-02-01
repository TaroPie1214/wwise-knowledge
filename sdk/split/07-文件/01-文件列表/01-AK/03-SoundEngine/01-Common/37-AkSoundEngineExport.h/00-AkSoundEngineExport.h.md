# AkSoundEngineExport.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)

[宏定义](#define-members)

AkSoundEngineExport.h 文件参考

`#include <AK/AkPlatforms.h>`

[浏览源代码.](_ak_sound_engine_export_8h_source.html)

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AK\_DLLEXPORT](_ak_sound_engine_export_8h_ab291f969500ebc378f2344e1477d2dd7.html#ab291f969500ebc378f2344e1477d2dd7) |
|  | |
| #define | [AK\_DLLIMPORT](_ak_sound_engine_export_8h_a21c20351980d9090e8431ee00b5698bd.html#a21c20351980d9090e8431ee00b5698bd) |
|  | |
| #define | [AK\_ATTR\_USED](_ak_sound_engine_export_8h_a4a6ed3bb00082e572789fe20455d5dfb.html#a4a6ed3bb00082e572789fe20455d5dfb) |
|  | |
| #define | [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) |
|  | |
| #define | [AK\_FUNC](_ak_sound_engine_export_8h_a1fdcd1a75cdf8d556729382750204807.html#a1fdcd1a75cdf8d556729382750204807)(\_type, \_name)   \_type [AKSOUNDENGINE\_CALL](_platforms_2_windows_2_ak_types_8h_ac166d68f957db5cd6566201b6702ed64.html#ac166d68f957db5cd6566201b6702ed64) \_name |
|  | |
| #define | [AK\_EXTERNFUNC](_ak_sound_engine_export_8h_a6d5b906943937736500469defd1894d4.html#a6d5b906943937736500469defd1894d4)(\_type, \_name)   extern \_type [AKSOUNDENGINE\_CALL](_platforms_2_windows_2_ak_types_8h_ac166d68f957db5cd6566201b6702ed64.html#ac166d68f957db5cd6566201b6702ed64) \_name |
|  | |
| #define | [AK\_EXTERNAPIFUNC](_ak_sound_engine_export_8h_ae352ba27b5b4b0e49f7355a7cc0479c8.html#ae352ba27b5b4b0e49f7355a7cc0479c8)(\_type, \_name)   extern [AKSOUNDENGINE\_API](_ak_sound_engine_export_8h_ac6e96d34dfc0e12f9aaa7a47f4e9c322.html#ac6e96d34dfc0e12f9aaa7a47f4e9c322) \_type [AKSOUNDENGINE\_CALL](_platforms_2_windows_2_ak_types_8h_ac166d68f957db5cd6566201b6702ed64.html#ac166d68f957db5cd6566201b6702ed64) \_name |
|  | |
| #define | [AK\_CALLBACK](_ak_sound_engine_export_8h_a484ecbeacaa83263feae1176d5eb43cb.html#a484ecbeacaa83263feae1176d5eb43cb)(\_type, \_name)   typedef \_type ( [AKSOUNDENGINE\_CALL](_platforms_2_windows_2_ak_types_8h_ac166d68f957db5cd6566201b6702ed64.html#ac166d68f957db5cd6566201b6702ed64) \*\_name ) |
|  | |

## 详细描述

Export/calling convention definitions.

在文件 [AkSoundEngineExport.h](_ak_sound_engine_export_8h_source.html) 中定义.