# IAkPluginServicePlatformFuncs

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkPluginServicePlatformFuncs](class_a_k_1_1_i_ak_plugin_service_platform_funcs.html)

[所有成员列表](class_a_k_1_1_i_ak_plugin_service_platform_funcs-members.html) |
[Public 成员函数](#pub-methods) |
[Protected 成员函数](#pro-methods)

AK::IAkPluginServicePlatformFuncs类 参考abstract

Interface for the services related to the platform
[更多...](class_a_k_1_1_i_ak_plugin_service_platform_funcs.html#details)

`#include <IAkPluginServicePlatformFuncs.h>`

类 AK::IAkPluginServicePlatformFuncs 继承关系图:

![](../../../../images/class_a_k_1_1_i_ak_plugin_service_platform_funcs.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual void | [CreateThread](class_a_k_1_1_i_ak_plugin_service_platform_funcs_a479e2a73845ec15f51aceb894073a9ed.html#a479e2a73845ec15f51aceb894073a9ed) ([AkThreadRoutine](_platforms_2_windows_2_ak_types_8h_a11f699a47a92db1df41d038c95267931.html#a11f699a47a92db1df41d038c95267931) in\_pStartRoutine, void \*in\_pParams, const [AkThreadProperties](struct_ak_thread_properties.html) &in\_threadProperties, [AkThread](_platforms_2_windows_2_ak_types_8h_a7cd2d8431cd51231604a8fa348a800d5.html#a7cd2d8431cd51231604a8fa348a800d5) \*out\_pThread, const char \*in\_szThreadName)=0 |
|  | |
| virtual bool | [IsValidThread](class_a_k_1_1_i_ak_plugin_service_platform_funcs_a86395aad20e01e0f7c113d5f5a1c06d0.html#a86395aad20e01e0f7c113d5f5a1c06d0) ([AkThread](_platforms_2_windows_2_ak_types_8h_a7cd2d8431cd51231604a8fa348a800d5.html#a7cd2d8431cd51231604a8fa348a800d5) \*in\_pThread)=0 |
|  | |
| virtual void | [DestroyThread](class_a_k_1_1_i_ak_plugin_service_platform_funcs_ae112f9dcf3bd95ab29e904f78dd79751.html#ae112f9dcf3bd95ab29e904f78dd79751) ([AkThread](_platforms_2_windows_2_ak_types_8h_a7cd2d8431cd51231604a8fa348a800d5.html#a7cd2d8431cd51231604a8fa348a800d5) \*in\_pThread)=0 |
|  | |
| virtual void | [WaitForSingleThread](class_a_k_1_1_i_ak_plugin_service_platform_funcs_ab8cf438573d4102af66da0c1597cf019.html#ab8cf438573d4102af66da0c1597cf019) ([AkThread](_platforms_2_windows_2_ak_types_8h_a7cd2d8431cd51231604a8fa348a800d5.html#a7cd2d8431cd51231604a8fa348a800d5) \*in\_pThread)=0 |
|  | |
| virtual [AkThreadID](_platforms_2_windows_2_ak_types_8h_a300efeb7dbe0b9bde253dd9b9bbcb6ee.html#a300efeb7dbe0b9bde253dd9b9bbcb6ee) | [CurrentThread](class_a_k_1_1_i_ak_plugin_service_platform_funcs_aa9cd7c3f00d56b5df5ebce8f07ef2f57.html#aa9cd7c3f00d56b5df5ebce8f07ef2f57) ()=0 |
|  | |
| virtual void | [GetDefaultThreadProperties](class_a_k_1_1_i_ak_plugin_service_platform_funcs_a2d7d2830f36a7fb6f84817ea729bdb38.html#a2d7d2830f36a7fb6f84817ea729bdb38) ([AkThreadProperties](struct_ak_thread_properties.html) &out\_threadProperties)=0 |
|  | |
| virtual void | [GetDefaultHighPriorityThreadProperties](class_a_k_1_1_i_ak_plugin_service_platform_funcs_aca0665f93ae12b26183bf57ae74c5b1f.html#aca0665f93ae12b26183bf57ae74c5b1f) ([AkThreadProperties](struct_ak_thread_properties.html) &out\_threadProperties)=0 |
|  | |
| virtual void | [Sleep](class_a_k_1_1_i_ak_plugin_service_platform_funcs_a927faa1a5c925022c7297d46743391f0.html#a927faa1a5c925022c7297d46743391f0) ([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_ulMilliseconds)=0 |
|  | |

|  |  |
| --- | --- |
| Protected 成员函数 | |
| virtual | [~IAkPluginServicePlatformFuncs](class_a_k_1_1_i_ak_plugin_service_platform_funcs_a116b4803164d22a4bb202ae978189df3.html#a116b4803164d22a4bb202ae978189df3) () |
|  | |
| - Protected 成员函数 继承自 [AK::IAkPluginService](class_a_k_1_1_i_ak_plugin_service.html) | |
| virtual | [~IAkPluginService](class_a_k_1_1_i_ak_plugin_service_af880be6eab8f4f3cd124ec8db8b562de.html#af880be6eab8f4f3cd124ec8db8b562de) () |
|  | |

## 详细描述

Interface for the services related to the platform

在文件 [IAkPluginServicePlatformFuncs.h](_i_ak_plugin_service_platform_funcs_8h_source.html) 第 [38](_i_ak_plugin_service_platform_funcs_8h_source.html#l00038) 行定义.