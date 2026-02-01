# IAkLinuxContext

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkLinuxContext](class_a_k_1_1_i_ak_linux_context.html)

[所有成员列表](class_a_k_1_1_i_ak_linux_context-members.html) |
[Public 成员函数](#pub-methods)

AK::IAkLinuxContext类 参考abstract

Context specific to the Linux port of [Wwise](namespace_a_k_1_1_wwise.html) SDK.
[更多...](class_a_k_1_1_i_ak_linux_context.html#details)

`#include <AkPlatformContext.h>`

类 AK::IAkLinuxContext 继承关系图:

![](../../../../images/class_a_k_1_1_i_ak_linux_context.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual bool | [UsePulseAudioServerInfo](class_a_k_1_1_i_ak_linux_context_a32743476c85c8dea03933e657083e276.html#a32743476c85c8dea03933e657083e276) ()=0 |
|  | |
| virtual const char \* | [GetStreamName](class_a_k_1_1_i_ak_linux_context_a00c1bd4b1468d584904d812a80863d24.html#a00c1bd4b1468d584904d812a80863d24) ([AkDeviceID](_ak_typedefs_8h_a9fb6f04697979f304a7b2b4f405e8260.html#a9fb6f04697979f304a7b2b4f405e8260) deviceID=0)=0 |
|  | |
| virtual [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [GetChannelCount](class_a_k_1_1_i_ak_linux_context_aaba3937b9fd9b4917798367676b8efc9.html#aaba3937b9fd9b4917798367676b8efc9) ([AkDeviceID](_ak_typedefs_8h_a9fb6f04697979f304a7b2b4f405e8260.html#a9fb6f04697979f304a7b2b4f405e8260) deviceID=0)=0 |
|  | |
| virtual void | [SetSinkInitialized](class_a_k_1_1_i_ak_linux_context_a213960a6452fdb2c2b7c16e820b37ba4.html#a213960a6452fdb2c2b7c16e820b37ba4) (bool isInitialized)=0 |
|  | |
| virtual bool | [IsPluginSupported](class_a_k_1_1_i_ak_linux_context_aadfd002ea03e21c412edd6d7506f9f03.html#aadfd002ea03e21c412edd6d7506f9f03) ([AkPluginID](_ak_typedefs_8h_ad1d16d137b445ef6f7c2dd5ff1c9a6d8.html#ad1d16d137b445ef6f7c2dd5ff1c9a6d8) pluginID)=0 |
|  | |
| virtual bool | [IsStreamReady](class_a_k_1_1_i_ak_linux_context_acec738b3d3d7c2618cd4cb8211533272.html#acec738b3d3d7c2618cd4cb8211533272) ([AkPluginID](_ak_typedefs_8h_ad1d16d137b445ef6f7c2dd5ff1c9a6d8.html#ad1d16d137b445ef6f7c2dd5ff1c9a6d8) pluginID)=0 |
|  | |
| virtual const char \* | [GetStreamName](class_a_k_1_1_i_ak_linux_context_a74b3b686576b84490a6b58f96f34cf43.html#a74b3b686576b84490a6b58f96f34cf43) ([AkPluginID](_ak_typedefs_8h_ad1d16d137b445ef6f7c2dd5ff1c9a6d8.html#ad1d16d137b445ef6f7c2dd5ff1c9a6d8) pluginID, [AkDeviceID](_ak_typedefs_8h_a9fb6f04697979f304a7b2b4f405e8260.html#a9fb6f04697979f304a7b2b4f405e8260) deviceID)=0 |
|  | |
| virtual [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | [GetChannelCount](class_a_k_1_1_i_ak_linux_context_a4b6db21c820016ca31a1f3511cf4fba4.html#a4b6db21c820016ca31a1f3511cf4fba4) ([AkPluginID](_ak_typedefs_8h_ad1d16d137b445ef6f7c2dd5ff1c9a6d8.html#ad1d16d137b445ef6f7c2dd5ff1c9a6d8) pluginID, [AkDeviceID](_ak_typedefs_8h_a9fb6f04697979f304a7b2b4f405e8260.html#a9fb6f04697979f304a7b2b4f405e8260) deviceID)=0 |
|  | |
| virtual void | [SetSinkInitialized](class_a_k_1_1_i_ak_linux_context_a02a7e3f193f4413d41d81d0a9ab74483.html#a02a7e3f193f4413d41d81d0a9ab74483) ([AkPluginID](_ak_typedefs_8h_ad1d16d137b445ef6f7c2dd5ff1c9a6d8.html#ad1d16d137b445ef6f7c2dd5ff1c9a6d8) pluginID, bool isInitialized)=0 |
|  | |
| - Public 成员函数 继承自 [AK::IAkPlatformContext](class_a_k_1_1_i_ak_platform_context.html) | |
| virtual | [~IAkPlatformContext](class_a_k_1_1_i_ak_platform_context_a4fe82c039fea5a15da6bf763868f2633.html#a4fe82c039fea5a15da6bf763868f2633) () |
|  | |

## 详细描述

Context specific to the Linux port of [Wwise](namespace_a_k_1_1_wwise.html) SDK.

在文件 [AkPlatformContext.h](_linux_2_ak_platform_context_8h_source.html) 第 [36](_linux_2_ak_platform_context_8h_source.html#l00036) 行定义.