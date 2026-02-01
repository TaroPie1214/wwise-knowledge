# RequestedHostInterface&lt; PropertySet &gt;

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [RequestedHostInterface< PropertySet >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_property_set_01_4.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_property_set_01_4-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AK.Wwise::Plugin::RequestedHostInterface< PropertySet >类 参考

`#include <HostPropertySet.h>`

类 AK.Wwise::Plugin::RequestedHostInterface< PropertySet > 继承关系图:

![](../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_property_set_01_4.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [HostInterfaceDefinition](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_property_set_01_4_a34ab7c76253beb80c4617e312c4c9dd9.html#a34ab7c76253beb80c4617e312c4c9dd9) = [HostInterfaceGlue](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html)< [PropertySet](namespace_a_k_1_1_wwise_1_1_plugin_a052a63312bad5bdbd0adc1b07decf6de.html#a052a63312bad5bdbd0adc1b07decf6de), true > |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< PropertySet, true >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| enum |  |
|  | |
| enum |  |
|  | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) = typename CPPInstance::GluedInterface |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a8bdb82de06eb8956882fe9d524e96e08.html#a8bdb82de06eb8956882fe9d524e96e08) = [PropertySet](namespace_a_k_1_1_wwise_1_1_plugin_a052a63312bad5bdbd0adc1b07decf6de.html#a052a63312bad5bdbd0adc1b07decf6de) |
|  | |
| using | [CInstance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_af60fd0de7e69af6931e04ea9ec1ffc09.html#af60fd0de7e69af6931e04ea9ec1ffc09) = typename CPPInstance::Instance |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::V1::Notifications::PropertySet\_](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set__.html) | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set___a3029d44a95407f34ed4f18a40d01648d.html#a3029d44a95407f34ed4f18a40d01648da147fa96b3ce68bf7f9c77ccff7d9e106) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_NOTIFICATIONS\_PROPERTY\_SET } |
|  | The interface type, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set___a3029d44a95407f34ed4f18a40d01648d.html#a3029d44a95407f34ed4f18a40d01648d) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set___af64394a4f53e41c31e98b14da7a43e2a.html#af64394a4f53e41c31e98b14da7a43e2aa8c1768dc5d2f64b3a6e260f97bd6ccc6) = 1 } |
|  | The interface version, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set___af64394a4f53e41c31e98b14da7a43e2a.html#af64394a4f53e41c31e98b14da7a43e2a) |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set___af37e81a6ca6f29faf32ae11baff0041d.html#af37e81a6ca6f29faf32ae11baff0041d) = [CPropertySet\_::Instance](structak__wwise__plugin__notifications__property__set__v1_a914951e9383ed25224afd6b9c435f1a7.html#a914951e9383ed25224afd6b9c435f1a7) |
|  | Base instance type for receiving notifications on property set's changes. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set___af37e81a6ca6f29faf32ae11baff0041d.html#af37e81a6ca6f29faf32ae11baff0041d) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [RequestedHostInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_property_set_01_4_a69d24aa919c12abba22aaa5abdd47622.html#a69d24aa919c12abba22aaa5abdd47622) () |
|  | |
| - Public 成员函数 继承自 [AK.Wwise::Plugin::V1::Notifications::PropertySet\_](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set__.html) | |
| [InterfacePtr](namespace_a_k_1_1_wwise_1_1_plugin_a9131bb705f2bd282ad65cac4efa17095.html#a9131bb705f2bd282ad65cac4efa17095) | [GetInterfacePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set___a0577dcdbb2492658db8e2020b5b27828.html#a0577dcdbb2492658db8e2020b5b27828) () |
|  | |
| [CPropertySet\_::Instance](structak__wwise__plugin__notifications__property__set__v1_a914951e9383ed25224afd6b9c435f1a7.html#a914951e9383ed25224afd6b9c435f1a7) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set___ab75710d240c2bf4fba80265b703c14b0.html#ab75710d240c2bf4fba80265b703c14b0) () |
|  | |
| const [CPropertySet\_::Instance](structak__wwise__plugin__notifications__property__set__v1_a914951e9383ed25224afd6b9c435f1a7.html#a914951e9383ed25224afd6b9c435f1a7) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set___a599d5ac0bb91269755251a70dd2924a6.html#a599d5ac0bb91269755251a70dd2924a6) () const |
|  | |
|  | [PropertySet\_](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set___aa089872e49cc226c9658d7185e8bbf17.html#aa089872e49cc226c9658d7185e8bbf17) () |
|  | |
| virtual | [~PropertySet\_](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set___adc42a723aa87b04d312e77becb52e41a.html#adc42a723aa87b04d312e77becb52e41a) () |
|  | |
| virtual void | [NotifyPropertyChanged](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set___a90d279b0b03eed79cb10a5b56b0aff90.html#a90d279b0b03eed79cb10a5b56b0aff90) (const GUID &in\_guidPlatform, const char \*in\_pszPropertyName) |
|  | This function is called by [Wwise](namespace_a_k_1_1_wwise.html) when a plug-in property changes. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set___a90d279b0b03eed79cb10a5b56b0aff90.html#a90d279b0b03eed79cb10a5b56b0aff90) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [PropertySet](namespace_a_k_1_1_wwise_1_1_plugin_a052a63312bad5bdbd0adc1b07decf6de.html#a052a63312bad5bdbd0adc1b07decf6de) ::[Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set___1_1_interface.html) & | [g\_propertySetInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_property_set_01_4_ab4eea23a1518dd50bb2a5a326e1206a0.html#ab4eea23a1518dd50bb2a5a326e1206a0) = HostInterfaceDefinition::g\_cppinterface |
|  | |
| [HostInterfaceDefinition::Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a8bdb82de06eb8956882fe9d524e96e08.html#a8bdb82de06eb8956882fe9d524e96e08) & | [m\_propertySet](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_property_set_01_4_a43d7875a8eaa59633e91a22422526acb.html#a43d7875a8eaa59633e91a22422526acb) = \*HostInterfaceDefinition::m\_instance |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - 静态 Public 属性 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< PropertySet, true >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) | [g\_cppinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | The unique interface for this plug-in interface. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | |

## 详细描述

在文件 [HostPropertySet.h](_host_property_set_8h_source.html) 第 [362](_host_property_set_8h_source.html#l00362) 行定义.