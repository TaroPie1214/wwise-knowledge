# ISourceControlUtilities

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [ISourceControlUtilities](class_a_k_1_1_wwise_1_1_i_source_control_utilities.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_i_source_control_utilities-members.html) |
[Public 成员函数](#pub-methods)

AK.Wwise::ISourceControlUtilities类 参考abstract

`#include <ISourceControlUtilities.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual [ISourceControlProgress](class_a_k_1_1_wwise_1_1_i_source_control_progress.html) \* | [GetProgress](class_a_k_1_1_wwise_1_1_i_source_control_utilities_a0d837ea57c43632efa5cd56010943ad5.html#a0d837ea57c43632efa5cd56010943ad5) ()=0 |
|  | |
| virtual int | [MessageBox](class_a_k_1_1_wwise_1_1_i_source_control_utilities_a736122aef2131361b82063d4a43b765e.html#a736122aef2131361b82063d4a43b765e) (HWND in\_hWnd, LPCWSTR in\_pszText, LPCWSTR in\_pszCaption, UINT in\_uiType)=0 |
|  | |
| virtual int | [PromptMessage](class_a_k_1_1_wwise_1_1_i_source_control_utilities_ac4b40e38b05dbfc51c180b5b1632eaae.html#ac4b40e38b05dbfc51c180b5b1632eaae) (HWND in\_hWnd, LPCWSTR in\_pszText, LPCWSTR in\_pszCaption, LPWSTR out\_pszInput, UINT in\_uiInputSize, bool in\_bIsPassword)=0 |
|  | |
| virtual bool | [ShowBrowseForFolderDialog](class_a_k_1_1_wwise_1_1_i_source_control_utilities_ae593965f847137f09f75b11d7bf91a8c.html#ae593965f847137f09f75b11d7bf91a8c) (LPCWSTR in\_pszDialogTitle, LPWSTR out\_pszChoosenPath, UINT in\_uiChoosenPathSize, LPCWSTR in\_pszRootPath=NULL)=0 |
|  | |
| virtual INT\_PTR | [CreateModalCustomDialog](class_a_k_1_1_wwise_1_1_i_source_control_utilities_a6e7f5369fce4769309e2ba6fe5ed72d1.html#a6e7f5369fce4769309e2ba6fe5ed72d1) ([ISourceControlDialogBase](class_a_k_1_1_wwise_1_1_i_source_control_dialog_base.html) \*in\_pDialog)=0 |
|  | |
| virtual void | [SetUserPreferenceDword](class_a_k_1_1_wwise_1_1_i_source_control_utilities_ab4a564b8752876d3aedf7c43c3b41eed.html#ab4a564b8752876d3aedf7c43c3b41eed) (LPCWSTR in\_pszPreference, DWORD in\_dwValue)=0 |
|  | |
| virtual void | [GetUserPreferenceDword](class_a_k_1_1_wwise_1_1_i_source_control_utilities_a65ae7949058398550b9441c71089dd98.html#a65ae7949058398550b9441c71089dd98) (LPCWSTR in\_pszPreference, DWORD &io\_dwValue)=0 |
|  | |
| virtual void | [SetUserPreferenceString](class_a_k_1_1_wwise_1_1_i_source_control_utilities_a1f4161986adb0344b5acfcb1401fb8eb.html#a1f4161986adb0344b5acfcb1401fb8eb) (LPCWSTR in\_pszPreference, LPCWSTR in\_pszValue)=0 |
|  | |
| virtual void | [GetUserPreferenceString](class_a_k_1_1_wwise_1_1_i_source_control_utilities_a86d685e72df0da42dd2debeb5bfd41c3.html#a86d685e72df0da42dd2debeb5bfd41c3) (LPCWSTR in\_pszPreference, LPWSTR io\_pszValue, DWORD in\_dwSize)=0 |
|  | |
| virtual void | [GetMoveRootPath](class_a_k_1_1_wwise_1_1_i_source_control_utilities_aa0714958ba23eb129942028862f7bdcd.html#aa0714958ba23eb129942028862f7bdcd) (LPCWSTR in\_pszFullPath, LPWSTR out\_pszRootPath, UINT in\_uiRootPathSize)=0 |
|  | |
| virtual void | [CreateFileStatusListControl](class_a_k_1_1_wwise_1_1_i_source_control_utilities_ad787cd994fad6357513153b544e6e487.html#ad787cd994fad6357513153b544e6e487) (HWND in\_hWndParent, UINT in\_idStatic, const WCHAR \*\*in\_ppFilenameList, unsigned int in\_uiFilenameListCount)=0 |
|  | |
| virtual bool | [IsCancelRequested](class_a_k_1_1_wwise_1_1_i_source_control_utilities_a8055bf50361187af75764c0b63e60fc6.html#a8055bf50361187af75764c0b63e60fc6) () const =0 |
|  | |
| virtual void | [LogMessage](class_a_k_1_1_wwise_1_1_i_source_control_utilities_a7458275d1a2e65d82a2b338c1bbe9748.html#a7458275d1a2e65d82a2b338c1bbe9748) (LPCWSTR in\_pszMessage)=0 |
|  | |

## 详细描述

[Wwise](namespace_a_k_1_1_wwise.html) source control utilities interface. This interface is provided when the plug-in is initialized. With this interface, you can display a progress dialog, create custom dialogs, display message boxes, and save the plug-in configuration to the registry.

在文件 [ISourceControlUtilities.h](_i_source_control_utilities_8h_source.html) 第 [48](_i_source_control_utilities_8h_source.html#l00048) 行定义.