# ak_wwise_plugin_host_object_store_v1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](structak__wwise__plugin__host__object__store__v1-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

ak\_wwise\_plugin\_host\_object\_store\_v1结构体 参考

Custom inner property set interface.
[更多...](structak__wwise__plugin__host__object__store__v1.html#details)

`#include <HostObjectStore.h>`

类 ak\_wwise\_plugin\_host\_object\_store\_v1 继承关系图:

![](../../../images/structak__wwise__plugin__host__object__store__v1.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [Instance](structak__wwise__plugin__host__object__store__v1_ac8e04472f1e5c174c1e594fcf1f4a831.html#ac8e04472f1e5c174c1e594fcf1f4a831) = [ak\_wwise\_plugin\_host\_object\_store\_instance\_v1](structak__wwise__plugin__host__object__store__instance__v1.html) |
|  | Base host-provided instance type for [ak\_wwise\_plugin\_host\_object\_store\_v1](structak__wwise__plugin__host__object__store__v1.html "Custom inner property set interface."). [更多...](structak__wwise__plugin__host__object__store__v1_ac8e04472f1e5c174c1e594fcf1f4a831.html#ac8e04472f1e5c174c1e594fcf1f4a831) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [ak\_wwise\_plugin\_host\_object\_store\_v1](structak__wwise__plugin__host__object__store__v1_abf5cabf830e6ad43477141cbc05ebbb8.html#abf5cabf830e6ad43477141cbc05ebbb8) () |
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
| void(\* | [InsertPropertySet](structak__wwise__plugin__host__object__store__v1_aea505a993b576b48c81a9b1c0818dc9e.html#aea505a993b576b48c81a9b1c0818dc9e) )(struct [ak\_wwise\_plugin\_host\_object\_store\_instance\_v1](structak__wwise__plugin__host__object__store__instance__v1.html) \*in\_this, const char \*in\_pszListName, unsigned int in\_uiIndex, const struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_pPropertySet) |
|  | Inserts an inner property set into the specified list at the specified position. [更多...](structak__wwise__plugin__host__object__store__v1_aea505a993b576b48c81a9b1c0818dc9e.html#aea505a993b576b48c81a9b1c0818dc9e) |
|  | |
| bool(\* | [RemovePropertySet](structak__wwise__plugin__host__object__store__v1_a10ea13a4b27f6a8783d1acb4341ab116.html#a10ea13a4b27f6a8783d1acb4341ab116) )(struct [ak\_wwise\_plugin\_host\_object\_store\_instance\_v1](structak__wwise__plugin__host__object__store__instance__v1.html) \*in\_this, const struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_pPropertySet) |
|  | Removes an inner property set from any list, without deleting the object itself. [更多...](structak__wwise__plugin__host__object__store__v1_a10ea13a4b27f6a8783d1acb4341ab116.html#a10ea13a4b27f6a8783d1acb4341ab116) |
|  | |
| struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*(\* | [GetPropertySet](structak__wwise__plugin__host__object__store__v1_ae8c3b0976a1120bc4f13a96b4b8a8a46.html#ae8c3b0976a1120bc4f13a96b4b8a8a46) )(const struct [ak\_wwise\_plugin\_host\_object\_store\_instance\_v1](structak__wwise__plugin__host__object__store__instance__v1.html) \*in\_this, const char \*in\_pszListName, unsigned int in\_uiIndex) |
|  | Gets an inner property set inside the specified list at the specified position. [更多...](structak__wwise__plugin__host__object__store__v1_ae8c3b0976a1120bc4f13a96b4b8a8a46.html#ae8c3b0976a1120bc4f13a96b4b8a8a46) |
|  | |
| unsigned int(\* | [GetPropertySetCount](structak__wwise__plugin__host__object__store__v1_ac7a5db67d6c80bab8c15effe40504d63.html#ac7a5db67d6c80bab8c15effe40504d63) )(const struct [ak\_wwise\_plugin\_host\_object\_store\_instance\_v1](structak__wwise__plugin__host__object__store__instance__v1.html) \*in\_this, const char \*in\_pszListName) |
|  | Gets the number of inserted indexes inside the specified list. [更多...](structak__wwise__plugin__host__object__store__v1_ac7a5db67d6c80bab8c15effe40504d63.html#ac7a5db67d6c80bab8c15effe40504d63) |
|  | |
| struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*(\* | [CreatePropertySet](structak__wwise__plugin__host__object__store__v1_a99861b64da80f35a4224a92fbf967cb3.html#a99861b64da80f35a4224a92fbf967cb3) )(struct [ak\_wwise\_plugin\_host\_object\_store\_instance\_v1](structak__wwise__plugin__host__object__store__instance__v1.html) \*in\_this, const char \*in\_pszType) |
|  | Creates a new inner property set. [更多...](structak__wwise__plugin__host__object__store__v1_a99861b64da80f35a4224a92fbf967cb3.html#a99861b64da80f35a4224a92fbf967cb3) |
|  | |
| void(\* | [DeletePropertySet](structak__wwise__plugin__host__object__store__v1_af005199ea8b58c036505d4137a1dee6a.html#af005199ea8b58c036505d4137a1dee6a) )(struct [ak\_wwise\_plugin\_host\_object\_store\_instance\_v1](structak__wwise__plugin__host__object__store__instance__v1.html) \*in\_this, struct [ak\_wwise\_plugin\_host\_property\_set\_instance\_v1](structak__wwise__plugin__host__property__set__instance__v1.html) \*in\_pPropertySet) |
|  | Frees the inner property set. [更多...](structak__wwise__plugin__host__object__store__v1_af005199ea8b58c036505d4137a1dee6a.html#af005199ea8b58c036505d4137a1dee6a) |
|  | |
| unsigned int(\* | [GetListCount](structak__wwise__plugin__host__object__store__v1_a9e98e5f143b4f7ee9940dd65cd9c7160.html#a9e98e5f143b4f7ee9940dd65cd9c7160) )(const struct [ak\_wwise\_plugin\_host\_object\_store\_instance\_v1](structak__wwise__plugin__host__object__store__instance__v1.html) \*in\_this) |
|  | Returns the number of inner property set lists to be used with GetListName. [更多...](structak__wwise__plugin__host__object__store__v1_a9e98e5f143b4f7ee9940dd65cd9c7160.html#a9e98e5f143b4f7ee9940dd65cd9c7160) |
|  | |
| unsigned int(\* | [GetListName](structak__wwise__plugin__host__object__store__v1_ac3d12537281fa88a2bbfb71e4e6cebbf.html#ac3d12537281fa88a2bbfb71e4e6cebbf) )(const struct [ak\_wwise\_plugin\_host\_object\_store\_instance\_v1](structak__wwise__plugin__host__object__store__instance__v1.html) \*in\_this, unsigned int in\_uiListIndex, char \*out\_pszListName, unsigned int in\_uiBufferSize) |
|  | Gets the name of the list at the specified position. [更多...](structak__wwise__plugin__host__object__store__v1_ac3d12537281fa88a2bbfb71e4e6cebbf.html#ac3d12537281fa88a2bbfb71e4e6cebbf) |
|  | |
| - Public 属性 继承自 [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) | |
| [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9) | [m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9): 32 |
|  | Interface type (see [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9)) [更多...](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9) |
|  | |
| uint32\_t | [m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6): 32 |
|  | Version of the interface [更多...](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6) |
|  | |

## 详细描述

Custom inner property set interface.

The Object Store contains named lists, and those named lists each contains a vector of inner property sets.

For example, you can create a list named "Property curve points" and have 12 inner property sets with coordinates, configuration and information for the 12 user-created curve points.

Inner property sets can be created from any inner types, as defined in the plug-in's XML definition file `InnerTypes` section. Your lists should contain recognizable types, as there is no way to poll the type of the created object. This system was created with a one-list-one-type design pattern; however, there is no actual restriction in using different types in a same list.

You can define as many named lists as required. You should consider creating different inner property sets or lists for each platform if the property set indexes aren't linked.

You can create new inner property set with [CreatePropertySet](structak__wwise__plugin__host__object__store__v1_a99861b64da80f35a4224a92fbf967cb3.html#a99861b64da80f35a4224a92fbf967cb3), and insert it in a list's index with [InsertPropertySet](structak__wwise__plugin__host__object__store__v1_aea505a993b576b48c81a9b1c0818dc9e.html#aea505a993b576b48c81a9b1c0818dc9e).

You can also subscribe to notifications through [ak\_wwise\_plugin\_notifications\_object\_store\_v1](structak__wwise__plugin__notifications__object__store__v1.html "Interface able to receive notifications for custom inner property sets.") in order to be informed when some inner property set changed.

|  |  |
| --- | --- |
|  | **备注:** In order to manage property sets, you must make sure to use [AK::Wwise::Plugin::RequestPropertySet](namespace_a_k_1_1_wwise_1_1_plugin_a5eb9b772d01c414e7c77b44ef66e661f.html#a5eb9b772d01c414e7c77b44ef66e661f) in your plug-in. |

|  |  |
| --- | --- |
|  | **备注:** Historical naming convention described it as "inner object" and "inner type". For simplicity, since we are talking about property sets, the naming has been standardized to "inner property set". However, the names are interchangeable and are still being used. |

参见
:   - [内部对象](plugin_xml.html#wwiseplugin_objectstore)
    - [属性要素](plugin_xml_properties.html#wwiseplugin_xml_properties_tag)
    - [ak\_wwise\_plugin\_notifications\_object\_store\_v1](structak__wwise__plugin__notifications__object__store__v1.html)

在文件 [HostObjectStore.h](_host_object_store_8h_source.html) 第 [75](_host_object_store_8h_source.html#l00075) 行定义.