# Effects tab: Containers hierarchy objects

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [Audio tab](../00-Audio-tab.md) > [Common tabs and categories: audio structures](00-Common-tabs-and-categories-audio-structures.md) > Effects tab: Containers hierarchy objects

#### Effects tab: Containers hierarchy objects

Effects（效果器）选项卡允许将多达 255 个不同的效果器应用于对象。这些效果器将以它们出现在列表中的相同顺序来起作用。在将 Effect（效果器）应用于对象时，必须决定要应用哪种 Effect 类型、使用 ShareSet（共享集）还是自定义实例、是否渲染 Effect。此外，还可根据需要选择旁通 Effect。您可以随时单击 Edit（编辑）按钮来编辑效果器的属性。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| For information on the Busses object Effects tab, see [“Effects tab: busses”一节](../02-Busses-hierarchy/04-Common-tabs-and-categories-Busses-hierarchy-object/02-Effects-tab-busses.md "Effects tab: busses"). |

| General | |
| --- | --- |
| 界面元素 | 描述 |
| [name] | 对象的名称。 |
| (Object Color) | 显示对象的颜色。单击图标可打开颜色选择器。    选择一种颜色并将其应用于对象。在为对象选择某种颜色时，会在选定方块上显示调色板图标，并在右下角标注黄色三角（如图所示）。  若要沿用父对象的颜色，请选中颜色选择器最左侧的方块。 |
| (Mute and Solo) | 控制对象的 Mute（静音）和 Solo（单独播放）状态，也会显示该对象是否处于被动静音和 Solo 状态。  将对象静音会使其在当前监听中无法听到。让对象 Solo 会使工程中的所有其它对象无声。  粗体的 **M** 或 **S** 表明已为对象主动设置了 Mute 或 Solo 状态。褪色的非粗体 **M** 或 **S** 表明对象的 Mute 或 Solo 状态是由于其它对象状态而被动设置的。  将对象静音会让其子对象被动静音。  让对象 Solo 会使同级对象被动静音，并让子对象和父对象被动 Solo。  |  |  | | --- | --- | | [技巧] | 技巧 | | 在点击 Solo 按钮的同时按住 Ctrl 键，可以强制仅 Solo 该 Solo 按钮所在的对象。 |  |  |  | | --- | --- | | [备注] | 备注 | | Mute 和 Solo 仅用于监视目的，而不会保存在工程中或存储在 SoundBank（声音包）中。 | |
| (Show references) | 指示工程中有多少元素包含对对象的直接引用。若存在对对象的引用，则图标显示为橙色；若不存在此类引用，则图标显示为灰色。  通过单击该按钮，可打开 [“Reference View 视图”一节](../../12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")，并在 **References to:**（引用:）字段中查看对象的名称。 |

| Effects | |
| --- | --- |
| 界面元素 | 描述 |
| Override parent | 不沿用父项。确定所用效果器是从父项继承还是在层级结构的当前层级定义。不勾选此选项就用不了 Effects 选项。  如果对象是顶层对象，则 Override parent 选项将不可用。  Default value: false |
| **Effects** | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| （选择器） | 打开可应用于对象的一系列效果器及对应实例。若选择效果器，则其将替换之前占用插槽的效果器。  要删除效果器，请选择 **None**（无）选项。 |
| ID | 效果器的标识号。导流体 |
| Effect | 效果器。要应用于对象的效果器类型，如 Compressor、Matrix Reverb 或 Parametric EQ。 |
| Name | 名称。应用于对象的效果器实例的名称。效果器实例可以是 ShareSet 或 ShareSet 的自定义实例。  所选效果器类型的所有效果器实例都将显示在相应的列表中。 |
| Prev. | 上一个。选择 Effects 层级结构中的上一 ShareSet。 |
| Next | 下一个。选择 Effects 层级结构中的下一 ShareSet。 |
| Mode | 模式。确定是否共享效果器。模式可以是：  - **Define custom**（定义自定义）：创建其属性不在对象之间共享的自定义效果器实例。 - **Use ShareSets**（使用共享集）：使用效果器的 ShareSet，可在对象之间共享效果器属性。  |  |  | | --- | --- | | [备注] | 备注 | | 若添加自定义效果器，然后把 **Mode** 改为 **Use ShareSets**，将打开 Create ShareSet from Custom Object（通过自定义对象创建共享集）警告对话框。其设有三个选项：  - **Convert**（转码）：打开 New Effect（新建效果器）对话框，以便使用指定的效果器设置创建新的 ShareSet。 - **Revert**（还原）： 清除 Effect Editor 并将效果器还原为 ShareSet 的原始设置。 - **Cancel**（取消）：将 Mode 恢复为 Define custom，并返回未经修改的 Effect Editor。 | |
| Render | 渲染。决定是否在打包到 SoundBank 中之前渲染所选效果器实例。  在打包到 SoundBank 之前对效果器进行渲染可以节省游戏期间的运算消耗。然而，这也会限制游戏的互动性，因为在勾选了 Render 选项时就不能使用 RTPC 了。  Default value: false |
| Bypass | 旁通。决定是否旁通所选效果器实例。若选中复选框，则移除效果器。若取消选中复选框，则恢复使用效果器。  此选项在以下情况下非常有用：  - 在对游戏实施性能分析时，可启用或禁用此选项来确定效果器对声音设计及 Performance Monitor 中所示 CPU 用量的影响。 - 在按平台定制声音设计时，可取消链接对象上的效果器，并针对处理能力较弱的平台旁通该对象上的某些效果器。  另外，还可在 RTPC 中使用 Bypass 选项或在 Event 中使用 “Bypass Effect” Action 来针对特定游戏场景或 Event 移除效果器。  Default value: false |
| Edit | 编辑。打开 [“Effect Plug-in Editor”一节](../../05-ShareSets-选项卡/01-Effect-Plug-in-Editor.md "Effect Plug-in Editor") 以便实时编辑所选效果器实例的属性。 |
|  | 打开可应用于对象的一系列效果器及对应实例。选择效果器以将其添加到 Effects 列表底部的下一可用插槽。  在添加效果器后，可将其选中并在列表中上下拖动。使用 Ctrl 或 Shift 键来选择并拖动多个效果器。  另外，也可通过在 Project Explorer（工程资源管理器）的 ShareSets 选项卡中拖动 ShareSet 或右键单击列表中的效果器并选择 **Add Effect**（添加效果器）来将效果器添加到列表中。在这种情况下，会在当前插槽中插入新的效果器，并将所有后续效果器下移一列。 |
|  | 删除在 Effects 列表中选择的效果器。您可以使用 Ctrl 或 Shift 键来选择多个效果器。 |
| （在层级结构中的位置） | 显示在 Effect 层级结构中可以找到所选 ShareSet 的位置。如果它是效果器的自定义实例，它将显示自定义实例的名称。 |
| Bypass All | 全部旁通。决定是否旁通对象上插入的所有效果器。若选中复选框，则移除所有效果器。若取消选中复选框，则恢复使用效果器。  此选项在以下情况下非常有用：  - 在对游戏实施性能分析时，可启用或禁用此选项来确定效果器对声音设计及 Performance Monitor 中所示 CPU 用量的影响。 - 在按平台定制声音设计时，可取消链接对象上的效果器，并针对处理能力较弱的平台旁通该对象上的所有效果器。  另外，还可在 RTPC 中使用 Bypass 选项或在 Event 中使用 “Bypass Effect” Action 来针对特定游戏场景或 Event 移除效果器。  Default value: false |

**相关主题**

- [*管理效果器*](../../../../05-使用声音和振动来提升游戏体验/04-管理效果器/00-管理效果器.md "管理效果器")
- [“将 Effect ShareSet 转换为自定义实例”一节](../../../../05-使用声音和振动来提升游戏体验/04-管理效果器/00-管理效果器.md#converting_effect_sharesets_into_custom_instances "将 Effect ShareSet 转换为自定义实例")
- [“编辑效果器属性”一节](../../../../05-使用声音和振动来提升游戏体验/04-管理效果器/00-管理效果器.md#editing_effect_properties "编辑效果器属性")
- [“旁通效果器”一节](../../../../05-使用声音和振动来提升游戏体验/04-管理效果器/00-管理效果器.md#bypassing_an_effect "旁通效果器")
- [“渲染效果器”一节](../../../../05-使用声音和振动来提升游戏体验/04-管理效果器/00-管理效果器.md#rendering_effects "渲染效果器")
- [“对效果器重新排序”一节](../../../../05-使用声音和振动来提升游戏体验/04-管理效果器/00-管理效果器.md#re_ordering_effects "对效果器重新排序")

---