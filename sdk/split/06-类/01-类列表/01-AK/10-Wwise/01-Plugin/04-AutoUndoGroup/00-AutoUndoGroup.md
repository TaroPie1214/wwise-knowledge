# AutoUndoGroup

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [AutoUndoGroup](class_a_k_1_1_wwise_1_1_plugin_1_1_auto_undo_group.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_plugin_1_1_auto_undo_group-members.html) |
[Public 成员函数](#pub-methods) |
[Public 属性](#pub-attribs)

AK.Wwise::Plugin::AutoUndoGroup类 参考final

`#include <HostUndoManager.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AutoUndoGroup](class_a_k_1_1_wwise_1_1_plugin_1_1_auto_undo_group_a469c97c03b450a5c39790aee9044bf9f.html#a469c97c03b450a5c39790aee9044bf9f) ([UndoManager](namespace_a_k_1_1_wwise_1_1_plugin_a008216afc33ce6343231fe12ce496a4b.html#a008216afc33ce6343231fe12ce496a4b) &in\_undoManager, const char \*in\_applyEventName=nullptr, [ak\_wwise\_plugin\_undo\_group\_id](group__global_gaa45e88025407465159f485763021d524.html#gaa45e88025407465159f485763021d524) \*in\_reopenGroupId=nullptr, [ak\_wwise\_plugin\_undo\_group\_close\_action](group__global_ga49b0af3e4205b935aa476d7ab1c9f65c.html#ga49b0af3e4205b935aa476d7ab1c9f65c) in\_closeAction=[AK\_WWISE\_PLUGIN\_UNDO\_GROUP\_CLOSE\_ACTION\_APPLY](group__global_ga49b0af3e4205b935aa476d7ab1c9f65c.html#gga49b0af3e4205b935aa476d7ab1c9f65ca7b066ecc400936abe8602ec9deb27e5f)) |
|  | |
|  | [~AutoUndoGroup](class_a_k_1_1_wwise_1_1_plugin_1_1_auto_undo_group_ad77a63ea716947bdd30495f3ada86aa1.html#ad77a63ea716947bdd30495f3ada86aa1) () |
|  | |
| void | [Cancel](class_a_k_1_1_wwise_1_1_plugin_1_1_auto_undo_group_a952b7fa6bbdecd68ce81d20b8b4201ca.html#a952b7fa6bbdecd68ce81d20b8b4201ca) () |
|  | |
| void | [DontApply](class_a_k_1_1_wwise_1_1_plugin_1_1_auto_undo_group_ad531267f76333d51d7c300da0aa90a89.html#ad531267f76333d51d7c300da0aa90a89) () |
|  | |
| bool | [IsValid](class_a_k_1_1_wwise_1_1_plugin_1_1_auto_undo_group_a31bc7ec516283d9bd42f28af2a136b0d.html#a31bc7ec516283d9bd42f28af2a136b0d) () |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| [UndoManager](namespace_a_k_1_1_wwise_1_1_plugin_a008216afc33ce6343231fe12ce496a4b.html#a008216afc33ce6343231fe12ce496a4b) & | [m\_undoManager](class_a_k_1_1_wwise_1_1_plugin_1_1_auto_undo_group_ae7b0aabb2f9eef461a33e8b733472110.html#ae7b0aabb2f9eef461a33e8b733472110) |
|  | |
| char \* | [m\_applyEventName](class_a_k_1_1_wwise_1_1_plugin_1_1_auto_undo_group_a433191f2de5a2f0c1a6a9c41b33b8aab.html#a433191f2de5a2f0c1a6a9c41b33b8aab) |
|  | |
| [ak\_wwise\_plugin\_undo\_group\_id](group__global_gaa45e88025407465159f485763021d524.html#gaa45e88025407465159f485763021d524) | [m\_groupId](class_a_k_1_1_wwise_1_1_plugin_1_1_auto_undo_group_a28a20fdc910baeed86fcda3160bc03a1.html#a28a20fdc910baeed86fcda3160bc03a1) |
|  | |
| [ak\_wwise\_plugin\_undo\_group\_id](group__global_gaa45e88025407465159f485763021d524.html#gaa45e88025407465159f485763021d524) \* | [m\_reopenGroupId](class_a_k_1_1_wwise_1_1_plugin_1_1_auto_undo_group_ac9367104e6a94dd3714973f8ff13d4e9.html#ac9367104e6a94dd3714973f8ff13d4e9) |
|  | |
| [ak\_wwise\_plugin\_undo\_group\_close\_action](group__global_ga49b0af3e4205b935aa476d7ab1c9f65c.html#ga49b0af3e4205b935aa476d7ab1c9f65c) | [m\_closeAction](class_a_k_1_1_wwise_1_1_plugin_1_1_auto_undo_group_ace286ace1e8349ed2d5862a96d4fa754.html#ace286ace1e8349ed2d5862a96d4fa754) |
|  | |
| bool | [m\_valid](class_a_k_1_1_wwise_1_1_plugin_1_1_auto_undo_group_a1fe8bd027590d91de2ae5eab84ed719d.html#a1fe8bd027590d91de2ae5eab84ed719d) |
|  | |

## 详细描述

在文件 [HostUndoManager.h](_host_undo_manager_8h_source.html) 第 [659](_host_undo_manager_8h_source.html#l00659) 行定义.