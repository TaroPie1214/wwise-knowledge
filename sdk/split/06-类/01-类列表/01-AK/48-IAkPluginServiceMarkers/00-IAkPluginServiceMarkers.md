# IAkPluginServiceMarkers

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkPluginServiceMarkers](class_a_k_1_1_i_ak_plugin_service_markers.html)

[所有成员列表](class_a_k_1_1_i_ak_plugin_service_markers-members.html) |
[类](#nested-classes) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods)

AK::IAkPluginServiceMarkers类 参考abstract

Interface for the markers service.
[更多...](class_a_k_1_1_i_ak_plugin_service_markers.html#details)

`#include <IAkPlugin.h>`

类 AK::IAkPluginServiceMarkers 继承关系图:

![](../../../../images/class_a_k_1_1_i_ak_plugin_service_markers.png)

|  |  |
| --- | --- |
| 类 | |
| class | [IAkMarkerNotificationService](class_a_k_1_1_i_ak_plugin_service_markers_1_1_i_ak_marker_notification_service.html) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual [IAkMarkerNotificationService](class_a_k_1_1_i_ak_plugin_service_markers_1_1_i_ak_marker_notification_service.html) \* | [CreateMarkerNotificationService](class_a_k_1_1_i_ak_plugin_service_markers_adc860123c5af8918edcc787a8459d65b.html#adc860123c5af8918edcc787a8459d65b) ([IAkSourcePluginContext](class_a_k_1_1_i_ak_source_plugin_context.html) \*in\_pSourcePluginContext)=0 |
|  | |
| virtual void | [TerminateMarkerNotificationService](class_a_k_1_1_i_ak_plugin_service_markers_a4329a480eaff84f6930af67a4076dd5c.html#a4329a480eaff84f6930af67a4076dd5c) ([IAkMarkerNotificationService](class_a_k_1_1_i_ak_plugin_service_markers_1_1_i_ak_marker_notification_service.html) \*io\_pMarkerNotificationService)=0 |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| virtual | [~IAkPluginServiceMarkers](class_a_k_1_1_i_ak_plugin_service_markers_afff7d1aa5039cd322fa0ea0627e62e86.html#afff7d1aa5039cd322fa0ea0627e62e86) () |
|  | |
| - Protected 成员函数 继承自 [AK::IAkPluginService](class_a_k_1_1_i_ak_plugin_service.html) | |
| virtual | [~IAkPluginService](class_a_k_1_1_i_ak_plugin_service_af880be6eab8f4f3cd124ec8db8b562de.html#af880be6eab8f4f3cd124ec8db8b562de) () |
|  | |

## 详细描述

Interface for the markers service.

在文件 [IAkPlugin.h](_i_ak_plugin_8h_source.html) 第 [1949](_i_ak_plugin_8h_source.html#l01949) 行定义.