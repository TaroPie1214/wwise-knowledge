# GUIWindows

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [V1](namespace_a_k_1_1_wwise_1_1_plugin_1_1_v1.html)
- [GUIWindows](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows-members.html) |
[类](#nested-classes) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::V1::GUIWindows类 参考

Windows frontend plug-in API for Audio plug-ins.
[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows.html#details)

`#include <GUIWindows.h>`

类 AK.Wwise::Plugin::V1::GUIWindows 继承关系图:

![](../../../../../../../images/class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows.png)

|  |  |
| --- | --- |
| 类 | |
| struct | [Interface](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows_1_1_interface.html) |
|  | The C interface, fulfilled by your plug-in. [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows_1_1_interface.html#details) |
|  | |

|  |  |
| --- | --- |
| Public 类型 | |
| enum | : InterfaceTypeValue { [k\_interfaceType](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows_afc4ae50ba44b267bf688b06e7652a1b9.html#afc4ae50ba44b267bf688b06e7652a1b9a535ffc9f2f9b435b8b58cd6b7942d0b6) = AK\_WWISE\_PLUGIN\_INTERFACE\_TYPE\_GUI\_WINDOWS } |
|  | The interface type, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows_afc4ae50ba44b267bf688b06e7652a1b9.html#afc4ae50ba44b267bf688b06e7652a1b9) |
|  | |
| enum | : InterfaceVersion { [k\_interfaceVersion](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows_af8654f047cedddc889b117e8f1735b39.html#af8654f047cedddc889b117e8f1735b39a2ebae04c2270146aa861b5f06ead1f98) = 1 } |
|  | The interface version, as provided by this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows_af8654f047cedddc889b117e8f1735b39.html#af8654f047cedddc889b117e8f1735b39) |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| [InterfacePtr](namespace_a_k_1_1_wwise_1_1_plugin_a9131bb705f2bd282ad65cac4efa17095.html#a9131bb705f2bd282ad65cac4efa17095) | [GetInterfacePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows_ac5d5846860c28043a4b8dfce30b62ced.html#ac5d5846860c28043a4b8dfce30b62ced) () |
|  | |
| [CGUIWindows::Instance](structak__wwise__plugin__gui__windows__v1_a09c7632c820f2c3e31d583b814463279.html#a09c7632c820f2c3e31d583b814463279) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows_a011913e403311cf3121d3a264746f8e9.html#a011913e403311cf3121d3a264746f8e9) () |
|  | |
| const [CGUIWindows::Instance](structak__wwise__plugin__gui__windows__v1_a09c7632c820f2c3e31d583b814463279.html#a09c7632c820f2c3e31d583b814463279) \* | [GetInstancePointer](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows_aa64794d183747710ce9d1219a9906352.html#aa64794d183747710ce9d1219a9906352) () const |
|  | |
|  | [GUIWindows](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows_a174395cd8eb6c1fb6d7155f204e9ba6d.html#a174395cd8eb6c1fb6d7155f204e9ba6d) () |
|  | |
| virtual | [~GUIWindows](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows_acb08454d82be52348c849da527cd14a4.html#acb08454d82be52348c849da527cd14a4) () |
|  | |
| virtual HINSTANCE | [GetResourceHandle](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows_a400dc71bed3f216d4c5afe2297474de1.html#a400dc71bed3f216d4c5afe2297474de1) () const |
|  | Retrieves the plug-in's HINSTANCE used for loading resources. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows_a400dc71bed3f216d4c5afe2297474de1.html#a400dc71bed3f216d4c5afe2297474de1) |
|  | |
| virtual bool | [GetDialog](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows_a21b81136769b185c244ada93e6767f14.html#a21b81136769b185c244ada93e6767f14) ([eDialog](namespace_a_k_1_1_wwise_1_1_plugin_a5a9328b141630d1de228c92e81e9034d.html#a5a9328b141630d1de228c92e81e9034d) in\_eDialog, uint32\_t &out\_uiDialogID, [PopulateTableItem](struct_a_k_1_1_wwise_1_1_plugin_1_1_populate_table_item.html) \*&out\_pTable) const |
|  | Retrieves the plug-in dialog parameters. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows_a21b81136769b185c244ada93e6767f14.html#a21b81136769b185c244ada93e6767f14) |
|  | |
| virtual bool | [WindowProc](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows_a8ea33835cc026463f2f64b4327f89b17.html#a8ea33835cc026463f2f64b4327f89b17) ([eDialog](namespace_a_k_1_1_wwise_1_1_plugin_a5a9328b141630d1de228c92e81e9034d.html#a5a9328b141630d1de228c92e81e9034d) in\_eDialog, HWND in\_hWnd, uint32\_t in\_message, WPARAM in\_wParam, LPARAM in\_lParam, LRESULT &out\_lResult) |
|  | Window message handler for dialogs. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows_a8ea33835cc026463f2f64b4327f89b17.html#a8ea33835cc026463f2f64b4327f89b17) |
|  | |
| virtual bool | [Help](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows_a4923a0688cfc1bca88fcd33196c897a7.html#a4923a0688cfc1bca88fcd33196c897a7) (HWND in\_hWnd, [eDialog](namespace_a_k_1_1_wwise_1_1_plugin_a5a9328b141630d1de228c92e81e9034d.html#a5a9328b141630d1de228c92e81e9034d) in\_eDialog, const char \*in\_szLanguageCode) const |
|  | Called when the user clicks on the '?' icon. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows_a4923a0688cfc1bca88fcd33196c897a7.html#a4923a0688cfc1bca88fcd33196c897a7) |
|  | |
| - Public 成员函数 继承自 [ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance.html) | |
| virtual | [~ak\_wwise\_plugin\_cpp\_base\_instance](structak__wwise__plugin__cpp__base__instance_a38e5192dde370d925b0489a70374ff01.html#a38e5192dde370d925b0489a70374ff01) () |
|  | |

## 详细描述

Windows frontend plug-in API for Audio plug-ins.

You must create this interface in order to support the GUI part of the user interface.

参见
:   - [实现 Windows 前端](plugin_frontend_windows.html)

在文件 [GUIWindows.h](_g_u_i_windows_8h_source.html) 第 [199](_g_u_i_windows_8h_source.html#l00199) 行定义.