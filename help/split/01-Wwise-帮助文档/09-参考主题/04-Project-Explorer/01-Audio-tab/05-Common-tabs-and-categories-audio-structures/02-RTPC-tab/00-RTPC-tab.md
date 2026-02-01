# RTPC tab

[Wwise 帮助文档](../../../../../00-Wwise-帮助文档.md) > [参考主题](../../../../00-参考主题.md) > [Project Explorer](../../../00-Project-Explorer.md) > [Audio tab](../../00-Audio-tab.md) > [Common tabs and categories: audio structures](../00-Common-tabs-and-categories-audio-structures.md) > RTPC tab

#### RTPC tab

  

|  |  |
| --- | --- |
| [备注] | 备注 |
| The RTPC tab for busses is exactly the same as the RTPC tab for objects in the Containers hierarchy except that the Inclusion box does not apply. The [“Effect Plug-in Editor”一节](../../../05-ShareSets-选项卡/01-Effect-Plug-in-Editor.md "Effect Plug-in Editor") has an identical RTPC tab to the one for objects in the Containers hierarchy. |

RTPC（实时参数控制）选项卡可让您将游戏中的参数映射到 Wwise 属性值上去。两者之间的关系表示为坐标图视图中的 RTPC 曲线，其中 X 轴代表游戏中的参数，Y 轴代表 Wwise 属性。您可以沿各条曲线添加控制点，来定义两个值之间的具体关系。您可以选择一次显示一条曲线，也可以选择全部同时显示，以便进行比较。您还可以将曲线从一个属性复制到另一个属性或者从一个对象复制到另一个对象。

坐标图中显示有 Game Parameter 光标，方便在播放期间前后拖动以测试属性值映射效果。您还可以在播放期间实时修改这些点。播放期间，坐标图视图还将显示游戏对象的参数值。也即对于显示的各条曲线，将根据游戏对象来显示相应的参数值。

在坐标图下方，RTPC 选项卡分成了两个面板。在左侧面板中，可创建 RTPC、重新指派 Wwise 属性值或更改关联的游戏参数。右侧面板（RTPC 侧面板）看起来像是简化版的 [“Multi Editor”一节](../../../12-搜索和工程全局编辑/03-Multi-Editor.md "Multi Editor")。在该面板中，可编辑多个选定参数的属性，包括调制器 ShareSet。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 须在 Project Explorer（工程资源管理器）的 Game Syncs（游戏同步器）选项卡中创建至少一个 Game Parameter，RTPC 选项卡中的选项才会启用。 |

|  |  |
| --- | --- |
| [备注] | 备注 |
| 若要在播放期间旁通 Game Parameter 插值，请在按住 Ctrl 的同时操作 Game Parameter 光标。 |

| General | |
| --- | --- |
| 界面元素 | 描述 |
| [name] | 对象的名称。 |
| (Object Color) | 显示对象的颜色。单击图标可打开颜色选择器。    选择一种颜色并将其应用于对象。在为对象选择某种颜色时，会在选定方块上显示调色板图标，并在右下角标注黄色三角（如图所示）。  若要沿用父对象的颜色，请选中颜色选择器最左侧的方块。 |
| (Mute and Solo) | 控制对象的 Mute（静音）和 Solo（单独播放）状态，也会显示该对象是否处于被动静音和 Solo 状态。  将对象静音会使其在当前监听中无法听到。让对象 Solo 会使工程中的所有其它对象无声。  粗体的 **M** 或 **S** 表明已为对象主动设置了 Mute 或 Solo 状态。褪色的非粗体 **M** 或 **S** 表明对象的 Mute 或 Solo 状态是由于其它对象状态而被动设置的。  将对象静音会让其子对象被动静音。  让对象 Solo 会使同级对象被动静音，并让子对象和父对象被动 Solo。  |  |  | | --- | --- | | [技巧] | 技巧 | | 在点击 Solo 按钮的同时按住 Ctrl 键，可以强制仅 Solo 该 Solo 按钮所在的对象。 |  |  |  | | --- | --- | | [备注] | 备注 | | Mute 和 Solo 仅用于监视目的，而不会保存在工程中或存储在 SoundBank（声音包）中。 | |
| (Show references) | 指示工程中有多少元素包含对对象的直接引用。若存在对对象的引用，则图标显示为橙色；若不存在此类引用，则图标显示为灰色。  通过单击该按钮，可打开 [“Reference View 视图”一节](../../../12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")，并在 **References to:**（引用:）字段中查看对象的名称。 |

| RTPC（实时参数控制） | |
| --- | --- |
| 界面元素 | 描述 |
| (坐标图) | 游戏中参数（X 轴）与 Wwise 属性值（Y 轴）之间关系的图形表示。  坐标图视图可同时显示多条曲线。 |
|  | 基于坐标图视图的中心进行放大。 |
|  | 将坐标图视图重置为默认的 1:1 缩放比例。 |
|  | 基于坐标图视图的中心进行缩小。 |
| **坐标** | |
| X | 所选控制点的 X 轴坐标。  如果选择了多个控制点，则字段显示 0 值，这时可以针对所有已选控制点的当前值，进行统一的增大或减小。例如，如果您选择两个控制点并在 X 文本框中输入 -5，则两个控制点都将向左移动 5 个单位。 |
| Y | 所选控制点的 Y 轴坐标。  如果选择了多个控制点，则字段显示 0 值，这时可以针对所有已选控制点的当前值，进行统一的增大或减小。例如，如果您选择两个控制点并在 Y 文本框中输入 -5，则两个控制点都将向下移动 5 个单位。 |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../../12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../../07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../../12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| （选择器） | 打开选择器菜单，在此您可以选择您要映射到游戏中参数的 Wwise 属性。  对于用户定义和游戏定义的辅助发送，其低通滤波器和高通滤波器参数虽然在 General Settings 中未显示，但可以将它们用于 RTPC 控制。 |
| (固定/取消固定) | 决定坐标图视图中是否显示 RTPC 曲线。  如果选择了 Pin 图标，则无论是否选中该曲线，RTPC 曲线都会显示在坐标图视图中。 |
| |  | | --- | |  |  （颜色块） | 在坐标图视图中显示 RTPC 曲线的颜色。每条新曲线都会被分配一种不同的颜色。  相对属性（音量、音高、低通滤波器等）始终为相同的颜色。 |
| Y axis | Y 轴。分配给 Y 轴的 Wwise 属性。  要更改分配给 Y 轴的 Wwise 属性，请点击 Wwise Property Display 按钮并选择新的属性。 |
| X axis | X 轴。指派给 X 轴的 Game Parameter、MIDI 控制器或调制器。  若要选择不同的 X 轴指派，请展开列表。 |
| Notes | 备注。有关 RTPC 的任何额外信息。 |
| **RTPC 侧面板** | |
| [name field] | 名称字段。可编辑文本字段，用于显示所选 RTPC 对象 (X Axis) 的名称。 |
|  | References（引用）按钮，用于显示工程中引用了多少个当前所选 RTPC 对象。  在单击该按钮后，将打开 [“Reference View 视图”一节](../../../12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图") 并显示直接引用所选 RTPC 对象的所有工程对象/元素。  |  |  | | --- | --- | | [备注] | 备注 | | 在选择多个 RTPC 对象时，该按钮将变为灰色并显示 0。  显示的最大值为 999。在个别情况下有 1,000 个或更多引用时，该数值不会继续增大，但 Reference 视图中会显示所有对象/元素。 | |
| RTPC 侧面板的 Name 和 Value 列会显示当前所选 RTPC 对象 (X Axis) 的所有属性和对应值（可直接编辑）。若多个所选 RTPC 影响的属性相同，但其值各不相同，则将显示破折号。  |  |  | | --- | --- | | [注意] | 注意 | | 即便属性值中显示破折号，也照样可以进行编辑。不过，所做修改将应用于涉及的所有选定 RTPC。 |  双击 RTPC 对象可打开编辑器视图。下述 Simulation Value 属性除外。双击该属性将转到对象的编辑器帮助页面（[“Game Parameter Property Editor”一节](../../../04-Game-Syncs-选项卡/03-Game-Parameters/01-Game-Parameter-Property-Editor/00-Game-Parameter-Property-Editor.md "Game Parameter Property Editor") 或 [“Modulator Editor 视图”一节](../../../05-ShareSets-选项卡/04-Modulator-Editor-视图/00-Modulator-Editor-视图.md "Modulator Editor 视图")），并显示属性信息。 | |
| Simulation Value | 模拟值。设置所选 Game Parameter 的当前值来定位坐标图中的 Game Parameter 光标，仅用于设计工具内的模拟。您可以在 Game Parameter 的 Property Editor 中设置相应字段和滑杆范围；不过，此属性仅会显示在 RTPC 部分，如 [RTPC 侧面板](00-RTPC-tab.md#rtpc_side_panel) 和 [Multi Editor](../../../12-搜索和工程全局编辑/03-Multi-Editor.md "Multi Editor") 。  Default value: 50 |

**相关主题**

- [“将 Wwise 属性指派给游戏参数”一节](../../../../../04-与游戏互动/05-使用-RTPC/03-使用-Game-Parameter-控制属性值/01-将-Wwise-属性指派给游戏参数.md "将 Wwise 属性指派给游戏参数")
- [“映射 RTPC 坐标图中的值”一节](../../../../../04-与游戏互动/05-使用-RTPC/03-使用-Game-Parameter-控制属性值/02-映射-RTPC-坐标图中的值.md "映射 RTPC 坐标图中的值")
- [“从列表中移除 RTPC”一节](../../../../../04-与游戏互动/05-使用-RTPC/03-使用-Game-Parameter-控制属性值/04-从列表中移除-RTPC.md "从列表中移除 RTPC")
- [“Creating Game Parameters”一节](../../../../../04-与游戏互动/05-使用-RTPC/02-管理-RTPC-中使用的-Game-Parameter.md#creating_game_parameter "Creating Game Parameters")
- [“查看 Game Object”一节](../../../../../04-与游戏互动/05-使用-RTPC/07-查看-Game-Object.md "查看 Game Object")
- [“更改坐标图的显示内容”一节](../../../../../08-使用-Wwise/07-了解坐标图视图/01-更改坐标图的显示内容.md "更改坐标图的显示内容")
- [“添加控制点”一节](../../../../../08-使用-Wwise/07-了解坐标图视图/02-在坐标图中使用控制点.md#adding_control_points "添加控制点")
- [“选择控制点”一节](../../../../../08-使用-Wwise/07-了解坐标图视图/02-在坐标图中使用控制点.md#selecting_control_points "选择控制点")
- [“移动控制点”一节](../../../../../08-使用-Wwise/07-了解坐标图视图/02-在坐标图中使用控制点.md#moving_control_points "移动控制点")
- [“删除控制点”一节](../../../../../08-使用-Wwise/07-了解坐标图视图/02-在坐标图中使用控制点.md#deleting_control_points "删除控制点")

---