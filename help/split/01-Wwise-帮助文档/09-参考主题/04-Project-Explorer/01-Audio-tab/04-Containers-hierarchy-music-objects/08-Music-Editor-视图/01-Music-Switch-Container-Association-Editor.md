# Music Switch Container Association Editor

[Wwise 帮助文档](../../../../../00-Wwise-帮助文档.md) > [参考主题](../../../../00-参考主题.md) > [Project Explorer](../../../00-Project-Explorer.md) > [Audio tab](../../00-Audio-tab.md) > [Containers hierarchy: music objects](../00-Containers-hierarchy-music-objects.md) > [Music Editor 视图](00-Music-Editor-视图.md) > Music Switch Container Association Editor

##### Music Switch Container Association Editor

在 Switch Container Association Editor（音乐切换容器关联编辑器）中，您可以排列和组合 State 或 Switch 来创建不同“路径”（Path），用于动态地确定在游戏中选择进行播放的一段音乐。在编辑器中，您可以添加并排列您希望执行所选音乐的不同 State Group 或 Switch Group。然后选择 State 或 Switch 的不同组合来定义路径，各条路径都可与特定音乐对象相关联。在运行时，声音引擎根据预定义的路径匹配当前 State 或 Switch，从而确定要播放的一段声音。您还可以使用权重值来决定特定路径被选择的可能性高低。

| 界面元素 | 描述 |
| --- | --- |
|  | 创建完整的通用路径（\*.\*），来适用任意状态或切换开关。  此选项仅在通用路径尚不存在时才可用。 |
|  | 适用所选的状态/切换开关组或状态/切换开关值创建路径。 |
|  | 更新路径。针对所选音频对象更新路径。此选项会将所选对象的路径替换为当前选择的 State 或 Switch。  此选项仅在所选路径尚未出现在列表中，并且在列表中选择了一个对象时才可用。 |
|  | 从路径列表中删除所选路径。 |
|  | 取消选中 States/Switches 窗格中的所有 State 和 Switch。 |
| （States/Switches 窗格） | 显示已分配给当前所选 Music Switch Container 的 State Group 和 Switch Group。您可以选择不同的状态或切换开关，来创建不同路径组合。 |
|  | 打开可让用户从备选 Switch Group 或 State Group 对象列表中进行选择的菜单。The user may also create a new State Group or Switch Group from this menu by selecting "New". |
| Mode | 模式。在运行时触发的状态或切换开关有不只一条预定义路径可以匹配的情况下，指定声音引擎将选择哪条路径。  - **Best Match** – 最佳匹配。选择与运行时触发的状态或切换开关最匹配的路径。如果不能完全匹配，则将会选择具有最少通配符 (\*) 的路径。 - **Weighted** – 加权。基于各路径的权重值，随机选择匹配路径之一。  因为在路径中可以使用通配符（\*），所以可能同时有几条预定义的路径都能够匹配在运行时触发的状态或切换开关。  Default value: Best Match |
| Path Filter | 路径筛选器。显示可用于筛选路径的列表。可以使用以下筛选器：  **All** -- 所有。显示所有已创建的路径。  **Current Selection** -- 当前选中项。仅显示包含所选切换开关或状态的路径。 |
| Object Filter | - 路径筛选器。显示可用于筛选路径的列表。可以使用以下筛选器： - **All** -- 所有。显示所有已创建的路径。 - **Assigned object** -- 指派对象。仅显示与对象关联的路径。 - **Missing** -- 缺失。仅显示与已删除的对象相关联的路径。 - **None** -- 无。仅显示未与对象进行关联的路径。 |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Path | 路径。包含 Music Switch Container 中可能存在的 Switch 或 State 的多种组合之一的特定路径。这些路径与音乐对象相关联。  路径可能包含通配符，这将匹配任何相应的 Switch 或 State。通配符由星号表示。 |
| Weight | 权重。当存在其它匹配路径的情况下，该路径被选择的可能性。  在一条匹配路径的权重为 100 时，其它权重低于 100 的匹配路径会被自动弃用。在一条配路径的权重为 0 时，除非其它所有匹配路径的权重也都为 0，否则该路径会被弃用。  此选项仅在 Dialogue Event 处于“Weighted”模式时才适用。  单位：%  Default value: 50  Range: 0 to 100 |
| Object（对象） | 指派给路径的对象。  可以将指派给路径的对象与其它平台断开链接，以便为相同路径根据不同平台来指派不同的对象。 |
| (浏览) | 浏览。打开Project Explorer - Browser（工程浏览器 —— 浏览器），可以在其中选择将指派给此路径的对象。  您还可以直接从 Project Explorer 中拖拽对象。 |

**相关主题**

- [“将音乐对象与 State 和 Switch 关联”一节](../../../../../06-创建互动音乐/03-定义音乐对象播放行为/03-定义-Music-Switch-Container-的内容和行为.md#associating_music_objects_with_states_and_or_switches "将音乐对象与 State 和 Switch 关联")
- [“将 Music Switch Container 与 Game Sync 关联”一节](../../../../../06-创建互动音乐/03-定义音乐对象播放行为/03-定义-Music-Switch-Container-的内容和行为.md#associating_music_switch_container_to_one_or_more_game_syncs "将 Music Switch Container 与 Game Sync 关联")
- [“定义 Music Switch Container 内各个音乐对象的行为”一节](../../../../../06-创建互动音乐/03-定义音乐对象播放行为/03-定义-Music-Switch-Container-的内容和行为.md#defining_behaviors_of_music_objects_within_music_switch_containers "定义 Music Switch Container 内各个音乐对象的行为")

---