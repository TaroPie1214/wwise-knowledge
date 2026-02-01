# AkResourceMonitorDataSummary

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_resource_monitor_data_summary-members.html) |
[Public 属性](#pub-attribs)

AkResourceMonitorDataSummary结构体 参考

Resources data summary structure containing general information about the system
[更多...](struct_ak_resource_monitor_data_summary.html#details)

`#include <AkCallbackTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [totalCPU](struct_ak_resource_monitor_data_summary_a26911464945912bc6fd3f91ba0bca372.html#a26911464945912bc6fd3f91ba0bca372) |
|  | Pourcentage of the cpu time used for processing audio. Please note that the numbers may add up when using multiple threads. [更多...](struct_ak_resource_monitor_data_summary_a26911464945912bc6fd3f91ba0bca372.html#a26911464945912bc6fd3f91ba0bca372) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [pluginCPU](struct_ak_resource_monitor_data_summary_aa6b9ec496e0c6d798d60557004190a0f.html#aa6b9ec496e0c6d798d60557004190a0f) |
|  | Pourcentage of the cpu time used by plugin processing. Please note that the numbers may add up when using multiple threads. [更多...](struct_ak_resource_monitor_data_summary_aa6b9ec496e0c6d798d60557004190a0f.html#aa6b9ec496e0c6d798d60557004190a0f) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [physicalVoices](struct_ak_resource_monitor_data_summary_aadca481caf4a71dda3be0a53fffc0722.html#aadca481caf4a71dda3be0a53fffc0722) |
|  | Number of active physical voices [更多...](struct_ak_resource_monitor_data_summary_aadca481caf4a71dda3be0a53fffc0722.html#aadca481caf4a71dda3be0a53fffc0722) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [virtualVoices](struct_ak_resource_monitor_data_summary_a993996a995107c03545d6ac1c55d4030.html#a993996a995107c03545d6ac1c55d4030) |
|  | Number of active virtual voices [更多...](struct_ak_resource_monitor_data_summary_a993996a995107c03545d6ac1c55d4030.html#a993996a995107c03545d6ac1c55d4030) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [totalVoices](struct_ak_resource_monitor_data_summary_a8003ff25d67e5b2f88a2e6a80f2bac59.html#a8003ff25d67e5b2f88a2e6a80f2bac59) |
|  | Number of active physical and virtual voices [更多...](struct_ak_resource_monitor_data_summary_a8003ff25d67e5b2f88a2e6a80f2bac59.html#a8003ff25d67e5b2f88a2e6a80f2bac59) |
|  | |
| [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [nbActiveEvents](struct_ak_resource_monitor_data_summary_ae9501f2b6d1a65192dfd514f4c99731f.html#ae9501f2b6d1a65192dfd514f4c99731f) |
|  | Number of events triggered at a certain time [更多...](struct_ak_resource_monitor_data_summary_ae9501f2b6d1a65192dfd514f4c99731f.html#ae9501f2b6d1a65192dfd514f4c99731f) |
|  | |

## 详细描述

Resources data summary structure containing general information about the system

在文件 [AkCallbackTypes.h](_ak_callback_types_8h_source.html) 第 [303](_ak_callback_types_8h_source.html#l00303) 行定义.