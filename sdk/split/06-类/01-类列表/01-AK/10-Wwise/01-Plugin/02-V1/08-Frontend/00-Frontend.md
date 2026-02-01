# Frontend

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [Frontend](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend-members.html) |
[类](#nested-classes) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::Frontend类 参考

[Frontend](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend.html "Frontend plug-in API for Audio plug-ins.") plug-in API for Audio plug-ins.
[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend.html#details)

`#include <Frontend.h>`

类 AK.Wwise::Plugin::V1::Frontend 继承关系图:

![](../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend.png)

|  |  |
| --- | --- |
| 类 | |
| struct | [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_1_1_interface.html) |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_1_1_interface.html#details) |
|  | |

|  |  |
| --- | --- |
| Public 类型 | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_a151ae71299798237af749b5da2171c16.html#a151ae71299798237af749b5da2171c16a84d3dfe336829d18265b073874fedc53) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_FRONTEND } |
|  | The interface type, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_a151ae71299798237af749b5da2171c16.html#a151ae71299798237af749b5da2171c16) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_afc41c0027ea2d231a92be08851f5af26.html#afc41c0027ea2d231a92be08851f5af26a826284a1bac2f8da59af76947e332c6f) = 1 } |
|  | The interface version, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_afc41c0027ea2d231a92be08851f5af26.html#afc41c0027ea2d231a92be08851f5af26) |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::RequestedHostInterface< FrontendModel >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_frontend_model_01_4.html) | |
| using | [HostInterfaceDefinition](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_frontend_model_01_4_a75d2de4f24814d36432cdfc4e60f854a.html#a75d2de4f24814d36432cdfc4e60f854a) = [HostInterfaceGlue](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html)< [FrontendModel](namespace_a_k_1_1_wwise_1_1_plugin_a4a9f58481252d4d6223ec1880f77c8eb.html#a4a9f58481252d4d6223ec1880f77c8eb), true > |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< FrontendModel, true >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| enum |  |
|  | |
| enum |  |
|  | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) = typename CPPInstance::GluedInterface |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a8bdb82de06eb8956882fe9d524e96e08.html#a8bdb82de06eb8956882fe9d524e96e08) = [FrontendModel](namespace_a_k_1_1_wwise_1_1_plugin_a4a9f58481252d4d6223ec1880f77c8eb.html#a4a9f58481252d4d6223ec1880f77c8eb) |
|  | |
| using | [CInstance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_af60fd0de7e69af6931e04ea9ec1ffc09.html#af60fd0de7e69af6931e04ea9ec1ffc09) = typename CPPInstance::Instance |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| [InterfacePtr](namespace_a_k_1_1_wwise_1_1_plugin_a9131bb705f2bd282ad65cac4efa17095.html#a9131bb705f2bd282ad65cac4efa17095) | [GetInterfacePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_a12498e450a820747b96ebb1f0e855a4e.html#a12498e450a820747b96ebb1f0e855a4e) () |
|  | |
| [CFrontend::Instance](structak__wwise__plugin__frontend__v1_af5fae19b939e1f024089549609ae8f0b.html#af5fae19b939e1f024089549609ae8f0b) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_a4cd2adf823c12f4a1a218966dd296099.html#a4cd2adf823c12f4a1a218966dd296099) () |
|  | |
| const [CFrontend::Instance](structak__wwise__plugin__frontend__v1_af5fae19b939e1f024089549609ae8f0b.html#af5fae19b939e1f024089549609ae8f0b) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_ad44a007f925d1c6d3446266c4c124d0d.html#ad44a007f925d1c6d3446266c4c124d0d) () const |
|  | |
|  | [Frontend](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_a2b4a93b0b20e8fd6d70e109f83d43194.html#a2b4a93b0b20e8fd6d70e109f83d43194) () |
|  | |
| virtual | [~Frontend](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend_ae2c59f9c8a9bf1726880001d93caf786.html#ae2c59f9c8a9bf1726880001d93caf786) () |
|  | |
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance.html) | |
| virtual | [~ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance_a38e5192dde370d925b0489a70374ff01.html#a38e5192dde370d925b0489a70374ff01) () |
|  | |
| - Public 成员函数 继承自 [AK.Wwise::Plugin::RequestedHostInterface< FrontendModel >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_frontend_model_01_4.html) | |
|  | [RequestedHostInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_frontend_model_01_4_a27e048c16f130f38db6bd3f96b0253a4.html#a27e048c16f130f38db6bd3f96b0253a4) () |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - Public 属性 继承自 [AK.Wwise::Plugin::RequestedHostInterface< FrontendModel >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_frontend_model_01_4.html) | |
| [FrontendModel](namespace_a_k_1_1_wwise_1_1_plugin_a4a9f58481252d4d6223ec1880f77c8eb.html#a4a9f58481252d4d6223ec1880f77c8eb) ::Interface & | [g\_frontendModelInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_frontend_model_01_4_ae6db1f88379847865a0185d4fb792c30.html#ae6db1f88379847865a0185d4fb792c30) = HostInterfaceDefinition::g\_cppinterface |
|  | |
| HostInterfaceDefinition::Instance & | [m\_frontendModel](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_frontend_model_01_4_a43347228a10a3c5261e1377d2b9d5791.html#a43347228a10a3c5261e1377d2b9d5791) = \*HostInterfaceDefinition::m\_instance |
|  | |
| - 静态 Public 属性 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< FrontendModel, true >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) | [g\_cppinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | The unique interface for this plug-in interface. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | |

## 详细描述

[Frontend](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_frontend.html "Frontend plug-in API for Audio plug-ins.") plug-in API for Audio plug-ins.

You must create this interface in order to support the frontend part of the user interface.

在文件 [Frontend.h](_frontend_8h_source.html) 第 [77](_frontend_8h_source.html#l00077) 行定义.