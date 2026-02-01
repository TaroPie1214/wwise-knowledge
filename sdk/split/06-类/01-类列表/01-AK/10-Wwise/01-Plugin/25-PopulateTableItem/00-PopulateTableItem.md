# PopulateTableItem

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [Wwise](namespace_a_k_1_1_wwise.html)
- [Plugin](namespace_a_k_1_1_wwise_1_1_plugin.html)
- [PopulateTableItem](struct_a_k_1_1_wwise_1_1_plugin_1_1_populate_table_item.html)

[所有成员列表](struct_a_k_1_1_wwise_1_1_plugin_1_1_populate_table_item-members.html) |
[Public 属性](#pub-attribs)

AK.Wwise::Plugin::PopulateTableItem结构体 参考

`#include <PluginDef.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| uint32\_t | [uiID](struct_a_k_1_1_wwise_1_1_plugin_1_1_populate_table_item_abc706d9d6db2e1b4fde932b8216a721b.html#abc706d9d6db2e1b4fde932b8216a721b) |
|  | The dialog control resource ID [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_populate_table_item_abc706d9d6db2e1b4fde932b8216a721b.html#abc706d9d6db2e1b4fde932b8216a721b) |
|  | |
| const char \* | [pszProp](struct_a_k_1_1_wwise_1_1_plugin_1_1_populate_table_item_aa0eb647da5657f12c51362e9401fbe4a.html#aa0eb647da5657f12c51362e9401fbe4a) |
|  | The property name [更多...](struct_a_k_1_1_wwise_1_1_plugin_1_1_populate_table_item_aa0eb647da5657f12c51362e9401fbe4a.html#aa0eb647da5657f12c51362e9401fbe4a) |
|  | |

## 详细描述

Represents the association between a dialog control (such as a checkbox or radio button) and a plug-in property.

|  |  |
| --- | --- |
|  | **备注:** You should not need to use this structure directly. Instead, use the AK\_BEGIN\_POPULATE\_TABLE(), AK\_POP\_ITEM(), and AK\_END\_POPULATE\_TABLE() macros. |

参见
:   - [如何将常规控件绑定到属性](wwiseplugin_dialog_guide.html#wwiseplugin_dialog_guide_poptable)

在文件 [PluginDef.h](_plugin_def_8h_source.html) 第 [126](_plugin_def_8h_source.html#l00126) 行定义.