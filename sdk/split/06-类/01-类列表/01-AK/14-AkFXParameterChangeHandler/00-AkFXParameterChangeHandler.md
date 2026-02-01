# AkFXParameterChangeHandler

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [AkFXParameterChangeHandler](class_a_k_1_1_ak_f_x_parameter_change_handler.html)

[所有成员列表](class_a_k_1_1_ak_f_x_parameter_change_handler-members.html) |
[Public 成员函数](#pub-methods) |
[Protected 属性](#pro-attribs)

AK::AkFXParameterChangeHandler< T\_MAXNUMPARAMS > 模板类 参考

`#include <AkFXParameterChangeHandler.h>`

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | [AkFXParameterChangeHandler](class_a_k_1_1_ak_f_x_parameter_change_handler_aae9faea3112afa5898c055eddf876704.html#aae9faea3112afa5898c055eddf876704) () |
|  | |
| void | [SetParamChange](class_a_k_1_1_ak_f_x_parameter_change_handler_a5ebcd10be3825aedc339205b9f8aab53.html#a5ebcd10be3825aedc339205b9f8aab53) ([AkPluginParamID](_ak_typedefs_8h_a4cb8ff0b7014efdaa21697f4ef928926.html#a4cb8ff0b7014efdaa21697f4ef928926) in\_ID) |
|  | |
| bool | [HasChanged](class_a_k_1_1_ak_f_x_parameter_change_handler_ad38c0556e179b3da1a8f646113647b12.html#ad38c0556e179b3da1a8f646113647b12) ([AkPluginParamID](_ak_typedefs_8h_a4cb8ff0b7014efdaa21697f4ef928926.html#a4cb8ff0b7014efdaa21697f4ef928926) in\_ID) |
|  | |
| bool | [HasAnyChanged](class_a_k_1_1_ak_f_x_parameter_change_handler_a7e6159ddfc30fe859f399a94cbb9b757.html#a7e6159ddfc30fe859f399a94cbb9b757) () |
|  | |
| void | [ResetParamChange](class_a_k_1_1_ak_f_x_parameter_change_handler_a78ccf65fc62066b5de90bae4e17e8abe.html#a78ccf65fc62066b5de90bae4e17e8abe) ([AkPluginParamID](_ak_typedefs_8h_a4cb8ff0b7014efdaa21697f4ef928926.html#a4cb8ff0b7014efdaa21697f4ef928926) in\_ID) |
|  | |
| void | [ResetAllParamChanges](class_a_k_1_1_ak_f_x_parameter_change_handler_a2fbd9afd327b0a49aaee2f64f7bd2b7f.html#a2fbd9afd327b0a49aaee2f64f7bd2b7f) () |
|  | |
| void | [SetAllParamChanges](class_a_k_1_1_ak_f_x_parameter_change_handler_a8363e6442fc0574c4dbe25d8e552fe9f.html#a8363e6442fc0574c4dbe25d8e552fe9f) () |
|  | |

|  |  |
| --- | --- |
| Protected 属性 | |
| [AkUInt8](_ak_numeral_types_8h_a6a754f6e0ddd97ae59f3aae854cde270.html#a6a754f6e0ddd97ae59f3aae854cde270) | [m\_uParamBitArray](class_a_k_1_1_ak_f_x_parameter_change_handler_a2180146ada0a4df8779cc3735a2c02e7.html#a2180146ada0a4df8779cc3735a2c02e7) [(((T\_MAXNUMPARAMS)+((8) -1)) &~((8) -1))/8] |
|  | |

## 详细描述

### template<AkUInt32 T\_MAXNUMPARAMS> class AK::AkFXParameterChangeHandler< T\_MAXNUMPARAMS >

在文件 [AkFXParameterChangeHandler.h](_ak_f_x_parameter_change_handler_8h_source.html) 第 [40](_ak_f_x_parameter_change_handler_8h_source.html#l00040) 行定义.