# Audio Device Editor：Effects

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [Audio tab](../00-Audio-tab.md) > [Audio Devices](00-Audio-Devices.md) > Audio Device Editor：Effects

#### Audio Device Editor：Effects

在与 Audio Device 对应的 Effects 选项卡中，若有 Mastering Suite 和/或 GME Real-time Voice Service 插件，最多可向 Audio Device 应用 255 个效果器。各个插件会分别提供对应的效果器类型：Mastering Suite 和 Tencent GME Session。

Mastering Suite 存在一定的限制。若使用 Mastering Suite 效果器类型，则仅可添加单个效果器，且须添加到最后一个插槽（其他效果器类型没有这种限制）。有关详细信息，请参阅“[“Mastering Suite”一节](../../../../10-Wwise-插件/02-Audio-Device-效果器插件/01-Mastering-Suite/00-Mastering-Suite.md "Mastering Suite")”和“[“了解声部管线”一节](../../../../07-完善工程/01-管理输出/05-了解声部管线.md "了解声部管线")”章节。

在 Wwise 中应用效果器时，要注意声部可能会经过以下四个层级的效果器渲染：

- Up to 255 Effects can be applied to a voice in the Containers
  hierarchy, but remember that child objects can also override their parent objects'
  Effects.
- 总线层级结构输出路径中的每条 Audio Bus 和 Auxiliary Bus 最多可应用 255 个效果器。
- Up to 255 Effects can be applied to the final main bus (the Main Audio or the
  Main Secondary Bus).
- Audio Device（音频设备）最多可应用 255 个效果器。

这意味着允许将一系列效果器应用于最终输出。您可以通过执行以下操作来管理这些效果器：

- 使用 Mode 选项将效果器设为 ShareSet，以此来同时调节同一效果器的多个实例。另外，还可根据需要将 Mode 设为 Custom，来将特定设置应用于单个效果器实例。
- 根据需要选中 Bypass 复选框来暂时移除效果器，或取消选中该复选框来恢复使用效果器。这样方便在测试当中确定效果器所产生的影响。另外，还可在 RTPC 中使用 Bypass 选项或在 Event 中使用 "Bypass Effect" Action 来针对特定游戏场景或 Event 移除效果器。

|  |  |
| --- | --- |
| [备注] | 备注 |
| Effects on Audio Devices are slightly different from Effects on objects in the Containers hierarchy or Busses hierarchy. 注意以下几点：  - 若添加 Mastering Suite 效果器类型，则仅可向 Audio Device 添加单个效果器，且须将其添加到最后一个效果器插槽。 - 可用的效果器特定于 Audio Device。 - Audio Device 效果器不支持 RTPC。 - Unlike Effects on objects in the Containers hierarchy, Audio Device Effects   cannot be rendered. For information on the Effects tab of objects   in the Containers hierarchy, see [“Effects tab: Containers hierarchy objects”一节](../05-Common-tabs-and-categories-audio-structures/08-Effects-tab-Containers-hierarchy-objects.md "Effects tab: Containers hierarchy objects"). - 在 PS5 上，会在将音频发送到扬声器或耳机之前在平台的专用单元上对 Mastering Suite 进行处理。在其他平台上，会在 Wwise 音频管线末端在软件模式下对 Mastering Suite 进行处理。 |

| General | |
| --- | --- |
| 界面元素 | 描述 |
| [name] | 对象的名称。 |
| (Object Color) | 显示对象的颜色。单击图标可打开颜色选择器。    选择一种颜色并将其应用于对象。在为对象选择某种颜色时，会在选定方块上显示调色板图标，并在右下角标注黄色三角（如图所示）。  若要沿用父对象的颜色，请选中颜色选择器最左侧的方块。 |
| (Show references) | 指示工程中有多少元素包含对对象的直接引用。若存在对对象的引用，则图标显示为橙色；若不存在此类引用，则图标显示为灰色。  通过单击该按钮，可打开 [“Reference View 视图”一节](../../12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")，并在 **References to:**（引用:）字段中查看对象的名称。 |
| Notes | 备注。对象属性的额外信息。 |
|  | 设置 Property Editor 中选定标签页的显示方式。默认情况下，整体面板中仅显示一个选定选项卡。不过，您可以通过单击分隔器按钮将面板沿横向或纵向一分为二。当前所选选项将以高亮背景色显示。  无法同时在两个面板中打开同一选项卡。若尝试在两个面板中打开同一选项卡，则第一个面板将自动打开别的选项卡。  |  |  | | --- | --- | | [技巧] | 技巧 | | - 在按住 Ctrl 的同时按下与所要查看的 Property Editor 选项卡的编号对应的数字。比如，若 RTPC 为第四个可见选项卡，则按下 Ctrl+4 时将打开 RTPC 选项卡。 | |

| Effects | |
| --- | --- |
| 界面元素 | 描述 |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| **Effects** | |
| （选择器） | 可应用于 Audio Device 的效果器及对应实例列表。为此，必须先通过 Audiokinetic Launcher 安装至少一个以下插件：  - Mastering Suite 插件提供 Mastering Suite 效果器。 - GME Real-time Voice Service 插件提供 Tencent GME Session 效果器。  若要移除效果器，可选择 **None**（无）。 |
| ID | 效果器的标识号。导流体对于 Mastering Suite 效果器，仅可添加单个效果器，且须将其放在最后一个插槽。 |
| Effect | 效果器。应用于 Audio Device 的效果器的类型。 |
| Name | 名称。应用于 Audio Device 的效果器实例的名称。效果器实例可以是 ShareSet 或 ShareSet 的自定义实例。  对应列表中会显示选定效果器类型的所有效果器实例。 |
| Prev. | 上一个。选择 Effects 层级结构中的上一 ShareSet。 |
| Next | 下一个。选择 Effects 层级结构中的下一 ShareSet。 |
| Mode | 模式。确定是否共享效果器。模式可以是：  - **Define custom**（定义自定义）：创建自定义效果器实例，不在对象之间共享其属性。 - **Use ShareSet**（使用共享集）：使用效果器的 ShareSet，可在对象之间共享效果器属性。  |  |  | | --- | --- | | [备注] | 备注 | | 若添加自定义效果器，然后把 **Mode** 改为 **Use ShareSets**，将打开 Create ShareSet from Custom Object（通过自定义对象创建共享集）警告对话框。其设有三个选项：  - **Convert**（转码）：打开 New Effect（新建效果器）对话框，以便使用指定的效果器设置创建新的 ShareSet。 - **Revert**（还原）： 清除 Effect Editor 并将效果器还原为 ShareSet 的原始设置。 - **Cancel**（取消）：将 Mode 恢复为 Define custom，并返回未经修改的 Effect Editor。 | |
| （在层级结构中的位置） | 显示 ShareSet 在 Effects 层级结构中的位置。若为效果器的自定义实例，则显示自定义实例的名称。 |
| Bypass | 旁通。决定是否旁通所选效果器实例。若选中复选框，则移除效果器。若取消选中复选框，则恢复使用效果器。  此选项在以下情况下非常有用：  - 在对游戏实施性能分析时，可启用或禁用此选项来确定效果器对声音设计及 Performance Monitor 中所示 CPU 用量的影响。 - 在按平台定制声音设计时，可取消链接对象上的效果器，并针对处理能力较弱的平台旁通该对象上的某些效果器。  另外，还可在 RTPC 中使用 Bypass 选项或在 Event 中使用 “Bypass Effect” Action 来针对特定游戏场景或 Event 移除效果器。  Default value: false |
| Edit | 编辑。打开 Effect Editor，以便实时编辑所选效果器实例的属性。 |
| Bypass All | 全部旁通。决定是否旁通对象上插入的所有效果器。若选中复选框，则移除所有效果器。若取消选中复选框，则恢复使用效果器。  此选项在以下情况下非常有用：  - 在对游戏实施性能分析时，可启用或禁用此选项来确定效果器对声音设计及 Performance Monitor 中所示 CPU 用量的影响。 - 在按平台定制声音设计时，可取消链接对象上的效果器，并针对处理能力较弱的平台旁通该对象上的所有效果器。  另外，还可在 RTPC 中使用 Bypass 选项或在 Event 中使用 “Bypass Effect” Action 来针对特定游戏场景或 Event 移除效果器。  Default value: false |

---