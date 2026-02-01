# Host.h

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

Host.h 文件参考

Wwise Authoring Plug-ins - API to request host's current state and services.
[更多...](#details)

`#include "./V1/Host.h"`  
`#include "PlatformID.h"`  
`#include "PluginInfoGenerator.h"`

[浏览源代码.](_host_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [ak\_wwise\_plugin\_host\_v2](structak__wwise__plugin__host__v2.html) |
|  | API to request host's current state and services. [更多...](structak__wwise__plugin__host__v2.html#details) |
|  | |
| class | [AK.Wwise::Plugin::V2::Host](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_host.html) |
|  | API to request host's current state and services. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_host.html#details) |
|  | |
| class | [AK.Wwise::Plugin::RequestedHostInterface< Host >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_host_01_4.html) |
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
|  | [AK::Wwise::Plugin::V2](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v2.html) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AK\_WWISE\_PLUGIN\_HOST\_V2\_ID](_host_8h_a00e54ea69000b77560ebe4f0f2a74ec7.html#a00e54ea69000b77560ebe4f0f2a74ec7)()    [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9af1c18a159e804b70aa8e3bafd53ccfe1), 2) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_HOST\_V2\_CTOR](_host_8h_afbc4e5d660f04bfaeb63eab3cc8b9145.html#afbc4e5d660f04bfaeb63eab3cc8b9145)() |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| using | [AK::Wwise::Plugin::V2::CHost](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v2_a5af2573092f8990f393f30066f9ea80c.html#a5af2573092f8990f393f30066f9ea80c) = [ak\_wwise\_plugin\_host\_v2](structak__wwise__plugin__host__v2.html) |
|  | |
| using | [AK::Wwise::Plugin::V2::RequestHost](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v2_ae121d77285491869dcc7e169b2342133.html#ae121d77285491869dcc7e169b2342133) = RequestedHostInterface< Host > |
|  | Requests a [Host](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_host.html "API to request host's current state and services.") interface, provided as m\_host variable. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v2_ae121d77285491869dcc7e169b2342133.html#ae121d77285491869dcc7e169b2342133) |
|  | |
| using | [AK::Wwise::Plugin::CHost](namespace_a_k_1_1_wwise_1_1_plugin_aa96b27e8272b257ab8bf4cedc96122ca.html#aa96b27e8272b257ab8bf4cedc96122ca) = V2::CHost |
|  | Latest version of the C Host interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_aa96b27e8272b257ab8bf4cedc96122ca.html#aa96b27e8272b257ab8bf4cedc96122ca) |
|  | |
| using | [AK::Wwise::Plugin::Host](namespace_a_k_1_1_wwise_1_1_plugin_af6f9dc5d367c3383c37f96fe9e1b943f.html#af6f9dc5d367c3383c37f96fe9e1b943f) = V2::Host |
|  | Latest version of the C++ Host interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_af6f9dc5d367c3383c37f96fe9e1b943f.html#af6f9dc5d367c3383c37f96fe9e1b943f) |
|  | |
| using | [AK::Wwise::Plugin::RequestHost](namespace_a_k_1_1_wwise_1_1_plugin_a4ef1b0bee4438ded222bf1a691d61722.html#a4ef1b0bee4438ded222bf1a691d61722) = V2::RequestHost |
|  | Latest version of the requested C++ Host interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a4ef1b0bee4438ded222bf1a691d61722.html#a4ef1b0bee4438ded222bf1a691d61722) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_ae0968ed5f70b5d9ad77150d7149f3d40.html#ae0968ed5f70b5d9ad77150d7149f3d40) (Host) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a0014bc14ffa048fa75715061da406527.html#a0014bc14ffa048fa75715061da406527) (Host) |
|  | |

## 详细描述

Wwise Authoring Plug-ins - API to request host's current state and services.

在文件 [Host.h](_host_8h_source.html) 中定义.