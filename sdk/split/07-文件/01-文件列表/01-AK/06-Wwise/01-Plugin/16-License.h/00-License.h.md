# License.h

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

License.h 文件参考

Wwise Authoring Plug-ins - Plug-in API for licensing.
[更多...](#details)

`#include "PluginInfoGenerator.h"`

[浏览源代码.](_license_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [ak\_wwise\_plugin\_license\_v1](structak__wwise__plugin__license__v1.html) |
|  | Backend API to specify licensing requirements [更多...](structak__wwise__plugin__license__v1.html#details) |
|  | |
| class | [AK.Wwise::Plugin::V1::License](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_license.html) |
|  | |
| struct | [AK.Wwise::Plugin::V1::License::Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_license_1_1_interface.html) |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_license_1_1_interface.html#details) |
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
| #define | [AK\_WWISE\_PLUGIN\_LICENSE\_V1\_ID](_license_8h_aef8d3e7f093866656f0dc978f0232a30.html#aef8d3e7f093866656f0dc978f0232a30)()    [AK\_WWISE\_PLUGIN\_BASE\_INTERFACE\_FROM\_ID](group__global_ga2e92de39750f51adaec9aba5a094f699.html#ga2e92de39750f51adaec9aba5a094f699)([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_LICENSE](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9aae5f79946e2cbff79d92163117f5dd8b), 1) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_LICENSE\_V1\_CTOR](_license_8h_a45de613816ba926289c445fe9542a50b.html#a45de613816ba926289c445fe9542a50b)(in\_pluginInfo, in\_data) |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| using | [AK::Wwise::Plugin::V1::CLicense](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1_a55306977c4bf0fa433a290066c952b96.html#a55306977c4bf0fa433a290066c952b96) = [ak\_wwise\_plugin\_license\_v1](structak__wwise__plugin__license__v1.html) |
|  | |
| using | [AK::Wwise::Plugin::CLicense](namespace_a_k_1_1_wwise_1_1_plugin_a4011d9267cc30115f858d75973fdce54.html#a4011d9267cc30115f858d75973fdce54) = V1::CLicense |
|  | Latest version of the C License interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a4011d9267cc30115f858d75973fdce54.html#a4011d9267cc30115f858d75973fdce54) |
|  | |
| using | [AK::Wwise::Plugin::License](namespace_a_k_1_1_wwise_1_1_plugin_a44e186a822b15e2230c95b695b01c101.html#a44e186a822b15e2230c95b695b01c101) = V1::License |
|  | Latest version of the C++ License interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a44e186a822b15e2230c95b695b01c101.html#a44e186a822b15e2230c95b695b01c101) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_aa34006f329cf976481aefb5f3d4db338.html#aa34006f329cf976481aefb5f3d4db338) (License) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_a94d6f011e8790b420a14fac03d154468.html#a94d6f011e8790b420a14fac03d154468) (License) |
|  | |

## 详细描述

Wwise Authoring Plug-ins - Plug-in API for licensing.

在文件 [License.h](_license_8h_source.html) 中定义.