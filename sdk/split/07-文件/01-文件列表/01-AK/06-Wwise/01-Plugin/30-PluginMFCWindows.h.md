# PluginMFCWindows.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Wwise](dir_6ea5b71cdf4c60d3386ed2d84846331f.html)
- [Plugin](dir_00900ac4c96da97e1d767c263ed2fa21.html)

[类](#nested-classes) |
[命名空间](#namespaces)

PluginMFCWindows.h 文件参考

Wwise Authoring Plug-ins - Provides MFC initialization on plug-in instantiation.
[更多...](#details)

`#include <afxwin.h>`  
`#include <memory>`

[浏览源代码.](_plugin_m_f_c_windows_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| class | [AK.Wwise::Plugin::PluginMFCWindows< CWinApp >](class_a_k_1_1_wwise_1_1_plugin_1_1_plugin_m_f_c_windows.html) |
|  | Initializes MFC for this plug-in. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_plugin_m_f_c_windows.html#details) |
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

## 详细描述

Wwise Authoring Plug-ins - Provides MFC initialization on plug-in instantiation.

By default, an MFC-based DLL initializes itself when the DLL is loaded. However, not all plug-ins in a DLL container require MFC, so this makes sure to initialize MFC only on instantiation of a particular plug-in.

参见
:   C++ interfaces

    - [AK::Wwise::Plugin::PluginMFCWindows](class_a_k_1_1_wwise_1_1_plugin_1_1_plugin_m_f_c_windows.html)

在文件 [PluginMFCWindows.h](_plugin_m_f_c_windows_8h_source.html) 中定义.