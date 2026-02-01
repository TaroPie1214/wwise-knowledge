# TestService

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V2](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v2.html)
- [TestService](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_test_service.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_test_service-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V2::TestService类 参考

[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_test_service.html#details)

`#include <TestService.h>`

类 AK.Wwise::Plugin::V2::TestService 继承关系图:

![](../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_test_service.png)

|  |  |
| --- | --- |
| Public 类型 | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_test_service_adf18464697d54a3633a4816a1f742238.html#adf18464697d54a3633a4816a1f742238a2dcdb567fd62659b5fb287134b2a84e1) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_TESTSERVICE } |
|  | The interface type, as requested by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_test_service_adf18464697d54a3633a4816a1f742238.html#adf18464697d54a3633a4816a1f742238) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_test_service_adf52b2d35071f778e8548bd80b0fb4ed.html#adf52b2d35071f778e8548bd80b0fb4edafa7a3fa5302908c9a0003cfabae6a8a8) = 2 } |
|  | The interface version, as requested by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_test_service_adf52b2d35071f778e8548bd80b0fb4ed.html#adf52b2d35071f778e8548bd80b0fb4ed) |
|  | |
| using | [Interface](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_test_service_a9d6c077168dc17a3c8258147f2a735b7.html#a9d6c077168dc17a3c8258147f2a735b7) = [CTestService](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v2_a0e1b0deb15b99022916424617bb4cd25.html#a0e1b0deb15b99022916424617bb4cd25) |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_test_service_ac9e0e8061de95945ae0a0153cecfc17c.html#ac9e0e8061de95945ae0a0153cecfc17c) = [CTestService::Instance](structak__wwise__plugin__test__service__v2_a17c2ec8a554d4900797377f90f539981.html#a17c2ec8a554d4900797377f90f539981) |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::CBaseInstanceGlue< CTestService >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue.html) | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue_aff6221118cb1d81f1e67f1932fb66b60.html#aff6221118cb1d81f1e67f1932fb66b60) = typename CInterface::Instance |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::CBaseInterfaceGlue< CTestService >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html) | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a270936e06e5c9627548246cbebde0467.html#a270936e06e5c9627548246cbebde0467) = [CTestService](namespace_a_k_1_1_wwise_1_1_plugin_a153b1d2e36ab2eb663b0830baf3b1d72.html#a153b1d2e36ab2eb663b0830baf3b1d72) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| uint32\_t | [TestCall](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_test_service_a1be381a53d1fbac0e2c011f518272433.html#a1be381a53d1fbac0e2c011f518272433) () const |
|  | |
| uint32\_t | [NewCall](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_test_service_a3bbe5aa7d9c988e7d68141aa55a1c22b.html#a3bbe5aa7d9c988e7d68141aa55a1c22b) () const |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - 静态 Public 属性 继承自 [AK.Wwise::Plugin::CBaseInterfaceGlue< CTestService >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html) | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a270936e06e5c9627548246cbebde0467.html#a270936e06e5c9627548246cbebde0467) \* | [g\_cinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a8b682b3105da8940f7ea75845254d491.html#a8b682b3105da8940f7ea75845254d491) |
|  | The unique instance of the CInterface interface. Defined at nullptr first, overridden by the Host once loaded. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a8b682b3105da8940f7ea75845254d491.html#a8b682b3105da8940f7ea75845254d491) |
|  | |

## 详细描述

在文件 [TestService.h](_test_service_8h_source.html) 第 [67](_test_service_8h_source.html#l00067) 行定义.