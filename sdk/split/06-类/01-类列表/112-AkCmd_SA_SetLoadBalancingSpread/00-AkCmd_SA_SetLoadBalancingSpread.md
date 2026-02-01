# AkCmd_SA_SetLoadBalancingSpread

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___set_load_balancing_spread-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_SetLoadBalancingSpread结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [uNbFrames](struct_ak_cmd___s_a___set_load_balancing_spread_af5fc6cf3eeb4692c5255630701344581.html#af5fc6cf3eeb4692c5255630701344581) |
|  | Number of spread frames [更多...](struct_ak_cmd___s_a___set_load_balancing_spread_af5fc6cf3eeb4692c5255630701344581.html#af5fc6cf3eeb4692c5255630701344581) |
|  | |

## 详细描述

Set the number of frames on which the path validation phase will be spread. Value between [1..[ High values delay the validation of paths. A value of 1 indicates no spread at all.

参见
:   - [AkCommand\_SA\_SetLoadBalancingSpread](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda42a4a33357945ca8fb23cbf45170dbd7)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1946](_ak_command_types_8h_source.html#l01946) 行定义.