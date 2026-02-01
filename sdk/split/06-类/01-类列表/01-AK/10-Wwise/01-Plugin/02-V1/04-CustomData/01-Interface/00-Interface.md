# Interface

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [CustomData](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data.html)
- [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_1_1_interface.html)

[所有成员列表](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_1_1_interface-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::CustomData::Interface结构体 参考

`#include <CustomData.h>`

类 AK.Wwise::Plugin::V1::CustomData::Interface 继承关系图:

![](../../../../../../../../images/struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_1_1_interface.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [Instance](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_1_1_interface_a0d82e509004c2e2ee35652d5f5b95cec.html#a0d82e509004c2e2ee35652d5f5b95cec) = [CustomData](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data.html) |
|  | |
| - Public 类型 继承自 [ak\_wwise\_plugin\_custom\_data\_v1](structak__wwise__plugin__custom__data__v1.html) | |
| using | [Instance](structak__wwise__plugin__custom__data__v1_af1603ab1092422cd732f495185ba71d3.html#af1603ab1092422cd732f495185ba71d3) = [ak\_wwise\_plugin\_custom\_data\_instance\_v1](structak__wwise__plugin__custom__data__instance__v1.html) |
|  | Base instance type for providing custom data loading and saving. [更多...](structak__wwise__plugin__custom__data__v1_af1603ab1092422cd732f495185ba71d3.html#af1603ab1092422cd732f495185ba71d3) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_custom_data_1_1_interface_a8752ef71487e0d1cc10b040cfc7089c7.html#a8752ef71487e0d1cc10b040cfc7089c7) () |
|  | |
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_custom\_data\_v1](structak__wwise__plugin__custom__data__v1.html) | |
|  | [ak\_wwise\_plugin\_custom\_data\_v1](structak__wwise__plugin__custom__data__v1_ad74a9bfecbfb108a07060aedbe699466.html#ad74a9bfecbfb108a07060aedbe699466) () |
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
| 额外继承的成员函数 | |
| - Public 属性 继承自 [ak\_wwise\_plugin\_custom\_data\_v1](structak__wwise__plugin__custom__data__v1.html) | |
| void(\* | [InitToDefault](structak__wwise__plugin__custom__data__v1_aff4d18650d949fcc5e2cc4e18f6b573f.html#aff4d18650d949fcc5e2cc4e18f6b573f) )(struct [ak\_wwise\_plugin\_custom\_data\_instance\_v1](structak__wwise__plugin__custom__data__instance__v1.html) \*in\_this) |
|  | Initializes the plug-in's custom data to its default values. [更多...](structak__wwise__plugin__custom__data__v1_aff4d18650d949fcc5e2cc4e18f6b573f.html#aff4d18650d949fcc5e2cc4e18f6b573f) |
|  | |
| bool(\* | [InitFromInstance](structak__wwise__plugin__custom__data__v1_a08ee5fa4ca95daadaf1cffaadb60ca1e.html#a08ee5fa4ca95daadaf1cffaadb60ca1e) )(struct [ak\_wwise\_plugin\_custom\_data\_instance\_v1](structak__wwise__plugin__custom__data__instance__v1.html) \*in\_this, const struct [ak\_wwise\_plugin\_custom\_data\_instance\_v1](structak__wwise__plugin__custom__data__instance__v1.html) \*in\_source) |
|  | Copy the plug-in's custom data from another instance of the same plug-in. [更多...](structak__wwise__plugin__custom__data__v1_a08ee5fa4ca95daadaf1cffaadb60ca1e.html#a08ee5fa4ca95daadaf1cffaadb60ca1e) |
|  | |
| bool(\* | [InitFromWorkunit](structak__wwise__plugin__custom__data__v1_a495350302ff7bbd1c02d988668142445.html#a495350302ff7bbd1c02d988668142445) )(struct [ak\_wwise\_plugin\_custom\_data\_instance\_v1](structak__wwise__plugin__custom__data__instance__v1.html) \*in\_this, struct [ak\_wwise\_plugin\_host\_xml\_reader\_instance\_v1](structak__wwise__plugin__host__xml__reader__instance__v1.html) \*in\_pReader) |
|  | Load the custom data structure from the provided Work Unit's XML. [更多...](structak__wwise__plugin__custom__data__v1_a495350302ff7bbd1c02d988668142445.html#a495350302ff7bbd1c02d988668142445) |
|  | |
| bool(\* | [Save](structak__wwise__plugin__custom__data__v1_a8d0eb7c0dfdd6a74c1cec5a610a6a3c2.html#a8d0eb7c0dfdd6a74c1cec5a610a6a3c2) )(struct [ak\_wwise\_plugin\_custom\_data\_instance\_v1](structak__wwise__plugin__custom__data__instance__v1.html) \*in\_this, struct [ak\_wwise\_plugin\_host\_xml\_writer\_instance\_v1](structak__wwise__plugin__host__xml__writer__instance__v1.html) \*in\_pWriter) |
|  | Save custom data structure in the provided Work Unit's XML. [更多...](structak__wwise__plugin__custom__data__v1_a8d0eb7c0dfdd6a74c1cec5a610a6a3c2.html#a8d0eb7c0dfdd6a74c1cec5a610a6a3c2) |
|  | |
| void(\* | [OnDelete](structak__wwise__plugin__custom__data__v1_a48aded0f100bf7db38b151aa88f3e56f.html#a48aded0f100bf7db38b151aa88f3e56f) )(struct [ak\_wwise\_plugin\_custom\_data\_instance\_v1](structak__wwise__plugin__custom__data__instance__v1.html) \*in\_this) |
|  | OnDelete function is called when the user presses the "delete" button on a plug-in. [更多...](structak__wwise__plugin__custom__data__v1_a48aded0f100bf7db38b151aa88f3e56f.html#a48aded0f100bf7db38b151aa88f3e56f) |
|  | |
| bool(\* | [GetPluginData](structak__wwise__plugin__custom__data__v1_ae2a50eda33df6c0c7da86b967751cf40.html#ae2a50eda33df6c0c7da86b967751cf40) )(const struct [ak\_wwise\_plugin\_custom\_data\_instance\_v1](structak__wwise__plugin__custom__data__instance__v1.html) \*in\_this, const GUID \*in\_guidPlatform, [AkPluginParamID](_ak_typedefs_8h_a4cb8ff0b7014efdaa21697f4ef928926.html#a4cb8ff0b7014efdaa21697f4ef928926) in\_idParam, struct [ak\_wwise\_plugin\_host\_data\_writer\_instance\_v1](structak__wwise__plugin__host__data__writer__instance__v1.html) \*in\_pDataWriter) |
|  | Obtains parameters that will be sent to the sound engine when Wwise is connected. [更多...](structak__wwise__plugin__custom__data__v1_ae2a50eda33df6c0c7da86b967751cf40.html#ae2a50eda33df6c0c7da86b967751cf40) |
|  | |
| - Public 属性 继承自 [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) | |
| [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9) | [m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9): 32 |
|  | Interface type (see [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9)) [更多...](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9) |
|  | |
| uint32\_t | [m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6): 32 |
|  | Version of the interface [更多...](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6) |
|  | |

## 详细描述

在文件 [CustomData.h](_custom_data_8h_source.html) 第 [224](_custom_data_8h_source.html#l00224) 行定义.