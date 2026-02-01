# IFileOperationResult

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [ISourceControl](class_a_k_1_1_wwise_1_1_i_source_control.html)
- [IFileOperationResult](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_file_operation_result.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_file_operation_result-members.html) |
[Public 成员函数](#pub-methods)

AK.Wwise::ISourceControl::IFileOperationResult类 参考abstract

`#include <ISourceControl.h>`

类 AK.Wwise::ISourceControl::IFileOperationResult 继承关系图:

![](../../../../../../images/class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_file_operation_result.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual void | [GetMovedFile](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_file_operation_result_a33726538aaac562be5b32de46f18b34e.html#a33726538aaac562be5b32de46f18b34e) (unsigned int in\_uiIndex, LPWSTR out\_szFrom, LPWSTR out\_szTo, unsigned int in\_uiArraySize)=0 |
|  | Return the move source and destination for the file at index in\_uiIndex [更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_file_operation_result_a33726538aaac562be5b32de46f18b34e.html#a33726538aaac562be5b32de46f18b34e) |
|  | |
| virtual void | [GetFile](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_file_operation_result_ae68be19e4a417667d831affe84f73e51.html#ae68be19e4a417667d831affe84f73e51) (unsigned int in\_uiIndex, LPWSTR out\_szPath, unsigned int in\_uiArraySize)=0 |
|  | Return the successful file at index in\_uiIndex [更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_file_operation_result_ae68be19e4a417667d831affe84f73e51.html#ae68be19e4a417667d831affe84f73e51) |
|  | |
| virtual unsigned int | [GetFileCount](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_file_operation_result_a1a0a60903c3186af3a59292d3e6e82df.html#a1a0a60903c3186af3a59292d3e6e82df) ()=0 |
|  | Returns how many files were moved during the operation [更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_file_operation_result_a1a0a60903c3186af3a59292d3e6e82df.html#a1a0a60903c3186af3a59292d3e6e82df) |
|  | |
| - Public 成员函数 继承自 [AK.Wwise::ISourceControl::IOperationResult](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_operation_result.html) | |
| virtual [OperationResult](class_a_k_1_1_wwise_1_1_i_source_control_acf444a7a6671eacbee4a2a29aeb82286.html#acf444a7a6671eacbee4a2a29aeb82286) | [GetOperationResult](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_operation_result_a8725526d5081903361ef47fed2c9a3f9.html#a8725526d5081903361ef47fed2c9a3f9) ()=0 |
|  | Returns OperationResult\_Succeed or OperationResult\_Failed [更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_operation_result_a8725526d5081903361ef47fed2c9a3f9.html#a8725526d5081903361ef47fed2c9a3f9) |
|  | |
| virtual void | [Destroy](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_operation_result_a4ddcac159063a4bdb0310d5175283187.html#a4ddcac159063a4bdb0310d5175283187) ()=0 |
|  | Implementations should call "delete this;". [更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_operation_result_a4ddcac159063a4bdb0310d5175283187.html#a4ddcac159063a4bdb0310d5175283187) |
|  | |

## 详细描述

The result returned by DoOperation for a Move, Rename or Delete operation. An instance of this class is allocated by the plugin and freed by [Wwise](namespace_a_k_1_1_wwise.html). The operation ID must be identified by : [PluginInfo::m\_dwMoveCommandID](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_aec77a60a22f4960b0e222e13a9583361.html#aec77a60a22f4960b0e222e13a9583361 "Indicates the command ID for the Move command, s_dwInvalidOperationID (-1) if not supported"), [PluginInfo::m\_dwMoveNoUICommandID](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_a8a31d2194891dcc57b2d633f42aa746a.html#a8a31d2194891dcc57b2d633f42aa746a "Indicates the command ID for the Move command, showing no User Interface, s_dwInvalidOperationID (-1)..."), [PluginInfo::m\_dwRenameCommandID](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_adfa06e905971c7b871d8acbd553d80aa.html#adfa06e905971c7b871d8acbd553d80aa "Indicates the command ID for the Rename command, s_dwInvalidOperationID (-1) if not supported") or [PluginInfo::m\_dwRenameNoUICommandID](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_a755709add59549c396cd6553135fdd8a.html#a755709add59549c396cd6553135fdd8a "Indicates the command ID for the Rename command, showing no User Interface, s_dwInvalidOperationID (-...") [PluginInfo::m\_dwDeleteCommandID](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_a8e526f939e68b77247562571376644c5.html#a8e526f939e68b77247562571376644c5 "Indicates the command ID for the Delete command, s_dwInvalidOperationID (-1) if not supported") or [PluginInfo::m\_dwDeleteNoUICommandID](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info_af78e363e34c7fce88c6b5484f95c0e59.html#af78e363e34c7fce88c6b5484f95c0e59 "Indicates the command ID for the Delete command, showing no User Interface, s_dwInvalidOperationID (-...")

在文件 [ISourceControl.h](_i_source_control_8h_source.html) 第 [125](_i_source_control_8h_source.html#l00125) 行定义.