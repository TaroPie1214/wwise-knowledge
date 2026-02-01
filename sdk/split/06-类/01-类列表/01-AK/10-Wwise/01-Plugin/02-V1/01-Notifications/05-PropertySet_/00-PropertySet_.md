# PropertySet_

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [Notifications](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications.html)
- [PropertySet\_](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set__.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set__-members.html) |
[类](#nested-classes) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::Notifications::PropertySet\_类 参考

[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set__.html#details)

`#include <HostPropertySet.h>`

类 AK.Wwise::Plugin::V1::Notifications::PropertySet\_ 继承关系图:

![](../../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set__.png)

|  |  |
| --- | --- |
| 类 | |
| struct | [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set___1_1_interface.html) |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set___1_1_interface.html#details) |
|  | |

|  |  |
| --- | --- |
| Public 类型 | |
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
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance.html) | |
| virtual | [~ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance_a38e5192dde370d925b0489a70374ff01.html#a38e5192dde370d925b0489a70374ff01) () |
|  | |

## 详细描述

在文件 [HostPropertySet.h](_v1_2_host_property_set_8h_source.html) 第 [2336](_v1_2_host_property_set_8h_source.html#l02336) 行定义.