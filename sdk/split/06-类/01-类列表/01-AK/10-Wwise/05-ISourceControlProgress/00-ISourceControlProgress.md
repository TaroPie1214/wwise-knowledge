# ISourceControlProgress

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [ISourceControlProgress](class_a_k_1_1_wwise_1_1_i_source_control_progress.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_i_source_control_progress-members.html) |
[Public 类型](#pub-types) |
[Public 成员函数](#pub-methods)

AK.Wwise::ISourceControlProgress类 参考abstract

`#include <ISourceControlProgress.h>`

|  |  |
| --- | --- |
| Public 类型 | |
| enum | [Severity](class_a_k_1_1_wwise_1_1_i_source_control_progress_a0890a232f77c873c71ae053933ea6cfa.html#a0890a232f77c873c71ae053933ea6cfa) { [Severity\_Info](class_a_k_1_1_wwise_1_1_i_source_control_progress_a0890a232f77c873c71ae053933ea6cfa.html#a0890a232f77c873c71ae053933ea6cfaa4887ebd38c687d9e5ffa9daa831a1696), [Severity\_Warning](class_a_k_1_1_wwise_1_1_i_source_control_progress_a0890a232f77c873c71ae053933ea6cfa.html#a0890a232f77c873c71ae053933ea6cfaa980a9194c243c4131777307bc00220a1), [Severity\_Error](class_a_k_1_1_wwise_1_1_i_source_control_progress_a0890a232f77c873c71ae053933ea6cfa.html#a0890a232f77c873c71ae053933ea6cfaabb354f9586f0710c21f58044ee3e3b08) } |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual void | [BeginOperation](class_a_k_1_1_wwise_1_1_i_source_control_progress_a09b79a53feb4d2122bddfcef8935b08c.html#a09b79a53feb4d2122bddfcef8935b08c) ()=0 |
|  | Creates and displays the progress dialog. [更多...](class_a_k_1_1_wwise_1_1_i_source_control_progress_a09b79a53feb4d2122bddfcef8935b08c.html#a09b79a53feb4d2122bddfcef8935b08c) |
|  | |
| virtual void | [AddLogMessage](class_a_k_1_1_wwise_1_1_i_source_control_progress_abd15c23f394c64d24d02af13b637d270.html#abd15c23f394c64d24d02af13b637d270) ([Severity](class_a_k_1_1_wwise_1_1_i_source_control_progress_a0890a232f77c873c71ae053933ea6cfa.html#a0890a232f77c873c71ae053933ea6cfa) in\_severity, LPCWSTR in\_pszMessage)=0 |
|  | |
| virtual bool | [IsCanceled](class_a_k_1_1_wwise_1_1_i_source_control_progress_aee296e50c7c4eb64a8a17552b83b88e0.html#aee296e50c7c4eb64a8a17552b83b88e0) () const =0 |
|  | |
| virtual void | [Cancel](class_a_k_1_1_wwise_1_1_i_source_control_progress_ad5e4ad7a680e12b640a5344dd121d842.html#ad5e4ad7a680e12b640a5344dd121d842) ()=0 |
|  | |
| virtual void | [EndOperation](class_a_k_1_1_wwise_1_1_i_source_control_progress_ac634d468eb39fb1a6069c050f5acd92e.html#ac634d468eb39fb1a6069c050f5acd92e) (bool in\_bWaitForOK=true)=0 |
|  | |
| virtual bool | [IsSilent](class_a_k_1_1_wwise_1_1_i_source_control_progress_af1692b1c0a011738dc5eb64a76a0f3dd.html#af1692b1c0a011738dc5eb64a76a0f3dd) () const =0 |
|  | |
| virtual bool | [IsAutoCheckout](class_a_k_1_1_wwise_1_1_i_source_control_progress_aeb3e8bc266f52546385310c101d0980b.html#aeb3e8bc266f52546385310c101d0980b) () const =0 |
|  | |
| virtual bool | [IsAutoAdd](class_a_k_1_1_wwise_1_1_i_source_control_progress_a2d2f6809f75b7b897d6f6619141cc1d5.html#a2d2f6809f75b7b897d6f6619141cc1d5) () const =0 |
|  | |
| virtual LPCWSTR | [GetCommitMessage](class_a_k_1_1_wwise_1_1_i_source_control_progress_a9b1e5ba7e9d8a4880c50573a8f7eef66.html#a9b1e5ba7e9d8a4880c50573a8f7eef66) () const =0 |
|  | |

## 详细描述

[Wwise](namespace_a_k_1_1_wwise.html) progress dialog interface. This interface is given by [AK::Wwise::ISourceControlUtilities](class_a_k_1_1_wwise_1_1_i_source_control_utilities.html). You can use this interface to display a simple progress dialog while performing operations.

|  |  |
| --- | --- |
|  | **警告:** The functions in this interface are not thread-safe, unless stated otherwise. |

参见
:   - [实现版本控制操作进度接口](source_control_dll.html#source_control_dll_creation_progress)

在文件 [ISourceControlProgress.h](_i_source_control_progress_8h_source.html) 第 [48](_i_source_control_progress_8h_source.html#l00048) 行定义.