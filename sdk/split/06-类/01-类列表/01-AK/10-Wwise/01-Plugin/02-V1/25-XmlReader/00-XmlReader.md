# XmlReader

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [XmlReader](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::XmlReader类 参考

API interface for XML-based plug-in persistence.
[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader.html#details)

`#include <HostXml.h>`

类 AK.Wwise::Plugin::V1::XmlReader 继承关系图:

![](../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader.png)

|  |  |
| --- | --- |
| Public 类型 | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_a97266654bc65c9671939d4b666d45bc2.html#a97266654bc65c9671939d4b666d45bc2af2cb67552bf7035b90eb354d0937caac) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_HOST\_XML } |
|  | The interface type, as requested by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_a97266654bc65c9671939d4b666d45bc2.html#a97266654bc65c9671939d4b666d45bc2) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_a28684cf253b8af946e55e9d8dd4a410f.html#a28684cf253b8af946e55e9d8dd4a410fa827b039c93f17d4470cd96122b40c5e5) = 1 } |
|  | The interface version, as requested by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_a28684cf253b8af946e55e9d8dd4a410f.html#a28684cf253b8af946e55e9d8dd4a410f) |
|  | |
| using | [Interface](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_a7bb26d4ee9adab3b6d3917698e2d059f.html#a7bb26d4ee9adab3b6d3917698e2d059f) = [CHostXml](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a074a0bfcc47a57a8a183590d1251f4bb.html#a074a0bfcc47a57a8a183590d1251f4bb) |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::CBaseInstanceGlue< CHostXml, CHostXml::ReaderInstance >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue.html) | |
| using | [Instance](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_instance_glue_aff6221118cb1d81f1e67f1932fb66b60.html#aff6221118cb1d81f1e67f1932fb66b60) = [CHostXml::ReaderInstance](structak__wwise__plugin__host__xml__v1_ad6c2ef03a11df90181a5e905b5276225.html#ad6c2ef03a11df90181a5e905b5276225) |
|  | |
| - Public 类型 继承自 [AK.Wwise::Plugin::CBaseInterfaceGlue< CHostXml >](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue.html) | |
| using | [GluedInterface](class_a_k_1_1_wwise_1_1_plugin_1_1_c_base_interface_glue_a270936e06e5c9627548246cbebde0467.html#a270936e06e5c9627548246cbebde0467) = [CHostXml](namespace_a_k_1_1_wwise_1_1_plugin_a3dc2daeee0ab37ad19f0077ae3bfc9a2.html#a3dc2daeee0ab37ad19f0077ae3bfc9a2) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| const char \* | [GetName](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_a651df1743780dccfad6ea357c02b357f.html#a651df1743780dccfad6ea357c02b357f) () const |
|  | Returns the name of the current node being read. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_a651df1743780dccfad6ea357c02b357f.html#a651df1743780dccfad6ea357c02b357f) |
|  | |
| [AK::Wwise::Plugin::XmlNodeType::NodeType](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type_a2fa372cb0681531259c177a5938a22ff.html#a2fa372cb0681531259c177a5938a22ff) | [GetNodeType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_a9223f89dd64f0edb359b0b6527628835.html#a9223f89dd64f0edb359b0b6527628835) () const |
|  | Returns the type of the current node being read. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_a9223f89dd64f0edb359b0b6527628835.html#a9223f89dd64f0edb359b0b6527628835) |
|  | |
| bool | [IsEmptyElement](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_a634b05b742735175f34ff52f6bd391bd.html#a634b05b742735175f34ff52f6bd391bd) () const |
|  | Tests whether the current node being read is empty. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_a634b05b742735175f34ff52f6bd391bd.html#a634b05b742735175f34ff52f6bd391bd) |
|  | |
| const char \* | [GetValue](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_a13bdbca50afb46c79a00b60fb05ebdf7.html#a13bdbca50afb46c79a00b60fb05ebdf7) () const |
|  | Returns the value of the current node being read. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_a13bdbca50afb46c79a00b60fb05ebdf7.html#a13bdbca50afb46c79a00b60fb05ebdf7) |
|  | |
| bool | [IsEOF](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_a278cea16cb39b338053d5872b6208f6a.html#a278cea16cb39b338053d5872b6208f6a) () const |
|  | Tests whether the end of file is reached while reading the XML. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_a278cea16cb39b338053d5872b6208f6a.html#a278cea16cb39b338053d5872b6208f6a) |
|  | |
| int | [GetLineNumber](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_ad5b01fa46bf1ce592d03bcce9c898f38.html#ad5b01fa46bf1ce592d03bcce9c898f38) () const |
|  | Retrieves the line number that contains the start of the current node being read. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_ad5b01fa46bf1ce592d03bcce9c898f38.html#ad5b01fa46bf1ce592d03bcce9c898f38) |
|  | |
| int | [GetLinePosition](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_a0acc0d09e2527c41d67d45ae2eff151a.html#a0acc0d09e2527c41d67d45ae2eff151a) () const |
|  | Retrieves the column in the line that contains the start of the current node being read. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_a0acc0d09e2527c41d67d45ae2eff151a.html#a0acc0d09e2527c41d67d45ae2eff151a) |
|  | |
| [AK::Wwise::Plugin::XmlNodeType::NodeType](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type_a2fa372cb0681531259c177a5938a22ff.html#a2fa372cb0681531259c177a5938a22ff) | [MoveToContent](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_ae2377d898baed48ce83ea217c5379519.html#ae2377d898baed48ce83ea217c5379519) () |
|  | Makes sure the cursor points to a content-type entity while reading XML. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_ae2377d898baed48ce83ea217c5379519.html#ae2377d898baed48ce83ea217c5379519) |
|  | |
| bool | [Read](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_aaf2aa8d1886d7590e29e70d450509fb5.html#aaf2aa8d1886d7590e29e70d450509fb5) () |
|  | Sets the reading pointer to the next node, recursively. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_aaf2aa8d1886d7590e29e70d450509fb5.html#aaf2aa8d1886d7590e29e70d450509fb5) |
|  | |
| const char \* | [ReadElementString](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_a25cbd56eda252f4cba5b2ca0c73fba22.html#a25cbd56eda252f4cba5b2ca0c73fba22) () |
|  | Reads simple text-only elements, and increments the pointer. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_a25cbd56eda252f4cba5b2ca0c73fba22.html#a25cbd56eda252f4cba5b2ca0c73fba22) |
|  | |
| void | [ReadInnerXml](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_a98eb3b633829c4bc53f0e2e30381d69a.html#a98eb3b633829c4bc53f0e2e30381d69a) (const char \*&out\_csXml) |
|  | Reads all the contents of an Element or Attribute as a string, including markup. Increments the pointer. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_a98eb3b633829c4bc53f0e2e30381d69a.html#a98eb3b633829c4bc53f0e2e30381d69a) |
|  | |
| void | [ReadOuterXml](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_a827a776cc6831921a4b77d558a990da6.html#a827a776cc6831921a4b77d558a990da6) (const char \*&out\_csXml) |
|  | Reads the Element or Attribute as a string, including markup. Increments the pointer. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_a827a776cc6831921a4b77d558a990da6.html#a827a776cc6831921a4b77d558a990da6) |
|  | |
| void | [Skip](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_a2e7911bffd406055956e9219502f7211.html#a2e7911bffd406055956e9219502f7211) () |
|  | Sets the reading pointer past the current node, skipping any inner content. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_a2e7911bffd406055956e9219502f7211.html#a2e7911bffd406055956e9219502f7211) |
|  | |
| bool | [GetAttribute](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_a33f5529a1a1a1d3b625599f6a169c84e.html#a33f5529a1a1a1d3b625599f6a169c84e) (const char \*in\_rcsAttributeName, const char \*&out\_rcsValue) |
|  | Reads the value of a particular attribute under the current node. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_xml_reader_a33f5529a1a1a1d3b625599f6a169c84e.html#a33f5529a1a1a1d3b625599f6a169c84e) |
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

在文件 [HostXml.h](_host_xml_8h_source.html) 第 [529](_host_xml_8h_source.html#l00529) 行定义.