# TestService

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [TestService](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_test_service.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_test_service-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::TestService类 参考

[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_test_service.html#details)

`#include <TestService_v1.h>`

类 AK.Wwise::Plugin::V1::TestService 继承关系图:

![](../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_test_service.png)

|  |  |
| --- | --- |
| Public 类型 | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_test_service_a81f680247cd48d6bffafa0e55f61dcdb.html#a81f680247cd48d6bffafa0e55f61dcdba28943302f00e7f96328c96082e19ced3) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_TESTSERVICE } |
|  | The interface type, as requested by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_test_service_a81f680247cd48d6bffafa0e55f61dcdb.html#a81f680247cd48d6bffafa0e55f61dcdb) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_test_service_a3d86c9fd579be1a40d8357ff3c411fcc.html#a3d86c9fd579be1a40d8357ff3c411fccada9e610fabf037b3dd2a55ea4bf87369) = 1 } |
|  | The interface version, as requested by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_test_service_a3d86c9fd579be1a40d8357ff3c411fcc.html#a3d86c9fd579be1a40d8357ff3c411fcc) |
|  | |
| using | [Interface](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_test_service_a16879545b6d7957853a86dcdf91eedcc.html#a16879545b6d7957853a86dcdf91eedcc) = [CTestService](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_ab13f96dc55327bbf82fd5a8aed5a4526.html#ab13f96dc55327bbf82fd5a8aed5a4526) |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_test_service_a2beca4dd6f28185bb50d97d336597216.html#a2beca4dd6f28185bb50d97d336597216) = [CTestService::Instance](structak__wwise__plugin__test__service__v1_aeb064a7d7a39d382641dbfa2aa3cb5b9.html#aeb064a7d7a39d382641dbfa2aa3cb5b9) |
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
| uint32\_t | [TestCall](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_test_service_aa0951830c96481ebd86602fbda140fe1.html#aa0951830c96481ebd86602fbda140fe1) () |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - 静态 Public 属性 继承自 [AK.Wwise::Plugin::CBaseInterfaceGlue< CTestService >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html) | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a270936e06e5c9627548246cbebde0467.html#a270936e06e5c9627548246cbebde0467) \* | [g\_cinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a8b682b3105da8940f7ea75845254d491.html#a8b682b3105da8940f7ea75845254d491) |
|  | The unique instance of the CInterface interface. Defined at nullptr first, overridden by the Host once loaded. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a8b682b3105da8940f7ea75845254d491.html#a8b682b3105da8940f7ea75845254d491) |
|  | |

## 详细描述

在文件 [TestService\_v1.h](_test_service__v1_8h_source.html) 第 [66](_test_service__v1_8h_source.html#l00066) 行定义.