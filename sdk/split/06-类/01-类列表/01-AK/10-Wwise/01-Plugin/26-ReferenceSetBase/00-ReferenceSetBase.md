# ReferenceSetBase

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [ReferenceSetBase](class_a_k_1_1_wwise_1_1_plugin_1_1_reference_set_base.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_reference_set_base-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::ReferenceSetBase< CHostReferenceSetT, interface\_version > 模板类 参考

Interface used to interact with reference sets.
[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_reference_set_base.html#details)

`#include <HostReferenceSet.h>`

类 AK.Wwise::Plugin::ReferenceSetBase< CHostReferenceSetT, interface\_version > 继承关系图:

![](../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_reference_set_base.png)

|  |  |
| --- | --- |
| Public 类型 | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_reference_set_base_a17ef52a7588301b4423239a3f60367ed.html#a17ef52a7588301b4423239a3f60367eda0d53aaf0a47518af767b259b86b4ad5a) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_REFERENCE\_SET } |
|  | The interface type, as requested by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_reference_set_base_a17ef52a7588301b4423239a3f60367ed.html#a17ef52a7588301b4423239a3f60367ed) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_reference_set_base_ae53ef524ef516c878da84efe748223aa.html#ae53ef524ef516c878da84efe748223aaaab9a178c3d864a56419e73e6374383d0) = interface\_version } |
|  | The interface version, as requested by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_reference_set_base_ae53ef524ef516c878da84efe748223aa.html#ae53ef524ef516c878da84efe748223aa) |
|  | |
| using | [Interface](class_a_k_1_1_wwise_1_1_plugin_1_1_reference_set_base_a020cc27c07ae80e1772c2460731385c4.html#a020cc27c07ae80e1772c2460731385c4) = [CHostReferenceSet](namespace_a_k_1_1_wwise_1_1_plugin_a536d3a045013fa219001b7b005112feb.html#a536d3a045013fa219001b7b005112feb) |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::CBaseInstanceGlue< CHostReferenceSet >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue.html) | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue_aff6221118cb1d81f1e67f1932fb66b60.html#aff6221118cb1d81f1e67f1932fb66b60) = typename CInterface::Instance |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::CBaseInterfaceGlue< CHostReferenceSet >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html) | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a270936e06e5c9627548246cbebde0467.html#a270936e06e5c9627548246cbebde0467) = [CHostReferenceSet](namespace_a_k_1_1_wwise_1_1_plugin_a536d3a045013fa219001b7b005112feb.html#a536d3a045013fa219001b7b005112feb) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| GUID | [GetReferenceGuid](class_a_k_1_1_wwise_1_1_plugin_1_1_reference_set_base_a7cdf0eaff67613b514ae55db73b44a8e.html#a7cdf0eaff67613b514ae55db73b44a8e) (const GUID &in\_guidPlatform, const char \*in\_pszReferenceName) const |
|  | Retrieves the value of a specific reference as a GUID. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_reference_set_base_a7cdf0eaff67613b514ae55db73b44a8e.html#a7cdf0eaff67613b514ae55db73b44a8e) |
|  | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [GetReferenceShortId](class_a_k_1_1_wwise_1_1_plugin_1_1_reference_set_base_a71e0471770dff35a5ee1d8714b8ea34b.html#a71e0471770dff35a5ee1d8714b8ea34b) (const GUID &in\_guidPlatform, const char \*in\_pszReferenceName) const |
|  | Returns the Unique ID (or "ShortID") of the corresponding object. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_reference_set_base_a71e0471770dff35a5ee1d8714b8ea34b.html#a71e0471770dff35a5ee1d8714b8ea34b) |
|  | |
| bool | [SetReferenceByGuid](class_a_k_1_1_wwise_1_1_plugin_1_1_reference_set_base_a18fd9e527b1fe2eb19f7fe720b66dd2f.html#a18fd9e527b1fe2eb19f7fe720b66dd2f) (const GUID &in\_guidPlatform, const char \*in\_pszReferenceName, const GUID &in\_guidReference) |
|  | Updates the value of a specific reference to the provided GUID. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_reference_set_base_a18fd9e527b1fe2eb19f7fe720b66dd2f.html#a18fd9e527b1fe2eb19f7fe720b66dd2f) |
|  | |
| bool | [ReferenceHasUnlinked](class_a_k_1_1_wwise_1_1_plugin_1_1_reference_set_base_a362a0fa10486c01b62f11e123d3c01e8.html#a362a0fa10486c01b62f11e123d3c01e8) (const char \*in\_pszReferenceName) const |
|  | Returns whether the specified reference has one or more platforms that are not linked. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_reference_set_base_a362a0fa10486c01b62f11e123d3c01e8.html#a362a0fa10486c01b62f11e123d3c01e8) |
|  | |
| bool | [ReferencePlatformIsLinked](class_a_k_1_1_wwise_1_1_plugin_1_1_reference_set_base_ab6246f08223027dc4a8c48f92b6e56c5.html#ab6246f08223027dc4a8c48f92b6e56c5) (const GUID &in\_guidPlatform, const char \*in\_pszReferenceName) const |
|  | Returns whether the specified reference's platform is linked. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_reference_set_base_ab6246f08223027dc4a8c48f92b6e56c5.html#ab6246f08223027dc4a8c48f92b6e56c5) |
|  | |
| const char \* | [GetReferenceName](class_a_k_1_1_wwise_1_1_plugin_1_1_reference_set_base_afabfbba3cfad4f8a38c236fe73298070.html#afabfbba3cfad4f8a38c236fe73298070) (const GUID &in\_guidPlatform, const char \*in\_pszReferenceName) const |
|  | Retrieves the name of an object being referenced. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_reference_set_base_afabfbba3cfad4f8a38c236fe73298070.html#afabfbba3cfad4f8a38c236fe73298070) |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - 静态 Public 属性 继承自 [AK.Wwise::Plugin::CBaseInterfaceGlue< CHostReferenceSet >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html) | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a270936e06e5c9627548246cbebde0467.html#a270936e06e5c9627548246cbebde0467) \* | [g\_cinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a8b682b3105da8940f7ea75845254d491.html#a8b682b3105da8940f7ea75845254d491) |
|  | The unique instance of the CInterface interface. Defined at nullptr first, overridden by the Host once loaded. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a8b682b3105da8940f7ea75845254d491.html#a8b682b3105da8940f7ea75845254d491) |
|  | |

## 详细描述

### template<typename CHostReferenceSetT = CHostReferenceSet, int interface\_version = 1> class AK.Wwise::Plugin::ReferenceSetBase< CHostReferenceSetT, interface\_version >

Interface used to interact with reference sets.

A reference set is a dictionary of references to other Objects that exist in a user's Authoring project. Whenever a reference name is specified, it corresponds to the reference name set in the plug-in's XML. These Object references can be resolved to GUIDs for use in the Authoring project, or to Short IDs for use in the [Wwise](namespace_a_k_1_1_wwise.html) Runtime.

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

在文件 [HostReferenceSet.h](_host_reference_set_8h_source.html) 第 [274](_host_reference_set_8h_source.html#l00274) 行定义.