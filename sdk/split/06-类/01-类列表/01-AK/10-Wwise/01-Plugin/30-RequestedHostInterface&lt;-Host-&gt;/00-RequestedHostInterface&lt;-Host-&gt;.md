# RequestedHostInterface&lt; Host &gt;

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [RequestedHostInterface< Host >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_host_01_4.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_host_01_4-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AK.Wwise::Plugin::RequestedHostInterface< Host >类 参考

`#include <Host.h>`

类 AK.Wwise::Plugin::RequestedHostInterface< Host > 继承关系图:

![](../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_host_01_4.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [HostInterfaceDefinition](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_host_01_4_a1f9fa5c7f07672d2e63ec6578dcea21f.html#a1f9fa5c7f07672d2e63ec6578dcea21f) = [HostInterfaceGlue](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html)< [Host](namespace_a_k_1_1_wwise_1_1_plugin_af6f9dc5d367c3383c37f96fe9e1b943f.html#af6f9dc5d367c3383c37f96fe9e1b943f), true > |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< Host, true >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| enum |  |
|  | |
| enum |  |
|  | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) = typename CPPInstance::GluedInterface |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a8bdb82de06eb8956882fe9d524e96e08.html#a8bdb82de06eb8956882fe9d524e96e08) = [Host](namespace_a_k_1_1_wwise_1_1_plugin_af6f9dc5d367c3383c37f96fe9e1b943f.html#af6f9dc5d367c3383c37f96fe9e1b943f) |
|  | |
| using | [CInstance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_af60fd0de7e69af6931e04ea9ec1ffc09.html#af60fd0de7e69af6931e04ea9ec1ffc09) = typename CPPInstance::Instance |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::V1::Notifications::Host\_](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_host__.html) | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_host___ac7a98851ae6442a682c98e71f92b5681.html#ac7a98851ae6442a682c98e71f92b5681a46c703a2c904893fbff7c093c1a1437e) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NOTIFICATIONS\_HOST } |
|  | The interface type, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_host___ac7a98851ae6442a682c98e71f92b5681.html#ac7a98851ae6442a682c98e71f92b5681) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_host___a08695bf572d49cb8eb3a5784ae6b8645.html#a08695bf572d49cb8eb3a5784ae6b8645af08637508b586c6de5f660d29c258aa9) = 1 } |
|  | The interface version, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_host___a08695bf572d49cb8eb3a5784ae6b8645.html#a08695bf572d49cb8eb3a5784ae6b8645) |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_host___a5535b60f002f1a0ff92a22ea8e8f8ae5.html#a5535b60f002f1a0ff92a22ea8e8f8ae5) = [CHost\_::Instance](structak__wwise__plugin__notifications__host__v1_a2be163bb727db442e2a06b70ce45dcd0.html#a2be163bb727db442e2a06b70ce45dcd0) |
|  | Base instance type for receiving notifications on host changes events. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_host___a5535b60f002f1a0ff92a22ea8e8f8ae5.html#a5535b60f002f1a0ff92a22ea8e8f8ae5) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [RequestedHostInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_host_01_4_a35a437da9be2eca7b9e39ff3a1de6172.html#a35a437da9be2eca7b9e39ff3a1de6172) () |
|  | |
| - Public 成员函数 继承自 [AK.Wwise::Plugin::V1::Notifications::Host\_](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_host__.html) | |
| [InterfacePtr](namespace_a_k_1_1_wwise_1_1_plugin_a9131bb705f2bd282ad65cac4efa17095.html#a9131bb705f2bd282ad65cac4efa17095) | [GetInterfacePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_host___a68c63418eec79544d91415fdc3c3208d.html#a68c63418eec79544d91415fdc3c3208d) () |
|  | |
| [CHost\_::Instance](structak__wwise__plugin__notifications__host__v1_a2be163bb727db442e2a06b70ce45dcd0.html#a2be163bb727db442e2a06b70ce45dcd0) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_host___afc37ae3469f7e94594d65f6d9dc6a82a.html#afc37ae3469f7e94594d65f6d9dc6a82a) () |
|  | |
| const [CHost\_::Instance](structak__wwise__plugin__notifications__host__v1_a2be163bb727db442e2a06b70ce45dcd0.html#a2be163bb727db442e2a06b70ce45dcd0) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_host___a6f879c454f87738062cda8b4ddcf5430.html#a6f879c454f87738062cda8b4ddcf5430) () const |
|  | |
|  | [Host\_](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_host___a24a7776948b798a8ea69f5400706e7e6.html#a24a7776948b798a8ea69f5400706e7e6) () |
|  | |
| virtual | [~Host\_](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_host___a99e919b0de2e4f56d0a974c40f7915ee.html#a99e919b0de2e4f56d0a974c40f7915ee) () |
|  | |
| virtual void | [NotifyCurrentPlatformChanged](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_host___acfae550cb659b0ce04c0b43761471323.html#acfae550cb659b0ce04c0b43761471323) (const GUID &in\_guidCurrentPlatform) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [Host](namespace_a_k_1_1_wwise_1_1_plugin_af6f9dc5d367c3383c37f96fe9e1b943f.html#af6f9dc5d367c3383c37f96fe9e1b943f) ::[Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_host___1_1_interface.html) & | [g\_hostInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_host_01_4_a0bde3d2d74f96b79d1d03ffc7a3a65c3.html#a0bde3d2d74f96b79d1d03ffc7a3a65c3) = HostInterfaceDefinition::g\_cppinterface |
|  | |
| HostInterfaceDefinition::Instance & | [m\_host](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_host_01_4_adb63d05e1ac3005634e0c771feb2e5d1.html#adb63d05e1ac3005634e0c771feb2e5d1) = \*HostInterfaceDefinition::m\_instance |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - 静态 Public 属性 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< Host, true >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) | [g\_cppinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | The unique interface for this plug-in interface. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | |

## 详细描述

在文件 [Host.h](_host_8h_source.html) 第 [164](_host_8h_source.html#l00164) 行定义.