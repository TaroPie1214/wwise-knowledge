# PluginMFCWindows

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [PluginMFCWindows](class_a_k_1_1_wwise_1_1_plugin_1_1_plugin_m_f_c_windows.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_plugin_m_f_c_windows-members.html) |
[Public 成员函数](#pub-methods) |
[静态 Public 成员函数](#pub-static-methods)

AK.Wwise::Plugin::PluginMFCWindows< CWinApp > 模板类 参考

Initializes MFC for this plug-in.
[更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_plugin_m_f_c_windows.html#details)

`#include <PluginMFCWindows.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [PluginMFCWindows](class_a_k_1_1_wwise_1_1_plugin_1_1_plugin_m_f_c_windows_a6a246672ea7ea78c67a931ff5a7d935f.html#a6a246672ea7ea78c67a931ff5a7d935f) () |
|  | Initializes g\_theApp singleton [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_plugin_m_f_c_windows_a6a246672ea7ea78c67a931ff5a7d935f.html#a6a246672ea7ea78c67a931ff5a7d935f) |
|  | |

|  |  |
| --- | --- |
| 静态 Public 成员函数 | |
| static CWinApp \* | [GetMFCApp](class_a_k_1_1_wwise_1_1_plugin_1_1_plugin_m_f_c_windows_a5cc8220c9627278506e29f0c7e4dfa8e.html#a5cc8220c9627278506e29f0c7e4dfa8e) () |
|  | Retrieves the CWinApp singleton. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_plugin_m_f_c_windows_a5cc8220c9627278506e29f0c7e4dfa8e.html#a5cc8220c9627278506e29f0c7e4dfa8e) |
|  | |

## 详细描述

### template<typename CWinApp = ::CWinApp> class AK.Wwise::Plugin::PluginMFCWindows< CWinApp >

Initializes MFC for this plug-in.

By default, an MFC-based DLL initializes itself when the DLL is loaded. However, not all plug-ins in a DLL container require MFC, so this makes sure to initialize MFC only on instantiation of a particular plug-in.

If you need to modify the CWinApp class on your own, you can update the template.

: public [AK::Wwise::Plugin::PluginMFCWindows<MyWinApp>](class_a_k_1_1_wwise_1_1_plugin_1_1_plugin_m_f_c_windows.html)

|  |  |
| --- | --- |
|  | **备注:** This should be the first interface of the plug-in, as it needs to be initialized before anything. |

在文件 [PluginMFCWindows.h](_plugin_m_f_c_windows_8h_source.html) 第 [68](_plugin_m_f_c_windows_8h_source.html#l00068) 行定义.

[AK.Wwise::Plugin::PluginMFCWindows](class_a_k_1_1_wwise_1_1_plugin_1_1_plugin_m_f_c_windows.html)

Initializes MFC for this plug-in.

**Definition:** [PluginMFCWindows.h:69](_plugin_m_f_c_windows_8h_source.html#l00068)