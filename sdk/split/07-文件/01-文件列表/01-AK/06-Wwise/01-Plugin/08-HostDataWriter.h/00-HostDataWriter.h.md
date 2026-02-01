# HostDataWriter.h

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

HostDataWriter.h 文件参考

Wwise Authoring Plug-ins - API to write data that can be converted for the target platform.
[更多...](#details)

`#include "PluginInfoGenerator.h"`

[浏览源代码.](_host_data_writer_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [ak\_wwise\_plugin\_host\_data\_writer\_v1](structak__wwise__plugin__host__data__writer__v1.html) |
|  | Interface used to write data during sound bank generation. [更多...](structak__wwise__plugin__host__data__writer__v1.html#details) |
|  | |
| class | [AK.Wwise::Plugin::V1::DataWriter](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer.html) |
|  | Interface used to write data during sound bank generation. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer.html#details) |
|  | |
| class | [AK.Wwise::Plugin::RequestedHostInterface< DataWriter >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_data_writer_01_4.html) |
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

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AK\_WWISE\_PLUGIN\_HOST\_WRITE\_V1\_ID](_host_data_writer_8h_a4c0dde75a85e0882adc1dcc010303f5f.html#a4c0dde75a85e0882adc1dcc010303f5f)()    [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_DATA\_WRITER](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9aa1aa181e6241b63d3a1d204e403a94ad), 1) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_HOST\_WRITE\_V1\_CTOR](_host_data_writer_8h_a136303c1d26bc30ed062d130c0233d5c.html#a136303c1d26bc30ed062d130c0233d5c)() |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| using | [AK::Wwise::Plugin::V1::CHostDataWriter](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_afd451009f6669cae2d5f092544a15f96.html#afd451009f6669cae2d5f092544a15f96) = [ak\_wwise\_plugin\_host\_data\_writer\_v1](structak__wwise__plugin__host__data__writer__v1.html) |
|  | |
| using | [AK::Wwise::Plugin::V1::RequestWrite](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a367ed0e46ef3a05f90889603621c623f.html#a367ed0e46ef3a05f90889603621c623f) = RequestedHostInterface< DataWriter > |
|  | Requests a [DataWriter](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer.html "Interface used to write data during sound bank generation.") interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a367ed0e46ef3a05f90889603621c623f.html#a367ed0e46ef3a05f90889603621c623f) |
|  | |
| using | [AK::Wwise::Plugin::CHostDataWriter](namespace_a_k_1_1_wwise_1_1_plugin_a57477155e587be4bb9216ede425ea93e.html#a57477155e587be4bb9216ede425ea93e) = V1::CHostDataWriter |
|  | Latest version of the C DataWriter interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a57477155e587be4bb9216ede425ea93e.html#a57477155e587be4bb9216ede425ea93e) |
|  | |
| using | [AK::Wwise::Plugin::DataWriter](namespace_a_k_1_1_wwise_1_1_plugin_a32526a23215a4452f561220b527e12f8.html#a32526a23215a4452f561220b527e12f8) = V1::DataWriter |
|  | Latest version of the C++ DataWriter interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a32526a23215a4452f561220b527e12f8.html#a32526a23215a4452f561220b527e12f8) |
|  | |
| using | [AK::Wwise::Plugin::RequestWrite](namespace_a_k_1_1_wwise_1_1_plugin_a4b87b9ead392d9ede43fed7d3629496f.html#a4b87b9ead392d9ede43fed7d3629496f) = V1::RequestWrite |
|  | Latest version of the requested C++ DataWriter interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a4b87b9ead392d9ede43fed7d3629496f.html#a4b87b9ead392d9ede43fed7d3629496f) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_a0a7784a13a51940a70f54854680ffb9a.html#a0a7784a13a51940a70f54854680ffb9a) (DataWriter) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_ac1c1a60136371be582ba5e187f7ee675.html#ac1c1a60136371be582ba5e187f7ee675) (DataWriter) |
|  | |

## 详细描述

Wwise Authoring Plug-ins - API to write data that can be converted for the target platform.

在文件 [HostDataWriter.h](_host_data_writer_8h_source.html) 中定义.