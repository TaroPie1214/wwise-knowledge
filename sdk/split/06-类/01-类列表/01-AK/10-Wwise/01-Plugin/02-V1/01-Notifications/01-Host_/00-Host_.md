# Host_

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [Notifications](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications.html)
- [Host\_](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_host__.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_host__-members.html) |
[类](#nested-classes) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::Notifications::Host\_类 参考

API to receive host's update notifications.
[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_host__.html#details)

`#include <Host.h>`

类 AK.Wwise::Plugin::V1::Notifications::Host\_ 继承关系图:

![](../../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_host__.png)

|  |  |
| --- | --- |
| 类 | |
| struct | [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_host___1_1_interface.html) |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_host___1_1_interface.html#details) |
|  | |

|  |  |
| --- | --- |
| Public 类型 | |
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
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance.html) | |
| virtual | [~ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance_a38e5192dde370d925b0489a70374ff01.html#a38e5192dde370d925b0489a70374ff01) () |
|  | |

## 详细描述

API to receive host's update notifications.

在文件 [Host.h](_v1_2_host_8h_source.html) 第 [391](_v1_2_host_8h_source.html#l00391) 行定义.