# XmlWriter

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [XmlWriter](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer-members.html) |
[类](#nested-classes) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::XmlWriter类 参考

API interface for XML-based plug-in persistence.
[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer.html#details)

`#include <HostXml.h>`

类 AK.Wwise::Plugin::V1::XmlWriter 继承关系图:

![](../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer.png)

|  |  |
| --- | --- |
| 类 | |
| class | [AutoStartEndElement](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_1_1_auto_start_end_element.html) |
|  | Use this class to handle the WriteStartElement/WriteEndElement pair automatically in a C++ scope. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_1_1_auto_start_end_element.html#details) |
|  | |

|  |  |
| --- | --- |
| Public 类型 | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_a177c9597ab47079f2db1d59c26a66344.html#a177c9597ab47079f2db1d59c26a66344ab1a1f8b038336b7a227e162e35fdf3a3) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_XML } |
|  | The interface type, as requested by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_a177c9597ab47079f2db1d59c26a66344.html#a177c9597ab47079f2db1d59c26a66344) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_aa4e2aa05f08806b2a5765081a7b3d7e5.html#aa4e2aa05f08806b2a5765081a7b3d7e5a5a091d1bd31b5229c9093b6baaff5ac8) = 1 } |
|  | The interface version, as requested by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_aa4e2aa05f08806b2a5765081a7b3d7e5.html#aa4e2aa05f08806b2a5765081a7b3d7e5) |
|  | |
| using | [Interface](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_a94ff2a79fcfeb840681846229b379fed.html#a94ff2a79fcfeb840681846229b379fed) = [CHostXml](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a074a0bfcc47a57a8a183590d1251f4bb.html#a074a0bfcc47a57a8a183590d1251f4bb) |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::CBaseInstanceGlue< CHostXml, CHostXml::WriterInstance >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue.html) | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue_aff6221118cb1d81f1e67f1932fb66b60.html#aff6221118cb1d81f1e67f1932fb66b60) = [CHostXml::WriterInstance](structak__wwise__plugin__host__xml__v1_a06c351967680d8541028f3c10091c4a5.html#a06c351967680d8541028f3c10091c4a5) |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::CBaseInterfaceGlue< CHostXml >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html) | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a270936e06e5c9627548246cbebde0467.html#a270936e06e5c9627548246cbebde0467) = [CHostXml](namespace_a_k_1_1_wwise_1_1_plugin_a3dc2daeee0ab37ad19f0077ae3bfc9a2.html#a3dc2daeee0ab37ad19f0077ae3bfc9a2) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| bool | [IsReady](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_a1595fe6e55cf4854a72083a59c8c3b77.html#a1595fe6e55cf4854a72083a59c8c3b77) () const |
|  | Determines if the writer is ready to be used. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_a1595fe6e55cf4854a72083a59c8c3b77.html#a1595fe6e55cf4854a72083a59c8c3b77) |
|  | |
| [AK::Wwise::Plugin::XmlWriteReady::WriteReady](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_write_ready_afff47a0c6c5350e7c2f0f390af13f382.html#afff47a0c6c5350e7c2f0f390af13f382) | [GetReadyState](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_ace112b62b13a1a00d766da59822b4fe9.html#ace112b62b13a1a00d766da59822b4fe9) () const |
|  | Determines the state of readiness of the writer. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_ace112b62b13a1a00d766da59822b4fe9.html#ace112b62b13a1a00d766da59822b4fe9) |
|  | |
| bool | [Append](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_a18180435b215ef9d11c1ffb14c717668.html#a18180435b215ef9d11c1ffb14c717668) ([XmlWriter](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer.html) &in\_writerToAppend) |
|  | Appending a first XML writer to a second XML writer. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_a18180435b215ef9d11c1ffb14c717668.html#a18180435b215ef9d11c1ffb14c717668) |
|  | |
| [AK::Wwise::Plugin::XmlWriteState::WriteState](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_write_state_a9802053bd44c7926486300763e602293.html#a9802053bd44c7926486300763e602293) | [GetWriteState](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_a5b0ee38f5938a8a108a7d3499e13f9a5.html#a5b0ee38f5938a8a108a7d3499e13f9a5) () const |
|  | Retrieves the state of the node the writer is currently populating. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_a5b0ee38f5938a8a108a7d3499e13f9a5.html#a5b0ee38f5938a8a108a7d3499e13f9a5) |
|  | |
| void | [WriteStartDocument](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_a6036943367f91cbce59e3f1ecc3ba2e0.html#a6036943367f91cbce59e3f1ecc3ba2e0) () |
|  | Starts a new XML document. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_a6036943367f91cbce59e3f1ecc3ba2e0.html#a6036943367f91cbce59e3f1ecc3ba2e0) |
|  | |
| void | [WriteEndDocument](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_a5a92ac9e6c87bbcf63a645aa73171927.html#a5a92ac9e6c87bbcf63a645aa73171927) () |
|  | Ends a completed XML document. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_a5a92ac9e6c87bbcf63a645aa73171927.html#a5a92ac9e6c87bbcf63a645aa73171927) |
|  | |
| void | [WriteStartElement](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_a7a866ea14233332e304f456b31c6bed8.html#a7a866ea14233332e304f456b31c6bed8) (const char \*in\_rcsElementName, [AK::Wwise::Plugin::XmlElementType::ElementType](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_element_type_a36556de11c47219369f6545a96c53583.html#a36556de11c47219369f6545a96c53583) in\_eType) |
|  | Creates a new inner node. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_a7a866ea14233332e304f456b31c6bed8.html#a7a866ea14233332e304f456b31c6bed8) |
|  | |
| void | [WriteEndElement](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_a80ca14f8259d4d8c09c1b84a7c86bed3.html#a80ca14f8259d4d8c09c1b84a7c86bed3) () |
|  | Closes the previous node. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_a80ca14f8259d4d8c09c1b84a7c86bed3.html#a80ca14f8259d4d8c09c1b84a7c86bed3) |
|  | |
| void | [WriteAttributeString](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_ad7350d80d578c2f718a108bfc4a2dd62.html#ad7350d80d578c2f718a108bfc4a2dd62) (const char \*in\_rcsAttribute, const char \*in\_rcsValue) |
|  | Adds an attribute to the current node. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_ad7350d80d578c2f718a108bfc4a2dd62.html#ad7350d80d578c2f718a108bfc4a2dd62) |
|  | |
| void | [WriteString](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_a8296d87c9595a35ebd564407c11b657f.html#a8296d87c9595a35ebd564407c11b657f) (const char \*in\_rcsValue) |
|  | Appends a string as value to the current node. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_a8296d87c9595a35ebd564407c11b657f.html#a8296d87c9595a35ebd564407c11b657f) |
|  | |
| void | [WriteCData](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_ab4185aca65c82228fdf52d9c0f2df461.html#ab4185aca65c82228fdf52d9c0f2df461) (const char \*in\_rcsValue) |
|  | Appends a raw CDATA string as value to the current node. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_ab4185aca65c82228fdf52d9c0f2df461.html#ab4185aca65c82228fdf52d9c0f2df461) |
|  | |
| void | [WriteRaw](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_aa9e2eda930e00894413253113f580e7a.html#aa9e2eda930e00894413253113f580e7a) (const char \*in\_rcsValue) |
|  | Appends a raw string at this precise point of the XML file. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_aa9e2eda930e00894413253113f580e7a.html#aa9e2eda930e00894413253113f580e7a) |
|  | |
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance.html) | |
| virtual | [~ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance_a38e5192dde370d925b0489a70374ff01.html#a38e5192dde370d925b0489a70374ff01) () |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - 静态 Public 属性 继承自 [AK.Wwise::Plugin::CBaseInterfaceGlue< CHostXml >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html) | |
| static [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a270936e06e5c9627548246cbebde0467.html#a270936e06e5c9627548246cbebde0467) \* | [g\_cinterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a8b682b3105da8940f7ea75845254d491.html#a8b682b3105da8940f7ea75845254d491) |
|  | The unique instance of the CInterface interface. Defined at nullptr first, overridden by the Host once loaded. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a8b682b3105da8940f7ea75845254d491.html#a8b682b3105da8940f7ea75845254d491) |
|  | |

## 详细描述

API interface for XML-based plug-in persistence.

The XML plug-in persistence is useful when a plug-in provides custom data handling. Normally, plug-in data is stored through the property sets (see [PropertySet](plugin_backend_model.html#wwiseplugin_propertyset) and [ObjectStore](plugin_xml.html#wwiseplugin_objectstore)). However, a plug-in might provide its own custom handling. For complex interfaces, it might be worthwhile to use the [CustomData](plugin_backend_model.html#wwiseplugin_complexproperty) interface. Loading and saving can then be done through this XML interface.

The XML interface represents a cursor pointing to a node (element), alongside methods to navigate through the hierarchy.

|  |  |
| --- | --- |
|  | **备注:** One unique XML interface is provided for both reading and writing XML. Depending on the instance being provided, it will allow reading or writing through this interface.  It can either be a [ak\_wwise\_plugin\_host\_xml\_reader\_instance\_v1](structak__wwise__plugin__host__xml__reader__instance__v1.html) or a [ak\_wwise\_plugin\_host\_xml\_writer\_instance\_v1](structak__wwise__plugin__host__xml__writer__instance__v1.html). |

在文件 [HostXml.h](_host_xml_8h_source.html) 第 [755](_host_xml_8h_source.html#l00755) 行定义.