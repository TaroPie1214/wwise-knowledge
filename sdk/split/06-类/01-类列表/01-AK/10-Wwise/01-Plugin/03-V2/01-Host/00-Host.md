# Host

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V2](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v2.html)
- [Host](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_host.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_host-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V2::Host类 参考

API to request host's current state and services.
[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_host.html#details)

`#include <Host.h>`

类 AK.Wwise::Plugin::V2::Host 继承关系图:

![](../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_host.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [Interface](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_host_a2027052e5a5363f630ed76ce118f86d2.html#a2027052e5a5363f630ed76ce118f86d2) = [CHost](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v2_a5af2573092f8990f393f30066f9ea80c.html#a5af2573092f8990f393f30066f9ea80c) |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_host_a8093773173185507ebff35423d807036.html#a8093773173185507ebff35423d807036) = [CHost::Instance](structak__wwise__plugin__host__v2_aaed6fdc821c2577ff7d95ba861d747b4.html#aaed6fdc821c2577ff7d95ba861d747b4) |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::V1::HostBase< CHost, 2 >](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base.html) | |
| enum |  |
|  | The interface type, as requested by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base_a7e9820096b3ab84c093b27074d700a5d.html#a7e9820096b3ab84c093b27074d700a5d) |
|  | |
| enum |  |
|  | The interface version, as requested by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base_aefd40e4f7593d17ad634ad92d5c3743d.html#aefd40e4f7593d17ad634ad92d5c3743d) |
|  | |
| using | [Interface](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base_a4798a75d76977903457b2599cd38588f.html#a4798a75d76977903457b2599cd38588f) = [CHost](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_aa4a7e1a93cadbaa4c6804a5a5c663024.html#aa4a7e1a93cadbaa4c6804a5a5c663024) |
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
| [LicenseID](struct_a_k_1_1_wwise_1_1_plugin_1_1_license_i_d.html) | [GetProjectLicenseID](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_host_a71112114b3ebee73f180bedb97c27b68.html#a71112114b3ebee73f180bedb97c27b68) () const |
|  | Obtain the project license ID [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_host_a71112114b3ebee73f180bedb97c27b68.html#a71112114b3ebee73f180bedb97c27b68) |
|  | |
| GUID | [GetCurrentPlatform](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_host_a29cc3ec4a5426cae069eb60d61b39b11.html#a29cc3ec4a5426cae069eb60d61b39b11) () const |
|  | |
| [BasePlatformID](struct_base_platform_i_d.html) | [GetCurrentBasePlatform](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_host_aa714b25ea88962562793065ce025ae43.html#aa714b25ea88962562793065ce025ae43) () const |
|  | |
| [BasePlatformID](struct_base_platform_i_d.html) | [GetDefaultNativeAuthoringPlaybackPlatform](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_host_a03477ac21e747b7604f65842502759e7.html#a03477ac21e747b7604f65842502759e7) () const |
|  | |
| GUID | [GetAuthoringPlaybackPlatform](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_host_a61735255c133bdc085d48b7680a29898.html#a61735255c133bdc085d48b7680a29898) () const |
|  | |
| void | [NotifyInternalDataChanged](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_host_a55d16793cbfce0c58f9a0d004cf1f814.html#a55d16793cbfce0c58f9a0d004cf1f814) ([AkPluginParamID](_ak_typedefs_8h_a4cb8ff0b7014efdaa21697f4ef928926.html#a4cb8ff0b7014efdaa21697f4ef928926) in\_idData, bool in\_bMakeProjectDirty) |
|  | |
| void | [GetLicenseStatus](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_host_ad464d7703658e5cfad6de1bfeaa24c66.html#ad464d7703658e5cfad6de1bfeaa24c66) (const GUID &in\_guidPlatform, [LicenseType](namespace_a_k_1_1_wwise_1_1_plugin_a58ce97270e1033ca4f52b145c8fd21eb.html#a58ce97270e1033ca4f52b145c8fd21eb) &out\_eType, [LicenseStatus](namespace_a_k_1_1_wwise_1_1_plugin_a74c80204b884826c56e3d208bd3d1df4.html#a74c80204b884826c56e3d208bd3d1df4) &out\_eStatus, uint32\_t &out\_uDaysToExpiry) const |
|  | |
| void | [GetAssetLicenseStatus](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_host_abaf53b46f9a7bea52dcfcf3c4c18b1e9.html#abaf53b46f9a7bea52dcfcf3c4c18b1e9) (const GUID &in\_guidPlatform, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uAssetID, [LicenseType](namespace_a_k_1_1_wwise_1_1_plugin_a58ce97270e1033ca4f52b145c8fd21eb.html#a58ce97270e1033ca4f52b145c8fd21eb) &out\_eType, [LicenseStatus](namespace_a_k_1_1_wwise_1_1_plugin_a74c80204b884826c56e3d208bd3d1df4.html#a74c80204b884826c56e3d208bd3d1df4) &out\_eStatus, uint32\_t &out\_uDaysToExpiry) const |
|  | |
| void | [WaapiCall](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_host_a9b037370b1afd2f198efc440a61b6755.html#a9b037370b1afd2f198efc440a61b6755) (const char \*in\_szUri, const char \*in\_szArgs, const char \*in\_szOptions, [AK::IAkPluginMemAlloc](class_a_k_1_1_i_ak_plugin_mem_alloc.html) &in\_alloc, char \*&out\_szResults, char \*&out\_szError) const |
|  | |
| - Public 成员函数 继承自 [AK.Wwise::Plugin::V1::HostBase< CHost, 2 >](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base.html) | |
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
|  | Use this function to tell Wwise that something other than properties has changed within the plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_host_base_ad84d8687a173358da099727443e26957.html#ad84d8687a173358da099727443e26957) |
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

API to request host's current state and services.

If requested, this contains information on the current state of the host as well as generic operations.

For example, the currently selected platform, tools to post when internal plug-in data changed, or a way to make Waapi calls.

In order to be reactive to host's state, you should consider implementing [ak\_wwise\_plugin\_notifications\_host\_v1](structak__wwise__plugin__notifications__host__v1.html "API to receive host's update notifications.") notifications.

在文件 [Host.h](_host_8h_source.html) 第 [94](_host_8h_source.html#l00094) 行定义.