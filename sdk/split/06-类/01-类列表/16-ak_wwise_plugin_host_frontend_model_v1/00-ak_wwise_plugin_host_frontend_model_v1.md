# ak_wwise_plugin_host_frontend_model_v1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](structak__wwise__plugin__host__frontend__model__v1-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

ak\_wwise\_plugin\_host\_frontend\_model\_v1结构体 参考

Interface used to interact with the frontend model.
[更多...](structak__wwise__plugin__host__frontend__model__v1.html#details)

`#include <HostFrontendModel.h>`

类 ak\_wwise\_plugin\_host\_frontend\_model\_v1 继承关系图:

![](../../../images/structak__wwise__plugin__host__frontend__model__v1.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [Instance](structak__wwise__plugin__host__frontend__model__v1_a7a0a431cc709963431762c9f1a28359f.html#a7a0a431cc709963431762c9f1a28359f) = [ak\_wwise\_plugin\_host\_frontend\_model\_instance\_v1](structak__wwise__plugin__host__frontend__model__instance__v1.html) |
|  | Base host-provided instance type for [ak\_wwise\_plugin\_host\_frontend\_model\_v1](structak__wwise__plugin__host__frontend__model__v1.html "Interface used to interact with the frontend model."). [更多...](structak__wwise__plugin__host__frontend__model__v1_a7a0a431cc709963431762c9f1a28359f.html#a7a0a431cc709963431762c9f1a28359f) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [ak\_wwise\_plugin\_host\_frontend\_model\_v1](structak__wwise__plugin__host__frontend__model__v1_a7cee255eb54eaa59ba3b7897e999ab19.html#a7cee255eb54eaa59ba3b7897e999ab19) () |
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
| bool(\* | [HasWidget](structak__wwise__plugin__host__frontend__model__v1_a9efb37dbb92a90bd8509b10c31440177.html#a9efb37dbb92a90bd8509b10c31440177) )(struct [ak\_wwise\_plugin\_host\_frontend\_model\_instance\_v1](structak__wwise__plugin__host__frontend__model__instance__v1.html) \*in\_this, const char \*in\_absoluteId) |
|  | Checks if a specific widget exists. [更多...](structak__wwise__plugin__host__frontend__model__v1_a9efb37dbb92a90bd8509b10c31440177.html#a9efb37dbb92a90bd8509b10c31440177) |
|  | |
| [ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) \*(\* | [GetParentWidget](structak__wwise__plugin__host__frontend__model__v1_a29bc5800d1eb10e887cbc5869a259b6b.html#a29bc5800d1eb10e887cbc5869a259b6b) )(struct [ak\_wwise\_plugin\_host\_frontend\_model\_instance\_v1](structak__wwise__plugin__host__frontend__model__instance__v1.html) \*in\_this, const char \*in\_absoluteId) |
|  | Returns the parent widget of a given Frontend Handle hierarchy. [更多...](structak__wwise__plugin__host__frontend__model__v1_a29bc5800d1eb10e887cbc5869a259b6b.html#a29bc5800d1eb10e887cbc5869a259b6b) |
|  | |
| [ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) \*(\* | [GetRootWidget](structak__wwise__plugin__host__frontend__model__v1_a6738a6f6a2a5e76d58f587cf0af7068e.html#a6738a6f6a2a5e76d58f587cf0af7068e) )(struct [ak\_wwise\_plugin\_host\_frontend\_model\_instance\_v1](structak__wwise__plugin__host__frontend__model__instance__v1.html) \*in\_this) |
|  | Returns the main layout widget of a given Frontend Handle hierarchy. [更多...](structak__wwise__plugin__host__frontend__model__v1_a6738a6f6a2a5e76d58f587cf0af7068e.html#a6738a6f6a2a5e76d58f587cf0af7068e) |
|  | |
| [ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) \*(\* | [GetWidget](structak__wwise__plugin__host__frontend__model__v1_a19add841b923aedf610087f4153495a7.html#a19add841b923aedf610087f4153495a7) )(struct [ak\_wwise\_plugin\_host\_frontend\_model\_instance\_v1](structak__wwise__plugin__host__frontend__model__instance__v1.html) \*in\_this, const char \*in\_absoluteId) |
|  | Returns a specific widget of a given Frontend Handle hierarchy. [更多...](structak__wwise__plugin__host__frontend__model__v1_a19add841b923aedf610087f4153495a7.html#a19add841b923aedf610087f4153495a7) |
|  | |
| const char \*(\* | [GetWidgetID](structak__wwise__plugin__host__frontend__model__v1_a834fd8c94359c4211f25bd65b1afbc2f.html#a834fd8c94359c4211f25bd65b1afbc2f) )(struct [ak\_wwise\_plugin\_host\_frontend\_model\_instance\_v1](structak__wwise__plugin__host__frontend__model__instance__v1.html) \*in\_this, [ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) \*in\_widget) |
|  | Gets the ID of a widget. [更多...](structak__wwise__plugin__host__frontend__model__v1_a834fd8c94359c4211f25bd65b1afbc2f.html#a834fd8c94359c4211f25bd65b1afbc2f) |
|  | |
| const char \*(\* | [GetWidgetType](structak__wwise__plugin__host__frontend__model__v1_a866ef8e07a2a6335950aba467d6e8828.html#a866ef8e07a2a6335950aba467d6e8828) )(struct [ak\_wwise\_plugin\_host\_frontend\_model\_instance\_v1](structak__wwise__plugin__host__frontend__model__instance__v1.html) \*in\_this, [ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) \*in\_widget) |
|  | Gets the type ID of a widget. [更多...](structak__wwise__plugin__host__frontend__model__v1_a866ef8e07a2a6335950aba467d6e8828.html#a866ef8e07a2a6335950aba467d6e8828) |
|  | |
| bool(\* | [IsWidgetContainer](structak__wwise__plugin__host__frontend__model__v1_aa46958444ca832a5d7812d04065fd4d1.html#aa46958444ca832a5d7812d04065fd4d1) )(struct [ak\_wwise\_plugin\_host\_frontend\_model\_instance\_v1](structak__wwise__plugin__host__frontend__model__instance__v1.html) \*in\_this, [ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) \*in\_widget) |
|  | Checks if the widget can contain other widgets. [更多...](structak__wwise__plugin__host__frontend__model__v1_aa46958444ca832a5d7812d04065fd4d1.html#aa46958444ca832a5d7812d04065fd4d1) |
|  | |
| bool(\* | [IsWidgetTopLevel](structak__wwise__plugin__host__frontend__model__v1_a410b52465de0d8a0ff16d112fa9cc3c2.html#a410b52465de0d8a0ff16d112fa9cc3c2) )(struct [ak\_wwise\_plugin\_host\_frontend\_model\_instance\_v1](structak__wwise__plugin__host__frontend__model__instance__v1.html) \*in\_this, [ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) \*in\_widget) |
|  | Checks if the widget is top-level. [更多...](structak__wwise__plugin__host__frontend__model__v1_a410b52465de0d8a0ff16d112fa9cc3c2.html#a410b52465de0d8a0ff16d112fa9cc3c2) |
|  | |
| bool(\* | [IsWidgetVisible](structak__wwise__plugin__host__frontend__model__v1_ad77efb4c6d9476b2fda81c9e631a4f53.html#ad77efb4c6d9476b2fda81c9e631a4f53) )(struct [ak\_wwise\_plugin\_host\_frontend\_model\_instance\_v1](structak__wwise__plugin__host__frontend__model__instance__v1.html) \*in\_this, [ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) \*in\_widget) |
|  | Determines the visibility state of the given widget. [更多...](structak__wwise__plugin__host__frontend__model__v1_ad77efb4c6d9476b2fda81c9e631a4f53.html#ad77efb4c6d9476b2fda81c9e631a4f53) |
|  | |
| bool(\* | [IsWidgetEnabled](structak__wwise__plugin__host__frontend__model__v1_ab41d25550c18574aa5ad089d63405d88.html#ab41d25550c18574aa5ad089d63405d88) )(struct [ak\_wwise\_plugin\_host\_frontend\_model\_instance\_v1](structak__wwise__plugin__host__frontend__model__instance__v1.html) \*in\_this, [ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) \*in\_widget) |
|  | Determines if a widget is enabled for mouse and keyboard input. [更多...](structak__wwise__plugin__host__frontend__model__v1_ab41d25550c18574aa5ad089d63405d88.html#ab41d25550c18574aa5ad089d63405d88) |
|  | |
| void(\* | [EnableWidget](structak__wwise__plugin__host__frontend__model__v1_acfc30c44a9b589540bce7ae3d2a85ec0.html#acfc30c44a9b589540bce7ae3d2a85ec0) )(struct [ak\_wwise\_plugin\_host\_frontend\_model\_instance\_v1](structak__wwise__plugin__host__frontend__model__instance__v1.html) \*in\_this, [ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) \*in\_widget, bool in\_enable) |
|  | Enables or disables mouse and keyboard input for the widget. [更多...](structak__wwise__plugin__host__frontend__model__v1_acfc30c44a9b589540bce7ae3d2a85ec0.html#acfc30c44a9b589540bce7ae3d2a85ec0) |
|  | |
| void(\* | [ShowWidget](structak__wwise__plugin__host__frontend__model__v1_ae5b6c4804d39cf1be40b4e6b75c5f902.html#ae5b6c4804d39cf1be40b4e6b75c5f902) )(struct [ak\_wwise\_plugin\_host\_frontend\_model\_instance\_v1](structak__wwise__plugin__host__frontend__model__instance__v1.html) \*in\_this, [ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) \*in\_widget, bool in\_show) |
|  | Sets the visibility state of the widget. [更多...](structak__wwise__plugin__host__frontend__model__v1_ae5b6c4804d39cf1be40b4e6b75c5f902.html#ae5b6c4804d39cf1be40b4e6b75c5f902) |
|  | |
| void(\* | [SetWidgetFocus](structak__wwise__plugin__host__frontend__model__v1_ae2e37c9170296b2cf853482c09972210.html#ae2e37c9170296b2cf853482c09972210) )(struct [ak\_wwise\_plugin\_host\_frontend\_model\_instance\_v1](structak__wwise__plugin__host__frontend__model__instance__v1.html) \*in\_this, [ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) \*in\_widget) |
|  | Claims the input focus for the widget. [更多...](structak__wwise__plugin__host__frontend__model__v1_ae2e37c9170296b2cf853482c09972210.html#ae2e37c9170296b2cf853482c09972210) |
|  | |
| bool(\* | [Connect](structak__wwise__plugin__host__frontend__model__v1_a11d37d6ca763903760e96bd30a4a3d2c.html#a11d37d6ca763903760e96bd30a4a3d2c) )(struct [ak\_wwise\_plugin\_host\_frontend\_model\_instance\_v1](structak__wwise__plugin__host__frontend__model__instance__v1.html) \*in\_this, [ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) \*in\_widget, const char \*in\_name, void(\*in\_handler)(), void \*in\_userData) |
|  | Connects a signal to a handler taking some user-defined data. [更多...](structak__wwise__plugin__host__frontend__model__v1_a11d37d6ca763903760e96bd30a4a3d2c.html#a11d37d6ca763903760e96bd30a4a3d2c) |
|  | |
| void(\* | [ForEachChildren](structak__wwise__plugin__host__frontend__model__v1_abc479ded886633e72e149022e481a0cf.html#abc479ded886633e72e149022e481a0cf) )(struct [ak\_wwise\_plugin\_host\_frontend\_model\_instance\_v1](structak__wwise__plugin__host__frontend__model__instance__v1.html) \*in\_this, const char \*in\_absoluteId, void(\*in\_handler)([ak\_wwise\_plugin\_widget](group__global_ga8b203f1b0ef4a48d2cee97d89eaae042.html#ga8b203f1b0ef4a48d2cee97d89eaae042) \*, void \*), void \*in\_userData) |
|  | Applies a user-defined handler to every child of a container. [更多...](structak__wwise__plugin__host__frontend__model__v1_abc479ded886633e72e149022e481a0cf.html#abc479ded886633e72e149022e481a0cf) |
|  | |
| - Public 属性 继承自 [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) | |
| [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9) | [m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9): 32 |
|  | Interface type (see [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9)) [更多...](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9) |
|  | |
| uint32\_t | [m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6): 32 |
|  | Version of the interface [更多...](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6) |
|  | |

## 详细描述

Interface used to interact with the frontend model.

The frontend model is the service in charge of building GUI views and managing the objects's lifetime. It takes the description of a view in the form of a WAFM file, creates the widget hierarchy, and stores the objects in a specific handle. The handle is shared to the user to allow interaction with the view's widgets.

在文件 [HostFrontendModel.h](_host_frontend_model_8h_source.html) 第 [45](_host_frontend_model_8h_source.html#l00045) 行定义.