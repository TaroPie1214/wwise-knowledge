# ak_wwise_plugin_container

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](structak__wwise__plugin__container-members.html) |
[Public 成员函数](#pub-methods) |
[静态 Public 成员函数](#pub-static-methods) |
[Public 属性](#pub-attribs)

ak\_wwise\_plugin\_container结构体 参考

Root interface allowing a logical unit (variable, library) to contain more than one interface.
[更多...](structak__wwise__plugin__container.html#details)

`#include <PluginContainer.h>`

类 ak\_wwise\_plugin\_container 继承关系图:

![](../../../images/structak__wwise__plugin__container.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| constexpr uint32\_t | [MajorSdkVersion](structak__wwise__plugin__container_a266f454e93e25d57fae5266fe965239a.html#a266f454e93e25d57fae5266fe965239a) () const |
|  | (C++) Major SDK version (ex. 2020) [更多...](structak__wwise__plugin__container_a266f454e93e25d57fae5266fe965239a.html#a266f454e93e25d57fae5266fe965239a) |
|  | |
| constexpr uint32\_t | [MinorSdkVersion](structak__wwise__plugin__container_ac5429e9b9e002969a463200817c77c87.html#ac5429e9b9e002969a463200817c77c87) () const |
|  | (C++) Minor SDK version (ex. 1) [更多...](structak__wwise__plugin__container_ac5429e9b9e002969a463200817c77c87.html#ac5429e9b9e002969a463200817c77c87) |
|  | |
| constexpr uint32\_t | [SubminorSdkVersion](structak__wwise__plugin__container_aa26fd72fad242685538aabf71df5d6f7.html#aa26fd72fad242685538aabf71df5d6f7) () const |
|  | (C++) Patch / Subminor SDK version (ex. 0) [更多...](structak__wwise__plugin__container_aa26fd72fad242685538aabf71df5d6f7.html#aa26fd72fad242685538aabf71df5d6f7) |
|  | |
| constexpr uint32\_t | [BuildSdkVersion](structak__wwise__plugin__container_ad51733888df18e4ce62d2653674a606a.html#ad51733888df18e4ce62d2653674a606a) () const |
|  | (C++) Build number (ex. 9404) [更多...](structak__wwise__plugin__container_ad51733888df18e4ce62d2653674a606a.html#ad51733888df18e4ce62d2653674a606a) |
|  | |
|  | [ak\_wwise\_plugin\_container](structak__wwise__plugin__container_a9cc1b8f521f08a3be4d4a6863c0e5e25.html#a9cc1b8f521f08a3be4d4a6863c0e5e25) () |
|  | |
|  | [ak\_wwise\_plugin\_container](structak__wwise__plugin__container_ab9f57f74d4ed605d416c3d9c30a27348.html#ab9f57f74d4ed605d416c3d9c30a27348) ([ak\_wwise\_plugin\_info](structak__wwise__plugin__info.html) \*in\_pluginInfos) |
|  | |
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) | |
| constexpr | [ak\_wwise\_plugin\_base\_interface](structak__wwise__plugin__base__interface_a7d1ff21fd409fc7363077edecb25a85d.html#a7d1ff21fd409fc7363077edecb25a85d) (decltype([m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9)) in\_interface, decltype([m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6)) in\_version) |
|  | |
| constexpr | [ak\_wwise\_plugin\_base\_interface](structak__wwise__plugin__base__interface_aef726120a06d869829ad6ec67df4f2a4.html#aef726120a06d869829ad6ec67df4f2a4) () |
|  | |
| constexpr | [ak\_wwise\_plugin\_base\_interface](structak__wwise__plugin__base__interface_acefd1ca37e4c88b6c792ec43953d3f9c.html#acefd1ca37e4c88b6c792ec43953d3f9c) (std::underlying\_type< decltype([m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9))>::type in\_interface, decltype([m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6)) in\_version) |
|  | |

|  |  |
| --- | --- |
| 静态 Public 成员函数 | |
| constexpr static uint64\_t | [SdkVersionBuildMultiplier](structak__wwise__plugin__container_a63a5652df75de44e8846b1fb7c748e17.html#a63a5652df75de44e8846b1fb7c748e17) () |
|  | |
| constexpr static uint64\_t | [SdkVersionBuildMax](structak__wwise__plugin__container_a22eb93919e3e9460a5d11d83919c74ce.html#a22eb93919e3e9460a5d11d83919c74ce) () |
|  | |
| constexpr static uint64\_t | [SdkVersionSubminorMultiplier](structak__wwise__plugin__container_aa3824dd4c777a875827ede475c6ab9aa.html#aa3824dd4c777a875827ede475c6ab9aa) () |
|  | |
| constexpr static uint64\_t | [SdkVersionSubminorMax](structak__wwise__plugin__container_ae980f5a06a5830cac7391246ff5fecc8.html#ae980f5a06a5830cac7391246ff5fecc8) () |
|  | |
| constexpr static uint64\_t | [SdkVersionMinorMultiplier](structak__wwise__plugin__container_a1bdca42ec8559576637b4f13a360d3f7.html#a1bdca42ec8559576637b4f13a360d3f7) () |
|  | |
| constexpr static uint64\_t | [SdkVersionMinorMax](structak__wwise__plugin__container_a47103b197dcb41e1ef1ae2173cd78e74.html#a47103b197dcb41e1ef1ae2173cd78e74) () |
|  | |
| constexpr static uint64\_t | [SdkVersionMajorMultiplier](structak__wwise__plugin__container_a4d4d7334c1d114fc250bf3ad8735bb8c.html#a4d4d7334c1d114fc250bf3ad8735bb8c) () |
|  | |
| constexpr static uint64\_t | [SdkVersionMajorMax](structak__wwise__plugin__container_a862b470a5f6fa433e44b7ebd092b4e39.html#a862b470a5f6fa433e44b7ebd092b4e39) () |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| uint64\_t | [m\_wwiseSdkVersion](structak__wwise__plugin__container_ad19e22254af3fc0b1fdca68880334223.html#ad19e22254af3fc0b1fdca68880334223) |
|  | Wwise Authoring version included with this SDK. [更多...](structak__wwise__plugin__container_ad19e22254af3fc0b1fdca68880334223.html#ad19e22254af3fc0b1fdca68880334223) |
|  | |
| struct [ak\_wwise\_plugin\_info](structak__wwise__plugin__info.html) \* | [m\_pluginInfos](structak__wwise__plugin__container_af8b8d528ee03cd6b7a24c907e25d500d.html#af8b8d528ee03cd6b7a24c907e25d500d) |
|  | A chained list of all the plug-ins embedded in this container [更多...](structak__wwise__plugin__container_af8b8d528ee03cd6b7a24c907e25d500d.html#af8b8d528ee03cd6b7a24c907e25d500d) |
|  | |
| - Public 属性 继承自 [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) | |
| [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9) | [m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9): 32 |
|  | Interface type (see [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9)) [更多...](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9) |
|  | |
| uint32\_t | [m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6): 32 |
|  | Version of the interface [更多...](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6) |
|  | |

## 详细描述

Root interface allowing a logical unit (variable, library) to contain more than one interface.

The container is a required element to define the base of a logical unit. It contains basic information on the build being used by the enclosed plug-ins. This allows the host to quickly determine if it should pursue loading this container or not, and might need to apply patches to fix interface variations appearing between SDK versions.

The container being versioned means this format could eventually change, but the goal was to make it generic enough to keep it stable. It's easier to add up plug-ins to extend the format than to modify it.

在文件 [PluginContainer.h](_plugin_container_8h_source.html) 第 [47](_plugin_container_8h_source.html#l00047) 行定义.