# AkFPUtilities.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [SoundEngine](dir_99a03347615d0b3a42409b24d959a474.html)
- [Common](dir_d95da6bd1d27077206201426d7500a88.html)

[宏定义](#define-members) |
[函数](#func-members)

AkFPUtilities.h 文件参考

`#include <AK/SoundEngine/Common/AkTypes.h>`

[浏览源代码.](_ak_f_p_utilities_8h_source.html)

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AK\_FSEL](_ak_f_p_utilities_8h_a23a0d5b20372a53f5cda9ab4950297c8.html#a23a0d5b20372a53f5cda9ab4950297c8)(\_\_a\_\_, \_\_b\_\_, \_\_c\_\_)   (((\_\_a\_\_) >= 0) ? (\_\_b\_\_) : (\_\_c\_\_)) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [AK\_FPMin](_ak_f_p_utilities_8h_a9d14293ced0e21bcd4d379040f073b00.html#a9d14293ced0e21bcd4d379040f073b00) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) fA, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) fB) |
|  | Branchless (where available) version returning minimum value between two AkReal32 values [更多...](_ak_f_p_utilities_8h_a9d14293ced0e21bcd4d379040f073b00.html#a9d14293ced0e21bcd4d379040f073b00) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [AK\_FPMax](_ak_f_p_utilities_8h_a8a9d556e262212b931e8b664472ad5f2.html#a8a9d556e262212b931e8b664472ad5f2) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) fA, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) fB) |
|  | Branchless (where available) version returning maximum value between two AkReal32 values [更多...](_ak_f_p_utilities_8h_a8a9d556e262212b931e8b664472ad5f2.html#a8a9d556e262212b931e8b664472ad5f2) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [AK\_FPSetValGT](_ak_f_p_utilities_8h_a56038139143ae7fd694f311d76580547.html#a56038139143ae7fd694f311d76580547) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fComparandA, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fComparandB, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) &io\_fVariableToSet, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fValueIfTrue) |
|  | Branchless comparison (where available) setting 3rd argument to 4th argument if 1st argument is greater than 2nd argument. [更多...](_ak_f_p_utilities_8h_a56038139143ae7fd694f311d76580547.html#a56038139143ae7fd694f311d76580547) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [AK\_FPSetValGTE](_ak_f_p_utilities_8h_acb59feb62771be08f32739f8fa8f835e.html#acb59feb62771be08f32739f8fa8f835e) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fComparandA, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fComparandB, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) &io\_fVariableToSet, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fValueIfTrue) |
|  | Branchless comparison (where available) setting 3rd argument to 4th argument if 1st argument is greater than equal 2nd argument. [更多...](_ak_f_p_utilities_8h_acb59feb62771be08f32739f8fa8f835e.html#acb59feb62771be08f32739f8fa8f835e) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [AK\_FPSetValLT](_ak_f_p_utilities_8h_a11797be4dd0217aad44a731a9308db23.html#a11797be4dd0217aad44a731a9308db23) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fComparandA, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fComparandB, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) &io\_fVariableToSet, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fValueIfTrue) |
|  | Branchless comparison (where available) setting 3rd argument to 4th argument if 1st argument is less than 2nd argument. [更多...](_ak_f_p_utilities_8h_a11797be4dd0217aad44a731a9308db23.html#a11797be4dd0217aad44a731a9308db23) |
|  | |
| static [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [AK\_FPSetValLTE](_ak_f_p_utilities_8h_a705b04c9ddd0d9c19752990fdeccad4f.html#a705b04c9ddd0d9c19752990fdeccad4f) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fComparandA, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fComparandB, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) &io\_fVariableToSet, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fValueIfTrue) |
|  | Branchless comparison (where available) setting 3rd argument to 4th argument if 1st argument is less than equal 2nd argument. [更多...](_ak_f_p_utilities_8h_a705b04c9ddd0d9c19752990fdeccad4f.html#a705b04c9ddd0d9c19752990fdeccad4f) |
|  | |

## 详细描述

Floating point performance utilities.

在文件 [AkFPUtilities.h](_ak_f_p_utilities_8h_source.html) 中定义.