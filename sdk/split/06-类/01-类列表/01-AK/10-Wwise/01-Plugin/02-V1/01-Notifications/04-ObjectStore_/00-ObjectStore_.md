# ObjectStore_

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [Notifications](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications.html)
- [ObjectStore\_](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store__.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store__-members.html) |
[类](#nested-classes) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::Notifications::ObjectStore\_< PropertySetT > 模板类 参考

[Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store___1_1_interface.html "The C interface, fulfilled by your plug-in.") able to receive notifications for custom inner property sets.
[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store__.html#details)

`#include <HostObjectStore.h>`

类 AK.Wwise::Plugin::V1::Notifications::ObjectStore\_< PropertySetT > 继承关系图:

![](../../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store__.png)

|  |  |
| --- | --- |
| 类 | |
| struct | [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store___1_1_interface.html) |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store___1_1_interface.html#details) |
|  | |

|  |  |
| --- | --- |
| Public 类型 | |
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
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance.html) | |
| virtual | [~ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance_a38e5192dde370d925b0489a70374ff01.html#a38e5192dde370d925b0489a70374ff01) () |
|  | |

## 详细描述

### template<typename PropertySetT = AK::Wwise::Plugin::PropertySet> class AK.Wwise::Plugin::V1::Notifications::ObjectStore\_< PropertySetT >

[Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_store___1_1_interface.html "The C interface, fulfilled by your plug-in.") able to receive notifications for custom inner property sets.

|  |  |
| --- | --- |
|  | **备注:** In order to manage property sets, you must make sure to use [AK::Wwise::Plugin::RequestPropertySet](namespace_a_k_1_1_wwise_1_1_plugin_a5eb9b772d01c414e7c77b44ef66e661f.html#a5eb9b772d01c414e7c77b44ef66e661f) in your plug-in. |

参见
:   - [内部对象](plugin_xml.html#wwiseplugin_objectstore)
    - [ak\_wwise\_plugin\_host\_object\_store\_v1](structak__wwise__plugin__host__object__store__v1.html)

在文件 [HostObjectStore.h](_host_object_store_8h_source.html) 第 [610](_host_object_store_8h_source.html#l00610) 行定义.