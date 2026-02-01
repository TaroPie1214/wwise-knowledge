# AkBusMeteringCallbackInfo

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_bus_metering_callback_info-members.html) |
[Public 属性](#pub-attribs)

AkBusMeteringCallbackInfo结构体 参考

`#include <AkCallbackTypes.h>`

类 AkBusMeteringCallbackInfo 继承关系图:

![](../../../images/struct_ak_bus_metering_callback_info.png)

|  |  |
| --- | --- |
| Public 属性 | |
| [AK::AkMetering](struct_a_k_1_1_ak_metering.html) \* | [pMetering](struct_ak_bus_metering_callback_info_a015994a25526d01043e2e3b6f8790cef.html#a015994a25526d01043e2e3b6f8790cef) |
|  | Struct containing metering information. [更多...](struct_ak_bus_metering_callback_info_a015994a25526d01043e2e3b6f8790cef.html#a015994a25526d01043e2e3b6f8790cef) |
|  | |
| [AkChannelConfig](struct_ak_channel_config.html) | [channelConfig](struct_ak_bus_metering_callback_info_a89d50d7c945d4935dce9c44f3f468be5.html#a89d50d7c945d4935dce9c44f3f468be5) |
|  | Channel configuration of the bus. [更多...](struct_ak_bus_metering_callback_info_a89d50d7c945d4935dce9c44f3f468be5.html#a89d50d7c945d4935dce9c44f3f468be5) |
|  | |
| [AkMeteringFlags](_ak_enums_8h_a29f798f121cb4138f9c92f8421d5e729.html#a29f798f121cb4138f9c92f8421d5e729) | [eMeteringFlags](struct_ak_bus_metering_callback_info_a3e69eb6775d5a34c1b0ce6084b3f92c0.html#a3e69eb6775d5a34c1b0ce6084b3f92c0) |
|  | Metering flags that were asked for in [RegisterBusMeteringCallback()](namespace_a_k_1_1_sound_engine_a4935dbc8c375c82c03475a1dbde37a51.html#a4935dbc8c375c82c03475a1dbde37a51). You may only access corresponding meter values from in\_pMeteringInfo. Others will fail. [更多...](struct_ak_bus_metering_callback_info_a3e69eb6775d5a34c1b0ce6084b3f92c0.html#a3e69eb6775d5a34c1b0ce6084b3f92c0) |
|  | |
| - Public 属性 继承自 [AkCallbackInfo](struct_ak_callback_info.html) | |
| void \* | [pCookie](struct_ak_callback_info_a459248bd71e5a7fc85846d845c38dbe8.html#a459248bd71e5a7fc85846d845c38dbe8) |
|  | User data, passed to [PostEvent()](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e) [更多...](struct_ak_callback_info_a459248bd71e5a7fc85846d845c38dbe8.html#a459248bd71e5a7fc85846d845c38dbe8) |
|  | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjID](struct_ak_callback_info_a035c8b8516ffcb2975a5df8fec1dcc39.html#a035c8b8516ffcb2975a5df8fec1dcc39) |
|  | Game object ID [更多...](struct_ak_callback_info_a035c8b8516ffcb2975a5df8fec1dcc39.html#a035c8b8516ffcb2975a5df8fec1dcc39) |
|  | |

## 详细描述

Callback information structure allowing to query signal metering on busses, at each frame, after having mixed all their inputs and processed their effects. Register the callback using [AK::SoundEngine::RegisterBusMeteringCallback](namespace_a_k_1_1_sound_engine_a4935dbc8c375c82c03475a1dbde37a51.html#a4935dbc8c375c82c03475a1dbde37a51).

在文件 [AkCallbackTypes.h](_ak_callback_types_8h_source.html) 第 [280](_ak_callback_types_8h_source.html#l00280) 行定义.