# AkZeroMemAligned

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Tools](dir_044f82abbf9804de57b7455f5736f74d.html)
- [Common](dir_3473269f4f57a4c2151a78abe7278350.html)
- [AkPlatformFuncs.h](_common_2_ak_platform_funcs_8h.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [AK\_FORCE\_CRASH](_common_2_ak_platform_funcs_8h_a869402461ee413c74d903c6c592fa585.html#a869402461ee413c74d903c6c592fa585) | | [AK\_THREAD\_INIT\_CODE](_common_2_ak_platform_funcs_8h_a8edb6983a1b26c16e683dcc1e205af43.html#a8edb6983a1b26c16e683dcc1e205af43) | | [AkPrefetchZero](_common_2_ak_platform_funcs_8h_a948f8234e77c82826ef1427963ce79ff.html#a948f8234e77c82826ef1427963ce79ff) | | [AkPrefetchZeroAligned](_common_2_ak_platform_funcs_8h_a9577f84ebe2c6dab4b4dbab32f093ab9.html#a9577f84ebe2c6dab4b4dbab32f093ab9) | | [AkZeroMemAligned](_common_2_ak_platform_funcs_8h_a47d685aca03fd3503d34dddc2fa2f49f.html#a47d685aca03fd3503d34dddc2fa2f49f) | | [AkZeroMemLarge](_common_2_ak_platform_funcs_8h_ad253eddc87f890ca9677913bd66299b5.html#ad253eddc87f890ca9677913bd66299b5) | | [AkZeroMemSmall](_common_2_ak_platform_funcs_8h_a36b3303234948398066f358466a84e3c.html#a36b3303234948398066f358466a84e3c) | | [◆](#a47d685aca03fd3503d34dddc2fa2f49f)AkZeroMemAligned |  |  |  |  | | --- | --- | --- | --- | | #define AkZeroMemAligned | ( |  | \_\_\_Dest, | |  |  |  | \_\_\_Size | |  | ) |  | [AKPLATFORM::AkMemSet](namespace_a_k_p_l_a_t_f_o_r_m_afe598f5d7465d44a10e8414716fab233.html#afe598f5d7465d44a10e8414716fab233)(\_\_\_Dest, 0, \_\_\_Size); |  在文件 [AkPlatformFuncs.h](_common_2_ak_platform_funcs_8h_source.html) 第 [101](_common_2_ak_platform_funcs_8h_source.html#l00101) 行定义. |