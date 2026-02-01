# AkCmd_SA_SetReflectionsOrder

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___set_reflections_order-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_SetReflectionsOrder结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [reflectionsOrder](struct_ak_cmd___s_a___set_reflections_order_a75945d893028102676dd7f7c86cb5dbd.html#a75945d893028102676dd7f7c86cb5dbd) |
|  | Number of reflections to calculate. Valid range [0,4] [更多...](struct_ak_cmd___s_a___set_reflections_order_a75945d893028102676dd7f7c86cb5dbd.html#a75945d893028102676dd7f7c86cb5dbd) |
|  | |
| bool | [updatePaths](struct_ak_cmd___s_a___set_reflections_order_af0184c878489ccfc982f096433784b8a.html#af0184c878489ccfc982f096433784b8a) |
|  | Set to true to clear existing higher-order paths and to force the re-computation of new paths. If false, existing paths will remain and new paths will be computed when the emitter or listener moves. [更多...](struct_ak_cmd___s_a___set_reflections_order_af0184c878489ccfc982f096433784b8a.html#af0184c878489ccfc982f096433784b8a) |
|  | |

## 详细描述

Set the early reflections order for reflection calculation. The reflections order indicates the number of times sound can bounce off of a surface. A higher number requires more CPU resources but results in denser early reflections. Set to 0 to globally disable reflections processing.

This command can fail for the following reasons:

- AK\_InvalidParameter: `reflectionsOrder` is not in the accepted range.

参见
:   - [AkCommand\_SA\_SetReflectionsOrder](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdab8233281b4b6133266e3e951aa556185)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1848](_ak_command_types_8h_source.html#l01848) 行定义.