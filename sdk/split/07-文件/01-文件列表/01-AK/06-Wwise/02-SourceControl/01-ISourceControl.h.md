# ISourceControl.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Wwise](dir_6ea5b71cdf4c60d3386ed2d84846331f.html)
- [SourceControl](dir_c4fbb2e488221d2fb2602d6a1be17d65.html)

[类](#nested-classes) |
[命名空间](#namespaces)

ISourceControl.h 文件参考

`#include <wtypes.h>`  
`#include "ISourceControlUtilities.h"`  
`#include "SourceControlContainers.h"`

[浏览源代码.](_i_source_control_8h_source.html)

|  |  |
| --- | --- |
| 类 | |
| class | [AK.Wwise::SourceControlConstant](class_a_k_1_1_wwise_1_1_source_control_constant.html) |
|  | This class contains static constants that can be useful to the plug-in. [更多...](class_a_k_1_1_wwise_1_1_source_control_constant.html#details) |
|  | |
| class | [AK.Wwise::ISourceControl](class_a_k_1_1_wwise_1_1_i_source_control.html) |
|  | |
| class | [AK.Wwise::ISourceControl::IOperationResult](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_operation_result.html) |
|  | The base interface for operations that return information to [Wwise](namespace_a_k_1_1_wwise.html) [更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_operation_result.html#details) |
|  | |
| class | [AK.Wwise::ISourceControl::IFileOperationResult](class_a_k_1_1_wwise_1_1_i_source_control_1_1_i_file_operation_result.html) |
|  | |
| struct | [AK.Wwise::ISourceControl::FilenameToStatusMapItem](struct_a_k_1_1_wwise_1_1_i_source_control_1_1_filename_to_status_map_item.html) |
|  | |
| struct | [AK.Wwise::ISourceControl::OperationListItem](struct_a_k_1_1_wwise_1_1_i_source_control_1_1_operation_list_item.html) |
|  | Operation list item. This is the type used in the [AK::Wwise::ISourceControl::OperationList](class_a_k_1_1_wwise_1_1_i_source_control_a252fa3e07c09cdc0327d6abfb6edef0e.html#a252fa3e07c09cdc0327d6abfb6edef0e) [SourceControlContainers::IAkList](class_a_k_1_1_wwise_1_1_source_control_containers_1_1_i_ak_list.html) template class. [更多...](struct_a_k_1_1_wwise_1_1_i_source_control_1_1_operation_list_item.html#details) |
|  | |
| struct | [AK.Wwise::ISourceControl::FilenameToIconMapItem](struct_a_k_1_1_wwise_1_1_i_source_control_1_1_filename_to_icon_map_item.html) |
|  | |
| class | [AK.Wwise::ISourceControl::PluginInfo](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info.html) |
|  | Plug-in information structure. This structure gives a simple overview of the plug-in's capabilities. [更多...](class_a_k_1_1_wwise_1_1_i_source_control_1_1_plugin_info.html#details) |
|  | |

|  |  |
| --- | --- |
| 命名空间 | |
| namespace | [AK](namespace_a_k.html) |
|  | Definition of data structures for [AkAudioObject](struct_ak_audio_object.html) |
|  | |
| namespace | [AK.Wwise](namespace_a_k_1_1_wwise.html) |
|  | |

## 详细描述

Wwise source control plug-in interface, used to implement the source control plug-in.

在文件 [ISourceControl.h](_i_source_control_8h_source.html) 中定义.