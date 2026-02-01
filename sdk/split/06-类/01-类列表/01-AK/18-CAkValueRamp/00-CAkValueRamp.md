# CAkValueRamp

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [CAkValueRamp](class_a_k_1_1_c_ak_value_ramp.html)

[所有成员列表](class_a_k_1_1_c_ak_value_ramp-members.html) |
[Public 成员函数](#pub-methods)

AK::CAkValueRamp类 参考

`#include <AkValueRamp.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [CAkValueRamp](class_a_k_1_1_c_ak_value_ramp_af1126956bed3777bbd0c10a685907ab9.html#af1126956bed3777bbd0c10a685907ab9) () |
|  | Constructor method. [更多...](class_a_k_1_1_c_ak_value_ramp_af1126956bed3777bbd0c10a685907ab9.html#af1126956bed3777bbd0c10a685907ab9) |
|  | |
|  | [~CAkValueRamp](class_a_k_1_1_c_ak_value_ramp_a61eb06fd8bd5aed867113046d3fd3d38.html#a61eb06fd8bd5aed867113046d3fd3d38) () |
|  | Destructor method. [更多...](class_a_k_1_1_c_ak_value_ramp_a61eb06fd8bd5aed867113046d3fd3d38.html#a61eb06fd8bd5aed867113046d3fd3d38) |
|  | |
| void | [RampSetup](class_a_k_1_1_c_ak_value_ramp_a831ac8bab29ae6c2ed0baa9215492f8e.html#a831ac8bab29ae6c2ed0baa9215492f8e) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) fStepIncrement, [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) fInitVal) |
|  | Initial parameter interpolation ramp setup. [更多...](class_a_k_1_1_c_ak_value_ramp_a831ac8bab29ae6c2ed0baa9215492f8e.html#a831ac8bab29ae6c2ed0baa9215492f8e) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) void | [SetTarget](class_a_k_1_1_c_ak_value_ramp_a9ad5dcdb9d44fd34610492c2bd85ea65.html#a9ad5dcdb9d44fd34610492c2bd85ea65) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) fTarget) |
|  | Set the ramp's target value. [更多...](class_a_k_1_1_c_ak_value_ramp_a9ad5dcdb9d44fd34610492c2bd85ea65.html#a9ad5dcdb9d44fd34610492c2bd85ea65) |
|  | |
| [AkForceInline](_platforms_2_windows_2_ak_types_8h_a3b6f41972bf6fa55e80b687ca50fbd12.html#a3b6f41972bf6fa55e80b687ca50fbd12) [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [Tick](class_a_k_1_1_c_ak_value_ramp_a5338eeebff6dbd429909cc4667ecbf56.html#a5338eeebff6dbd429909cc4667ecbf56) () |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [GetCurrent](class_a_k_1_1_c_ak_value_ramp_abc5361e4df6298c15e8dc426ea1a9e9b.html#abc5361e4df6298c15e8dc426ea1a9e9b) () |
|  | |
| void | [SetCurrent](class_a_k_1_1_c_ak_value_ramp_a7c4ea2a3610cee3b12dbaf28b465a701.html#a7c4ea2a3610cee3b12dbaf28b465a701) ([AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) in\_fCurrent) |
|  | Set the current interpolated value. [更多...](class_a_k_1_1_c_ak_value_ramp_a7c4ea2a3610cee3b12dbaf28b465a701.html#a7c4ea2a3610cee3b12dbaf28b465a701) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [GetRampCount](class_a_k_1_1_c_ak_value_ramp_a87ed62234e0fd3836383517203d86d60.html#a87ed62234e0fd3836383517203d86d60) () |
|  | |
| void | [SetRampCount](class_a_k_1_1_c_ak_value_ramp_ad28f5c564efdbadc9a39bfafe7692408.html#ad28f5c564efdbadc9a39bfafe7692408) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uRampCount) |
|  | Set the current interpolation frame count. [更多...](class_a_k_1_1_c_ak_value_ramp_ad28f5c564efdbadc9a39bfafe7692408.html#ad28f5c564efdbadc9a39bfafe7692408) |
|  | |
| void | [StopRamp](class_a_k_1_1_c_ak_value_ramp_a46b485248251df5c3bc087b51f16031a.html#a46b485248251df5c3bc087b51f16031a) () |
|  | The ramp is no longer necessary; set to target [更多...](class_a_k_1_1_c_ak_value_ramp_a46b485248251df5c3bc087b51f16031a.html#a46b485248251df5c3bc087b51f16031a) |
|  | |

## 详细描述

Platform-independent parameter interpolation service for software plug-ins.

|  |  |
| --- | --- |
|  | **备注:** Algorithm performs linear interpolation. |

参见
:   - [参数节点接口的实现](soundengine_plugins.html#shared_parameter_interface)

在文件 [AkValueRamp.h](_ak_value_ramp_8h_source.html) 第 [48](_ak_value_ramp_8h_source.html#l00048) 行定义.