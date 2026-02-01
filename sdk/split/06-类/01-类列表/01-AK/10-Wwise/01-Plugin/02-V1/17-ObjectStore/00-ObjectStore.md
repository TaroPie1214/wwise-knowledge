# ObjectStore

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [ObjectStore](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::ObjectStore< PropertySetT > 模板类 参考

Custom inner property set interface.
[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store.html#details)

`#include <HostObjectStore.h>`

类 AK.Wwise::Plugin::V1::ObjectStore< PropertySetT > 继承关系图:

![](../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store.png)

|  |  |
| --- | --- |
| Public 类型 | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_afe547fd194e897d26d2848a16c6459c6.html#afe547fd194e897d26d2848a16c6459c6a354c15b3e9cf419e050da788050c00b0) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_OBJECT\_STORE } |
|  | The interface type, as requested by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_afe547fd194e897d26d2848a16c6459c6.html#afe547fd194e897d26d2848a16c6459c6) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_a32b8f5cbab42b71fff3cfb16e3669db6.html#a32b8f5cbab42b71fff3cfb16e3669db6a9aa65e6f1a89b3d0a0edd42bd18c866d) = 1 } |
|  | The interface version, as requested by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_a32b8f5cbab42b71fff3cfb16e3669db6.html#a32b8f5cbab42b71fff3cfb16e3669db6) |
|  | |
| using | [Interface](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_abc3a8b0601ec4e0856f2d78214c38ae4.html#abc3a8b0601ec4e0856f2d78214c38ae4) = [CHostObjectStore](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a47bf77f6f1de2492c10a8788039f1a08.html#a47bf77f6f1de2492c10a8788039f1a08) |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::CBaseInstanceGlue< CHostObjectStore >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue.html) | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue_aff6221118cb1d81f1e67f1932fb66b60.html#aff6221118cb1d81f1e67f1932fb66b60) = typename CInterface::Instance |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::CBaseInterfaceGlue< CHostObjectStore >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html) | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a270936e06e5c9627548246cbebde0467.html#a270936e06e5c9627548246cbebde0467) = [CHostObjectStore](namespace_a_k_1_1_wwise_1_1_plugin_adaab29f68e9ece2d4649c56f52c53e96.html#adaab29f68e9ece2d4649c56f52c53e96) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| void | [InsertPropertySet](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_a23316a944101ac1a01d331fd6c187606.html#a23316a944101ac1a01d331fd6c187606) (const char \*in\_pszListName, unsigned int in\_uiIndex, const PropertySetT &in\_propertySet) |
|  | Inserts an inner property set into the specified list at the specified position. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_a23316a944101ac1a01d331fd6c187606.html#a23316a944101ac1a01d331fd6c187606) |
|  | |
| bool | [RemovePropertySet](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_a7bea99b254754de1c3bdc148e38762da.html#a7bea99b254754de1c3bdc148e38762da) (const PropertySetT &in\_propertySet) |
|  | Removes an inner property set from any list, without deleting the object itself. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_a7bea99b254754de1c3bdc148e38762da.html#a7bea99b254754de1c3bdc148e38762da) |
|  | |
| PropertySetT \* | [GetPropertySet](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_a19d0d8fd9bf69c75a06203e92e7ee4bd.html#a19d0d8fd9bf69c75a06203e92e7ee4bd) (const char \*in\_pszListName, unsigned int in\_uiIndex) const |
|  | Gets an inner property set inside the specified list at the specified position. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_a19d0d8fd9bf69c75a06203e92e7ee4bd.html#a19d0d8fd9bf69c75a06203e92e7ee4bd) |
|  | |
| unsigned int | [GetPropertySetCount](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_a23765d008b043c66845c60ccdfc621b2.html#a23765d008b043c66845c60ccdfc621b2) (const char \*in\_pszListName) const |
|  | Gets the number of inserted indexes inside the specified list. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_a23765d008b043c66845c60ccdfc621b2.html#a23765d008b043c66845c60ccdfc621b2) |
|  | |
| PropertySetT \* | [CreatePropertySet](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_a1a507782ef4fee515e91df6426c6fd88.html#a1a507782ef4fee515e91df6426c6fd88) (const char \*in\_pszType) |
|  | Creates a new inner property set. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_a1a507782ef4fee515e91df6426c6fd88.html#a1a507782ef4fee515e91df6426c6fd88) |
|  | |
| void | [DeletePropertySet](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_aac799692bc78125ac4d2ef8c70b5997a.html#aac799692bc78125ac4d2ef8c70b5997a) (PropertySetT \*in\_pPropertySet) |
|  | Frees the inner property set. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_aac799692bc78125ac4d2ef8c70b5997a.html#aac799692bc78125ac4d2ef8c70b5997a) |
|  | |
| unsigned int | [GetListCount](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_a73ef145057358801fe7f40dfba7e50e9.html#a73ef145057358801fe7f40dfba7e50e9) () const |
|  | Returns the number of inner property set lists to be used with GetListName. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_a73ef145057358801fe7f40dfba7e50e9.html#a73ef145057358801fe7f40dfba7e50e9) |
|  | |
| unsigned int | [GetListName](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_a58fc861ef17b997430f6775b905dfc22.html#a58fc861ef17b997430f6775b905dfc22) (unsigned int in\_uiListIndex, char \*out\_pszListName, unsigned int in\_uiBufferSize) const |
|  | Gets the name of the list at the specified position. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_a58fc861ef17b997430f6775b905dfc22.html#a58fc861ef17b997430f6775b905dfc22) |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - 静态 Public 属性 继承自 [AK.Wwise::Plugin::CBaseInterfaceGlue< CHostObjectStore >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html) | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a270936e06e5c9627548246cbebde0467.html#a270936e06e5c9627548246cbebde0467) \* | [g\_cinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a8b682b3105da8940f7ea75845254d491.html#a8b682b3105da8940f7ea75845254d491) |
|  | The unique instance of the CInterface interface. Defined at nullptr first, overridden by the Host once loaded. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a8b682b3105da8940f7ea75845254d491.html#a8b682b3105da8940f7ea75845254d491) |
|  | |

## 详细描述

### template<typename PropertySetT = AK::Wwise::Plugin::PropertySet> class AK.Wwise::Plugin::V1::ObjectStore< PropertySetT >

Custom inner property set interface.

The Object Store contains named lists, and those named lists each contains a vector of inner property sets.

For example, you can create a list named "Property curve points" and have 12 inner property sets with coordinates, configuration and information for the 12 user-created curve points.

Inner property sets can be created from any inner types, as defined in the plug-in's XML definition file `InnerTypes` section. Your lists should contain recognizable types, as there is no way to poll the type of the created object. This system was created with a one-list-one-type design pattern; however, there is no actual restriction in using different types in a same list.

You can define as many named lists as required. You should consider creating different inner property sets or lists for each platform if the property set indexes aren't linked.

You can create new inner property set with [CreatePropertySet](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_a1a507782ef4fee515e91df6426c6fd88.html#a1a507782ef4fee515e91df6426c6fd88), and insert it in a list's index with [InsertPropertySet](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_object_store_a23316a944101ac1a01d331fd6c187606.html#a23316a944101ac1a01d331fd6c187606).

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

在文件 [HostObjectStore.h](_host_object_store_8h_source.html) 第 [381](_host_object_store_8h_source.html#l00381) 行定义.