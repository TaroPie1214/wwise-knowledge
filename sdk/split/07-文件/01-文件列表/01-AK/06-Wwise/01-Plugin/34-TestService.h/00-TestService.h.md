# TestService.h

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

TestService.h 文件参考

`#include "PluginInfoGenerator.h"`

[浏览源代码.](_test_service_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| struct | [ak\_wwise\_plugin\_test\_service\_v2](structak__wwise__plugin__test__service__v2.html) |
|  | |
| class | [AK.Wwise::Plugin::V2::TestService](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_test_service.html) |
|  | |
| class | [AK.Wwise::Plugin::RequestedHostInterface< TestService >](class_a_k_1_1_wwise_1_1_plugin_1_1_requested_host_interface_3_01_test_service_01_4.html) |
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
|  | [AK::Wwise::Plugin::V2](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v2.html) |
|  | |

|  |  |
| --- | --- |
| 宏定义 | |
| #define | [AK\_WWISE\_PLUGIN\_TESTSERVICE\_V2\_ID](_test_service_8h_a2b4b1830253441f6e71852751e3b3e9f.html#a2b4b1830253441f6e71852751e3b3e9f)()    AK\_WWISE\_PLUGIN\_TEST\_SERVICE\_INTERFACE\_FROM\_ID([AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_TESTSERVICE](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#gga6611f8c24af9575c6be02f8a963b57c9aa350fb41f83e8b444aed3f757dac68f5), 2) |
|  | |
| #define | [AK\_WWISE\_PLUGIN\_TESTSERVICE\_V2\_CTOR](_test_service_8h_a827a2d15ead1804e7520511a7d5383d8.html#a827a2d15ead1804e7520511a7d5383d8)() |
|  | |

|  |  |
| --- | --- |
| 类型定义 | |
| using | [AK::Wwise::Plugin::V2::CTestService](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v2_a0e1b0deb15b99022916424617bb4cd25.html#a0e1b0deb15b99022916424617bb4cd25) = [ak\_wwise\_plugin\_test\_service\_v2](structak__wwise__plugin__test__service__v2.html) |
|  | |
| using | [AK::Wwise::Plugin::V2::RequestTestService](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v2_a144ede7e4897699ff8003e781d7f5e77.html#a144ede7e4897699ff8003e781d7f5e77) = RequestedHostInterface< TestService > |
|  | |
| using | [AK::Wwise::Plugin::CTestService](namespace_a_k_1_1_wwise_1_1_plugin_a153b1d2e36ab2eb663b0830baf3b1d72.html#a153b1d2e36ab2eb663b0830baf3b1d72) = V2::CTestService |
|  | Latest version of the C TestService interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a153b1d2e36ab2eb663b0830baf3b1d72.html#a153b1d2e36ab2eb663b0830baf3b1d72) |
|  | |
| using | [AK::Wwise::Plugin::TestService](namespace_a_k_1_1_wwise_1_1_plugin_a49755cf687541087df2007b0303785de.html#a49755cf687541087df2007b0303785de) = V2::TestService |
|  | Latest version of the C++ TestService interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a49755cf687541087df2007b0303785de.html#a49755cf687541087df2007b0303785de) |
|  | |
| using | [AK::Wwise::Plugin::RequestTestService](namespace_a_k_1_1_wwise_1_1_plugin_a37bfa715acab11a6e0025f7c36a47ea6.html#a37bfa715acab11a6e0025f7c36a47ea6) = V2::RequestTestService |
|  | Latest version of the requested C++ TestService interface. [更多...](namespace_a_k_1_1_wwise_1_1_plugin_a37bfa715acab11a6e0025f7c36a47ea6.html#a37bfa715acab11a6e0025f7c36a47ea6) |
|  | |

|  |  |
| --- | --- |
| 函数 | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_CLASS](namespace_a_k_1_1_wwise_1_1_plugin_a474a7d81fd6e81f7414806a9a6e114b3.html#a474a7d81fd6e81f7414806a9a6e114b3) (TestService) |
|  | |
|  | [AK::Wwise::Plugin::AK\_WWISE\_PLUGIN\_SPECIALIZE\_INTERFACE\_VERSION](namespace_a_k_1_1_wwise_1_1_plugin_ae5f0fd9f38b858a04593ee2d4474227f.html#ae5f0fd9f38b858a04593ee2d4474227f) (TestService) |
|  | |