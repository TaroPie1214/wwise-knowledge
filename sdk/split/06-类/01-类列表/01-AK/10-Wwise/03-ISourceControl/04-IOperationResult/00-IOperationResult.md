# IOperationResult

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [ISourceControl](class_a_k_1_1_wwise_1_1_i_source_control.html)
- [IOperationResult](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_operation_result.html)

[所有成员列表](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_operation_result-members.html) |
[Public 成员函数](#pub-methods)

AK.Wwise::ISourceControl::IOperationResult类 参考abstract

The base interface for operations that return information to [Wwise](namespace_a_k_1_1_wwise.html)
[更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_operation_result.html#details)

`#include <ISourceControl.h>`

类 AK.Wwise::ISourceControl::IOperationResult 继承关系图:

![](../../../../../../images/class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_operation_result.png)

|  |  |
| --- | --- |
| Public 成员函数 | |
| virtual [OperationResult](class_a_k_1_1_wwise_1_1_i_source_control_acf444a7a6671eacbee4a2a29aeb82286.html#acf444a7a6671eacbee4a2a29aeb82286) | [GetOperationResult](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_operation_result_a8725526d5081903361ef47fed2c9a3f9.html#a8725526d5081903361ef47fed2c9a3f9) ()=0 |
|  | Returns OperationResult\_Succeed or OperationResult\_Failed [更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_operation_result_a8725526d5081903361ef47fed2c9a3f9.html#a8725526d5081903361ef47fed2c9a3f9) |
|  | |
| virtual void | [Destroy](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_operation_result_a4ddcac159063a4bdb0310d5175283187.html#a4ddcac159063a4bdb0310d5175283187) ()=0 |
|  | Implementations should call "delete this;". [更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_operation_result_a4ddcac159063a4bdb0310d5175283187.html#a4ddcac159063a4bdb0310d5175283187) |
|  | |

## 详细描述

The base interface for operations that return information to [Wwise](namespace_a_k_1_1_wwise.html)

在文件 [ISourceControl.h](_i_source_control_8h_source.html) 第 [109](_i_source_control_8h_source.html#l00109) 行定义.