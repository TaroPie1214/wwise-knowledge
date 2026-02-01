# Dialogue Event Editor 视图

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Project Explorer](../00-Project-Explorer.md) > [Events 选项卡](00-Events-选项卡.md) > Dialogue Event Editor 视图

### Dialogue Event Editor 视图

在 Dialogue Event Editor（对白事件编辑器）中，您可以排列和组合状态或切换开关来创建不同“路径”，用于在游戏中动态选择要播放哪个单词或词组。在该编辑器中，可添加并排列想要包含在 Event 中的 State Group（状态组）或 Switch Group（切换开关组）。随后可以选择状态或切换开关的不同组合来定义路径，每条路径可以与一个特定声部或声音对象相关联。在运行时，声音引擎会根据预定义路径来匹配触发的 State 或 Switch，以便确定要播放哪个声音。您还可以使用权重值来决定特定路径被选择的可能性高低。

| 界面元素 | 描述 |
| --- | --- |
| Name | Dialogue Event 的名称。 |
| Notes | 备注。与 Dialogue Event 有关的附加信息。 |
| **Settings（设置）** | |
| Probability | 概率。使用该路径播放音频的可能性。  最终的播放概率是所选路径概率和对白事件概率的组合。  单位：%  Default value: 100  Range: 0 to 100 |
|  | 创建完整的通用路径（\*.\*），来适用任意状态或切换开关。  此选项仅在通用路径尚不存在时才可用。 |
|  | 适用所选的状态/切换开关组或状态/切换开关值创建路径。 |
|  | 更新路径。针对所选音频对象更新路径。此选项会将所选对象的路径替换为当前选择的状态或切换开关。  此选项仅在所选路径尚未出现在列表中，并且在列表中选择了一个对象时才可用。 |
|  | 从路径列表中删除所选路径。 |
|  | 取消选中窗格中的所有状态和切换开关。 |
| （State/Switch 窗格） | 显示已分配给当前所选 Dialogue Event 的 State Group 和 Switch Group。您可以选择不同的状态或切换开关，来创建不同路径组合。 |
|  | 打开可让用户从备选 Switch Group 或 State Group 对象列表中进行选择的菜单。The user may also create a new State Group or Switch Group from this menu by selecting "New". |
| Mode | 模式。在运行时触发的状态或切换开关有不只一条预定义路径可以匹配的情况下，指定声音引擎将选择哪条路径。  - **Best Match** – 最佳匹配。选择与运行时触发的状态或切换开关最匹配的路径。如果不能完全匹配，则将会选择具有最少通配符 (\*) 的路径。 - **Weighted** – 加权。基于各路径的权重值，随机选择匹配路径之一。  因为在路径中可以使用通配符（\*），所以可能同时有几条预定义的路径都能够匹配在运行时触发的状态或切换开关。  Default value: Best Match |
| Path Filter | 路径筛选器。显示可用于筛选路径的列表。可以使用以下筛选器：  - **All** -- 所有。显示所有已创建的路径。 - **Current Selection** -- 当前选中项。仅显示包含所选切换开关或状态的路径。 |
| Object Filter | 路径筛选器。显示可用于筛选路径的列表。可以使用以下筛选器：  - **All** -- 所有。显示所有已创建的路径。 - **Assigned object** -- 指派对象。仅显示与对象关联的路径。 - **Missing** -- 缺失。仅显示与已删除的对象相关联的路径。 - **None** -- 无。仅显示未与对象进行关联的路径。 |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Path | 路径。路径是对白事件中一组切换开关或状态的特定组合。这些路径将与声部或声音对象相关联。  路径可能包含通配符，这将匹配任何相应的 Switch 或 State。通配符由星号表示。 |
| Probability | 概率。使用该路径播放音频的可能性。  最终的播放概率是所选路径概率和对白事件概率的组合。  单位：%  Default value: 100  Range: 0 to 100 |
| Weight | 权重。当存在其它匹配路径的情况下，该路径被选择的可能性。  在一条匹配路径的权重为 100 时，其它权重低于 100 的匹配路径会被自动弃用。在一条配路径的权重为 0 时，除非其它所有匹配路径的权重也都为 0，否则该路径会被弃用。  此选项仅在 Dialogue Event 处于“Weighted”模式时才适用。  单位：%  Default value: 50  Range: 0 to 100 |
| Object（对象） | 指派给路径的对象。  可以将指派给路径的对象与其它平台断开链接，以便为相同路径根据不同平台来指派不同的对象。 |
| (浏览) | 浏览。打开Project Explorer - Browser（工程浏览器 —— 浏览器），可以在其中选择将指派给此路径的对象。  您还可以直接从 Project Explorer 中拖拽对象。 |

**相关主题**

- [“创建新的 Dialogue Event”一节](../../../04-与游戏互动/02-管理动态对话/01-创建-Dialogue-Event/01-创建新的-Dialogue-Event.md "创建新的 Dialogue Event")
- [“将 State Group 添加到 Dialogue Event”一节](../../../04-与游戏互动/02-管理动态对话/01-创建-Dialogue-Event/03-将-State-Group-添加到-Dialogue-Event.md "将 State Group 添加到 Dialogue Event")
- [“利用 State 创建路径”一节](../../../04-与游戏互动/02-管理动态对话/01-创建-Dialogue-Event/04-使用-Path-重现游戏中的条件.md#creating_paths_using_states "利用 State 创建路径")
- [“创建后备路径”一节](../../../04-与游戏互动/02-管理动态对话/01-创建-Dialogue-Event/04-使用-Path-重现游戏中的条件.md#creating_fallback_paths "创建后备路径")
- [“筛选路径列表”一节](../../../04-与游戏互动/02-管理动态对话/01-创建-Dialogue-Event/05-将对象指派给路径.md#filtering_path_list "筛选路径列表")
- [“为路径设置概率和权重”一节](../../../04-与游戏互动/02-管理动态对话/01-创建-Dialogue-Event/06-为路径设置概率和权重.md "为路径设置概率和权重")
- [“将对象指派给路径”一节](../../../04-与游戏互动/02-管理动态对话/01-创建-Dialogue-Event/05-将对象指派给路径.md "将对象指派给路径")
- [“对 Dialogue Event 中的 State Group 重新排序”一节](../../../04-与游戏互动/02-管理动态对话/02-处理-Dialogue-Event.md#re_ordering_state_groups_in_dialogue_event "对 Dialogue Event 中的 State Group 重新排序")
- [“从 Dialogue Event 中移除 State Group”一节](../../../04-与游戏互动/02-管理动态对话/02-处理-Dialogue-Event.md#removing_state_groups_from_dialogue_event "从 Dialogue Event 中移除 State Group")
- [“播放 Dialogue Event 内的对象”一节](../../../04-与游戏互动/02-管理动态对话/02-处理-Dialogue-Event.md#playing_back_objects_within_dialogue_event "播放 Dialogue Event 内的对象")

---