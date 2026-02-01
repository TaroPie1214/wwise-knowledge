# ak_wwise_plugin_host_reference_set_v1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](structak__wwise__plugin__host__reference__set__v1-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

ak\_wwise\_plugin\_host\_reference\_set\_v1结构体 参考

Interface used to interact with reference sets.
[更多...](structak__wwise__plugin__host__reference__set__v1.html#details)

`#include <HostReferenceSet.h>`

类 ak\_wwise\_plugin\_host\_reference\_set\_v1 继承关系图:

![](../../../images/structak__wwise__plugin__host__reference__set__v1.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [Instance](structak__wwise__plugin__host__reference__set__v1_adb211da55a8e4b4fcd675851f95b1895.html#adb211da55a8e4b4fcd675851f95b1895) = [ak\_wwise\_plugin\_host\_reference\_set\_instance\_v1](structak__wwise__plugin__host__reference__set__instance__v1.html) |
|  | Base host-provided instance type for [ak\_wwise\_plugin\_host\_reference\_set\_v1](structak__wwise__plugin__host__reference__set__v1.html "Interface used to interact with reference sets."). [更多...](structak__wwise__plugin__host__reference__set__v1_adb211da55a8e4b4fcd675851f95b1895.html#adb211da55a8e4b4fcd675851f95b1895) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [ak\_wwise\_plugin\_host\_reference\_set\_v1](structak__wwise__plugin__host__reference__set__v1_a72164e795f020e066c83acdf10bce24d.html#a72164e795f020e066c83acdf10bce24d) (int version=1) |
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
| Public 属性 | |
| GUID(\* | [GetReferenceGuid](structak__wwise__plugin__host__reference__set__v1_ab1c30800bd53ebe6de06a00460f51260.html#ab1c30800bd53ebe6de06a00460f51260) )(const struct [ak\_wwise\_plugin\_host\_reference\_set\_instance\_v1](structak__wwise__plugin__host__reference__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszReferenceName) |
|  | Retrieves the value of a specific reference as a GUID. [更多...](structak__wwise__plugin__host__reference__set__v1_ab1c30800bd53ebe6de06a00460f51260.html#ab1c30800bd53ebe6de06a00460f51260) |
|  | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc)(\* | [GetReferenceShortId](structak__wwise__plugin__host__reference__set__v1_a367130c323082754b465cb0acd14f449.html#a367130c323082754b465cb0acd14f449) )(const struct [ak\_wwise\_plugin\_host\_reference\_set\_instance\_v1](structak__wwise__plugin__host__reference__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszReferenceName) |
|  | Returns the Unique ID (or "ShortID") of the corresponding object. [更多...](structak__wwise__plugin__host__reference__set__v1_a367130c323082754b465cb0acd14f449.html#a367130c323082754b465cb0acd14f449) |
|  | |
| bool(\* | [SetReferenceByGuid](structak__wwise__plugin__host__reference__set__v1_a6147cb5497358eb7dc984e31ef847667.html#a6147cb5497358eb7dc984e31ef847667) )(struct [ak\_wwise\_plugin\_host\_reference\_set\_instance\_v1](structak__wwise__plugin__host__reference__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszReferenceName, const GUID \*in\_guidReference) |
|  | Updates the value of a specific reference to the provided GUID. [更多...](structak__wwise__plugin__host__reference__set__v1_a6147cb5497358eb7dc984e31ef847667.html#a6147cb5497358eb7dc984e31ef847667) |
|  | |
| bool(\* | [ReferenceHasLinked](structak__wwise__plugin__host__reference__set__v1_aef3b4738132d73ba701d0a98a28b8a6b.html#aef3b4738132d73ba701d0a98a28b8a6b) )(const struct [ak\_wwise\_plugin\_host\_reference\_set\_instance\_v1](structak__wwise__plugin__host__reference__set__instance__v1.html) \*in\_this, const char \*in\_pszReferenceName) |
|  | Returns whether the specified reference has at least some linked platforms. [更多...](structak__wwise__plugin__host__reference__set__v1_aef3b4738132d73ba701d0a98a28b8a6b.html#aef3b4738132d73ba701d0a98a28b8a6b) |
|  | |
| bool(\* | [ReferenceHasUnlinked](structak__wwise__plugin__host__reference__set__v1_affeb8baebf42b16beb1bda37021be88b.html#affeb8baebf42b16beb1bda37021be88b) )(const struct [ak\_wwise\_plugin\_host\_reference\_set\_instance\_v1](structak__wwise__plugin__host__reference__set__instance__v1.html) \*in\_this, const char \*in\_pszReferenceName) |
|  | Returns whether the specified reference has one or more platforms that are not linked. [更多...](structak__wwise__plugin__host__reference__set__v1_affeb8baebf42b16beb1bda37021be88b.html#affeb8baebf42b16beb1bda37021be88b) |
|  | |
| bool(\* | [ReferencePlatformIsLinked](structak__wwise__plugin__host__reference__set__v1_ad90e4d3a5193af8a4474e8c33dc58255.html#ad90e4d3a5193af8a4474e8c33dc58255) )(const struct [ak\_wwise\_plugin\_host\_reference\_set\_instance\_v1](structak__wwise__plugin__host__reference__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszReferenceName) |
|  | Returns whether the specified reference's platform is linked. [更多...](structak__wwise__plugin__host__reference__set__v1_ad90e4d3a5193af8a4474e8c33dc58255.html#ad90e4d3a5193af8a4474e8c33dc58255) |
|  | |
| const char \*(\* | [GetReferenceName](structak__wwise__plugin__host__reference__set__v1_a01ffdd6ec03e9b34be40451daae0e5fc.html#a01ffdd6ec03e9b34be40451daae0e5fc) )(const struct [ak\_wwise\_plugin\_host\_reference\_set\_instance\_v1](structak__wwise__plugin__host__reference__set__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, const char \*in\_pszReferenceName) |
|  | Retrieves the name of a referenced object. [更多...](structak__wwise__plugin__host__reference__set__v1_a01ffdd6ec03e9b34be40451daae0e5fc.html#a01ffdd6ec03e9b34be40451daae0e5fc) |
|  | |
| - Public 属性 继承自 [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) | |
| [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9) | [m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9): 32 |
|  | Interface type (see [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9)) [更多...](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9) |
|  | |
| uint32\_t | [m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6): 32 |
|  | Version of the interface [更多...](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6) |
|  | |

## 详细描述

Interface used to interact with reference sets.

A reference set is a dictionary of references to other Objects that exist in a user's Authoring project. Whenever a reference name is specified, it corresponds to the reference name set in the plug-in's XML. These Object references can be resolved to GUIDs for use in the Authoring project, or to Short IDs for use in the Wwise Runtime.

The methods in this interface which use in\_guidPlatform as an input parameter assume that you have access to a Platform defined as a GUID, either provided by the caller function or retrieved through the Host interface.

You can retrieve GUIDs in the following ways:

- Use the in\_guidPlatform provided as an input parameter in [ak\_wwise\_plugin\_audio\_plugin\_v1::GetBankParameters](structak__wwise__plugin__audio__plugin__v1_abd584886ab95277158307efdf633af78.html#abd584886ab95277158307efdf633af78) or [ak\_wwise\_plugin\_custom\_data\_v1::GetPluginData](structak__wwise__plugin__custom__data__v1_ae2a50eda33df6c0c7da86b967751cf40.html#ae2a50eda33df6c0c7da86b967751cf40)
- Poll the currently-active platform from [ak\_wwise\_plugin\_host\_v1::GetCurrentPlatform](structak__wwise__plugin__host__v1_abb94fc626e520d00c4f77e9b8fab3adb.html#abb94fc626e520d00c4f77e9b8fab3adb) or [ak\_wwise\_plugin\_host\_v1::GetAuthoringPlaybackPlatform](structak__wwise__plugin__host__v1_a04c6938e999f9d1b3da2599155680e1f.html#a04c6938e999f9d1b3da2599155680e1f)

You can also provide GUID\_NULL as a parameter, which accesses data for all platforms at once as a linked value. However, GUID\_NULL only works when no platform-specific data is possible for a value. Using the current platform is always the preferred access method.

参见
:   - [属性要素](plugin_xml_properties.html#wwiseplugin_xml_properties_tag)
    - [Reference Set](plugin_backend_model.html#wwiseplugin_referenceset)
    - [ak\_wwise\_plugin\_notifications\_reference\_set\_v1](structak__wwise__plugin__notifications__reference__set__v1.html)
    - [ak\_wwise\_plugin\_host\_object\_store\_v1](structak__wwise__plugin__host__object__store__v1.html)

在文件 [HostReferenceSet.h](_host_reference_set_8h_source.html) 第 [65](_host_reference_set_8h_source.html#l00065) 行定义.