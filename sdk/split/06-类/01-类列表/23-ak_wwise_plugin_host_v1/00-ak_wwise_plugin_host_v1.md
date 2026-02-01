# ak_wwise_plugin_host_v1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](structak__wwise__plugin__host__v1-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

ak\_wwise\_plugin\_host\_v1结构体 参考

API to request host's current state and services.
[更多...](structak__wwise__plugin__host__v1.html#details)

`#include <Host.h>`

类 ak\_wwise\_plugin\_host\_v1 继承关系图:

![](../../../images/structak__wwise__plugin__host__v1.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [Instance](structak__wwise__plugin__host__v1_a6f9e30f00d3d35b188f14ff2a5145858.html#a6f9e30f00d3d35b188f14ff2a5145858) = [ak\_wwise\_plugin\_host\_instance\_v1](structak__wwise__plugin__host__instance__v1.html) |
|  | Base host-provided instance type. [更多...](structak__wwise__plugin__host__v1_a6f9e30f00d3d35b188f14ff2a5145858.html#a6f9e30f00d3d35b188f14ff2a5145858) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [ak\_wwise\_plugin\_host\_v1](structak__wwise__plugin__host__v1_a65856445e065d89070bb3be6526b0fae.html#a65856445e065d89070bb3be6526b0fae) (int in\_version=1) |
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
| GUID(\* | [GetCurrentPlatform](structak__wwise__plugin__host__v1_abb94fc626e520d00c4f77e9b8fab3adb.html#abb94fc626e520d00c4f77e9b8fab3adb) )(const struct [ak\_wwise\_plugin\_host\_v1](structak__wwise__plugin__host__v1.html) \*in\_this) |
|  | Retrieves the current platform identifier. [更多...](structak__wwise__plugin__host__v1_abb94fc626e520d00c4f77e9b8fab3adb.html#abb94fc626e520d00c4f77e9b8fab3adb) |
|  | |
| [BasePlatformID](struct_base_platform_i_d.html)(\* | [GetCurrentBasePlatform](structak__wwise__plugin__host__v1_a5b4582317147fd5532dfd5a042c8c011.html#a5b4582317147fd5532dfd5a042c8c011) )(const struct [ak\_wwise\_plugin\_host\_v1](structak__wwise__plugin__host__v1.html) \*in\_this) |
|  | Retrieves the current base platform identifier. [更多...](structak__wwise__plugin__host__v1_a5b4582317147fd5532dfd5a042c8c011.html#a5b4582317147fd5532dfd5a042c8c011) |
|  | |
| [BasePlatformID](struct_base_platform_i_d.html)(\* | [GetDefaultNativeAuthoringPlaybackPlatform](structak__wwise__plugin__host__v1_a4669e74dee936afa74b231bddd12bb7a.html#a4669e74dee936afa74b231bddd12bb7a) )(const struct [ak\_wwise\_plugin\_host\_v1](structak__wwise__plugin__host__v1.html) \*in\_this) |
|  | Retrieves the requested playback base platform of the Authoring tool. [更多...](structak__wwise__plugin__host__v1_a4669e74dee936afa74b231bddd12bb7a.html#a4669e74dee936afa74b231bddd12bb7a) |
|  | |
| GUID(\* | [GetAuthoringPlaybackPlatform](structak__wwise__plugin__host__v1_a04c6938e999f9d1b3da2599155680e1f.html#a04c6938e999f9d1b3da2599155680e1f) )(const struct [ak\_wwise\_plugin\_host\_v1](structak__wwise__plugin__host__v1.html) \*in\_this) |
|  | Retrieves the requested playback platform of the Authoring tool. [更多...](structak__wwise__plugin__host__v1_a04c6938e999f9d1b3da2599155680e1f.html#a04c6938e999f9d1b3da2599155680e1f) |
|  | |
| void(\* | [NotifyInternalDataChanged](structak__wwise__plugin__host__v1_abae1f696cc611980e955b6b3c49860fd.html#abae1f696cc611980e955b6b3c49860fd) )(struct [ak\_wwise\_plugin\_host\_instance\_v1](structak__wwise__plugin__host__instance__v1.html) \*in\_this, [AkPluginParamID](_ak_typedefs_8h_a4cb8ff0b7014efdaa21697f4ef928926.html#a4cb8ff0b7014efdaa21697f4ef928926) in\_idData, bool in\_bMakeProjectDirty) |
|  | Use this function to tell Wwise that something other than properties has changed within the plug-in. [更多...](structak__wwise__plugin__host__v1_abae1f696cc611980e955b6b3c49860fd.html#abae1f696cc611980e955b6b3c49860fd) |
|  | |
| void(\* | [GetLicenseStatus](structak__wwise__plugin__host__v1_a6a0c21e47528efa66060ed0a2ea6245e.html#a6a0c21e47528efa66060ed0a2ea6245e) )(const struct [ak\_wwise\_plugin\_host\_instance\_v1](structak__wwise__plugin__host__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, [AK::Wwise::Plugin::LicenseType](namespace_a_k_1_1_wwise_1_1_plugin_a58ce97270e1033ca4f52b145c8fd21eb.html#a58ce97270e1033ca4f52b145c8fd21eb) \*out\_eType, [AK::Wwise::Plugin::LicenseStatus](namespace_a_k_1_1_wwise_1_1_plugin_a74c80204b884826c56e3d208bd3d1df4.html#a74c80204b884826c56e3d208bd3d1df4) \*out\_eStatus, uint32\_t \*out\_uDaysToExpiry) |
|  | Obtain licensing status for the plug-in. [更多...](structak__wwise__plugin__host__v1_a6a0c21e47528efa66060ed0a2ea6245e.html#a6a0c21e47528efa66060ed0a2ea6245e) |
|  | |
| void(\* | [GetAssetLicenseStatus](structak__wwise__plugin__host__v1_afdd53923c5f190d9e8f4f8073ac9471f.html#afdd53923c5f190d9e8f4f8073ac9471f) )(const struct [ak\_wwise\_plugin\_host\_instance\_v1](structak__wwise__plugin__host__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uAssetID, [AK::Wwise::Plugin::LicenseType](namespace_a_k_1_1_wwise_1_1_plugin_a58ce97270e1033ca4f52b145c8fd21eb.html#a58ce97270e1033ca4f52b145c8fd21eb) \*out\_eType, [AK::Wwise::Plugin::LicenseStatus](namespace_a_k_1_1_wwise_1_1_plugin_a74c80204b884826c56e3d208bd3d1df4.html#a74c80204b884826c56e3d208bd3d1df4) \*out\_eStatus, uint32\_t \*out\_uDaysToExpiry) |
|  | Obtain licensing status for a plug-in-specific asset ID. [更多...](structak__wwise__plugin__host__v1_afdd53923c5f190d9e8f4f8073ac9471f.html#afdd53923c5f190d9e8f4f8073ac9471f) |
|  | |
| void(\* | [WaapiCall](structak__wwise__plugin__host__v1_a583ae770addfdc00d6dd59c923cc4e06.html#a583ae770addfdc00d6dd59c923cc4e06) )(const struct [ak\_wwise\_plugin\_host\_v1](structak__wwise__plugin__host__v1.html) \*in\_this, const char \*in\_szUri, const char \*in\_szArgs, const char \*in\_szOptions, [AK::IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) \*in\_pAlloc, char \*\*out\_szResults, char \*\*out\_szError) |
|  | Find and call the specified procedure. [更多...](structak__wwise__plugin__host__v1_a583ae770addfdc00d6dd59c923cc4e06.html#a583ae770addfdc00d6dd59c923cc4e06) |
|  | |
| - Public 属性 继承自 [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) | |
| [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9) | [m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9): 32 |
|  | Interface type (see [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9)) [更多...](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9) |
|  | |
| uint32\_t | [m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6): 32 |
|  | Version of the interface [更多...](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6) |
|  | |

## 详细描述

API to request host's current state and services.

If requested, this contains information on the current state of the host as well as generic operations.

For example, the currently selected platform, tools to post when internal plug-in data changed, or a way to make Waapi calls.

In order to be reactive to host's state, you should consider implementing [ak\_wwise\_plugin\_notifications\_host\_v1](structak__wwise__plugin__notifications__host__v1.html "API to receive host's update notifications.") notifications.

在文件 [Host.h](_v1_2_host_8h_source.html) 第 [48](_v1_2_host_8h_source.html#l00048) 行定义.