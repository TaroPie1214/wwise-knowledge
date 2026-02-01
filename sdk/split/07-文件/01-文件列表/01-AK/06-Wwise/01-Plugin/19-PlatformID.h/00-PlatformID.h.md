# PlatformID.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Wwise](dir_6ea5b71cdf4c60d3386ed2d84846331f.html)
- [Plugin](dir_00900ac4c96da97e1d767c263ed2fa21.html)

[类](#nested-classes) |
[命名空间](#namespaces) |
[宏定义](#define-members) |
[函数](#func-members) |
[变量](#var-members)

PlatformID.h 文件参考

`#include "PluginHelpers.h"`

[浏览源代码.](_platform_i_d_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [BasePlatformID](struct_base_platform_i_d.html) |
|  | |
| struct | [BasePlatformID::GUIDLessNative](struct_base_platform_i_d_1_1_g_u_i_d_less_native.html) |
|  | |

|  |  |
| --- | --- |
| 命名空间 | |
|  | [PlatformID](namespace_platform_i_d.html) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AK\_ID\_DECLARE](_platform_i_d_8h_a79518b7890f142ea3da1c7fd56761201.html#a79518b7890f142ea3da1c7fd56761201)   extern const \_\_attribute\_\_( ( weak ) ) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| [BasePlatformID](struct_base_platform_i_d.html) | [ak\_wwise\_create\_base\_platform\_id](_platform_i_d_8h_ab4921ff3a6da5b9b6ff99f8a5dcb16a9.html#ab4921ff3a6da5b9b6ff99f8a5dcb16a9) () |
|  | |
| bool | [PlatformID::IsPlatformBigEndian](namespace_platform_i_d_ae250bb8a8cc47a22c111945b929d50a6.html#ae250bb8a8cc47a22c111945b929d50a6) (const [BasePlatformID](struct_base_platform_i_d.html) &) |
|  | Returns true if the given platform has Big Endian byte ordering. [更多...](namespace_platform_i_d_ae250bb8a8cc47a22c111945b929d50a6.html#ae250bb8a8cc47a22c111945b929d50a6) |
|  | |

|  |  |
| --- | --- |
| 变量 | |
| [AK\_ID\_DECLARE](_platform_i_d_8h_a79518b7890f142ea3da1c7fd56761201.html#a79518b7890f142ea3da1c7fd56761201) GUID | [PlatformID::Windows\_unsafeguid](namespace_platform_i_d_a11799f593d3aa4ee7da4b72eccdb3675.html#a11799f593d3aa4ee7da4b72eccdb3675) = { 0x6E0CB257, 0xC6C8, 0x4c5c, { 0x83, 0x66, 0x27, 0x40, 0xDF, 0xC4, 0x41, 0xEB } } |
|  | |
| [AK\_ID\_DECLARE](_platform_i_d_8h_a79518b7890f142ea3da1c7fd56761201.html#a79518b7890f142ea3da1c7fd56761201) [BasePlatformID](struct_base_platform_i_d.html) | [PlatformID::Windows](namespace_platform_i_d_a21b4bdace04cb72145c4c7eb72761486.html#a21b4bdace04cb72145c4c7eb72761486) = [BasePlatformID::Create](struct_base_platform_i_d_adeb8edfdfc5d747f6ef956f80681e7e7.html#adeb8edfdfc5d747f6ef956f80681e7e7)( Windows\_unsafeguid ) |
|  | |
| [AK\_ID\_DECLARE](_platform_i_d_8h_a79518b7890f142ea3da1c7fd56761201.html#a79518b7890f142ea3da1c7fd56761201) GUID | [PlatformID::Mac\_unsafeguid](namespace_platform_i_d_aa4cbb183bb1663b30be95cb29476d84e.html#aa4cbb183bb1663b30be95cb29476d84e) = { 0x9c6217d5, 0xdd11, 0x4795, { 0x87, 0xc1, 0x6c, 0xe0, 0x28, 0x53, 0xc5, 0x40 } } |
|  | |
| [AK\_ID\_DECLARE](_platform_i_d_8h_a79518b7890f142ea3da1c7fd56761201.html#a79518b7890f142ea3da1c7fd56761201) [BasePlatformID](struct_base_platform_i_d.html) | [PlatformID::Mac](namespace_platform_i_d_a880791f2b65b8cd7c0e7b96e1d74d958.html#a880791f2b65b8cd7c0e7b96e1d74d958) = [BasePlatformID::Create](struct_base_platform_i_d_adeb8edfdfc5d747f6ef956f80681e7e7.html#adeb8edfdfc5d747f6ef956f80681e7e7)( Mac\_unsafeguid ) |
|  | |
| [AK\_ID\_DECLARE](_platform_i_d_8h_a79518b7890f142ea3da1c7fd56761201.html#a79518b7890f142ea3da1c7fd56761201) GUID | [PlatformID::PS4\_unsafeguid](namespace_platform_i_d_a4a983219402086c0c84fd8ddb06cf543.html#a4a983219402086c0c84fd8ddb06cf543) = { 0x3af9b9b6, 0x6ef1, 0x47e9, { 0xb5, 0xfe, 0xe3, 0xc, 0x9e, 0x60, 0x2c, 0x77 } } |
|  | |
| [AK\_ID\_DECLARE](_platform_i_d_8h_a79518b7890f142ea3da1c7fd56761201.html#a79518b7890f142ea3da1c7fd56761201) [BasePlatformID](struct_base_platform_i_d.html) | [PlatformID::PS4](namespace_platform_i_d_a760d6ae36c93a4ac7956565b5afa81a1.html#a760d6ae36c93a4ac7956565b5afa81a1) = [BasePlatformID::Create](struct_base_platform_i_d_adeb8edfdfc5d747f6ef956f80681e7e7.html#adeb8edfdfc5d747f6ef956f80681e7e7)( PS4\_unsafeguid ) |
|  | |
| [AK\_ID\_DECLARE](_platform_i_d_8h_a79518b7890f142ea3da1c7fd56761201.html#a79518b7890f142ea3da1c7fd56761201) GUID | [PlatformID::PS5\_unsafeguid](namespace_platform_i_d_a221022688e0f5e2600d6bd0f0f95ac6b.html#a221022688e0f5e2600d6bd0f0f95ac6b) = { 0x662a5e67, 0x9d35, 0x48da, { 0xb6, 0xa8, 0xb7, 0x7c, 0x7f, 0x1d, 0x84, 0xe0 } } |
|  | |
| [AK\_ID\_DECLARE](_platform_i_d_8h_a79518b7890f142ea3da1c7fd56761201.html#a79518b7890f142ea3da1c7fd56761201) [BasePlatformID](struct_base_platform_i_d.html) | [PlatformID::PS5](namespace_platform_i_d_a7bf4c6443044f5e48210d3d09cc32a64.html#a7bf4c6443044f5e48210d3d09cc32a64) = [BasePlatformID::Create](struct_base_platform_i_d_adeb8edfdfc5d747f6ef956f80681e7e7.html#adeb8edfdfc5d747f6ef956f80681e7e7)(PS5\_unsafeguid) |
|  | |
| [AK\_ID\_DECLARE](_platform_i_d_8h_a79518b7890f142ea3da1c7fd56761201.html#a79518b7890f142ea3da1c7fd56761201) GUID | [PlatformID::iOS\_unsafeguid](namespace_platform_i_d_aacff090bcf37cf32b4559943d320e559.html#aacff090bcf37cf32b4559943d320e559) = { 0xece03db4, 0xf948, 0x462d, { 0xb2, 0xbb, 0xa9, 0x17, 0x30, 0x12, 0xb1, 0xf8 } } |
|  | |
| [AK\_ID\_DECLARE](_platform_i_d_8h_a79518b7890f142ea3da1c7fd56761201.html#a79518b7890f142ea3da1c7fd56761201) [BasePlatformID](struct_base_platform_i_d.html) | [PlatformID::iOS](namespace_platform_i_d_a5d980da03eeb40c7505ac990309b260d.html#a5d980da03eeb40c7505ac990309b260d) = [BasePlatformID::Create](struct_base_platform_i_d_adeb8edfdfc5d747f6ef956f80681e7e7.html#adeb8edfdfc5d747f6ef956f80681e7e7)( iOS\_unsafeguid ) |
|  | |
| [AK\_ID\_DECLARE](_platform_i_d_8h_a79518b7890f142ea3da1c7fd56761201.html#a79518b7890f142ea3da1c7fd56761201) GUID | [PlatformID::Android\_unsafeguid](namespace_platform_i_d_a1740bb523deb7f45d6a7c1a4445799d7.html#a1740bb523deb7f45d6a7c1a4445799d7) = { 0xa2d401de, 0xb8b6, 0x4feb, { 0x81, 0x42, 0x13, 0x7c, 0x34, 0xd5, 0x07, 0xCA } } |
|  | |
| [AK\_ID\_DECLARE](_platform_i_d_8h_a79518b7890f142ea3da1c7fd56761201.html#a79518b7890f142ea3da1c7fd56761201) [BasePlatformID](struct_base_platform_i_d.html) | [PlatformID::Android](namespace_platform_i_d_a8a149fa4fef1580be88ec762c60c7d16.html#a8a149fa4fef1580be88ec762c60c7d16) = [BasePlatformID::Create](struct_base_platform_i_d_adeb8edfdfc5d747f6ef956f80681e7e7.html#adeb8edfdfc5d747f6ef956f80681e7e7)( Android\_unsafeguid ) |
|  | |
| [AK\_ID\_DECLARE](_platform_i_d_8h_a79518b7890f142ea3da1c7fd56761201.html#a79518b7890f142ea3da1c7fd56761201) GUID | [PlatformID::XboxOne\_unsafeguid](namespace_platform_i_d_a79acd710fdef2ec032e7e6e9710bd4a4.html#a79acd710fdef2ec032e7e6e9710bd4a4) = { 0xb131584b, 0x9961, 0x4bb5, { 0x9c, 0x58, 0xa3, 0xe9, 0xab, 0xff, 0xbb, 0xf6 } } |
|  | |
| [AK\_ID\_DECLARE](_platform_i_d_8h_a79518b7890f142ea3da1c7fd56761201.html#a79518b7890f142ea3da1c7fd56761201) [BasePlatformID](struct_base_platform_i_d.html) | [PlatformID::XboxOne](namespace_platform_i_d_a69f06126406efc99cedb5a681f663d68.html#a69f06126406efc99cedb5a681f663d68) = [BasePlatformID::Create](struct_base_platform_i_d_adeb8edfdfc5d747f6ef956f80681e7e7.html#adeb8edfdfc5d747f6ef956f80681e7e7)( XboxOne\_unsafeguid ) |
|  | |
| [AK\_ID\_DECLARE](_platform_i_d_8h_a79518b7890f142ea3da1c7fd56761201.html#a79518b7890f142ea3da1c7fd56761201) GUID | [PlatformID::Linux\_unsafeguid](namespace_platform_i_d_adc64712ee43ad871e013955037b4c9b0.html#adc64712ee43ad871e013955037b4c9b0) = { 0xbd0bdf13, 0x3125, 0x454f, { 0x8b, 0xfd, 0x31, 0x95, 0x37, 0x16, 0x9f, 0x81 } } |
|  | |
| [AK\_ID\_DECLARE](_platform_i_d_8h_a79518b7890f142ea3da1c7fd56761201.html#a79518b7890f142ea3da1c7fd56761201) [BasePlatformID](struct_base_platform_i_d.html) | [PlatformID::Linux](namespace_platform_i_d_a27dcd10a84a2c6b802ee0411c8149240.html#a27dcd10a84a2c6b802ee0411c8149240) = [BasePlatformID::Create](struct_base_platform_i_d_adeb8edfdfc5d747f6ef956f80681e7e7.html#adeb8edfdfc5d747f6ef956f80681e7e7)( Linux\_unsafeguid ) |
|  | |
| [AK\_ID\_DECLARE](_platform_i_d_8h_a79518b7890f142ea3da1c7fd56761201.html#a79518b7890f142ea3da1c7fd56761201) GUID | [PlatformID::NintendoNX\_unsafeguid](namespace_platform_i_d_a44bdca03cb9b5d15d9024bf9460c25b4.html#a44bdca03cb9b5d15d9024bf9460c25b4) = { 0x874f26d2, 0x416d, 0x4698, { 0xbf, 0xb6, 0x34, 0x27, 0xca, 0xfc, 0xff, 0x9c } } |
|  | |
| [AK\_ID\_DECLARE](_platform_i_d_8h_a79518b7890f142ea3da1c7fd56761201.html#a79518b7890f142ea3da1c7fd56761201) [BasePlatformID](struct_base_platform_i_d.html) | [PlatformID::NintendoNX](namespace_platform_i_d_ac2082411a0a1e60aa9eeb219dc0075be.html#ac2082411a0a1e60aa9eeb219dc0075be) = [BasePlatformID::Create](struct_base_platform_i_d_adeb8edfdfc5d747f6ef956f80681e7e7.html#adeb8edfdfc5d747f6ef956f80681e7e7)(NintendoNX\_unsafeguid) |
|  | |
| [AK\_ID\_DECLARE](_platform_i_d_8h_a79518b7890f142ea3da1c7fd56761201.html#a79518b7890f142ea3da1c7fd56761201) GUID | [PlatformID::Web\_unsafeguid](namespace_platform_i_d_a3c8139c18a2ddf15a371543887a01200.html#a3c8139c18a2ddf15a371543887a01200) = { 0x639ad233, 0x23f2, 0x4c0f, { 0x91, 0x27, 0x79, 0xf4, 0x4c, 0x15, 0xe1, 0xdA } } |
|  | |
| [AK\_ID\_DECLARE](_platform_i_d_8h_a79518b7890f142ea3da1c7fd56761201.html#a79518b7890f142ea3da1c7fd56761201) [BasePlatformID](struct_base_platform_i_d.html) | [PlatformID::Web](namespace_platform_i_d_aac2c3bc487224021c9cc54b6357c02cd.html#aac2c3bc487224021c9cc54b6357c02cd) = [BasePlatformID::Create](struct_base_platform_i_d_adeb8edfdfc5d747f6ef956f80681e7e7.html#adeb8edfdfc5d747f6ef956f80681e7e7)(Web\_unsafeguid) |
|  | |
| [AK\_ID\_DECLARE](_platform_i_d_8h_a79518b7890f142ea3da1c7fd56761201.html#a79518b7890f142ea3da1c7fd56761201) GUID | [PlatformID::XboxSeriesX\_unsafeguid](namespace_platform_i_d_a7c864151ddd900918e63d59fb310bf88.html#a7c864151ddd900918e63d59fb310bf88) = { 0x26352fc0, 0x7716, 0x4f97, { 0x8d, 0xaf, 0x36, 0x65, 0xec, 0x2b, 0xb5, 0x01 } } |
|  | |
| [AK\_ID\_DECLARE](_platform_i_d_8h_a79518b7890f142ea3da1c7fd56761201.html#a79518b7890f142ea3da1c7fd56761201) [BasePlatformID](struct_base_platform_i_d.html) | [PlatformID::XboxSeriesX](namespace_platform_i_d_a3e00674609c4e6c431f8665476657635.html#a3e00674609c4e6c431f8665476657635) = [BasePlatformID::Create](struct_base_platform_i_d_adeb8edfdfc5d747f6ef956f80681e7e7.html#adeb8edfdfc5d747f6ef956f80681e7e7)(XboxSeriesX\_unsafeguid) |
|  | |
| [AK\_ID\_DECLARE](_platform_i_d_8h_a79518b7890f142ea3da1c7fd56761201.html#a79518b7890f142ea3da1c7fd56761201) GUID | [PlatformID::OpenHarmony\_unsafeguid](namespace_platform_i_d_ad9c26d0c57d840383c7fc08b653471a4.html#ad9c26d0c57d840383c7fc08b653471a4) = { 0xf1895123, 0x76d6, 0x4d2c, { 0x8b, 0xb4, 0x36, 0x50, 0xf8, 0xa4, 0x63, 0xeb } } |
|  | |
| [AK\_ID\_DECLARE](_platform_i_d_8h_a79518b7890f142ea3da1c7fd56761201.html#a79518b7890f142ea3da1c7fd56761201) [BasePlatformID](struct_base_platform_i_d.html) | [PlatformID::OpenHarmony](namespace_platform_i_d_a2bc29f7954f4e332b487311c6f9754ae.html#a2bc29f7954f4e332b487311c6f9754ae) = [BasePlatformID::Create](struct_base_platform_i_d_adeb8edfdfc5d747f6ef956f80681e7e7.html#adeb8edfdfc5d747f6ef956f80681e7e7)(OpenHarmony\_unsafeguid) |
|  | |
| [AK\_ID\_DECLARE](_platform_i_d_8h_a79518b7890f142ea3da1c7fd56761201.html#a79518b7890f142ea3da1c7fd56761201) GUID | [PlatformID::Ounce\_unsafeguid](namespace_platform_i_d_a3a7759cc235ee84e7e825e44c060710d.html#a3a7759cc235ee84e7e825e44c060710d) = { 0xa3dce7a2, 0x53e3, 0x4347, { 0x93, 0x63, 0x58, 0x4d, 0x63, 0xb8, 0x5a, 0xdf } } |
|  | |
| [AK\_ID\_DECLARE](_platform_i_d_8h_a79518b7890f142ea3da1c7fd56761201.html#a79518b7890f142ea3da1c7fd56761201) [BasePlatformID](struct_base_platform_i_d.html) | [PlatformID::Ounce](namespace_platform_i_d_abd545bc53013ff99fe9426b404d30c4e.html#abd545bc53013ff99fe9426b404d30c4e) = [BasePlatformID::Create](struct_base_platform_i_d_adeb8edfdfc5d747f6ef956f80681e7e7.html#adeb8edfdfc5d747f6ef956f80681e7e7)(Ounce\_unsafeguid) |
|  | |

## 详细描述

Unique identifiers for platforms in the Wwise authoring application.

在文件 [PlatformID.h](_platform_i_d_8h_source.html) 中定义.