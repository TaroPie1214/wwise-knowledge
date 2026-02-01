# SinkDevices.h

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

SinkDevices.h 文件参考

Wwise Authoring Plug-ins - Plug-in that lists supported output devices.
[更多...](#details)

`#include "PluginInfoGenerator.h"`

[浏览源代码.](_sink_devices_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [ak\_wwise\_plugin\_sink\_devices\_v1](structak__wwise__plugin__sink__devices__v1.html) |
|  | Device enumerator for sink plug-ins. [更多...](structak__wwise__plugin__sink__devices__v1.html#details) |
|  | |
| class | [AK.Wwise::Plugin::V1::SinkDevices](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_sink_devices.html) |
|  | C++ API to provide device enumeration for sink plug-ins. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_sink_devices.html#details) |
|  | |
| struct | [AK.Wwise::Plugin::V1::SinkDevices::Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_sink_devices_1_1_interface.html) |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_sink_devices_1_1_interface.html#details) |
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
| #define | [AK\_WWISE\_PLUGIN\_SINK\_DEVICES\_V1\_ID](_sink_devices_8h_aab9c7a90deefe0e7f9101e6269acdcb7.html#aab9c7a90deefe0e7f9101e6269acdcb7)()    [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_SINK\_DEVICES](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a821f9229a08f07baaf0783425ced53d1), 1) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_SINK\_DEVICES\_V1\_CTOR](_sink_devices_8h_af54f9c5ca985706cdafcea1c4ac5af03.html#af54f9c5ca985706cdafcea1c4ac5af03)(in\_pluginInfo, in\_data) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| using | [AK::Wwise::Plugin::V1::CSinkDevices](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a52aaccf63c00774a69e2a66a10163c9a.html#a52aaccf63c00774a69e2a66a10163c9a) = [ak\_wwise\_plugin\_sink\_devices\_v1](structak__wwise__plugin__sink__devices__v1.html) |
|  | Device enumerator for sink plug-ins. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a52aaccf63c00774a69e2a66a10163c9a.html#a52aaccf63c00774a69e2a66a10163c9a) |
|  | |
| using | [AK::Wwise::Plugin::CSinkDevices](namespace_a_k_1_1_wwise_1_1_plugin_a8f050047725e6e92dac6a425db59301b.html#a8f050047725e6e92dac6a425db59301b) = V1::CSinkDevices |
|  | Latest version of the C SinkDevices interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a8f050047725e6e92dac6a425db59301b.html#a8f050047725e6e92dac6a425db59301b) |
|  | |
| using | [AK::Wwise::Plugin::SinkDevices](namespace_a_k_1_1_wwise_1_1_plugin_afd1d6878bfb9cc5c27a1741a7a9cd5d1.html#afd1d6878bfb9cc5c27a1741a7a9cd5d1) = V1::SinkDevices |
|  | Latest version of the C++ SinkDevices interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_afd1d6878bfb9cc5c27a1741a7a9cd5d1.html#afd1d6878bfb9cc5c27a1741a7a9cd5d1) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_a39373dae3c76178133d93dde57058299.html#a39373dae3c76178133d93dde57058299) (SinkDevices) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a20d33cd469f7ec76283f884df02779eb.html#a20d33cd469f7ec76283f884df02779eb) (SinkDevices) |
|  | |

## 详细描述

Wwise Authoring Plug-ins - Plug-in that lists supported output devices.

Provides a list of up-to-date device IDs that can be used to instantiate a new Sound Engine sink.

参见
:   C interfaces

    - [ak\_wwise\_plugin\_sink\_devices\_v1](structak__wwise__plugin__sink__devices__v1.html)
:   C++ interfaces

    - [AK::Wwise::Plugin::SinkDevices](namespace_a_k_1_1_wwise_1_1_plugin_afd1d6878bfb9cc5c27a1741a7a9cd5d1.html#afd1d6878bfb9cc5c27a1741a7a9cd5d1)

在文件 [SinkDevices.h](_sink_devices_8h_source.html) 中定义.