# ak_wwise_plugin_gui_windows_v1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](structak__wwise__plugin__gui__windows__v1-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

ak\_wwise\_plugin\_gui\_windows\_v1结构体 参考

Windows frontend plug-in API for Audio plug-ins.
[更多...](structak__wwise__plugin__gui__windows__v1.html#details)

`#include <GUIWindows.h>`

类 ak\_wwise\_plugin\_gui\_windows\_v1 继承关系图:

![](../../../images/structak__wwise__plugin__gui__windows__v1.png)

|  |  |
| --- | --- |
| Public 类型 | |
| using | [Instance](structak__wwise__plugin__gui__windows__v1_a09c7632c820f2c3e31d583b814463279.html#a09c7632c820f2c3e31d583b814463279) = [ak\_wwise\_plugin\_gui\_windows\_instance\_v1](structak__wwise__plugin__gui__windows__instance__v1.html) |
|  | Base instance type for providing a Windows frontend for an audio plug-in. [更多...](structak__wwise__plugin__gui__windows__v1_a09c7632c820f2c3e31d583b814463279.html#a09c7632c820f2c3e31d583b814463279) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [ak\_wwise\_plugin\_gui\_windows\_v1](structak__wwise__plugin__gui__windows__v1_a20cada8d06bc0ef19afa66f617f30032.html#a20cada8d06bc0ef19afa66f617f30032) () |
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
| HINSTANCE(\* | [GetResourceHandle](structak__wwise__plugin__gui__windows__v1_a5b036698bfb04694254fe7a1a61ebd79.html#a5b036698bfb04694254fe7a1a61ebd79) )(const struct [ak\_wwise\_plugin\_gui\_windows\_instance\_v1](structak__wwise__plugin__gui__windows__instance__v1.html) \*in\_this) |
|  | Retrieves the plug-in's HINSTANCE used for loading resources. [更多...](structak__wwise__plugin__gui__windows__v1_a5b036698bfb04694254fe7a1a61ebd79.html#a5b036698bfb04694254fe7a1a61ebd79) |
|  | |
| bool(\* | [GetDialog](structak__wwise__plugin__gui__windows__v1_a3eb842cb63ed86b621bcea6ed692bd1c.html#a3eb842cb63ed86b621bcea6ed692bd1c) )(const struct [ak\_wwise\_plugin\_gui\_windows\_instance\_v1](structak__wwise__plugin__gui__windows__instance__v1.html) \*in\_this, [AK::Wwise::Plugin::eDialog](namespace_a_k_1_1_wwise_1_1_plugin_a5a9328b141630d1de228c92e81e9034d.html#a5a9328b141630d1de228c92e81e9034d) in\_eDialog, uint32\_t \*out\_uiDialogID, [AK::Wwise::Plugin::PopulateTableItem](struct_a_k_1_1_wwise_1_1_plugin_1_1_populate_table_item.html) \*\*out\_pTable) |
|  | Retrieves the plug-in dialog parameters. [更多...](structak__wwise__plugin__gui__windows__v1_a3eb842cb63ed86b621bcea6ed692bd1c.html#a3eb842cb63ed86b621bcea6ed692bd1c) |
|  | |
| bool(\* | [WindowProc](structak__wwise__plugin__gui__windows__v1_a61a4925c4d1df3c0cb1d05b35b5bbc46.html#a61a4925c4d1df3c0cb1d05b35b5bbc46) )(struct [ak\_wwise\_plugin\_gui\_windows\_instance\_v1](structak__wwise__plugin__gui__windows__instance__v1.html) \*in\_this, [AK::Wwise::Plugin::eDialog](namespace_a_k_1_1_wwise_1_1_plugin_a5a9328b141630d1de228c92e81e9034d.html#a5a9328b141630d1de228c92e81e9034d) in\_eDialog, HWND in\_hWnd, uint32\_t in\_message, WPARAM in\_wParam, LPARAM in\_lParam, LRESULT \*out\_lResult) |
|  | Window message handler for dialogs. [更多...](structak__wwise__plugin__gui__windows__v1_a61a4925c4d1df3c0cb1d05b35b5bbc46.html#a61a4925c4d1df3c0cb1d05b35b5bbc46) |
|  | |
| bool(\* | [Help](structak__wwise__plugin__gui__windows__v1_a1cd16b3f42ff0faf531a190b649da0cf.html#a1cd16b3f42ff0faf531a190b649da0cf) )(const struct [ak\_wwise\_plugin\_gui\_windows\_instance\_v1](structak__wwise__plugin__gui__windows__instance__v1.html) \*in\_this, HWND in\_hWnd, [AK::Wwise::Plugin::eDialog](namespace_a_k_1_1_wwise_1_1_plugin_a5a9328b141630d1de228c92e81e9034d.html#a5a9328b141630d1de228c92e81e9034d) in\_eDialog, const char \*in\_szLanguageCode) |
|  | Called when the user clicks on the '?' icon. [更多...](structak__wwise__plugin__gui__windows__v1_a1cd16b3f42ff0faf531a190b649da0cf.html#a1cd16b3f42ff0faf531a190b649da0cf) |
|  | |
| - Public 属性 继承自 [ak\_wwise\_plugin\_interface\_ptr](structak__wwise__plugin__base__interface.html) | |
| [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9) | [m\_interface](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9): 32 |
|  | Interface type (see [ak\_wwise\_plugin\_interface\_type](group__global_ga6611f8c24af9575c6be02f8a963b57c9.html#ga6611f8c24af9575c6be02f8a963b57c9)) [更多...](structak__wwise__plugin__base__interface_a146b64003437eb7327201578ee814bc9.html#a146b64003437eb7327201578ee814bc9) |
|  | |
| uint32\_t | [m\_version](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6): 32 |
|  | Version of the interface [更多...](structak__wwise__plugin__base__interface_ab047f9139a14c6f03e396493c7dc6fb6.html#ab047f9139a14c6f03e396493c7dc6fb6) |
|  | |

## 详细描述

Windows frontend plug-in API for Audio plug-ins.

You must create this interface in order to support the GUI part of the user interface.

参见
:   - [实现 Windows 前端](plugin_frontend_windows.html)

在文件 [GUIWindows.h](_g_u_i_windows_8h_source.html) 第 [88](_g_u_i_windows_8h_source.html#l00088) 行定义.