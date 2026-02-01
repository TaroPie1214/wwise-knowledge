# Platform Manager

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [工程](../00-工程.md) > Platform Manager

## Platform Manager

Platform Manager（平台管理器）对话框允许定义工程所用平台。各个目标 (SDK) 可拥有任意数量的平台。创建新工程时会为各个目标创建一个平台。

Platform Manager 列有全部所需的平台操作 (Add/Remove/Rename)。单击 **OK**（确定）按钮可执行所有待处理平台操作。单击 **Cancel**（取消）按钮则放弃所有待处理平台操作。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 执行平台操作要求 Wwise 保存然后重新加载该工程。 |

| 界面元素 | 描述 |
| --- | --- |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Platform | 已定义平台的独有字母数字名称。 |
| Base Platform | 平台的 SDK。 |
| Pending Actions | 待执行操作。点击 **OK** 即可执行操作（如指定平台的 **Add** 或 **Copy Settings**）。 |
| Volume Threshold | 音量阈值。在低于该默认音量电平时，将按照 Property Editor 的 Advanced Settings 中所定义行为管理声部。例如，可对低于音量阈值的声部执行以下任何操作：  - Continue to play - Be killed - Sent to the virtual voice list  可使用 Wwise SDK API 而不沿用该值。  **Note**:即便继续播放或变为虚声部，只要低于音量阈值，声部就不会被听到。 **Note**:默认滑杆范围为 -96 至 0。您可以通过直接输入值，或在编辑控件上移动鼠标来输入超出限制范围的值。  Default value: -80  Range: -96 to 0 |
| Max Voice Instances | 最大声部实例数。同一时刻能够在整个工程中同时处于激活状态的声部的最大数量。虚声部不会被记为活跃声部。超出这一限制后，具有最低优先级的声部将采取它们的虚声部行为。如果优先级相等，则出现时间早的声音将被认为有较高的优先级。各个声音可不沿用其自身的虚声部行为，虚声部行为包括：  - Continue to play（继续播放） - Be killed（被终止） - Send to virtual voice（发送至虚声部）  |  |  | | --- | --- | | [备注] | 备注 | | 如果某些声音的虚声部行为被设置为 **Continue to play**，则不会受声部实例最大数目的限制。要遵守此限制，播放声部时需要将其虚声部行为设置为 **Kill voice** 或 **Send to Virtual voice**。 |  可使用 Wwise SDK API 而不沿用该值。 |
|  | 添加…。打开 [“Add Platform”一节](01-Add-Platform.md "Add Platform") 对话框。新平台将添加至 **Platforms** 列表。  点击 **OK** 按钮即可将新平台将添加至工程。 |
|  | Removes the selected platform. 若平台是最近添加的（通过 **Add** 按钮），则只会从 Platforms 列表中移除该平台。否则，会将该平台标记为移除，点击 **OK** 按钮即可从工程中移除。 |
|  | Renames the selected platform. 重命名所选平台。新平台名称在所有平台中不能重名，只能包含字母数字字符。 |
|  | 添加…。打开 [“Copy Platform Settings”一节](02-Copy-Platform-Settings.md "Copy Platform Settings") 对话框。接受这些设置的平台将在 **Platforms** 列表中标记为复制。点击 **OK** 按钮即可复制这些平台设置。 |
|  | 确定。关闭 Platform Manager 对话框，并执行所有待处理的平台操作。 |
|  | 取消。关闭 Platform Manager 对话框，而不对工程做任何更改。 |

**相关主题**

- [*管理多平台*](../../../03-设置工程/02-管理多平台.md "管理多平台")
- [“Copy Platform Settings”一节](02-Copy-Platform-Settings.md "Copy Platform Settings")
- [“为工程指定 Volume Threshold”一节](../../../03-设置工程/01-处理工程/02-定义工程设置/08-为工程定义音量设置.md#specifying_volume_thresholds_for_project "为工程指定 Volume Threshold")

---