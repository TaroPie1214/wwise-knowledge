# AkXMLErrorMessageTranslator

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](class_ak_x_m_l_error_message_translator-members.html) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods)

AkXMLErrorMessageTranslator类 参考

`#include <AkXMLErrorMessageTranslator.h>`

类 AkXMLErrorMessageTranslator 继承关系图:

![](../../../images/class_ak_x_m_l_error_message_translator.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkXMLErrorMessageTranslator](class_ak_x_m_l_error_message_translator_a48ead54291d8eaef2cb47c28f06f2ba8.html#a48ead54291d8eaef2cb47c28f06f2ba8) () |
|  | MessageTranslator class constructor. [更多...](class_ak_x_m_l_error_message_translator_a48ead54291d8eaef2cb47c28f06f2ba8.html#a48ead54291d8eaef2cb47c28f06f2ba8) |
|  | |
|  | [AkXMLErrorMessageTranslator](class_ak_x_m_l_error_message_translator_af4924209b40237ac250b77792f71ca14.html#af4924209b40237ac250b77792f71ca14) (const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*in\_filePath, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_msTimeout=10) |
|  | |
|  | [~AkXMLErrorMessageTranslator](class_ak_x_m_l_error_message_translator_ae3a460ddc76d30d52c306b99d3c5cf84.html#ae3a460ddc76d30d52c306b99d3c5cf84) () |
|  | |
| void | [Init](class_ak_x_m_l_error_message_translator_aa461ef65a3c0b765749fc3866244d7f8.html#aa461ef65a3c0b765749fc3866244d7f8) () |
|  | |
| virtual void | [Term](class_ak_x_m_l_error_message_translator_a7a0cd01751701d79bf36b9064f2df852.html#a7a0cd01751701d79bf36b9064f2df852) () override |
|  | |
| [AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) | [SetFileName](class_ak_x_m_l_error_message_translator_a74cf1cdfc02e280a402edcfa0aea2d33.html#a74cf1cdfc02e280a402edcfa0aea2d33) (const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*in\_filePath, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_msTimeout=10) |
|  | |
| - Public 成员函数 继承自 [AkErrorMessageTranslator](class_ak_error_message_translator.html) | |
|  | [AkErrorMessageTranslator](class_ak_error_message_translator_adfa20561f854f60ead861e9ad7ee1956.html#adfa20561f854f60ead861e9ad7ee1956) () |
|  | |
| virtual | [~AkErrorMessageTranslator](class_ak_error_message_translator_a51416a5d01a9a44c80869d25a00841a7.html#a51416a5d01a9a44c80869d25a00841a7) () |
|  | ErrorMessageTranslator class destructor. [更多...](class_ak_error_message_translator_a51416a5d01a9a44c80869d25a00841a7.html#a51416a5d01a9a44c80869d25a00841a7) |
|  | |
| void | [SetFallBackTranslator](class_ak_error_message_translator_a64ecf37151fd647ea43ec56fb72452b9.html#a64ecf37151fd647ea43ec56fb72452b9) ([AkErrorMessageTranslator](class_ak_error_message_translator.html) \*in\_fallBackTranslator) |
|  | |
| virtual bool | [Translate](class_ak_error_message_translator_a28d465012d3cf8fff600b8ca46cc580c.html#a28d465012d3cf8fff600b8ca46cc580c) (const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*in\_pszError, [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*out\_translatedPszError, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_maxPszErrorSize, char \*in\_args, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uArgSize) |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| virtual bool | [GetInfo](class_ak_x_m_l_error_message_translator_a48da6e532c6b1b5452dafe6b3c8a484e.html#a48da6e532c6b1b5452dafe6b3c8a484e) ([TagInformation](struct_ak_error_message_translator_1_1_tag_information.html) \*in\_pTagList, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uCount, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) &io\_uTranslated) override |
|  | |
| - Protected 成员函数 继承自 [AkErrorMessageTranslator](class_ak_error_message_translator.html) | |
| void | [CharPrintResult](class_ak_error_message_translator_ae8685f36263bb0c6f75565bca9a2cc49.html#ae8685f36263bb0c6f75565bca9a2cc49) ([AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*out\_parsedInfo, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_maxSize, [AkInt32](_ak_numeral_types_8h_a81fc19413771f592b26e6b9e4f8ce154.html#a81fc19413771f592b26e6b9e4f8ce154) in\_stringSize, const char \*in\_string) |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| - Protected 属性 继承自 [AkErrorMessageTranslator](class_ak_error_message_translator.html) | |
| bool | [m\_isReadyForTranslation](class_ak_error_message_translator_af9006a88727f08ee7545602605e92ad5.html#af9006a88727f08ee7545602605e92ad5) |
|  | |
| [AkErrorMessageTranslator](class_ak_error_message_translator.html) \* | [m\_fallBackTranslator](class_ak_error_message_translator_aa34c6126193df5fd77b19f431f5760fd.html#aa34c6126193df5fd77b19f431f5760fd) |
|  | |

## 详细描述

在文件 [AkXMLErrorMessageTranslator.h](_ak_x_m_l_error_message_translator_8h_source.html) 第 [29](_ak_x_m_l_error_message_translator_8h_source.html#l00029) 行定义.