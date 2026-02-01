# Blend Track Editor

[Wwise 帮助文档](../../../../../00-Wwise-帮助文档.md) > [参考主题](../../../../00-参考主题.md) > [Project Explorer](../../../00-Project-Explorer.md) > [Audio tab](../../00-Audio-tab.md) > [Containers hierarchy: sound and motion objects](../00-Containers-hierarchy-sound-and-motion-objects.md) > [Property Editor：Blend Container](00-Property-Editor：Blend-Container.md) > Blend Track Editor

##### Blend Track Editor

您可以在 Blend Track Editor（混合轨编辑器）中编辑 Blend Container（混合容器）的内容。这些容器的内容同时播放，但您可以变动这些内容，使其属性能够通过 RTPC 曲线和交叉淡变进行控制。

Blend Track Editor 由两个主要区域构成：您可以在一个区域中启用和定义交叉淡变，在另一个区域中定义 RTPC 曲线并在坐标图视图中创建交叉淡变区域。您还可以将 RTPC 曲线从一个属性复制到另一个属性，从一条声轨复制到另一条声轨，或从一个对象复制到另一个对象。

坐标图中还显示 Game Parameter 光标，方便在播放期间前后拖动进行测试。您可以在播放期间实时修改这些点。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 您必须创建至少一条混合轨才能使 Blend Track Editor 中的大多数选项可见。 |

| 界面元素 | 描述 |
| --- | --- |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../../12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../../07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../../12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Blend Container（混合容器） | 混合容器。您当前正在编辑其混合轨的 Blend Container 的名称。 |
|  | 在 Blend Track Editor 中创建新的混合轨。 |
| Name | 名称。当前混合轨的名称。 |
|  | 删除当前混合轨。 |
| Crossfade | 交叉淡变。确定是否在当前混合轨中启用交叉淡变。如果选择此选项，您则可以在当前混合轨中使用交叉淡变区域。 |
| Crossfade Control Input | 交叉淡变控制输入。显示用于交叉淡变的 Game Parameter。若要更改用于交叉淡变的 Game Parameter，请展开列表并选择新的 Game Parameter。 |
|  | 显示可映射至 Game Parameter 的 Wwise 属性。 |
| (固定/取消固定) | 决定坐标图视图中是否显示 RTPC 曲线。  如果选择了 Pin 图标，则无论是否选中该曲线，RTPC 曲线都会显示在坐标图视图中。 |
| |  | | --- | |  |  （颜色块） | 在坐标图视图中显示 RTPC 曲线的颜色。每条新曲线都会被分配一种不同的颜色。  相对属性（音量、音高、低通滤波器等）始终为相同的颜色。 |
| Y axis | Y 轴。分配给 Y 轴的 Wwise 属性。  要更改分配给 Y 轴的 Wwise 属性，请点击 Wwise Property Display 按钮并选择新的属性。 |
| X axis | 指派到 X 轴的游戏中参数。  若要更改指派给 X 轴的 Game Parameter，请展开列表并选择新的 Game Parameter。 |
| Notes | 备注。有关 RTPC 的任何额外信息。 |
| (坐标图) | 游戏中参数（X 轴）与 Wwise 属性值（Y 轴）之间关系的图形表示。  坐标图视图可同时显示多条曲线。 |
| X | 所选控制点的 X 轴坐标。X 值代表所选 Game Parameter 的值。  如果选择了多个控制点，则字段显示 0 值，这时可以针对所有已选控制点的当前值，进行统一的增大或减小。例如，如果您选择两个控制点并在 X 文本框中输入 -5，则两个控制点都将向左移动 5 个单位。 |
| Y | 所选控制点的 Y 轴坐标。Y 值表示属性值（音量（单位为分贝）、音高（单位为音分）或低通滤波器（单位为百分比）。  如果选择了多个控制点，则字段显示 0 值，这时可以针对所有已选控制点的当前值，进行统一的增大或减小。例如，如果您选择两个控制点并在 Y 文本框中输入 -5，则两个控制点都将向下移动 5 个单位。 |
|  | 基于坐标图视图的中心进行放大。 |
|  | 将坐标图视图重置为默认的 1:1 缩放比例。 |
|  | 基于坐标图视图的中心进行缩小。 |

**相关主题**

- [“创建 Blend Container”一节](../../../../../05-使用声音和振动来提升游戏体验/01-定义对象播放行为/04-定义-Blend-Container-的内容和行为/00-定义-Blend-Container-的内容和行为.md#creating_blend_container "创建 Blend Container")
- [“使用 Blend Track”一节](../../../../../05-使用声音和振动来提升游戏体验/01-定义对象播放行为/04-定义-Blend-Container-的内容和行为/01-使用-Blend-Track.md "使用 Blend Track")
- [“为 Blend Track 添加和移除对象”一节](../../../../../05-使用声音和振动来提升游戏体验/01-定义对象播放行为/04-定义-Blend-Container-的内容和行为/01-使用-Blend-Track.md#adding_and_removing_objects_from_blend_tracks "为 Blend Track 添加和移除对象")
- [“管理交叉淡变”一节](../../../../../05-使用声音和振动来提升游戏体验/01-定义对象播放行为/04-定义-Blend-Container-的内容和行为/02-管理交叉淡变.md "管理交叉淡变")
- [“更改坐标图的显示内容”一节](../../../../../08-使用-Wwise/07-了解坐标图视图/01-更改坐标图的显示内容.md "更改坐标图的显示内容")
- [“在坐标图中使用控制点”一节](../../../../../08-使用-Wwise/07-了解坐标图视图/02-在坐标图中使用控制点.md "在坐标图中使用控制点")
- [“在坐标图中使用曲线”一节](../../../../../08-使用-Wwise/07-了解坐标图视图/03-在坐标图中使用曲线.md "在坐标图中使用曲线")

---