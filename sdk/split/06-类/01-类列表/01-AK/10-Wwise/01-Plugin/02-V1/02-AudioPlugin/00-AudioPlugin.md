# AudioPlugin

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [AudioPlugin](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin-members.html) |
[类](#nested-classes) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::AudioPlugin类 参考

[Wwise](namespace_a_k_1_1_wwise.html) API for general Audio Plug-in's backend.
[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin.html#details)

`#include <AudioPlugin.h>`

类 AK.Wwise::Plugin::V1::AudioPlugin 继承关系图:

![](../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin.png)

|  |  |
| --- | --- |
| 类 | |
| struct | [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin_1_1_interface.html) |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin_1_1_interface.html#details) |
|  | |

|  |  |
| --- | --- |
| Public 类型 | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin_a8ca8da54166ac70d051402dd76667d7b.html#a8ca8da54166ac70d051402dd76667d7ba487e620fb5b5c5845a762a9f315bab3b) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_AUDIO\_PLUGIN } |
|  | The interface type, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin_a8ca8da54166ac70d051402dd76667d7b.html#a8ca8da54166ac70d051402dd76667d7b) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin_a638c80e825149993e7c159a9602f52cb.html#a638c80e825149993e7c159a9602f52cba9a0313039b7bacb88807ec88b2c2e417) = 1 } |
|  | The interface version, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin_a638c80e825149993e7c159a9602f52cb.html#a638c80e825149993e7c159a9602f52cb) |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin_aec1f8d50d3708afe17057285915d12d1.html#aec1f8d50d3708afe17057285915d12d1) = [CAudioPlugin::Instance](structak__wwise__plugin__audio__plugin__v1_a98a20db02b16bcbb6e94d759fbadc6cf.html#a98a20db02b16bcbb6e94d759fbadc6cf) |
|  | Base instance type for providing audio plug-in backend services. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin_aec1f8d50d3708afe17057285915d12d1.html#aec1f8d50d3708afe17057285915d12d1) |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::RequestedHostInterface< PropertySet >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_property_set_01_4.html) | |
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
| - Public 类型 继承自 [AK.Wwise::Plugin::RequestedHostInterface< DataWriter >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_data_writer_01_4.html) | |
| using | [HostInterfaceDefinition](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_data_writer_01_4_a39d3089be9787530e343df10910e13be.html#a39d3089be9787530e343df10910e13be) = [HostInterfaceGlue](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html)< [DataWriter](namespace_a_k_1_1_wwise_1_1_plugin_a32526a23215a4452f561220b527e12f8.html#a32526a23215a4452f561220b527e12f8), false > |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< DataWriter, false >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| enum |  |
|  | |
| enum |  |
|  | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) = typename CPPInstance::GluedInterface |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a8bdb82de06eb8956882fe9d524e96e08.html#a8bdb82de06eb8956882fe9d524e96e08) = [DataWriter](namespace_a_k_1_1_wwise_1_1_plugin_a32526a23215a4452f561220b527e12f8.html#a32526a23215a4452f561220b527e12f8) |
|  | |
| using | [CInstance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_af60fd0de7e69af6931e04ea9ec1ffc09.html#af60fd0de7e69af6931e04ea9ec1ffc09) = typename CPPInstance::Instance |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| [InterfacePtr](namespace_a_k_1_1_wwise_1_1_plugin_a9131bb705f2bd282ad65cac4efa17095.html#a9131bb705f2bd282ad65cac4efa17095) | [GetInterfacePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin_aa42513e8697e14626ffc44a6b7a825f4.html#aa42513e8697e14626ffc44a6b7a825f4) () |
|  | |
| [CAudioPlugin::Instance](structak__wwise__plugin__audio__plugin__v1_a98a20db02b16bcbb6e94d759fbadc6cf.html#a98a20db02b16bcbb6e94d759fbadc6cf) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin_ae54a0c7e75a0b5f1b8d5c085aa7e4250.html#ae54a0c7e75a0b5f1b8d5c085aa7e4250) () |
|  | |
| const [CAudioPlugin::Instance](structak__wwise__plugin__audio__plugin__v1_a98a20db02b16bcbb6e94d759fbadc6cf.html#a98a20db02b16bcbb6e94d759fbadc6cf) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin_a43856097bb4e1b0dd0bc9ddc80f67bb0.html#a43856097bb4e1b0dd0bc9ddc80f67bb0) () const |
|  | |
|  | [AudioPlugin](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin_ac71cabaad796947523dbb83008f21e6a.html#ac71cabaad796947523dbb83008f21e6a) () |
|  | |
| virtual | [~AudioPlugin](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin_ae24dec3405d85dfb592f26f7b92d08f8.html#ae24dec3405d85dfb592f26f7b92d08f8) () |
|  | |
| virtual bool | [GetBankParameters](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin_ae59a3955718ed3bbde0521da21cd8539.html#ae59a3955718ed3bbde0521da21cd8539) (const GUID &in\_guidPlatform, [DataWriter](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer.html) &in\_dataWriter) const |
|  | Obtains parameters that will be written to a bank. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin_ae59a3955718ed3bbde0521da21cd8539.html#ae59a3955718ed3bbde0521da21cd8539) |
|  | |
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance.html) | |
| virtual | [~ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance_a38e5192dde370d925b0489a70374ff01.html#a38e5192dde370d925b0489a70374ff01) () |
|  | |
| - Public 成员函数 继承自 [AK.Wwise::Plugin::RequestedHostInterface< PropertySet >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_property_set_01_4.html) | |
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
| - Public 成员函数 继承自 [AK.Wwise::Plugin::RequestedHostInterface< DataWriter >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_data_writer_01_4.html) | |
|  | [RequestedHostInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_data_writer_01_4_a0c81060bc9ebdd8d1752e369699c8448.html#a0c81060bc9ebdd8d1752e369699c8448) () |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - Public 属性 继承自 [AK.Wwise::Plugin::RequestedHostInterface< PropertySet >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_property_set_01_4.html) | |
| [PropertySet](namespace_a_k_1_1_wwise_1_1_plugin_a052a63312bad5bdbd0adc1b07decf6de.html#a052a63312bad5bdbd0adc1b07decf6de) ::[Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_notifications_1_1_property_set___1_1_interface.html) & | [g\_propertySetInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_property_set_01_4_ab4eea23a1518dd50bb2a5a326e1206a0.html#ab4eea23a1518dd50bb2a5a326e1206a0) = HostInterfaceDefinition::g\_cppinterface |
|  | |
| [HostInterfaceDefinition::Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a8bdb82de06eb8956882fe9d524e96e08.html#a8bdb82de06eb8956882fe9d524e96e08) & | [m\_propertySet](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_property_set_01_4_a43d7875a8eaa59633e91a22422526acb.html#a43d7875a8eaa59633e91a22422526acb) = \*HostInterfaceDefinition::m\_instance |
|  | |
| - Public 属性 继承自 [AK.Wwise::Plugin::RequestedHostInterface< DataWriter >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_data_writer_01_4.html) | |
| [DataWriter](namespace_a_k_1_1_wwise_1_1_plugin_a32526a23215a4452f561220b527e12f8.html#a32526a23215a4452f561220b527e12f8) ::Interface & | [g\_dataWriterInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_data_writer_01_4_ab8db6bc9cbbfc72c186fb209aeef8859.html#ab8db6bc9cbbfc72c186fb209aeef8859) = HostInterfaceDefinition::g\_cppinterface |
|  | |
| - 静态 Public 属性 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< PropertySet, true >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) | [g\_cppinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | The unique interface for this plug-in interface. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | |
| - 静态 Public 属性 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< DataWriter, false >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) | [g\_cppinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | The unique interface for this plug-in interface. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | |

## 详细描述

[Wwise](namespace_a_k_1_1_wwise.html) API for general Audio Plug-in's backend.

参见
:   - [ak\_wwise\_plugin\_audio\_plugin\_instance\_v1](structak__wwise__plugin__audio__plugin__instance__v1.html) instance type
    - [ak\_wwise\_plugin\_audio\_plugin\_v1](structak__wwise__plugin__audio__plugin__v1.html) C [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin_1_1_interface.html "The C interface, fulfilled by your plug-in.")
    - [AK\_WWISE\_PLUGIN\_AUDIO\_PLUGIN\_V1\_ID](_audio_plugin_8h_af21f7290225f823c30ea9bba6173c2ae.html#af21f7290225f823c30ea9bba6173c2ae) Current ID for interface
    - [AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_AUDIO\_PLUGIN](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9af60f00124117a22873d01c98255478ed)
    - [设计工具插件的后端](wwiseplugin_backend.html)

|  |  |
| --- | --- |
|  | **备注:** The [AK::Wwise::Plugin::RequestPropertySet](namespace_a_k_1_1_wwise_1_1_plugin_a5eb9b772d01c414e7c77b44ef66e661f.html#a5eb9b772d01c414e7c77b44ef66e661f) and [AK::Wwise::Plugin::RequestWrite](namespace_a_k_1_1_wwise_1_1_plugin_a4b87b9ead392d9ede43fed7d3629496f.html#a4b87b9ead392d9ede43fed7d3629496f) classes are automatically derived when providing [AK::Wwise::Plugin::AudioPlugin](namespace_a_k_1_1_wwise_1_1_plugin_a989b8417cedde33d928b90171491fcc5.html#a989b8417cedde33d928b90171491fcc5) in C++. |

在文件 [AudioPlugin.h](_audio_plugin_8h_source.html) 第 [130](_audio_plugin_8h_source.html#l00130) 行定义.