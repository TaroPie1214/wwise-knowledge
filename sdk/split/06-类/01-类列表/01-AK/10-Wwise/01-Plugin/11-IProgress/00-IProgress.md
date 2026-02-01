# IProgress

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [IProgress](class_a_k_1_1_wwise_1_1_plugin_1_1_i_progress.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_i_progress-members.html) |
[Public 成员函数](#pub-methods)

AK.Wwise::Plugin::IProgress类 参考abstract

`#include <PluginDef.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual void | [SetCurrentOperationName](class_a_k_1_1_wwise_1_1_plugin_1_1_i_progress_a614204cbb0b851b0c87cafde36ee4330.html#a614204cbb0b851b0c87cafde36ee4330) (const char \*in\_szOperationName)=0 |
|  | |
| virtual void | [SetRange](class_a_k_1_1_wwise_1_1_plugin_1_1_i_progress_af8e34a3d90e226e19de4cfa63b09fb38.html#af8e34a3d90e226e19de4cfa63b09fb38) (uint32\_t in\_dwMinValue, uint32\_t in\_dwMaxValue)=0 |
|  | Should be called at the beginning of the operation to set the min and max value [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_i_progress_af8e34a3d90e226e19de4cfa63b09fb38.html#af8e34a3d90e226e19de4cfa63b09fb38) |
|  | |
| virtual void | [NotifyProgress](class_a_k_1_1_wwise_1_1_plugin_1_1_i_progress_a60e742bd2d53086e978e45c62a1415d1.html#a60e742bd2d53086e978e45c62a1415d1) (uint32\_t in\_dwProgress)=0 |
|  | Notify of the advancement of the task. [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_i_progress_a60e742bd2d53086e978e45c62a1415d1.html#a60e742bd2d53086e978e45c62a1415d1) |
|  | |
| virtual bool | [IsCancelled](class_a_k_1_1_wwise_1_1_plugin_1_1_i_progress_a17958067a0608c0bbd4fc1556b7f8767.html#a17958067a0608c0bbd4fc1556b7f8767) () const =0 |
|  | Check if the user has cancelled the task [更多...](class_a_k_1_1_wwise_1_1_plugin_1_1_i_progress_a17958067a0608c0bbd4fc1556b7f8767.html#a17958067a0608c0bbd4fc1556b7f8767) |
|  | |
| virtual void | [ErrorMessage](class_a_k_1_1_wwise_1_1_plugin_1_1_i_progress_a8e380c8480d74520139fbeffca5b9089.html#a8e380c8480d74520139fbeffca5b9089) (const char \*in\_rErrorText, [Severity](namespace_a_k_1_1_wwise_1_1_plugin_a9c61cf9f6b1cb69de3722982150b67ed.html#a9c61cf9f6b1cb69de3722982150b67ed) in\_eSeverity=[Severity\_Warning](namespace_a_k_1_1_wwise_1_1_plugin_a9c61cf9f6b1cb69de3722982150b67ed.html#a9c61cf9f6b1cb69de3722982150b67eda35f7fb0c5c0a59246ed922eb6af25794))=0 |
|  | |

## 详细描述

在文件 [PluginDef.h](_plugin_def_8h_source.html) 第 [154](_plugin_def_8h_source.html#l00154) 行定义.