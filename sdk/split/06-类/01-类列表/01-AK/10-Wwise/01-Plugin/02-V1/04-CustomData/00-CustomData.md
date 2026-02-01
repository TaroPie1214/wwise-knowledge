# CustomData

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [CustomData](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data-members.html) |
[类](#nested-classes) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::CustomData类 参考

Backend API to load and save custom data in XML format.
[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data.html#details)

`#include <CustomData.h>`

类 AK.Wwise::Plugin::V1::CustomData 继承关系图:

![](../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data.png)

|  |  |
| --- | --- |
| 类 | |
| struct | [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_1_1_interface.html) |
|  | |

|  |  |
| --- | --- |
| Public 类型 | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_a1b511bef9fc10d093e93050ddc99baf4.html#a1b511bef9fc10d093e93050ddc99baf4a70a178a1d48fdf6bba345b142e746955) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_CUSTOM\_DATA } |
|  | The interface type, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_a1b511bef9fc10d093e93050ddc99baf4.html#a1b511bef9fc10d093e93050ddc99baf4) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_a37c0850e356a81f04e8e453f49d48c25.html#a37c0850e356a81f04e8e453f49d48c25a34fa4313a84095b2353013562bd3d549) = 1 } |
|  | The interface version, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_a37c0850e356a81f04e8e453f49d48c25.html#a37c0850e356a81f04e8e453f49d48c25) |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_a9addbbb9bbd3655991ea99ad25cc90fb.html#a9addbbb9bbd3655991ea99ad25cc90fb) = [CCustomData::Instance](structak__wwise__plugin__custom__data__v1_af1603ab1092422cd732f495185ba71d3.html#af1603ab1092422cd732f495185ba71d3) |
|  | Base instance type for providing custom data loading and saving. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_a9addbbb9bbd3655991ea99ad25cc90fb.html#a9addbbb9bbd3655991ea99ad25cc90fb) |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::RequestedHostInterface< XmlReader >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_xml_reader_01_4.html) | |
| using | [HostInterfaceDefinition](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_xml_reader_01_4_ad30065a0e1e0e8736167b494f4a2fa65.html#ad30065a0e1e0e8736167b494f4a2fa65) = [HostInterfaceGlue](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html)< [XmlReader](namespace_a_k_1_1_wwise_1_1_plugin_ad4bfa579ff371e16befd0130d33d7150.html#ad4bfa579ff371e16befd0130d33d7150), false > |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< XmlReader, false >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| enum |  |
|  | |
| enum |  |
|  | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) = typename CPPInstance::GluedInterface |
|  | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a8bdb82de06eb8956882fe9d524e96e08.html#a8bdb82de06eb8956882fe9d524e96e08) = [XmlReader](namespace_a_k_1_1_wwise_1_1_plugin_ad4bfa579ff371e16befd0130d33d7150.html#ad4bfa579ff371e16befd0130d33d7150) |
|  | |
| using | [CInstance](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_af60fd0de7e69af6931e04ea9ec1ffc09.html#af60fd0de7e69af6931e04ea9ec1ffc09) = typename CPPInstance::Instance |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| [InterfacePtr](namespace_a_k_1_1_wwise_1_1_plugin_a9131bb705f2bd282ad65cac4efa17095.html#a9131bb705f2bd282ad65cac4efa17095) | [GetInterfacePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_af9fef76535336ca06b0c14462f697a91.html#af9fef76535336ca06b0c14462f697a91) () |
|  | The C interface, fulfilled by your plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_af9fef76535336ca06b0c14462f697a91.html#af9fef76535336ca06b0c14462f697a91) |
|  | |
| [CCustomData::Instance](structak__wwise__plugin__custom__data__v1_af1603ab1092422cd732f495185ba71d3.html#af1603ab1092422cd732f495185ba71d3) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_ae0ca944f33e61c9518dadcf39e169bc4.html#ae0ca944f33e61c9518dadcf39e169bc4) () |
|  | |
| const [CCustomData::Instance](structak__wwise__plugin__custom__data__v1_af1603ab1092422cd732f495185ba71d3.html#af1603ab1092422cd732f495185ba71d3) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_a3cc7fd45754ad20da92220a0c84eee3e.html#a3cc7fd45754ad20da92220a0c84eee3e) () const |
|  | |
|  | [CustomData](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_adc7bfcf5eeb05e7c37da46198462c3b4.html#adc7bfcf5eeb05e7c37da46198462c3b4) () |
|  | |
| virtual | [~CustomData](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_a7c30aef597fc9073ba8e344709d36f95.html#a7c30aef597fc9073ba8e344709d36f95) () |
|  | |
| virtual void | [InitToDefault](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_ace2504ae8a0dc5404e5a9035486ccdb5.html#ace2504ae8a0dc5404e5a9035486ccdb5) () |
|  | Initializes the plug-in's custom data to its default values. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_ace2504ae8a0dc5404e5a9035486ccdb5.html#ace2504ae8a0dc5404e5a9035486ccdb5) |
|  | |
| virtual bool | [InitFromInstance](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_a72ae7aacdfaf7739f0f47762f82b915a.html#a72ae7aacdfaf7739f0f47762f82b915a) (const [CustomData](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data.html) &in\_source) |
|  | Copy the plug-in's custom data from another instance of the same plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_a72ae7aacdfaf7739f0f47762f82b915a.html#a72ae7aacdfaf7739f0f47762f82b915a) |
|  | |
| virtual bool | [InitFromWorkunit](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_a98ef6df5fb929064e5bb3ffef29a1e10.html#a98ef6df5fb929064e5bb3ffef29a1e10) ([XmlReader](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader.html) &in\_reader) |
|  | Load the custom data structure from the provided Work Unit's XML. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_a98ef6df5fb929064e5bb3ffef29a1e10.html#a98ef6df5fb929064e5bb3ffef29a1e10) |
|  | |
| virtual bool | [Save](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_aa530abda0c93227689027585a756aa4b.html#aa530abda0c93227689027585a756aa4b) ([XmlWriter](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer.html) &in\_writer) |
|  | Save custom data structure in the provided XML. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_aa530abda0c93227689027585a756aa4b.html#aa530abda0c93227689027585a756aa4b) |
|  | |
| virtual void | [OnDelete](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_a4d67d63dcec584535d1faa0ec093b86d.html#a4d67d63dcec584535d1faa0ec093b86d) () |
|  | OnDelete function is called when the user presses the "delete" button on a plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_a4d67d63dcec584535d1faa0ec093b86d.html#a4d67d63dcec584535d1faa0ec093b86d) |
|  | |
| virtual bool | [GetPluginData](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_a6740b8fc3bfeec655cfcbe5fd69e1b98.html#a6740b8fc3bfeec655cfcbe5fd69e1b98) (const GUID &in\_guidPlatform, [AkPluginParamID](_ak_typedefs_8h_a4cb8ff0b7014efdaa21697f4ef928926.html#a4cb8ff0b7014efdaa21697f4ef928926) in\_idParam, [DataWriter](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer.html) &in\_dataWriter) const |
|  | Obtains parameters that will be sent to the sound engine when [Wwise](namespace_a_k_1_1_wwise.html) is connected. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_a6740b8fc3bfeec655cfcbe5fd69e1b98.html#a6740b8fc3bfeec655cfcbe5fd69e1b98) |
|  | |
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance.html) | |
| virtual | [~ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance_a38e5192dde370d925b0489a70374ff01.html#a38e5192dde370d925b0489a70374ff01) () |
|  | |
| - Public 成员函数 继承自 [AK.Wwise::Plugin::RequestedHostInterface< XmlReader >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_xml_reader_01_4.html) | |
|  | [RequestedHostInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_xml_reader_01_4_ad997b41806fb4df1cf9126e851389bff.html#ad997b41806fb4df1cf9126e851389bff) () |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - Public 属性 继承自 [AK.Wwise::Plugin::RequestedHostInterface< XmlReader >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_xml_reader_01_4.html) | |
| [XmlReader](namespace_a_k_1_1_wwise_1_1_plugin_ad4bfa579ff371e16befd0130d33d7150.html#ad4bfa579ff371e16befd0130d33d7150) ::Interface & | [g\_xmlTextReaderInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_xml_reader_01_4_a32a42c8fc228d083337c9b70e194729f.html#a32a42c8fc228d083337c9b70e194729f) = HostInterfaceDefinition::g\_cppinterface |
|  | |
| - 静态 Public 属性 继承自 [AK.Wwise::Plugin::HostInterfaceGlue< XmlReader, false >](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue.html) | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_ab0a65d64b13eccf1e05dd4c840f1cb9a.html#ab0a65d64b13eccf1e05dd4c840f1cb9a) | [g\_cppinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | The unique interface for this plug-in interface. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_host_interface_glue_a819405512e21a5dbc4128e959655ea77.html#a819405512e21a5dbc4128e959655ea77) |
|  | |

## 详细描述

Backend API to load and save custom data in XML format.

The initialization of custom-data-aware plug-ins is done using one of three mutually exclusive possibilities:

- **InitToDefault** : Initializes a new instance using the default values
- **InitFromInstance** : Initializes a new instance using the values provided by the original instance.
- **InitFromWorkunit** : Initializes a new instance using the values provided in the Save method.

|  |  |
| --- | --- |
|  | **备注:** AK::Wwise::Plugin::The RequestXml class is automatically derived when providing [CustomData](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data.html) in C++. |

在文件 [CustomData.h](_custom_data_8h_source.html) 第 [194](_custom_data_8h_source.html#l00194) 行定义.