# HostXml.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Wwise](dir_6ea5b71cdf4c60d3386ed2d84846331f.html)
- [Plugin](dir_00900ac4c96da97e1d767c263ed2fa21.html)

[类](#nested-classes) |
[命名空间](#namespaces) |
[宏定义](#define-members) |
[类型定义](#typedef-members) |
[枚举](#enum-members) |
[函数](#func-members)

HostXml.h 文件参考

Wwise Authoring Plug-ins - API for XML-based persistence, as used in CustomData.
[更多...](#details)

`#include "PluginInfoGenerator.h"`

[浏览源代码.](_host_xml_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [ak\_wwise\_plugin\_host\_xml\_v1](structak__wwise__plugin__host__xml__v1.html) |
|  | API interface for XML-based plug-in persistence. [更多...](structak__wwise__plugin__host__xml__v1.html#details) |
|  | |
| class | [AK.Wwise::Plugin::V1::XmlReader](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader.html) |
|  | API interface for XML-based plug-in persistence. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader.html#details) |
|  | |
| class | [AK.Wwise::Plugin::V1::XmlWriter](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer.html) |
|  | API interface for XML-based plug-in persistence. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer.html#details) |
|  | |
| class | [AK.Wwise::Plugin::V1::XmlWriter::AutoStartEndElement](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_1_1_auto_start_end_element.html) |
|  | Use this class to handle the WriteStartElement/WriteEndElement pair automatically in a C++ scope. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_writer_1_1_auto_start_end_element.html#details) |
|  | |
| class | [AK.Wwise::Plugin::RequestedHostInterface< XmlReader >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_xml_reader_01_4.html) |
|  | |
| class | [AK.Wwise::Plugin::RequestedHostInterface< XmlWriter >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_xml_writer_01_4.html) |
|  | |

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |
| namespace | [AK.Wwise](namespace_a_k_1_1_wwise.html) |
|  | |
|  | [AK::Wwise::Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html) |
|  | |
|  | [AK::Wwise::Plugin::XmlWhiteSpaceHandling](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_white_space_handling.html) |
|  | |
|  | [AK::Wwise::Plugin::XmlNodeType](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type.html) |
|  | Types of possible XML elements. See MSDN documentation topics for [XmlNodeType](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type.html "Types of possible XML elements. See MSDN documentation topics for XmlNodeType."). |
|  | |
|  | [AK::Wwise::Plugin::XmlWriteState](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_write_state.html) |
|  | |
|  | [AK::Wwise::Plugin::XmlWriteReady](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_write_ready.html) |
|  | Possible error codes when writing XML |
|  | |
|  | [AK::Wwise::Plugin::XmlElementType](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_element_type.html) |
|  | |
|  | [AK::Wwise::Plugin::V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AK\_WWISE\_PLUGIN\_HOST\_XML\_V1\_ID](_host_xml_8h_a0544a9ac4601bcf5fec44f4ac8928b9e.html#a0544a9ac4601bcf5fec44f4ac8928b9e)()    [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_XML](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a6544a9fc6225dbd24d33f5bef7495d18), 1) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_HOST\_XML\_V1\_CTOR](_host_xml_8h_a1aa711124a7acd32dee164ad85b35c2d.html#a1aa711124a7acd32dee164ad85b35c2d)() |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| using | [AK::Wwise::Plugin::V1::CHostXml](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a074a0bfcc47a57a8a183590d1251f4bb.html#a074a0bfcc47a57a8a183590d1251f4bb) = [ak\_wwise\_plugin\_host\_xml\_v1](structak__wwise__plugin__host__xml__v1.html) |
|  | |
| using | [AK::Wwise::Plugin::V1::RequestXml](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a984cc4dc918e2c4cad2bf43e30c80cbe.html#a984cc4dc918e2c4cad2bf43e30c80cbe) = RequestedHostInterface< XmlReader > |
|  | Requests the XML processing interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a984cc4dc918e2c4cad2bf43e30c80cbe.html#a984cc4dc918e2c4cad2bf43e30c80cbe) |
|  | |
| using | [AK::Wwise::Plugin::CHostXml](namespace_a_k_1_1_wwise_1_1_plugin_a3dc2daeee0ab37ad19f0077ae3bfc9a2.html#a3dc2daeee0ab37ad19f0077ae3bfc9a2) = V1::CHostXml |
|  | Latest version of the C XML interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a3dc2daeee0ab37ad19f0077ae3bfc9a2.html#a3dc2daeee0ab37ad19f0077ae3bfc9a2) |
|  | |
| using | [AK::Wwise::Plugin::XmlReader](namespace_a_k_1_1_wwise_1_1_plugin_ad4bfa579ff371e16befd0130d33d7150.html#ad4bfa579ff371e16befd0130d33d7150) = V1::XmlReader |
|  | Latest version of the C++ XmlReader interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_ad4bfa579ff371e16befd0130d33d7150.html#ad4bfa579ff371e16befd0130d33d7150) |
|  | |
| using | [AK::Wwise::Plugin::XmlWriter](namespace_a_k_1_1_wwise_1_1_plugin_a3917bff28ad1858f6fca96f72f064792.html#a3917bff28ad1858f6fca96f72f064792) = V1::XmlWriter |
|  | Latest version of the C++ XmlWriter interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a3917bff28ad1858f6fca96f72f064792.html#a3917bff28ad1858f6fca96f72f064792) |
|  | |
| using | [AK::Wwise::Plugin::RequestXml](namespace_a_k_1_1_wwise_1_1_plugin_a1612e53e47db2162331f0eb95a1c7b93.html#a1612e53e47db2162331f0eb95a1c7b93) = V1::RequestXml |
|  | Latest version of the requested C++ XML interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a1612e53e47db2162331f0eb95a1c7b93.html#a1612e53e47db2162331f0eb95a1c7b93) |
|  | |

|  |  |
| --- | --- |
| 枚举 | |
| enum | [AK::Wwise::Plugin::XmlWhiteSpaceHandling::WhiteSpaceHandling](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_white_space_handling_a510b0640d810e4ba39142629685c3134.html#a510b0640d810e4ba39142629685c3134) { [AK::Wwise::Plugin::XmlWhiteSpaceHandling::All](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_white_space_handling_a510b0640d810e4ba39142629685c3134.html#a510b0640d810e4ba39142629685c3134a4bb7fec9cf8439ab3d110a3f5f09121b), [AK::Wwise::Plugin::XmlWhiteSpaceHandling::None](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_white_space_handling_a510b0640d810e4ba39142629685c3134.html#a510b0640d810e4ba39142629685c3134ac4f11ed2a88e5f67a68bbdf30310a228), [AK::Wwise::Plugin::XmlWhiteSpaceHandling::Significant](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_white_space_handling_a510b0640d810e4ba39142629685c3134.html#a510b0640d810e4ba39142629685c3134a4fd957780c101b1ca9e7ed37a058b8d9) } |
|  | See MSDN documentation [更多...](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_white_space_handling_a510b0640d810e4ba39142629685c3134.html#a510b0640d810e4ba39142629685c3134) |
|  | |
| enum | [AK::Wwise::Plugin::XmlNodeType::NodeType](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type_a2fa372cb0681531259c177a5938a22ff.html#a2fa372cb0681531259c177a5938a22ff) {     [AK::Wwise::Plugin::XmlNodeType::Attribute](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type_a2fa372cb0681531259c177a5938a22ff.html#a2fa372cb0681531259c177a5938a22ffa75c0257c962a93971923dbe7c39a7232) = 2, [AK::Wwise::Plugin::XmlNodeType::CDATA](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type_a2fa372cb0681531259c177a5938a22ff.html#a2fa372cb0681531259c177a5938a22ffaa36731e1c3a3fc7bd6e27c2f4dc0c3d0) = 4, [AK::Wwise::Plugin::XmlNodeType::Comment](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type_a2fa372cb0681531259c177a5938a22ff.html#a2fa372cb0681531259c177a5938a22ffa2ab2a3705943f01bf06edbb15d909963) = 8, [AK::Wwise::Plugin::XmlNodeType::Document](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type_a2fa372cb0681531259c177a5938a22ff.html#a2fa372cb0681531259c177a5938a22ffafe099684193320746aae4bf5cd0258b7) = 9,     [AK::Wwise::Plugin::XmlNodeType::DocumentFragment](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type_a2fa372cb0681531259c177a5938a22ff.html#a2fa372cb0681531259c177a5938a22ffa1a752802e8089a2e8c93b49ebbb518ad) = 11, [AK::Wwise::Plugin::XmlNodeType::DocumentType](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type_a2fa372cb0681531259c177a5938a22ff.html#a2fa372cb0681531259c177a5938a22ffa980ea136bce4ad74d8024176fded0a2b) = 10, [AK::Wwise::Plugin::XmlNodeType::Element](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type_a2fa372cb0681531259c177a5938a22ff.html#a2fa372cb0681531259c177a5938a22ffa2035a27e4d6f0a7e5d82ae48964e6b2e) = 1, [AK::Wwise::Plugin::XmlNodeType::EndElement](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type_a2fa372cb0681531259c177a5938a22ff.html#a2fa372cb0681531259c177a5938a22ffa3be434228dd402b79c5f5aad76d4613a) = 15,     [AK::Wwise::Plugin::XmlNodeType::EndEntity](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type_a2fa372cb0681531259c177a5938a22ff.html#a2fa372cb0681531259c177a5938a22ffa02d284c7b7b4bed8031c66ae246bc550) = 16, [AK::Wwise::Plugin::XmlNodeType::Entity](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type_a2fa372cb0681531259c177a5938a22ff.html#a2fa372cb0681531259c177a5938a22ffa6b9ba0c0bd4e3b01d367f146925cf518) = 6, [AK::Wwise::Plugin::XmlNodeType::EntityReference](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type_a2fa372cb0681531259c177a5938a22ff.html#a2fa372cb0681531259c177a5938a22ffa376d529c212e2b2c07a738bfabe420d9) = 5, [AK::Wwise::Plugin::XmlNodeType::None](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type_a2fa372cb0681531259c177a5938a22ff.html#a2fa372cb0681531259c177a5938a22ffa7acc2067f1f8ffe705d6f00ffe2eb4d0) = 0,     [AK::Wwise::Plugin::XmlNodeType::Notation](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type_a2fa372cb0681531259c177a5938a22ff.html#a2fa372cb0681531259c177a5938a22ffab5fd172c15457d949411eb63d9058bb0) = 12, [AK::Wwise::Plugin::XmlNodeType::ProcessingInstruction](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type_a2fa372cb0681531259c177a5938a22ff.html#a2fa372cb0681531259c177a5938a22ffa142d6d02d9d5b526ff0dac9ad3de5a94) = 7, [AK::Wwise::Plugin::XmlNodeType::SignificantWhitespace](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type_a2fa372cb0681531259c177a5938a22ff.html#a2fa372cb0681531259c177a5938a22ffa46a1c1dd194c9a8364a803f90c272f14) = 14, [AK::Wwise::Plugin::XmlNodeType::Text](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type_a2fa372cb0681531259c177a5938a22ff.html#a2fa372cb0681531259c177a5938a22ffab6a6731f746a5518ec35cb863113cd7f) = 3,     [AK::Wwise::Plugin::XmlNodeType::Whitespace](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type_a2fa372cb0681531259c177a5938a22ff.html#a2fa372cb0681531259c177a5938a22ffa93649d43e906b25b9db51dc3f00978ba) = 13, [AK::Wwise::Plugin::XmlNodeType::XmlDeclaration](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type_a2fa372cb0681531259c177a5938a22ff.html#a2fa372cb0681531259c177a5938a22ffa024797e320823f0264d0da31b61060c6) = 17   } |
|  | |
| enum | [AK::Wwise::Plugin::XmlWriteState::WriteState](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_write_state_a9802053bd44c7926486300763e602293.html#a9802053bd44c7926486300763e602293) {     [AK::Wwise::Plugin::XmlWriteState::Attribute](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_write_state_a9802053bd44c7926486300763e602293.html#a9802053bd44c7926486300763e602293a863b12088df207d9e79e1db90bf768eb), [AK::Wwise::Plugin::XmlWriteState::Closed](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_write_state_a9802053bd44c7926486300763e602293.html#a9802053bd44c7926486300763e602293aa8700b7ecaa3caad7681d31cd553733b), [AK::Wwise::Plugin::XmlWriteState::Content](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_write_state_a9802053bd44c7926486300763e602293.html#a9802053bd44c7926486300763e602293adb39f0b3c31cea08990fbf95c2cab826), [AK::Wwise::Plugin::XmlWriteState::Element](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_write_state_a9802053bd44c7926486300763e602293.html#a9802053bd44c7926486300763e602293a6c20f4af80d7050c6072104e55c20736),     [AK::Wwise::Plugin::XmlWriteState::Prolog](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_write_state_a9802053bd44c7926486300763e602293.html#a9802053bd44c7926486300763e602293a67d54fef7baf5adefe138ef87940ca25), [AK::Wwise::Plugin::XmlWriteState::Start](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_write_state_a9802053bd44c7926486300763e602293.html#a9802053bd44c7926486300763e602293a681b2db48f90de72b60f64c23e183690)   } |
|  | WriteState [更多...](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_write_state_a9802053bd44c7926486300763e602293.html#a9802053bd44c7926486300763e602293) |
|  | |
| enum | [AK::Wwise::Plugin::XmlWriteReady::WriteReady](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_write_ready_afff47a0c6c5350e7c2f0f390af13f382.html#afff47a0c6c5350e7c2f0f390af13f382) { [AK::Wwise::Plugin::XmlWriteReady::Ready](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_write_ready_afff47a0c6c5350e7c2f0f390af13f382.html#afff47a0c6c5350e7c2f0f390af13f382a4c9800a07ca46d008c74e44397418005), [AK::Wwise::Plugin::XmlWriteReady::ErrorPathTooLong](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_write_ready_afff47a0c6c5350e7c2f0f390af13f382.html#afff47a0c6c5350e7c2f0f390af13f382a68bfc4edb035e3a9f9eaa6a42f18c140), [AK::Wwise::Plugin::XmlWriteReady::ErrorAccessDenied](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_write_ready_afff47a0c6c5350e7c2f0f390af13f382.html#afff47a0c6c5350e7c2f0f390af13f382a3102695005fb83f29a9a55cc55fb937a), [AK::Wwise::Plugin::XmlWriteReady::ErrorUnknown](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_write_ready_afff47a0c6c5350e7c2f0f390af13f382.html#afff47a0c6c5350e7c2f0f390af13f382a2c8ab192cce36ae126413428fb3bdd0a) } |
|  | Possible error codes when writing XML [更多...](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_write_ready_afff47a0c6c5350e7c2f0f390af13f382.html#afff47a0c6c5350e7c2f0f390af13f382) |
|  | |
| enum | [AK::Wwise::Plugin::XmlElementType::ElementType](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_element_type_a36556de11c47219369f6545a96c53583.html#a36556de11c47219369f6545a96c53583) { [AK::Wwise::Plugin::XmlElementType::Map](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_element_type_a36556de11c47219369f6545a96c53583.html#a36556de11c47219369f6545a96c53583ad3849f4efcdebb3a6ac05ac435573bf3), [AK::Wwise::Plugin::XmlElementType::Array](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_element_type_a36556de11c47219369f6545a96c53583.html#a36556de11c47219369f6545a96c53583a5cc7d45d9bf84efeb7d74e433c91b6ba), [AK::Wwise::Plugin::XmlElementType::MultiMap](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_element_type_a36556de11c47219369f6545a96c53583.html#a36556de11c47219369f6545a96c53583abb77b966ca77ad55773894eedcc08261) } |
|  | These element types have an impact when outputting in alternate formats such as JSON. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_element_type_a36556de11c47219369f6545a96c53583.html#a36556de11c47219369f6545a96c53583) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_a8e307c590578e6fb70510fef57545ba3.html#a8e307c590578e6fb70510fef57545ba3) (XmlReader) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_aedb0f5b1832f94f67b756e4af140cca7.html#aedb0f5b1832f94f67b756e4af140cca7) (XmlReader) |
|  | |

## 详细描述

Wwise Authoring Plug-ins - API for XML-based persistence, as used in CustomData.

在文件 [HostXml.h](_host_xml_8h_source.html) 中定义.