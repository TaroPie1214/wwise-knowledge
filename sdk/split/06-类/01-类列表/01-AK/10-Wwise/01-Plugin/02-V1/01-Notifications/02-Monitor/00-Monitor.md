# Monitor

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [Notifications](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications.html)
- [Monitor](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_monitor.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_monitor-members.html) |
[类](#nested-classes) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::Notifications::Monitor类 参考abstract

API for Sound Engine's [Monitor](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_monitor.html "API for Sound Engine's Monitor Data notification.") Data notification.
[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_monitor.html#details)

`#include <Notifications.h>`

类 AK.Wwise::Plugin::V1::Notifications::Monitor 继承关系图:

![](../../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_monitor.png)

|  |  |
| --- | --- |
| 类 | |
| struct | [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_monitor_1_1_interface.html) |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_monitor_1_1_interface.html#details) |
|  | |

|  |  |
| --- | --- |
| Public 类型 | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_monitor_a2c835b13bc0e5c43a0b330d192794418.html#a2c835b13bc0e5c43a0b330d192794418a5c5909e7f0106da44377f17f1a8641e1) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NOTIFICATIONS\_MONITOR } |
|  | The interface type, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_monitor_a2c835b13bc0e5c43a0b330d192794418.html#a2c835b13bc0e5c43a0b330d192794418) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_monitor_a3cf5e415f7855d013ee0901268aeef42.html#a3cf5e415f7855d013ee0901268aeef42ad9b7e85e9e3d9a2b4f278cf6758632b0) = 1 } |
|  | The interface version, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_monitor_a3cf5e415f7855d013ee0901268aeef42.html#a3cf5e415f7855d013ee0901268aeef42) |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_monitor_a5616c8d09bff74cdd28cce22521b3b9b.html#a5616c8d09bff74cdd28cce22521b3b9b) = [CMonitor::Instance](structak__wwise__plugin__notifications__monitor__v1_aec55cec473eaf42d4a1b95537417323d.html#aec55cec473eaf42d4a1b95537417323d) |
|  | Base instance type for receiving Sound Engine's monitoring data. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_monitor_a5616c8d09bff74cdd28cce22521b3b9b.html#a5616c8d09bff74cdd28cce22521b3b9b) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| [InterfacePtr](namespace_a_k_1_1_wwise_1_1_plugin_a9131bb705f2bd282ad65cac4efa17095.html#a9131bb705f2bd282ad65cac4efa17095) | [GetInterfacePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_monitor_a55e67339c40eb0733d4fb45126e59973.html#a55e67339c40eb0733d4fb45126e59973) () |
|  | |
| [CMonitor::Instance](structak__wwise__plugin__notifications__monitor__v1_aec55cec473eaf42d4a1b95537417323d.html#aec55cec473eaf42d4a1b95537417323d) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_monitor_a6ce75ff1a9e6931e9dc0dde310e78804.html#a6ce75ff1a9e6931e9dc0dde310e78804) () |
|  | |
| const [CMonitor::Instance](structak__wwise__plugin__notifications__monitor__v1_aec55cec473eaf42d4a1b95537417323d.html#aec55cec473eaf42d4a1b95537417323d) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_monitor_a38fad37940c646a82f31dc4ccfcecc6b.html#a38fad37940c646a82f31dc4ccfcecc6b) () const |
|  | |
|  | [Monitor](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_monitor_a18597377ad5112c55a964018878301c1.html#a18597377ad5112c55a964018878301c1) () |
|  | |
| virtual | [~Monitor](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_monitor_a719b7e811d52354cfd7f80aa2fa4a556.html#a719b7e811d52354cfd7f80aa2fa4a556) () |
|  | |
| virtual void | [NotifyMonitorData](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_monitor_aaa00d3622c1d400d5150261b0f7820f1.html#aaa00d3622c1d400d5150261b0f7820f1) ([AkTimeMs](_ak_typedefs_8h_a8a4d0aa5dba6f9922d6b7b3e48958b24.html#a8a4d0aa5dba6f9922d6b7b3e48958b24) in\_iTimeStamp, const [MonitorData](struct_a_k_1_1_wwise_1_1_plugin_1_1_monitor_data.html) \*in\_pMonitorDataArray, unsigned int in\_uMonitorDataArraySize, bool in\_bIsRealtime)=0 |
|  | Received a new [Monitor](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_monitor.html "API for Sound Engine's Monitor Data notification.") Data blob. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_monitor_aaa00d3622c1d400d5150261b0f7820f1.html#aaa00d3622c1d400d5150261b0f7820f1) |
|  | |
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance.html) | |
| virtual | [~ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance_a38e5192dde370d925b0489a70374ff01.html#a38e5192dde370d925b0489a70374ff01) () |
|  | |

## 详细描述

API for Sound Engine's [Monitor](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_monitor.html "API for Sound Engine's Monitor Data notification.") Data notification.

在文件 [Notifications.h](_notifications_8h_source.html) 第 [104](_notifications_8h_source.html#l00104) 行定义.