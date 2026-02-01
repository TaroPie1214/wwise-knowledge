# Interface

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [Notifications](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications.html)
- [ObjectStore\_](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store__.html)
- [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store___1_1_interface.html)

[所有成员列表](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store___1_1_interface-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::Notifications::ObjectStore\_< PropertySetT >::Interface结构体 参考

The C interface, fulfilled by your plug-in.
[更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store___1_1_interface.html#details)

`#include <HostObjectStore.h>`

类 AK.Wwise::Plugin::V1::Notifications::ObjectStore\_< PropertySetT >::Interface 继承关系图:

![](../../../../../../../../../images/struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store___1_1_interface.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [Instance](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store___1_1_interface_a82904426d83ca9b97c3e7172028489dd.html#a82904426d83ca9b97c3e7172028489dd) = [ObjectStore\_](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store__.html)< PropertySetT > |
|  | |
| - Public 类型 继承自 [ak\_wwise\_plugin\_notifications\_object\_store\_v1](structak__wwise__plugin__notifications__object__store__v1.html) | |
| using | [Instance](structak__wwise__plugin__notifications__object__store__v1_abc82b903f7060122edc75335deee109d.html#abc82b903f7060122edc75335deee109d) = [ak\_wwise\_plugin\_notifications\_object\_store\_instance\_v1](structak__wwise__plugin__notifications__object__store__instance__v1.html) |
|  | Base instance type for receiving notifications on related Object Store's changes. [更多...](structak__wwise__plugin__notifications__object__store__v1_abc82b903f7060122edc75335deee109d.html#abc82b903f7060122edc75335deee109d) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store___1_1_interface_a8bc0b2a1ac6b25f929506ff0a01f373b.html#a8bc0b2a1ac6b25f929506ff0a01f373b) () |
|  | |
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_notifications\_object\_store\_v1](structak__wwise__plugin__notifications__object__store__v1.html) | |
|  | [ak\_wwise\_plugin\_notifications\_object\_store\_v1](structak__wwise__plugin__notifications__object__store__v1_a7bd1a95b2d37093f6a7ecc6c8ecea4cb.html#a7bd1a95b2d37093f6a7ecc6c8ecea4cb) () |
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
| 额外继承的成员函数 | |
| - Public 属性 继承自 [ak\_wwise\_plugin\_notifications\_object\_store\_v1](structak__wwise__plugin__notifications__object__store__v1.html) | |
| void(\* | [NotifyInnerObjectPropertyChanged](structak__wwise__plugin__notifications__object__store__v1_ad523894ff2188cc3ee1f10322ace2440.html#ad523894ff2188cc3ee1f10322ace2440) )(struct [ak\_wwise\_plugin\_notifications\_object\_store\_instance\_v1](structak__wwise__plugin__notifications__object__store__instance__v1.html) \*in\_this, struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_pPSet, const GUID \*in\_guidPlatform, const char \*in\_pszPropertyName) |
|  | Called when an inner property set's data has changed. [更多...](structak__wwise__plugin__notifications__object__store__v1_ad523894ff2188cc3ee1f10322ace2440.html#ad523894ff2188cc3ee1f10322ace2440) |
|  | |
| void(\* | [NotifyInnerObjectAddedRemoved](structak__wwise__plugin__notifications__object__store__v1_a52356d1122e92ed58c93e44c3a525415.html#a52356d1122e92ed58c93e44c3a525415) )(struct [ak\_wwise\_plugin\_notifications\_object\_store\_instance\_v1](structak__wwise__plugin__notifications__object__store__instance__v1.html) \*in\_this, struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_pPSet, unsigned int in\_uiIndex, [AK::Wwise::Plugin::NotifyInnerObjectOperation](namespace_a_k_1_1_wwise_1_1_plugin_a8c06b37fdc871c51e7bc65b568b3c987.html#a8c06b37fdc871c51e7bc65b568b3c987) in\_eOperation) |
|  | Called when an inner property set has changed. [更多...](structak__wwise__plugin__notifications__object__store__v1_a52356d1122e92ed58c93e44c3a525415.html#a52356d1122e92ed58c93e44c3a525415) |
|  | |
| - Public 属性 继承自 [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) | |
| [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9) | [m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9): 32 |
|  | Interface type (see [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9)) [更多...](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9) |
|  | |
| uint32\_t | [m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6): 32 |
|  | Version of the interface [更多...](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6) |
|  | |

## 详细描述

### template<typename PropertySetT = AK::Wwise::Plugin::PropertySet> struct AK.Wwise::Plugin::V1::Notifications::ObjectStore\_< PropertySetT >::Interface

The C interface, fulfilled by your plug-in.

在文件 [HostObjectStore.h](_host_object_store_8h_source.html) 第 [642](_host_object_store_8h_source.html#l00642) 行定义.