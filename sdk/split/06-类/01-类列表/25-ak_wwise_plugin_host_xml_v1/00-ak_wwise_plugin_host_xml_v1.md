# ak_wwise_plugin_host_xml_v1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](structak__wwise__plugin__host__xml__v1-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

ak\_wwise\_plugin\_host\_xml\_v1结构体 参考

API interface for XML-based plug-in persistence.
[更多...](structak__wwise__plugin__host__xml__v1.html#details)

`#include <HostXml.h>`

类 ak\_wwise\_plugin\_host\_xml\_v1 继承关系图:

![](../../../images/structak__wwise__plugin__host__xml__v1.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [ReaderInstance](structak__wwise__plugin__host__xml__v1_ad6c2ef03a11df90181a5e905b5276225.html#ad6c2ef03a11df90181a5e905b5276225) = [ak\_wwise\_plugin\_host\_xml\_reader\_instance\_v1](structak__wwise__plugin__host__xml__reader__instance__v1.html) |
|  | |
| using | [WriterInstance](structak__wwise__plugin__host__xml__v1_a06c351967680d8541028f3c10091c4a5.html#a06c351967680d8541028f3c10091c4a5) = [ak\_wwise\_plugin\_host\_xml\_writer\_instance\_v1](structak__wwise__plugin__host__xml__writer__instance__v1.html) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [ak\_wwise\_plugin\_host\_xml\_v1](structak__wwise__plugin__host__xml__v1_ad5002b5981beebb4546fef1461297f86.html#ad5002b5981beebb4546fef1461297f86) () |
|  | |
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) | |
| constexpr | [ak\_wwise\_plugin\_base\_interface](structak__wwise__plugin__base__interface_a7d1ff21fd409fc7363077edecb25a85d.html#a7d1ff21fd409fc7363077edecb25a85d) (decltype([m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9)) in\_interface, decltype([m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6)) in\_version) |
|  | |
| constexpr | [ak\_wwise\_plugin\_base\_interface](structak__wwise__plugin__base__interface_aef726120a06d869829ad6ec67df4f2a4.html#aef726120a06d869829ad6ec67df4f2a4) () |
|  | |
| constexpr | [ak\_wwise\_plugin\_base\_interface](structak__wwise__plugin__base__interface_acefd1ca37e4c88b6c792ec43953d3f9c.html#acefd1ca37e4c88b6c792ec43953d3f9c) (std::underlying\_type< decltype([m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9))>::type in\_interface, decltype([m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6)) in\_version) |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| const char \*(\* | [GetName](structak__wwise__plugin__host__xml__v1_ac1ccf626e85cc1c13b732fe9fcbcb417.html#ac1ccf626e85cc1c13b732fe9fcbcb417) )(const struct [ak\_wwise\_plugin\_host\_xml\_reader\_instance\_v1](structak__wwise__plugin__host__xml__reader__instance__v1.html) \*in\_this) |
|  | Returns the name of the current node being read. [更多...](structak__wwise__plugin__host__xml__v1_ac1ccf626e85cc1c13b732fe9fcbcb417.html#ac1ccf626e85cc1c13b732fe9fcbcb417) |
|  | |
| [AK::Wwise::Plugin::XmlNodeType::NodeType](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type_a2fa372cb0681531259c177a5938a22ff.html#a2fa372cb0681531259c177a5938a22ff)(\* | [GetNodeType](structak__wwise__plugin__host__xml__v1_a52388de4328ac697aa1fde7ad8f7e2f9.html#a52388de4328ac697aa1fde7ad8f7e2f9) )(const struct [ak\_wwise\_plugin\_host\_xml\_reader\_instance\_v1](structak__wwise__plugin__host__xml__reader__instance__v1.html) \*in\_this) |
|  | Returns the type of the current node being read. [更多...](structak__wwise__plugin__host__xml__v1_a52388de4328ac697aa1fde7ad8f7e2f9.html#a52388de4328ac697aa1fde7ad8f7e2f9) |
|  | |
| bool(\* | [IsEmptyElement](structak__wwise__plugin__host__xml__v1_a369e5452a73bb0ff6b5a78c88cfbdad9.html#a369e5452a73bb0ff6b5a78c88cfbdad9) )(const struct [ak\_wwise\_plugin\_host\_xml\_reader\_instance\_v1](structak__wwise__plugin__host__xml__reader__instance__v1.html) \*in\_this) |
|  | Tests whether the current node being read is empty. [更多...](structak__wwise__plugin__host__xml__v1_a369e5452a73bb0ff6b5a78c88cfbdad9.html#a369e5452a73bb0ff6b5a78c88cfbdad9) |
|  | |
| const char \*(\* | [GetValue](structak__wwise__plugin__host__xml__v1_a34c7e682c031091853413758e216fc93.html#a34c7e682c031091853413758e216fc93) )(const struct [ak\_wwise\_plugin\_host\_xml\_reader\_instance\_v1](structak__wwise__plugin__host__xml__reader__instance__v1.html) \*in\_this) |
|  | Returns the value of the current node being read. [更多...](structak__wwise__plugin__host__xml__v1_a34c7e682c031091853413758e216fc93.html#a34c7e682c031091853413758e216fc93) |
|  | |
| bool(\* | [IsEOF](structak__wwise__plugin__host__xml__v1_a8961a07ae84d9d2952aaf61196282dc5.html#a8961a07ae84d9d2952aaf61196282dc5) )(const struct [ak\_wwise\_plugin\_host\_xml\_reader\_instance\_v1](structak__wwise__plugin__host__xml__reader__instance__v1.html) \*in\_this) |
|  | Tests whether the end of file is reached while reading the XML. [更多...](structak__wwise__plugin__host__xml__v1_a8961a07ae84d9d2952aaf61196282dc5.html#a8961a07ae84d9d2952aaf61196282dc5) |
|  | |
| int(\* | [GetLineNumber](structak__wwise__plugin__host__xml__v1_a5bb328e21602c506b701b98eaa4fcd67.html#a5bb328e21602c506b701b98eaa4fcd67) )(const struct [ak\_wwise\_plugin\_host\_xml\_reader\_instance\_v1](structak__wwise__plugin__host__xml__reader__instance__v1.html) \*in\_this) |
|  | Retrieves the line number that contains the start of the current node being read. [更多...](structak__wwise__plugin__host__xml__v1_a5bb328e21602c506b701b98eaa4fcd67.html#a5bb328e21602c506b701b98eaa4fcd67) |
|  | |
| int(\* | [GetLinePosition](structak__wwise__plugin__host__xml__v1_aeb6e8a28f9eb44f401794e7478a8c342.html#aeb6e8a28f9eb44f401794e7478a8c342) )(const struct [ak\_wwise\_plugin\_host\_xml\_reader\_instance\_v1](structak__wwise__plugin__host__xml__reader__instance__v1.html) \*in\_this) |
|  | Retrieves the column in the line that contains the start of the current node being read. [更多...](structak__wwise__plugin__host__xml__v1_aeb6e8a28f9eb44f401794e7478a8c342.html#aeb6e8a28f9eb44f401794e7478a8c342) |
|  | |
| [AK::Wwise::Plugin::XmlNodeType::NodeType](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_node_type_a2fa372cb0681531259c177a5938a22ff.html#a2fa372cb0681531259c177a5938a22ff)(\* | [MoveToContent](structak__wwise__plugin__host__xml__v1_a5b1199800f62503a4476aa0c0d8e2ea6.html#a5b1199800f62503a4476aa0c0d8e2ea6) )(struct [ak\_wwise\_plugin\_host\_xml\_reader\_instance\_v1](structak__wwise__plugin__host__xml__reader__instance__v1.html) \*in\_this) |
|  | Makes sure the cursor points to a content-type entity while reading XML. [更多...](structak__wwise__plugin__host__xml__v1_a5b1199800f62503a4476aa0c0d8e2ea6.html#a5b1199800f62503a4476aa0c0d8e2ea6) |
|  | |
| bool(\* | [Read](structak__wwise__plugin__host__xml__v1_a4cd5cb7f09d7bb150d1d8edf28cb85b6.html#a4cd5cb7f09d7bb150d1d8edf28cb85b6) )(struct [ak\_wwise\_plugin\_host\_xml\_reader\_instance\_v1](structak__wwise__plugin__host__xml__reader__instance__v1.html) \*in\_this) |
|  | Sets the reading pointer to the next node, recursively. [更多...](structak__wwise__plugin__host__xml__v1_a4cd5cb7f09d7bb150d1d8edf28cb85b6.html#a4cd5cb7f09d7bb150d1d8edf28cb85b6) |
|  | |
| const char \*(\* | [ReadElementString](structak__wwise__plugin__host__xml__v1_a89bad3f954551246f7156ec7debac923.html#a89bad3f954551246f7156ec7debac923) )(struct [ak\_wwise\_plugin\_host\_xml\_reader\_instance\_v1](structak__wwise__plugin__host__xml__reader__instance__v1.html) \*in\_this) |
|  | Reads simple text-only elements, and increments the pointer. [更多...](structak__wwise__plugin__host__xml__v1_a89bad3f954551246f7156ec7debac923.html#a89bad3f954551246f7156ec7debac923) |
|  | |
| void(\* | [ReadInnerXml](structak__wwise__plugin__host__xml__v1_aa30b22867f12e414ef5ffc2379e1f3a2.html#aa30b22867f12e414ef5ffc2379e1f3a2) )(struct [ak\_wwise\_plugin\_host\_xml\_reader\_instance\_v1](structak__wwise__plugin__host__xml__reader__instance__v1.html) \*in\_this, const char \*\*out\_csXml) |
|  | Reads all the contents of an Element or Attribute as a string, including markup. Increments the pointer. [更多...](structak__wwise__plugin__host__xml__v1_aa30b22867f12e414ef5ffc2379e1f3a2.html#aa30b22867f12e414ef5ffc2379e1f3a2) |
|  | |
| void(\* | [ReadOuterXml](structak__wwise__plugin__host__xml__v1_a351f60f88d656209f2992862f9032683.html#a351f60f88d656209f2992862f9032683) )(struct [ak\_wwise\_plugin\_host\_xml\_reader\_instance\_v1](structak__wwise__plugin__host__xml__reader__instance__v1.html) \*in\_this, const char \*\*out\_csXml) |
|  | Reads the Element or Attribute as a string, including markup. Increments the pointer. [更多...](structak__wwise__plugin__host__xml__v1_a351f60f88d656209f2992862f9032683.html#a351f60f88d656209f2992862f9032683) |
|  | |
| void(\* | [Skip](structak__wwise__plugin__host__xml__v1_a2a680e686e0a38145c4b67da6af5b720.html#a2a680e686e0a38145c4b67da6af5b720) )(struct [ak\_wwise\_plugin\_host\_xml\_reader\_instance\_v1](structak__wwise__plugin__host__xml__reader__instance__v1.html) \*in\_this) |
|  | Sets the reading pointer past the current node, skipping any inner content. [更多...](structak__wwise__plugin__host__xml__v1_a2a680e686e0a38145c4b67da6af5b720.html#a2a680e686e0a38145c4b67da6af5b720) |
|  | |
| bool(\* | [GetAttribute](structak__wwise__plugin__host__xml__v1_a46ebe6a6fe05def01563df3c121da586.html#a46ebe6a6fe05def01563df3c121da586) )(struct [ak\_wwise\_plugin\_host\_xml\_reader\_instance\_v1](structak__wwise__plugin__host__xml__reader__instance__v1.html) \*in\_this, const char \*in\_rcsAttributeName, const char \*\*out\_rcsValue) |
|  | Reads the value of a particular attribute under the current node. [更多...](structak__wwise__plugin__host__xml__v1_a46ebe6a6fe05def01563df3c121da586.html#a46ebe6a6fe05def01563df3c121da586) |
|  | |
| bool(\* | [IsReady](structak__wwise__plugin__host__xml__v1_ad597e400f57e36f12482d11a1d47301b.html#ad597e400f57e36f12482d11a1d47301b) )(const struct [ak\_wwise\_plugin\_host\_xml\_writer\_instance\_v1](structak__wwise__plugin__host__xml__writer__instance__v1.html) \*in\_this) |
|  | Determines if the writer is ready to be used. [更多...](structak__wwise__plugin__host__xml__v1_ad597e400f57e36f12482d11a1d47301b.html#ad597e400f57e36f12482d11a1d47301b) |
|  | |
| [AK::Wwise::Plugin::XmlWriteReady::WriteReady](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_write_ready_afff47a0c6c5350e7c2f0f390af13f382.html#afff47a0c6c5350e7c2f0f390af13f382)(\* | [GetReadyState](structak__wwise__plugin__host__xml__v1_a2f9b4d8953e6f63283845d9cdacad773.html#a2f9b4d8953e6f63283845d9cdacad773) )(const struct [ak\_wwise\_plugin\_host\_xml\_writer\_instance\_v1](structak__wwise__plugin__host__xml__writer__instance__v1.html) \*in\_this) |
|  | Determines the state of readiness of the writer. [更多...](structak__wwise__plugin__host__xml__v1_a2f9b4d8953e6f63283845d9cdacad773.html#a2f9b4d8953e6f63283845d9cdacad773) |
|  | |
| bool(\* | [Append](structak__wwise__plugin__host__xml__v1_a6a82a46f6e8c5f9cea22eb4afcfd24ae.html#a6a82a46f6e8c5f9cea22eb4afcfd24ae) )(struct [ak\_wwise\_plugin\_host\_xml\_writer\_instance\_v1](structak__wwise__plugin__host__xml__writer__instance__v1.html) \*in\_this, struct [ak\_wwise\_plugin\_host\_xml\_writer\_instance\_v1](structak__wwise__plugin__host__xml__writer__instance__v1.html) \*in\_pWriterToAppend) |
|  | Appending a first XML writer to a second XML writer. [更多...](structak__wwise__plugin__host__xml__v1_a6a82a46f6e8c5f9cea22eb4afcfd24ae.html#a6a82a46f6e8c5f9cea22eb4afcfd24ae) |
|  | |
| [AK::Wwise::Plugin::XmlWriteState::WriteState](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_write_state_a9802053bd44c7926486300763e602293.html#a9802053bd44c7926486300763e602293)(\* | [GetWriteState](structak__wwise__plugin__host__xml__v1_ae6036c96a1884f3020ac5cff8a66754f.html#ae6036c96a1884f3020ac5cff8a66754f) )(const struct [ak\_wwise\_plugin\_host\_xml\_writer\_instance\_v1](structak__wwise__plugin__host__xml__writer__instance__v1.html) \*in\_this) |
|  | Retrieves the state of the node the writer is currently populating. [更多...](structak__wwise__plugin__host__xml__v1_ae6036c96a1884f3020ac5cff8a66754f.html#ae6036c96a1884f3020ac5cff8a66754f) |
|  | |
| void(\* | [WriteStartDocument](structak__wwise__plugin__host__xml__v1_ac104d160e3f1b4cbf15903fe4967dc80.html#ac104d160e3f1b4cbf15903fe4967dc80) )(struct [ak\_wwise\_plugin\_host\_xml\_writer\_instance\_v1](structak__wwise__plugin__host__xml__writer__instance__v1.html) \*in\_this) |
|  | Starts a new XML document. [更多...](structak__wwise__plugin__host__xml__v1_ac104d160e3f1b4cbf15903fe4967dc80.html#ac104d160e3f1b4cbf15903fe4967dc80) |
|  | |
| void(\* | [WriteEndDocument](structak__wwise__plugin__host__xml__v1_a15e0aa4341c42edc978b2e240acbcd5c.html#a15e0aa4341c42edc978b2e240acbcd5c) )(struct [ak\_wwise\_plugin\_host\_xml\_writer\_instance\_v1](structak__wwise__plugin__host__xml__writer__instance__v1.html) \*in\_this) |
|  | Ends a completed XML document. [更多...](structak__wwise__plugin__host__xml__v1_a15e0aa4341c42edc978b2e240acbcd5c.html#a15e0aa4341c42edc978b2e240acbcd5c) |
|  | |
| void(\* | [WriteStartElement](structak__wwise__plugin__host__xml__v1_ae090cb83b25204271444becb482678a1.html#ae090cb83b25204271444becb482678a1) )(struct [ak\_wwise\_plugin\_host\_xml\_writer\_instance\_v1](structak__wwise__plugin__host__xml__writer__instance__v1.html) \*in\_this, const char \*in\_rcsElementName, [AK::Wwise::Plugin::XmlElementType::ElementType](namespace_a_k_1_1_wwise_1_1_plugin_1_1_xml_element_type_a36556de11c47219369f6545a96c53583.html#a36556de11c47219369f6545a96c53583) in\_eType) |
|  | Creates a new inner node. [更多...](structak__wwise__plugin__host__xml__v1_ae090cb83b25204271444becb482678a1.html#ae090cb83b25204271444becb482678a1) |
|  | |
| void(\* | [WriteEndElement](structak__wwise__plugin__host__xml__v1_ad8a271043159f36dfd14d2fcbc54e68c.html#ad8a271043159f36dfd14d2fcbc54e68c) )(struct [ak\_wwise\_plugin\_host\_xml\_writer\_instance\_v1](structak__wwise__plugin__host__xml__writer__instance__v1.html) \*in\_this) |
|  | Closes the previous node. [更多...](structak__wwise__plugin__host__xml__v1_ad8a271043159f36dfd14d2fcbc54e68c.html#ad8a271043159f36dfd14d2fcbc54e68c) |
|  | |
| void(\* | [WriteAttributeString](structak__wwise__plugin__host__xml__v1_a6762cd7addf5ab46ed41f1bb97237275.html#a6762cd7addf5ab46ed41f1bb97237275) )(struct [ak\_wwise\_plugin\_host\_xml\_writer\_instance\_v1](structak__wwise__plugin__host__xml__writer__instance__v1.html) \*in\_this, const char \*in\_rcsAttribute, const char \*in\_rcsValue) |
|  | Adds an attribute to the current node. [更多...](structak__wwise__plugin__host__xml__v1_a6762cd7addf5ab46ed41f1bb97237275.html#a6762cd7addf5ab46ed41f1bb97237275) |
|  | |
| void(\* | [WriteString](structak__wwise__plugin__host__xml__v1_a2600e468006377d1f469c9e7f3432e5b.html#a2600e468006377d1f469c9e7f3432e5b) )(struct [ak\_wwise\_plugin\_host\_xml\_writer\_instance\_v1](structak__wwise__plugin__host__xml__writer__instance__v1.html) \*in\_this, const char \*in\_rcsValue) |
|  | Appends a string as value to the current node. [更多...](structak__wwise__plugin__host__xml__v1_a2600e468006377d1f469c9e7f3432e5b.html#a2600e468006377d1f469c9e7f3432e5b) |
|  | |
| void(\* | [WriteCData](structak__wwise__plugin__host__xml__v1_a19e6982bbab1cd420227038d7bd9a4ce.html#a19e6982bbab1cd420227038d7bd9a4ce) )(struct [ak\_wwise\_plugin\_host\_xml\_writer\_instance\_v1](structak__wwise__plugin__host__xml__writer__instance__v1.html) \*in\_this, const char \*in\_rcsValue) |
|  | Appends a raw CDATA string as value to the current node. [更多...](structak__wwise__plugin__host__xml__v1_a19e6982bbab1cd420227038d7bd9a4ce.html#a19e6982bbab1cd420227038d7bd9a4ce) |
|  | |
| void(\* | [WriteRaw](structak__wwise__plugin__host__xml__v1_a01a72b730593d5812601bbf32a1b2c5d.html#a01a72b730593d5812601bbf32a1b2c5d) )(struct [ak\_wwise\_plugin\_host\_xml\_writer\_instance\_v1](structak__wwise__plugin__host__xml__writer__instance__v1.html) \*in\_this, const char \*in\_rcsValue) |
|  | Appends a raw string at this precise point of the XML file. [更多...](structak__wwise__plugin__host__xml__v1_a01a72b730593d5812601bbf32a1b2c5d.html#a01a72b730593d5812601bbf32a1b2c5d) |
|  | |
| - Public 属性 继承自 [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) | |
| [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9) | [m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9): 32 |
|  | Interface type (see [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9)) [更多...](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9) |
|  | |
| uint32\_t | [m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6): 32 |
|  | Version of the interface [更多...](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6) |
|  | |

## 详细描述

API interface for XML-based plug-in persistence.

The XML plug-in persistence is useful when a plug-in provides custom data handling. Normally, plug-in data is stored through the property sets (see [PropertySet](plugin_backend_model.html#wwiseplugin_propertyset) and [ObjectStore](plugin_xml.html#wwiseplugin_objectstore)). However, a plug-in might provide its own custom handling. For complex interfaces, it might be worthwhile to use the [CustomData](plugin_backend_model.html#wwiseplugin_complexproperty) interface. Loading and saving can then be done through this XML interface.

The XML interface represents a cursor pointing to a node (element), alongside methods to navigate through the hierarchy.

|  |  |
| --- | --- |
|  | **备注:** One unique XML interface is provided for both reading and writing XML. Depending on the instance being provided, it will allow reading or writing through this interface.  It can either be a [ak\_wwise\_plugin\_host\_xml\_reader\_instance\_v1](structak__wwise__plugin__host__xml__reader__instance__v1.html) or a [ak\_wwise\_plugin\_host\_xml\_writer\_instance\_v1](structak__wwise__plugin__host__xml__writer__instance__v1.html). |

在文件 [HostXml.h](_host_xml_8h_source.html) 第 [141](_host_xml_8h_source.html#l00141) 行定义.