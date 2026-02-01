# PluginLinks.h

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

PluginLinks.h 文件参考

Wwise Authoring Plug-ins - Provides links to the related backend and frontend instances.
[更多...](#details)

`#include "PluginInfoGenerator.h"`

[浏览源代码.](_plugin_links_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [ak\_wwise\_plugin\_link\_backend\_v1](structak__wwise__plugin__link__backend__v1.html) |
|  | Host API to retrieve a link to the plug-in's backend instance. [更多...](structak__wwise__plugin__link__backend__v1.html#details) |
|  | |
| struct | [ak\_wwise\_plugin\_link\_frontend\_v1](structak__wwise__plugin__link__frontend__v1.html) |
|  | Host API to retrieve a link to the plug-in's frontend interfaces. [更多...](structak__wwise__plugin__link__frontend__v1.html#details) |
|  | |
| class | [AK.Wwise::Plugin::V1::LinkBackend](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_backend.html) |
|  | Host API to retrieve a link to the plug-in's backend instance. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_backend.html#details) |
|  | |
| class | [AK.Wwise::Plugin::V1::LinkFrontend](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_frontend.html) |
|  | Host API to retrieve a link to the plug-in's frontend interfaces. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_link_frontend.html#details) |
|  | |
| class | [AK.Wwise::Plugin::RequestedHostInterface< LinkBackend >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_link_backend_01_4.html) |
|  | |
| class | [AK.Wwise::Plugin::RequestedHostInterface< LinkFrontend >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_link_frontend_01_4.html) |
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
| #define | [AK\_WWISE\_PLUGIN\_LINK\_BACKEND\_ID](_plugin_links_8h_a78ccbc1fa3ea47add69adea2c6568563.html#a78ccbc1fa3ea47add69adea2c6568563)()    [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_LINK\_BACKEND](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a7e6d9382217615a4d0205bcd87ffb8f8), 1) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_LINK\_BACKEND\_CTOR](_plugin_links_8h_a4162c8512e4df0feb0db4d666d19f2f7.html#a4162c8512e4df0feb0db4d666d19f2f7)(in\_pluginInfo, in\_data) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_LINK\_FRONTEND\_ID](_plugin_links_8h_af653e726574e860e700b5a12ca992172.html#af653e726574e860e700b5a12ca992172)()    [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_LINK\_FRONTEND](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a487278fb36df685b23d6ffbb7512b80a), 1) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_LINK\_FRONTEND\_CTOR](_plugin_links_8h_a8ec18de4da0513653dfed71796cac161.html#a8ec18de4da0513653dfed71796cac161)(in\_pluginInfo, in\_data) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| using | [AK::Wwise::Plugin::V1::CLinkBackend](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_aaa3fe7d7e70babc8d8aa9e0b88171ae6.html#aaa3fe7d7e70babc8d8aa9e0b88171ae6) = [ak\_wwise\_plugin\_link\_backend\_v1](structak__wwise__plugin__link__backend__v1.html) |
|  | |
| using | [AK::Wwise::Plugin::V1::CLinkFrontend](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_ae46b0c1760947987e45c7c736fafbc57.html#ae46b0c1760947987e45c7c736fafbc57) = [ak\_wwise\_plugin\_link\_frontend\_v1](structak__wwise__plugin__link__frontend__v1.html) |
|  | |
| using | [AK::Wwise::Plugin::V1::RequestLinkBackend](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a11cb14ccd572dab75f29946408d5c381.html#a11cb14ccd572dab75f29946408d5c381) = RequestedHostInterface< LinkBackend > |
|  | |
| using | [AK::Wwise::Plugin::V1::RequestLinkFrontend](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a7d7050323515e05e75e34c71aaa8c3ae.html#a7d7050323515e05e75e34c71aaa8c3ae) = RequestedHostInterface< LinkFrontend > |
|  | |
| using | [AK::Wwise::Plugin::CLinkBackend](namespace_a_k_1_1_wwise_1_1_plugin_acac65e4a746e5104e04b138a7889d3c5.html#acac65e4a746e5104e04b138a7889d3c5) = V1::CLinkBackend |
|  | Latest version of the C LinkBackend interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_acac65e4a746e5104e04b138a7889d3c5.html#acac65e4a746e5104e04b138a7889d3c5) |
|  | |
| using | [AK::Wwise::Plugin::LinkBackend](namespace_a_k_1_1_wwise_1_1_plugin_a3b9372eb28f4ed69d52c8b253b7542fd.html#a3b9372eb28f4ed69d52c8b253b7542fd) = V1::LinkBackend |
|  | Latest version of the C++ LinkBackend interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a3b9372eb28f4ed69d52c8b253b7542fd.html#a3b9372eb28f4ed69d52c8b253b7542fd) |
|  | |
| using | [AK::Wwise::Plugin::RequestLinkBackend](namespace_a_k_1_1_wwise_1_1_plugin_a4d4fbbc7cf09da60c669ce79799feba7.html#a4d4fbbc7cf09da60c669ce79799feba7) = V1::RequestLinkBackend |
|  | Latest version of the requested C++ LinkBackend interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a4d4fbbc7cf09da60c669ce79799feba7.html#a4d4fbbc7cf09da60c669ce79799feba7) |
|  | |
| using | [AK::Wwise::Plugin::CLinkFrontend](namespace_a_k_1_1_wwise_1_1_plugin_aff9067bc56d00cc3f5362d072df8337b.html#aff9067bc56d00cc3f5362d072df8337b) = V1::CLinkFrontend |
|  | Latest version of the C LinkFrontend interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_aff9067bc56d00cc3f5362d072df8337b.html#aff9067bc56d00cc3f5362d072df8337b) |
|  | |
| using | [AK::Wwise::Plugin::LinkFrontend](namespace_a_k_1_1_wwise_1_1_plugin_a54cf853c2d54b39672aa929f71b0c0c3.html#a54cf853c2d54b39672aa929f71b0c0c3) = V1::LinkFrontend |
|  | Latest version of the C++ LinkFrontend interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a54cf853c2d54b39672aa929f71b0c0c3.html#a54cf853c2d54b39672aa929f71b0c0c3) |
|  | |
| using | [AK::Wwise::Plugin::RequestLinkFrontend](namespace_a_k_1_1_wwise_1_1_plugin_ae784aa1d2e816b127f160a83410ffed8.html#ae784aa1d2e816b127f160a83410ffed8) = V1::RequestLinkFrontend |
|  | Latest version of the requested C++ LinkFrontend interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_ae784aa1d2e816b127f160a83410ffed8.html#ae784aa1d2e816b127f160a83410ffed8) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_ad4e9968230f88b574a0e597384cc87fc.html#ad4e9968230f88b574a0e597384cc87fc) (LinkBackend) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_af187e822bc5afe666401ec3a6f0f3f66.html#af187e822bc5afe666401ec3a6f0f3f66) (LinkBackend) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_ad0c8bcbead1331781fa72bb8a869626b.html#ad0c8bcbead1331781fa72bb8a869626b) (LinkFrontend) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a8f2607f76e734a1b740ae553afb70d21.html#a8f2607f76e734a1b740ae553afb70d21) (LinkFrontend) |
|  | |

## 详细描述

Wwise Authoring Plug-ins - Provides links to the related backend and frontend instances.

在文件 [PluginLinks.h](_plugin_links_8h_source.html) 中定义.