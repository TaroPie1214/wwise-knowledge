# HostBase

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [HostBase](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::HostBase< CHostT, interface\_version > 模板类 参考

API to request host's current state and services.
[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base.html#details)

`#include <Host.h>`

类 AK.Wwise::Plugin::V1::HostBase< CHostT, interface\_version > 继承关系图:

![](../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base.png)

|  |  |
| --- | --- |
| Public 类型 | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base_a7e9820096b3ab84c093b27074d700a5d.html#a7e9820096b3ab84c093b27074d700a5da51aa2668f2c6b1e4b7d4cb2363a158ef) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST } |
|  | The interface type, as requested by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base_a7e9820096b3ab84c093b27074d700a5d.html#a7e9820096b3ab84c093b27074d700a5d) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base_aefd40e4f7593d17ad634ad92d5c3743d.html#aefd40e4f7593d17ad634ad92d5c3743daf1572ae17c4d910e488e133f1d676e05) = interface\_version } |
|  | The interface version, as requested by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base_aefd40e4f7593d17ad634ad92d5c3743d.html#aefd40e4f7593d17ad634ad92d5c3743d) |
|  | |
| using | [Interface](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base_a4798a75d76977903457b2599cd38588f.html#a4798a75d76977903457b2599cd38588f) = CHostT |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base_aba252ad2483121e93fb5948a4fdd437e.html#aba252ad2483121e93fb5948a4fdd437e) = typename CHostT::Instance |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::CBaseInstanceGlue< CHost >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue.html) | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue_aff6221118cb1d81f1e67f1932fb66b60.html#aff6221118cb1d81f1e67f1932fb66b60) = typename CInterface::Instance |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::CBaseInterfaceGlue< CHost >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html) | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a270936e06e5c9627548246cbebde0467.html#a270936e06e5c9627548246cbebde0467) = [CHost](namespace_a_k_1_1_wwise_1_1_plugin_aa96b27e8272b257ab8bf4cedc96122ca.html#aa96b27e8272b257ab8bf4cedc96122ca) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| GUID | [GetCurrentPlatform](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base_a7759cee542d0e26cfb27e8c4b0693fbf.html#a7759cee542d0e26cfb27e8c4b0693fbf) () const |
|  | Retrieves the current platform identifier. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base_a7759cee542d0e26cfb27e8c4b0693fbf.html#a7759cee542d0e26cfb27e8c4b0693fbf) |
|  | |
| [BasePlatformID](struct_base_platform_i_d.html) | [GetCurrentBasePlatform](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base_a4a2fb183c44c7a125e8193b4cfbd69cb.html#a4a2fb183c44c7a125e8193b4cfbd69cb) () const |
|  | Retrieves the current base platform identifier. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base_a4a2fb183c44c7a125e8193b4cfbd69cb.html#a4a2fb183c44c7a125e8193b4cfbd69cb) |
|  | |
| [BasePlatformID](struct_base_platform_i_d.html) | [GetDefaultNativeAuthoringPlaybackPlatform](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base_ac79cc9e2b82e61aceae108882628228a.html#ac79cc9e2b82e61aceae108882628228a) () const |
|  | Retrieves the requested playback base platform of the Authoring tool. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base_ac79cc9e2b82e61aceae108882628228a.html#ac79cc9e2b82e61aceae108882628228a) |
|  | |
| GUID | [GetAuthoringPlaybackPlatform](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base_a586bc8d00a5bffd34dc0f32042239478.html#a586bc8d00a5bffd34dc0f32042239478) () const |
|  | Retrieves the requested playback platform of the Authoring tool. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base_a586bc8d00a5bffd34dc0f32042239478.html#a586bc8d00a5bffd34dc0f32042239478) |
|  | |
| void | [NotifyInternalDataChanged](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base_ad84d8687a173358da099727443e26957.html#ad84d8687a173358da099727443e26957) ([AkPluginParamID](_ak_typedefs_8h_a4cb8ff0b7014efdaa21697f4ef928926.html#a4cb8ff0b7014efdaa21697f4ef928926) in\_idData, bool in\_bMakeProjectDirty) |
|  | Use this function to tell [Wwise](namespace_a_k_1_1_wwise.html) that something other than properties has changed within the plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base_ad84d8687a173358da099727443e26957.html#ad84d8687a173358da099727443e26957) |
|  | |
| void | [GetLicenseStatus](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base_aec6351949b31356400b9eb50e4f3b25b.html#aec6351949b31356400b9eb50e4f3b25b) (const GUID &in\_guidPlatform, [LicenseType](namespace_a_k_1_1_wwise_1_1_plugin_a58ce97270e1033ca4f52b145c8fd21eb.html#a58ce97270e1033ca4f52b145c8fd21eb) &out\_eType, [LicenseStatus](namespace_a_k_1_1_wwise_1_1_plugin_a74c80204b884826c56e3d208bd3d1df4.html#a74c80204b884826c56e3d208bd3d1df4) &out\_eStatus, uint32\_t &out\_uDaysToExpiry) const |
|  | Obtain licensing status for the plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base_aec6351949b31356400b9eb50e4f3b25b.html#aec6351949b31356400b9eb50e4f3b25b) |
|  | |
| void | [GetAssetLicenseStatus](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base_a959b7fe0d152bcb30faea4821915b873.html#a959b7fe0d152bcb30faea4821915b873) (const GUID &in\_guidPlatform, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uAssetID, [LicenseType](namespace_a_k_1_1_wwise_1_1_plugin_a58ce97270e1033ca4f52b145c8fd21eb.html#a58ce97270e1033ca4f52b145c8fd21eb) &out\_eType, [LicenseStatus](namespace_a_k_1_1_wwise_1_1_plugin_a74c80204b884826c56e3d208bd3d1df4.html#a74c80204b884826c56e3d208bd3d1df4) &out\_eStatus, uint32\_t &out\_uDaysToExpiry) const |
|  | Obtain licensing status for a plug-in-specific asset ID. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base_a959b7fe0d152bcb30faea4821915b873.html#a959b7fe0d152bcb30faea4821915b873) |
|  | |
| void | [WaapiCall](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base_a8aa6cd36fdd51ce68dc8d2949deb5a9d.html#a8aa6cd36fdd51ce68dc8d2949deb5a9d) (const char \*in\_szUri, const char \*in\_szArgs, const char \*in\_szOptions, [AK::IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) &in\_alloc, char \*&out\_szResults, char \*&out\_szError) const |
|  | Find and call the specified procedure. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base_a8aa6cd36fdd51ce68dc8d2949deb5a9d.html#a8aa6cd36fdd51ce68dc8d2949deb5a9d) |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - 静态 Public 属性 继承自 [AK.Wwise::Plugin::CBaseInterfaceGlue< CHost >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html) | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a270936e06e5c9627548246cbebde0467.html#a270936e06e5c9627548246cbebde0467) \* | [g\_cinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a8b682b3105da8940f7ea75845254d491.html#a8b682b3105da8940f7ea75845254d491) |
|  | The unique instance of the CInterface interface. Defined at nullptr first, overridden by the Host once loaded. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a8b682b3105da8940f7ea75845254d491.html#a8b682b3105da8940f7ea75845254d491) |
|  | |

## 详细描述

### template<typename CHostT = CHost, int interface\_version = 1> class AK.Wwise::Plugin::V1::HostBase< CHostT, interface\_version >

API to request host's current state and services.

If requested, this contains information on the current state of the host as well as generic operations.

For example, the currently selected platform, tools to post when internal plug-in data changed, or a way to make Waapi calls.

In order to be reactive to host's state, you should consider implementing [ak\_wwise\_plugin\_notifications\_host\_v1](structak__wwise__plugin__notifications__host__v1.html "API to receive host's update notifications.") notifications.

在文件 [Host.h](_v1_2_host_8h_source.html) 第 [244](_v1_2_host_8h_source.html#l00244) 行定义.