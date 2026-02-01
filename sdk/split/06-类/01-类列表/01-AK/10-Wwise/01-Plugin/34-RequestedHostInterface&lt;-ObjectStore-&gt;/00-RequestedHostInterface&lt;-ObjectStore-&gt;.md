# RequestedHostInterface&lt; ObjectStore &gt;

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [RequestedHostInterface< ObjectStore >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_object_store_01_4.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_object_store_01_4-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AK.Wwise::Plugin::RequestedHostInterface< ObjectStore >类 参考

`#include <HostObjectStore.h>`

类 AK.Wwise::Plugin::RequestedHostInterface< ObjectStore > 继承关系图:

![](../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_object_store_01_4.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [HostInterfaceDefinition](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_object_store_01_4_af115714bd2a383e6a85946e508fb1df9.html#af115714bd2a383e6a85946e508fb1df9) = [HostInterfaceGlue](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html)< [ObjectStore](namespace_a_k_1_1_wwise_1_1_plugin_aa1a4c71b6a4959d8e06f9e3cc976c749.html#aa1a4c71b6a4959d8e06f9e3cc976c749), true > |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< ObjectStore, true >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| enum |  |
|  | |
| enum |  |
|  | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) = typename CPPInstance::GluedInterface |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a8bdb82de06eb8956882fe9d524e96e08.html#a8bdb82de06eb8956882fe9d524e96e08) = [ObjectStore](namespace_a_k_1_1_wwise_1_1_plugin_aa1a4c71b6a4959d8e06f9e3cc976c749.html#aa1a4c71b6a4959d8e06f9e3cc976c749) |
|  | |
| using | [CInstance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_af60fd0de7e69af6931e04ea9ec1ffc09.html#af60fd0de7e69af6931e04ea9ec1ffc09) = typename CPPInstance::Instance |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::V1::Notifications::ObjectStore\_< PropertySetT >](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store__.html) | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store___a4ddb71635b90ee63de4b56f3ca690712.html#a4ddb71635b90ee63de4b56f3ca690712a4f98d156c99eba60b507f5c00730fde7) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NOTIFICATIONS\_OBJECT\_STORE } |
|  | The interface type, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store___a4ddb71635b90ee63de4b56f3ca690712.html#a4ddb71635b90ee63de4b56f3ca690712) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store___addf5610ecf7fe99553e03115fa06f162.html#addf5610ecf7fe99553e03115fa06f162a7c14e84c0b20b0bc1c1bdd4a73486eae) = 1 } |
|  | The interface version, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store___addf5610ecf7fe99553e03115fa06f162.html#addf5610ecf7fe99553e03115fa06f162) |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store___af5943312cebd625a4ef059ddb777a5ce.html#af5943312cebd625a4ef059ddb777a5ce) = [CObjectStore\_::Instance](structak__wwise__plugin__notifications__object__store__v1_abc82b903f7060122edc75335deee109d.html#abc82b903f7060122edc75335deee109d) |
|  | Base instance type for receiving notifications on related Object Store's changes. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store___af5943312cebd625a4ef059ddb777a5ce.html#af5943312cebd625a4ef059ddb777a5ce) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [RequestedHostInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_object_store_01_4_a334aebe57b3b2c3df5726e0d9fec6e2d.html#a334aebe57b3b2c3df5726e0d9fec6e2d) () |
|  | |
| - Public 成员函数 继承自 [AK.Wwise::Plugin::V1::Notifications::ObjectStore\_< PropertySetT >](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store__.html) | |
| [InterfacePtr](namespace_a_k_1_1_wwise_1_1_plugin_a9131bb705f2bd282ad65cac4efa17095.html#a9131bb705f2bd282ad65cac4efa17095) | [GetInterfacePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store___a3b188424290e0c011a267eb9daf769ef.html#a3b188424290e0c011a267eb9daf769ef) () |
|  | |
| [CObjectStore\_::Instance](structak__wwise__plugin__notifications__object__store__v1_abc82b903f7060122edc75335deee109d.html#abc82b903f7060122edc75335deee109d) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store___a2ac96653558d2a936fe0308b7a40bc13.html#a2ac96653558d2a936fe0308b7a40bc13) () |
|  | |
| const [CObjectStore\_::Instance](structak__wwise__plugin__notifications__object__store__v1_abc82b903f7060122edc75335deee109d.html#abc82b903f7060122edc75335deee109d) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store___a53fa44f286e4637f58a7637667523c73.html#a53fa44f286e4637f58a7637667523c73) () const |
|  | |
|  | [ObjectStore\_](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store___ad0a53ac8a5aa1562d898ff61b0821a49.html#ad0a53ac8a5aa1562d898ff61b0821a49) () |
|  | |
| virtual | [~ObjectStore\_](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store___afbf84dcba94ba46561b8e6f8aeaa9e14.html#afbf84dcba94ba46561b8e6f8aeaa9e14) () |
|  | |
| virtual void | [NotifyInnerObjectPropertyChanged](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store___ae961ed7e4a171e3d2d5f1e7aee216636.html#ae961ed7e4a171e3d2d5f1e7aee216636) (PropertySetT &in\_PSet, const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) |
|  | Called when an inner property set's data has changed. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store___ae961ed7e4a171e3d2d5f1e7aee216636.html#ae961ed7e4a171e3d2d5f1e7aee216636) |
|  | |
| virtual void | [NotifyInnerObjectAddedRemoved](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store___a6c7998570b4d4da732791eae905d720a.html#a6c7998570b4d4da732791eae905d720a) (PropertySetT &in\_PSet, unsigned int in\_uiIndex, [NotifyInnerObjectOperation](namespace_a_k_1_1_wwise_1_1_plugin_a8c06b37fdc871c51e7bc65b568b3c987.html#a8c06b37fdc871c51e7bc65b568b3c987) in\_eOperation) |
|  | Called when an inner property set has changed. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store___a6c7998570b4d4da732791eae905d720a.html#a6c7998570b4d4da732791eae905d720a) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [ObjectStore](namespace_a_k_1_1_wwise_1_1_plugin_aa1a4c71b6a4959d8e06f9e3cc976c749.html#aa1a4c71b6a4959d8e06f9e3cc976c749) ::[Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store___1_1_interface.html) & | [g\_objectStoreInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_object_store_01_4_a1c2753c218147570ad20732d10be3dc2.html#a1c2753c218147570ad20732d10be3dc2) = HostInterfaceDefinition::g\_cppinterface |
|  | |
| HostInterfaceDefinition::Instance & | [m\_objectStore](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_object_store_01_4_a0b5a1431ace0cef53caaaedde46631b9.html#a0b5a1431ace0cef53caaaedde46631b9) = \*HostInterfaceDefinition::m\_instance |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - 静态 Public 属性 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< ObjectStore, true >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) | [g\_cppinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | The unique interface for this plug-in interface. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | |

## 详细描述

在文件 [HostObjectStore.h](_host_object_store_8h_source.html) 第 [763](_host_object_store_8h_source.html#l00763) 行定义.