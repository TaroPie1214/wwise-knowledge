# ObjectMedia_

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [Notifications](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications.html)
- [ObjectMedia\_](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_media__.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_media__-members.html) |
[类](#nested-classes) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::Notifications::ObjectMedia\_类 参考

[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_media__.html#details)

`#include <HostObjectMedia.h>`

类 AK.Wwise::Plugin::V1::Notifications::ObjectMedia\_ 继承关系图:

![](../../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_media__.png)

|  |  |
| --- | --- |
| 类 | |
| struct | [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_media___1_1_interface.html) |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_media___1_1_interface.html#details) |
|  | |

|  |  |
| --- | --- |
| Public 类型 | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_media___a52309616abc062053cbd72fcc076c368.html#a52309616abc062053cbd72fcc076c368a6ffa75137943e293d9769db5df2707f4) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NOTIFICATIONS\_OBJECT\_MEDIA } |
|  | The interface type, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_media___a52309616abc062053cbd72fcc076c368.html#a52309616abc062053cbd72fcc076c368) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_media___a3e6c6c3f0ab3a87f2677f2be4fcd3359.html#a3e6c6c3f0ab3a87f2677f2be4fcd3359a541f169651a1faba43ae08ecd9a1f6b3) = 1 } |
|  | The interface version, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_media___a3e6c6c3f0ab3a87f2677f2be4fcd3359.html#a3e6c6c3f0ab3a87f2677f2be4fcd3359) |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_media___ab38c25b0424fabf021bd3937123cebb7.html#ab38c25b0424fabf021bd3937123cebb7) = [CObjectMedia\_::Instance](structak__wwise__plugin__notifications__object__media__v1_ab0fc4bef5cfb0af039208cd8798864db.html#ab0fc4bef5cfb0af039208cd8798864db) |
|  | Base instance type for receiving notifications on related object media's changes. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_media___ab38c25b0424fabf021bd3937123cebb7.html#ab38c25b0424fabf021bd3937123cebb7) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| [InterfacePtr](namespace_a_k_1_1_wwise_1_1_plugin_a9131bb705f2bd282ad65cac4efa17095.html#a9131bb705f2bd282ad65cac4efa17095) | [GetInterfacePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_media___a1264b798e4b3b3294c964fac805c15a4.html#a1264b798e4b3b3294c964fac805c15a4) () |
|  | |
| [CObjectMedia\_::Instance](structak__wwise__plugin__notifications__object__media__v1_ab0fc4bef5cfb0af039208cd8798864db.html#ab0fc4bef5cfb0af039208cd8798864db) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_media___a2d0b813d80eb74faec2e30fb515d4f06.html#a2d0b813d80eb74faec2e30fb515d4f06) () |
|  | |
| const [CObjectMedia\_::Instance](structak__wwise__plugin__notifications__object__media__v1_ab0fc4bef5cfb0af039208cd8798864db.html#ab0fc4bef5cfb0af039208cd8798864db) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_media___a2d7024f7557b5e1491303bc2d6e7b964.html#a2d7024f7557b5e1491303bc2d6e7b964) () const |
|  | |
|  | [ObjectMedia\_](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_media___a7d1e6ac6f501e8b1ca5545451f040768.html#a7d1e6ac6f501e8b1ca5545451f040768) () |
|  | |
| virtual | [~ObjectMedia\_](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_media___a3e5ebdd4eb759854765b177c67eacbd0.html#a3e5ebdd4eb759854765b177c67eacbd0) () |
|  | |
| virtual void | [NotifyPluginMediaChanged](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_media___aeeade48f5038593806cbe55ee2204135.html#aeeade48f5038593806cbe55ee2204135) () |
|  | This function is called by [Wwise](namespace_a_k_1_1_wwise.html) when any of the plug-in media changes. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_media___aeeade48f5038593806cbe55ee2204135.html#aeeade48f5038593806cbe55ee2204135) |
|  | |
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance.html) | |
| virtual | [~ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance_a38e5192dde370d925b0489a70374ff01.html#a38e5192dde370d925b0489a70374ff01) () |
|  | |

## 详细描述

在文件 [HostObjectMedia.h](_host_object_media_8h_source.html) 第 [520](_host_object_media_8h_source.html#l00520) 行定义.