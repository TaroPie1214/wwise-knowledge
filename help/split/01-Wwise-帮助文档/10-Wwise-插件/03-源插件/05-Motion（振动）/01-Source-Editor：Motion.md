# Source Editor：Motion

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [Wwise 插件](../../00-Wwise-插件.md) > [源插件](../00-源插件.md) > [Motion（振动）](00-Motion（振动）.md) > Source Editor：Motion

### Source Editor：Motion

Source Editor 显示与 Motion 插件关联的所有属性。

您可以定义 Driver 偏置、RTPC 曲线或 State 偏置，以便为不同的 Driver 生成相应正值，从而输出各种类型的振动效果（其中，1 表示振动强度最大，0 或负值表示无振动效果）。此外，还可利用 [“Game Parameters”一节](../../../09-参考主题/04-Project-Explorer/04-Game-Syncs-选项卡/03-Game-Parameters/00-Game-Parameters.md "Game Parameters")、[MIDI](../../../09-参考主题/04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/00-MIDI-category-Containers-hierarchy-objects.md "MIDI category: Containers hierarchy objects") 和[调制器](../../../09-参考主题/04-Project-Explorer/05-ShareSets-选项卡/04-Modulator-Editor-视图/00-Modulator-Editor-视图.md "Modulator Editor 视图")来设置振动曲线的总体时长和强度变化。

然后，根据需要将这八个 Driver（编号 A ~ H）指派给适用于所选 Actuator Configuration 的不同促动器（电机）。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 一般来说，基于振动效果的手柄的振动强度会随着源波形振幅的增大而增大。不过，DualSense 手柄上的触觉设备的振动强度会随着波形振幅的*波动*而增大。因此，恒定的高振幅波形（比如由默认 Motion Source 生成的波形）会在基于振动效果的手柄上产生强烈的振动，但在 DualSense 手柄上却不会产生任何振动。  “想在 DualSense 手柄上产生更强的振动，但又不想对 Motion Source 内容进行重新设计”的权变措施：将 Actuator Configuration 设为 **DualSense 2-Channel**。 |

The following table describes the Settings tab of the Motion Source property editor. For
information about the RTPC tab, see [“RTPC tab”一节](../../../08-使用-Wwise/09-使用-Object-Tab-和-Object-Tab-Group/03-Primary-Editor-和-Secondary-Editor/02-RTPC-tab.md "RTPC tab"). For information about the States
tab, see [“States tab”一节](../../../08-使用-Wwise/09-使用-Object-Tab-和-Object-Tab-Group/03-Primary-Editor-和-Secondary-Editor/03-States-tab.md "States tab").

| 界面元素 | 描述 |
| --- | --- |
| Name | 名称。Motion 插件的名称。 |
| Notes | 备注。有关 Motion 插件的任何额外信息。 |
| **Internal Driver Channels** | |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../../09-参考主题/04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../../09-参考主题/04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../../09-参考主题/04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../../09-参考主题/04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
| Driver | 驱动器。用于驱动促动器振幅的曲线（共 8 条）。该值可以是绝对值，也可利用 RTPC 进行调整。比如，可利用 [Time Modulator](../../../09-参考主题/04-Project-Explorer/05-ShareSets-选项卡/04-Modulator-Editor-视图/03-调制器时间.md "调制器时间") 调整曲线如何随时间变化。所用驱动器曲线选项由 Driver Assignment 中的设置决定。  Default value: 0.0  Range: 0 to 1 |
| **Driver Assignment** | |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../../09-参考主题/04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../../09-参考主题/04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../../09-参考主题/04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../../09-参考主题/04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
| Actuator Configuration | 促动器配置。已知设备的一组配置，每项配置分别针对设备可用的促动器之一。有三种匿名配置可供未知设备使用。  - **Android**:单个匿名声道。 - **PlayStation Move**:单个匿名声道。 - **DualShock 2-Channel**:低频声道和高频声道各一个。 - **Switch 2-Channel**:低频声道和高频声道各一个。 - **Switch 4-Channel**:低频声道和高频声道各两个。 - **Xbox 4-Channel**:低频声道、高频声道、左侧触发器声道和右侧触发器声道各一个（无法在 Wwise 设计中工具测试）。 - **Generic 1-Channel**:单个匿名声道。 - **Generic 2-Channel**:两个匿名声道。 - **Generic 4-Channel**:四个匿名声道。 - **DualSense 2-Channel**:低频声道和高频声道各一个，可为支持高保真触觉效果的设备（如 DualSense™ 控制器）生成波形，以便模拟使用双电机振动的手柄（如 DUALSHOCK®4）的行为。  |  |  | | --- | --- | | [备注] | 备注 | | 促动器配置的默认平台名称指示适用于 Wwise 默认 sink 的已知平台。但是，这并不说这些配置仅可用于该平台。有时，甚至可能希望针对特定平台选择不同的配置。例如，有些 Android 平板电脑设有两个促动器，这时最好采用 2 Channel 配置，而非默认 sink 的单个匿名声道 Android 配置。声道数不匹配并不会影响振动；如果促动器的数量较多，会使用相同的 Driver 声道，而如果定义的声道数量较多，则会忽略部分声道。 |  Default value: Generic 1-Channel |
| Low Frequency 1 | 低频 1。使用此设置为设备的第一个低频（大号）促动器选择驱动器曲线。  Default value: Driver A |
| High Frequency 1 | 高频 1。使用此设置为设备的第一个高频（小号）促动器选择驱动器曲线。  Default value: Driver A |
| Low Frequency 2 | 低频 2。使用此设置为设备的第二个低频（大号）促动器选择驱动器曲线。  Default value: Driver A |
| High Frequency 2 | 高频 2。使用此设置为设备的第二个高频（小号）促动器选择驱动器曲线。  Default value: Driver A |
| Left Impulse Trigger | 左侧触发器。使用此设置为设备的左侧触发器促动器选择驱动器曲线。  Default value: Driver A |
| Right Impulse Trigger | 右侧触发器。使用此设置为设备的右侧触发器促动器选择驱动器曲线。  Default value: Driver A |
| Channel 1 (Anonymous) | 使用此设置为匿名促动器选择驱动器曲线。可供匿名配置使用。  Default value: Driver A |
| Channel 2 (Anonymous) | 使用此设置为匿名促动器选择驱动器曲线。可供匿名配置使用。  Default value: Driver A |
| Channel 3 (Anonymous) | 使用此设置为匿名促动器选择驱动器曲线。可供匿名配置使用。  Default value: Driver A |
| Channel 4 (Anonymous) | 使用此设置为匿名促动器选择驱动器曲线。可供匿名配置使用。  Default value: Driver A |

**相关主题**

- [“为游戏控制器生成振动效果”一节](../../../05-使用声音和振动来提升游戏体验/05-管理-Motion/03-为游戏创建振动效果/03-创建专用对象来生成振动效果/01-为游戏控制器生成振动效果.md "为游戏控制器生成振动效果")
- [*管理 Motion*](../../../05-使用声音和振动来提升游戏体验/05-管理-Motion/00-管理-Motion.md "管理 Motion")

---