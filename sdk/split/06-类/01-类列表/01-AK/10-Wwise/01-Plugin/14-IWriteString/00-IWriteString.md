# IWriteString

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [IWriteString](class_a_k_1_1_wwise_1_1_plugin_1_1_i_write_string.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_i_write_string-members.html) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::IWriteString类 参考abstract

`#include <PluginDef.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual void | [WriteString](class_a_k_1_1_wwise_1_1_plugin_1_1_i_write_string_a8ad8827cd12bc92cb6e0f15445e5aeab.html#a8ad8827cd12bc92cb6e0f15445e5aeab) (const char \*in\_szString, int in\_iStringLength)=0 |
|  | |

## 详细描述

Interface to let the plug in give us a string of any size. The pointer to the interface should not be kept.

在文件 [PluginDef.h](_plugin_def_8h_source.html) 第 [178](_plugin_def_8h_source.html#l00178) 行定义.