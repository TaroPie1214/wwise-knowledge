# ISourceControlDialogBase

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [ISourceControlDialogBase](class_a_k_1_1_wwise_1_1_i_source_control_dialog_base.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_i_source_control_dialog_base-members.html) |
[Public 成员函数](#pub-methods)

AK.Wwise::ISourceControlDialogBase类 参考abstract

`#include <ISourceControlDialogBase.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual HINSTANCE | [GetResourceHandle](class_a_k_1_1_wwise_1_1_i_source_control_dialog_base_a32a21b3e259526ad996d00ac946ca30f.html#a32a21b3e259526ad996d00ac946ca30f) () const =0 |
|  | |
| virtual void | [GetDialog](class_a_k_1_1_wwise_1_1_i_source_control_dialog_base_ac2e9e65eb75db832fc7ced9a398b1f4c.html#ac2e9e65eb75db832fc7ced9a398b1f4c) (UINT &out\_uiDialogID) const =0 |
|  | This function is called by [Wwise](namespace_a_k_1_1_wwise.html) to get the plug-in dialog's ID. [更多...](class_a_k_1_1_wwise_1_1_i_source_control_dialog_base_ac2e9e65eb75db832fc7ced9a398b1f4c.html#ac2e9e65eb75db832fc7ced9a398b1f4c) |
|  | |
| virtual bool | [HasHelp](class_a_k_1_1_wwise_1_1_i_source_control_dialog_base_a8efe7c9ea503058b2acbf848e680245f.html#a8efe7c9ea503058b2acbf848e680245f) () const =0 |
|  | |
| virtual bool | [Help](class_a_k_1_1_wwise_1_1_i_source_control_dialog_base_a40fff8f04f4b6532f9a21c1b794a5106.html#a40fff8f04f4b6532f9a21c1b794a5106) (HWND in\_hWnd) const =0 |
|  | |
| virtual bool | [WindowProc](class_a_k_1_1_wwise_1_1_i_source_control_dialog_base_afc8ab1f13cc6f3be3b423bb58597d4e3.html#afc8ab1f13cc6f3be3b423bb58597d4e3) (HWND in\_hWnd, UINT in\_message, WPARAM in\_wParam, LPARAM in\_lParam, LRESULT &out\_lResult)=0 |
|  | |

## 详细描述

[Wwise](namespace_a_k_1_1_wwise.html) dialog base interface. This must be implemented for each dialog that needs to be displayed with the [Wwise](namespace_a_k_1_1_wwise.html) look and feel.

|  |  |
| --- | --- |
|  | **警告:** The functions in this interface are not thread-safe, unless stated otherwise. |

参见
:   - [启用对话框](source_control_dll.html#source_control_dll_creation_dialog_implement)

在文件 [ISourceControlDialogBase.h](_i_source_control_dialog_base_8h_source.html) 第 [48](_i_source_control_dialog_base_8h_source.html#l00048) 行定义.