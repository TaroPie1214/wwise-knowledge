# RequestedHostInterface&lt; ObjectMedia &gt;

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [RequestedHostInterface< ObjectMedia >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_object_media_01_4.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_object_media_01_4-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AK.Wwise::Plugin::RequestedHostInterface< ObjectMedia >类 参考

`#include <HostObjectMedia.h>`

类 AK.Wwise::Plugin::RequestedHostInterface< ObjectMedia > 继承关系图:

![](../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_object_media_01_4.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [HostInterfaceDefinition](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_object_media_01_4_a93e9cb9886dab12f734b0c3419231e8c.html#a93e9cb9886dab12f734b0c3419231e8c) = [HostInterfaceGlue](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html)< [ObjectMedia](namespace_a_k_1_1_wwise_1_1_plugin_a0325d70f4523c31f1b4f5dc8acdf3e2b.html#a0325d70f4523c31f1b4f5dc8acdf3e2b), true > |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< ObjectMedia, true >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| enum |  |
|  | |
| enum |  |
|  | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) = typename CPPInstance::GluedInterface |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a8bdb82de06eb8956882fe9d524e96e08.html#a8bdb82de06eb8956882fe9d524e96e08) = [ObjectMedia](namespace_a_k_1_1_wwise_1_1_plugin_a0325d70f4523c31f1b4f5dc8acdf3e2b.html#a0325d70f4523c31f1b4f5dc8acdf3e2b) |
|  | |
| using | [CInstance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_af60fd0de7e69af6931e04ea9ec1ffc09.html#af60fd0de7e69af6931e04ea9ec1ffc09) = typename CPPInstance::Instance |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::V1::Notifications::ObjectMedia\_](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_media__.html) | |
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
|  | [RequestedHostInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_object_media_01_4_afc5731593c794ac9ede0dbb97570349d.html#afc5731593c794ac9ede0dbb97570349d) () |
|  | |
| - Public 成员函数 继承自 [AK.Wwise::Plugin::V1::Notifications::ObjectMedia\_](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_media__.html) | |
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

|  |  |
| --- | --- |
| Public 属性 | |
| [ObjectMedia](namespace_a_k_1_1_wwise_1_1_plugin_a0325d70f4523c31f1b4f5dc8acdf3e2b.html#a0325d70f4523c31f1b4f5dc8acdf3e2b) ::[Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_object_media___1_1_interface.html) & | [g\_objectMediaInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_object_media_01_4_a1d7619bb2bd7809a56ac76bdb69f452b.html#a1d7619bb2bd7809a56ac76bdb69f452b) = HostInterfaceDefinition::g\_cppinterface |
|  | |
| [HostInterfaceDefinition::Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a8bdb82de06eb8956882fe9d524e96e08.html#a8bdb82de06eb8956882fe9d524e96e08) & | [m\_objectMedia](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_object_media_01_4_a41a8f58bfb78858b1c7ebb75358edc3c.html#a41a8f58bfb78858b1c7ebb75358edc3c) = \*HostInterfaceDefinition::m\_instance |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - 静态 Public 属性 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< ObjectMedia, true >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) | [g\_cppinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | The unique interface for this plug-in interface. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | |

## 详细描述

在文件 [HostObjectMedia.h](_host_object_media_8h_source.html) 第 [622](_host_object_media_8h_source.html#l00622) 行定义.