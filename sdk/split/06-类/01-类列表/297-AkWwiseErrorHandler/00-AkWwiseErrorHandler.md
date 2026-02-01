# AkWwiseErrorHandler

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](class_ak_wwise_error_handler-members.html) |
[Public 成员函数](#pub-methods) |
[静态 Public 成员函数](#pub-static-methods)

AkWwiseErrorHandler类 参考

`#include <AkWwiseErrorHandler.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual | [~AkWwiseErrorHandler](class_ak_wwise_error_handler_a17114bfb51a8a12fe6057836b8ade9db.html#a17114bfb51a8a12fe6057836b8ade9db) () |
|  | ErrorHandler class destructor. [更多...](class_ak_wwise_error_handler_a17114bfb51a8a12fe6057836b8ade9db.html#a17114bfb51a8a12fe6057836b8ade9db) |
|  | |

|  |  |
| --- | --- |
| 静态 Public 成员函数 | |
| static void | [AddTranslator](class_ak_wwise_error_handler_a8db07d6427522acd2a284803783e115a.html#a8db07d6427522acd2a284803783e115a) ([AkErrorMessageTranslator](class_ak_error_message_translator.html) \*in\_errorMessageTranslator, bool in\_overridePreviousTranslator) |
|  | |
| static void | [Release](class_ak_wwise_error_handler_a8e9d6653558e26f7f4bc2e220e802fd0.html#a8e9d6653558e26f7f4bc2e220e802fd0) () |
|  | |
| static void | [ResetTranslator](class_ak_wwise_error_handler_a69c9b7d81457c7957b57351ab6710af8.html#a69c9b7d81457c7957b57351ab6710af8) () |
|  | |
| static void | [Execute](class_ak_wwise_error_handler_a9407a2030cf00a96028bf8313f0668d4.html#a9407a2030cf00a96028bf8313f0668d4) ([AK::Monitor::ErrorCode](namespace_a_k_1_1_monitor_a0e821a3df59a73288d040def2778cd7c.html#a0e821a3df59a73288d040def2778cd7c) in\_eErrorCode, const [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*in\_pszError, [AK::Monitor::ErrorLevel](namespace_a_k_1_1_monitor_a75374a589b6f43efc84d695d101698de.html#a75374a589b6f43efc84d695d101698de) in\_errorLevel, [AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) in\_pID, [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) in\_gId, [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) in\_sId, char \*in\_args, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uArgSize, [AkOSChar](_platforms_2_windows_2_ak_types_8h_af48843ed095e0ea7dd05bd1b64070664.html#af48843ed095e0ea7dd05bd1b64070664) \*out\_pBuffer=nullptr, [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_BufferSize=0) |
|  | Translate and then send back the translated message to the sound engine via it's m\_funcLocalOutput [更多...](class_ak_wwise_error_handler_a9407a2030cf00a96028bf8313f0668d4.html#a9407a2030cf00a96028bf8313f0668d4) |
|  | |
| static void | [SetLocalOutputFunc](class_ak_wwise_error_handler_ab1b579b0477ced24f3c1eba6a56391c7.html#ab1b579b0477ced24f3c1eba6a56391c7) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uErrorLevel, [AK::Monitor::LocalOutputFunc](namespace_a_k_1_1_monitor_ad2e6203a592069941058894225b14fc2.html#ad2e6203a592069941058894225b14fc2) in\_pMonitorFunc) |
|  | Sets the localoutputfunc [更多...](class_ak_wwise_error_handler_ab1b579b0477ced24f3c1eba6a56391c7.html#ab1b579b0477ced24f3c1eba6a56391c7) |
|  | |
| static [AK::Monitor::LocalOutputFunc](namespace_a_k_1_1_monitor_ad2e6203a592069941058894225b14fc2.html#ad2e6203a592069941058894225b14fc2) | [GetLocalOutputFunc](class_ak_wwise_error_handler_a6aa744af611087604211d77bdbba1fe7.html#a6aa744af611087604211d77bdbba1fe7) () |
|  | |
| static [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [GetLocalOutputErrorLevel](class_ak_wwise_error_handler_a13a22cb9cb356a043d3278d7feb32ff1.html#a13a22cb9cb356a043d3278d7feb32ff1) () |
|  | |

## 详细描述

在文件 [AkWwiseErrorHandler.h](_ak_wwise_error_handler_8h_source.html) 第 [32](_ak_wwise_error_handler_8h_source.html#l00032) 行定义.