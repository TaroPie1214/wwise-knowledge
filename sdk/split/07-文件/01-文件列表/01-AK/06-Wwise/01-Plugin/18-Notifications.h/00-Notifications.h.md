# Notifications.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Wwise](dir_6ea5b71cdf4c60d3386ed2d84846331f.html)
- [Plugin](dir_00900ac4c96da97e1d767c263ed2fa21.html)

[类](#nested-classes) |
[命名空间](#namespaces) |
[宏定义](#define-members) |
[类型定义](#typedef-members) |
[函数](#func-members)

Notifications.h 文件参考

Wwise Authoring Plug-ins - APIs for different host notifications.
[更多...](#details)

`#include "PluginInfoGenerator.h"`

[浏览源代码.](_notifications_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [ak\_wwise\_plugin\_notifications\_monitor\_v1](structak__wwise__plugin__notifications__monitor__v1.html) |
|  | API for Sound Engine's Monitor Data notification. [更多...](structak__wwise__plugin__notifications__monitor__v1.html#details) |
|  | |
| class | [AK.Wwise::Plugin::V1::Notifications::Monitor](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_monitor.html) |
|  | API for Sound Engine's [Monitor](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_monitor.html "API for Sound Engine's Monitor Data notification.") Data notification. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_monitor.html#details) |
|  | |
| struct | [AK.Wwise::Plugin::V1::Notifications::Monitor::Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_monitor_1_1_interface.html) |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_monitor_1_1_interface.html#details) |
|  | |

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |
| namespace | [AK.Wwise](namespace_a_k_1_1_wwise.html) |
|  | |
|  | [AK::Wwise::Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html) |
|  | |
|  | [AK::Wwise::Plugin::V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html) |
|  | |
|  | [AK::Wwise::Plugin::V1::Notifications](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications.html) |
|  | [Notifications](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications.html "Notifications namespace") namespace |
|  | |
|  | [AK::Wwise::Plugin::Notifications](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications.html) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AK\_WWISE\_PLUGIN\_NOTIFICATIONS\_MONITOR\_V1\_ID](_notifications_8h_a14c85492946e908bdcc0919a4185f67f.html#a14c85492946e908bdcc0919a4185f67f)()    [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NOTIFICATIONS\_MONITOR](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9ac04b4cc07950e34f1b4aa9f93ec6d5a3), 1) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_NOTIFICATIONS\_MONITOR\_V1\_CTOR](_notifications_8h_af89e4faea1bc113dacdb94b643f4fd44.html#af89e4faea1bc113dacdb94b643f4fd44)(in\_pluginInfo, in\_data) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| using | [AK::Wwise::Plugin::V1::Notifications::CMonitor](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_a6c8e999d0f733e9baf8876e151e3ffd9.html#a6c8e999d0f733e9baf8876e151e3ffd9) = [ak\_wwise\_plugin\_notifications\_monitor\_v1](structak__wwise__plugin__notifications__monitor__v1.html) |
|  | |
| using | [AK::Wwise::Plugin::Notifications::CMonitor](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_a60e1b670d92819cd4166fcf41cdf4ab7.html#a60e1b670d92819cd4166fcf41cdf4ab7) = V1::Notifications::CMonitor |
|  | Latest version of the C [Monitor](namespace_a_k_1_1_monitor.html) notification interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_a60e1b670d92819cd4166fcf41cdf4ab7.html#a60e1b670d92819cd4166fcf41cdf4ab7) |
|  | |
| using | [AK::Wwise::Plugin::Notifications::Monitor](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_a3693c119618107df7c86de8a4a887320.html#a3693c119618107df7c86de8a4a887320) = V1::Notifications::Monitor |
|  | Latest version of the C++ [Monitor](namespace_a_k_1_1_monitor.html) notification interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_1_1_notifications_a3693c119618107df7c86de8a4a887320.html#a3693c119618107df7c86de8a4a887320) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_ae3dce9779d615c919ba9d4bc1b356444.html#ae3dce9779d615c919ba9d4bc1b356444) (Notifications::Monitor) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a58b2c038aa942d74d243075933a24571.html#a58b2c038aa942d74d243075933a24571) (Notifications::Monitor) |
|  | |

## 详细描述

Wwise Authoring Plug-ins - APIs for different host notifications.

These are notifications not fitting in the other host services. For every host service, there is usually a notification to tell your plug-in something changed and to update data.

These are independent notifications, not linked on other services.

在文件 [Notifications.h](_notifications_8h_source.html) 中定义.