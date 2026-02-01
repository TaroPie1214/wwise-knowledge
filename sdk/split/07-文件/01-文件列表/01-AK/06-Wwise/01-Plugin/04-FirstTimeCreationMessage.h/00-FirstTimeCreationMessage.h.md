# FirstTimeCreationMessage.h

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
[函数](#func-members)

FirstTimeCreationMessage.h 文件参考

Wwise Authoring Plug-ins - Plug-in that provides a special usage message when first instantiated.
[更多...](#details)

`#include "PluginInfoGenerator.h"`

[浏览源代码.](_first_time_creation_message_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [ak\_wwise\_plugin\_first\_time\_creation\_message\_v1](structak__wwise__plugin__first__time__creation__message__v1.html) |
|  | Plug-in that provides a special usage message when first instantiated. [更多...](structak__wwise__plugin__first__time__creation__message__v1.html#details) |
|  | |
| class | [AK.Wwise::Plugin::V1::FirstTimeCreationMessage](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message.html) |
|  | |
| struct | [AK.Wwise::Plugin::V1::FirstTimeCreationMessage::Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_1_1_interface.html) |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_first_time_creation_message_1_1_interface.html#details) |
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
|  | [AK::Wwise::Plugin::V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AK\_WWISE\_PLUGIN\_FIRST\_TIME\_CREATION\_MESSAGE\_V1\_ID](_first_time_creation_message_8h_a01ba9996c5e4b6a269515aa1e2d66605.html#a01ba9996c5e4b6a269515aa1e2d66605)()    [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_FIRST\_TIME\_CREATION\_MESSAGE](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9a72c782c40df28013cce3676850064c02), 1) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_FIRST\_TIME\_CREATION\_MESSAGE\_V1\_CTOR](_first_time_creation_message_8h_a864485e9fe139c298137eaf16c006c22.html#a864485e9fe139c298137eaf16c006c22)(in\_pluginInfo, in\_data) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| using | [AK::Wwise::Plugin::V1::CFirstTimeCreationMessage](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_af924488c8495a657722804248de4c2c8.html#af924488c8495a657722804248de4c2c8) = [ak\_wwise\_plugin\_first\_time\_creation\_message\_v1](structak__wwise__plugin__first__time__creation__message__v1.html) |
|  | |
| using | [AK::Wwise::Plugin::CFirstTimeCreationMessage](namespace_a_k_1_1_wwise_1_1_plugin_a67b1d35db15070c3c69c9644357a8981.html#a67b1d35db15070c3c69c9644357a8981) = V1::CFirstTimeCreationMessage |
|  | Latest version of the C FirstTimeCreationMessage interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a67b1d35db15070c3c69c9644357a8981.html#a67b1d35db15070c3c69c9644357a8981) |
|  | |
| using | [AK::Wwise::Plugin::FirstTimeCreationMessage](namespace_a_k_1_1_wwise_1_1_plugin_a1120c7a177977ca71bdb7e5190489478.html#a1120c7a177977ca71bdb7e5190489478) = V1::FirstTimeCreationMessage |
|  | Latest version of the C++ FirstTimeCreationMessage interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a1120c7a177977ca71bdb7e5190489478.html#a1120c7a177977ca71bdb7e5190489478) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_a81218c5a455aab7138406ad0a566718d.html#a81218c5a455aab7138406ad0a566718d) (FirstTimeCreationMessage) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_ad109981b5ef8a531fdd10dadc281e4d4.html#ad109981b5ef8a531fdd10dadc281e4d4) (FirstTimeCreationMessage) |
|  | |

## 详细描述

Wwise Authoring Plug-ins - Plug-in that provides a special usage message when first instantiated.

在文件 [FirstTimeCreationMessage.h](_first_time_creation_message_8h_source.html) 中定义.