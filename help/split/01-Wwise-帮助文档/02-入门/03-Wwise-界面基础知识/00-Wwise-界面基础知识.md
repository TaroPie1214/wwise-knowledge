# Wwise 界面基础知识

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [入门](../00-入门.md) > Wwise 界面基础知识

## Wwise 界面基础知识

Wwise 界面分为多个不同的视图。各个视图都有其特定的目的，您可以访问其中的各种工具或选项，以管理和定义游戏的内容。这些视图组合在一起即成为布局，方便您处理特定任务或作业所需的工作。Wwise 中提供了不同的布局。有关详细信息，请参阅[“处理布局”一节](../04-个性化您的工作空间/02-处理布局/00-处理布局.md "处理布局")。

各个布局的顶端是菜单栏和工具栏。通过菜单栏可以访问所有基本信息（如工程名称）和基本命令（如保存工程、更改布局、打开视图或打开属性的帮助条目）。通过工具栏可以快速访问某些工具，如 Platform 或 Language Selector、Capture 工具、Remote Platform Connector 和 Search 工具。

![](../../../images/menu_toolbar.png)

下图详细显示了菜单栏的各项信息。

![](../../../images/menubar_details.png)

下图详细显示了工具栏左侧的各项信息。

![](../../../images/toolbar_details_left.png)

下图详细显示了工具栏右侧的各项信息。

![](../../../images/toolbar_details_right.png)

当您首次启动 Wwise 时会显示 **Designer** 布局。

![](../../../images/wwise_designer_layout.png)

该布局包含以下视图：

- **Project Explorer**：这是主要区域，您可在其中管理和组织 Wwise 工程的各种元素。详请参阅[*认识 Project Explorer 视图*](../../08-使用-Wwise/01-认识-Project-Explorer-视图/00-认识-Project-Explorer-视图.md "认识 Project Explorer 视图")。Project Explorer 包含以下选项卡：

  - **Audio**：一种层次树视图，非常像 Windows 资源管理器和 Mac Finder，可以在其中组织工程中的资源（asset）。The Audio tab has three main hierarchies: Devices, Busses, and Containers.
  - **Events**（事件）：显示工程中的事件，包括操作和对白事件。
  - **SoundBanks**（音频包）: 显示工程中的所有**SoundBank**。
  - **Game Syncs**（游戏同步器）: 显示工程中的所有Switch（切换开关）、State（状态）、Game Parameters（游戏参数）和Trigger（触发器）。
  - **ShareSets**（共享集）: 显示工程中的所有效果和衰减工程集。
  - **Sessions**（会话）: 显示工程中的所有 Soundcaster（声音选角器）会话。
  - **Queries**（查询）: 显示工程中的所有查询。
- **Contextual Help view**: Provides information on properties selected anywhere in the Wwise user interface as well as details on error messages selected in the [“Capture Log”一节](../../09-参考主题/06-Profiler-视图/01-Capture-Log/00-Capture-Log.md "Capture Log"). Refer to [“Contextual Help”一节](../../09-参考主题/02-视图/08-Contextual-Help.md "Contextual Help") for more information.
- **Object Tab Group**（对象选项卡分组）：可能不包含、包含一个或多个 Object Tab（具体取决于所作选择）。Wwise 中的任何对象都可显示在 Object Tab 中，其会根据各个对象的特性自动进行调整。各个 Object Tab 方便快速访问与对象最为相关的各种编辑器，并在一个集中位置定义声音、音乐或总线结构内对象的特性和行为。详请参阅[*使用 Object Tab 和 Object Tab Group*](../../08-使用-Wwise/09-使用-Object-Tab-和-Object-Tab-Group/00-使用-Object-Tab-和-Object-Tab-Group.md "使用 Object Tab 和 Object Tab Group")。
- **Transport Control**（播放控制）：播放您的对象。Transport Control 包含与音频播放相关的传统控件，如播放、停止和暂停。详请参阅[*认识 Transport Control 视图*](../../08-使用-Wwise/05-认识-Transport-Control-视图/00-认识-Transport-Control-视图.md "认识 Transport Control 视图")。
- **Meter view**（电平表视图）：为各个通道显示彩色电平值，可以选择三种不同类型之一，即峰值、真实峰值和 RMS值。对于 Ambisonics 总线，Meter 视图还可显示 3D Meter（显示方向数据）。

## 使用文本框和滑杆

Wwise 中的大部分视图都包含文本框。您可在其中键入适当的值或有关对象的特定信息。文本框的名称表示栏中所显示信息的类型。根据视图的不同，文本框的名称可位于视图的旁边、上方或下方。

![](../../../images/Slider_horiontal_online.png)

|  |  |
| --- | --- |
|  | 文本框名称。 |
|  | 属性值。 |

您可以通过右键单击文本并选择 **Copy**（复制）来复制文本框中的文本。若文本框中显示文本但无法编辑，则表示其不可用。

若要将属性值恢复为默认设置，请在按住 Ctrl 的同时单击文本框。

大部分包含属性值的文本框下方还会有一个横向滑杆。您可以拖动滑杆来在连续取值范围内设置文本框中的值。

横向滑杆包含滑块和滑动条。滑块是一个小点，代表当前属性值。滑动条代表当前值大小，它的取值在允许范围内。

![](../../../images/Slider_horiontal_online2.png)

|  |  |
| --- | --- |
|  | 滑动条。 |
|  | 滑块。 |

根据默认值相对取值范围所处的位置，滑块会显示在滑杆的不同位置。同样，根据默认值相对取值范围所处的位置，滑动条会由不同位置开始并向不同方向延伸。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 有些滑杆的默认取值范围只是属性完整取值范围的子集。若要为特定属性设置更大范围的值，请在文本框中输入默认取值范围以外的值。若要查看属性的默认取值范围和完整取值范围，请参阅属性的 Contextual Help 或相关视图的参考主题。 |

在文本框中点击并按住鼠标键时，会显示大型滑杆，以方便您微调该属性值。松开鼠标按钮时，较大的滑杆会消失。如果您需要更精确地定义该数值，则可按住 Shift 键同时拖动滑杆，以更小的增量来增加或减小该数值。

![](../../../images/Slider_super_online.png)

|  |  |
| --- | --- |
|  | 在文本框中单击并按住鼠标左键的时候，会显示大号滑杆以便拖动来更改属性值。 |

## 使用列表

Wwise 中包含两种类型的列表：下拉式列表和快捷方式列表（有时称为上下文列表）。下拉列表（本帮助文档中简称为“列表”）指包含很多预定义选项的下拉栏。要显示列表，请点击下拉栏右侧的箭头。

![](../../../images/Lists_normal_online.png)

|  |  |
| --- | --- |
|  | 单击箭头可显示选项列表。 |

选择器按钮 (>>) 用于显示一组选项或操作。快捷方式菜单可能包含相关信息栏，以显示所选的选项。点击该按钮，以显示菜单选项。

![](../../../images/Selector_Menu.png)

|  |  |
| --- | --- |
|  | 单击选择器按钮可显示选项列表。 |

## 使用推子

某些属性（如音量）使用垂直滑杆或推子（而不是水平滑杆）更改值。音量控件使用垂直滑杆以更好地模拟硬件和软件混音器中的推子。您可向上或向下拖动滑杆，以增加或减小这些属性值。如果需要更精确地定义该值，则可以按住 Shift 键同时点击推子上方或下方，以更小的增量来增加或减小该数值。

![](../../../images/Slider_vertical_online.png)

|  |  |
| --- | --- |
|  | 上下拖动推子可更改属性值。在按住 Ctrl 的同时单击推子或文本框可恢复为属性的默认值。 |
|  | 文本框：可在此处键入数值。 |

## 使用表格

您可以使用光标键浏览表格中的单元格。在大部分情况下，还可配置列、调整列宽、按列对行进行排序并编辑表格中的属性值。

|  |
| --- |
|  |

**在表格中配置列标题的方法如下：**

在大部分表格中，都可通过 Configure Columns 对话框来配置所要显示的列。

1. 右键单击表格标题并选择 **Configure Columns**（配置列）。
2. 在弹出的 Configure Columns（配置列）对话框中，指定要显示的列及其顺序。

| Configure Columns 对话框 | |
| --- | --- |
| 界面元素 | 描述 |
| Column names 面板 | 系统会以复选框的形式列出视图中可用的列。  - 选中列名称可将其包含到视图的表格中。取消选中复选框便可将相应的列移除。 - 上下拖放列可重新进行排序。Configure Columns 对话框中列表的上下顺序与视图中列表内的左右顺序对应。 |
| Reset to default | 重置为默认值。单击此按钮可将列名称面板中的所有选中（可见）列恢复为默认设置并按照视图的默认顺序进行排序。 |

**调整表格中的列宽的方法如下：**

- 将鼠标指针悬停在列分隔线之上。在指针变为双箭头时，左右拖动分隔线来调整列宽。
- 若要将列宽恢复为默认值，请右键单击表格标题并选择 **Reset Column Widths to Default**（将列宽重置为默认值）。

**对表格的行进行排序：**

根据表格执行以下操作：

- 单击列标题来针对该列按升序顺序对行进行排序。再次单击可按降序顺序进行排序。
- 拖放相应的行。

**在表格中筛选元素的方法如下：**

1. 在表格标题右侧，单击 **Find in List** ![](../../../images/search_icon.png) 或按下 Ctrl+F3（在 macOS 上按下 Command+F3）。

   随即显示标准字母数字搜索栏。

   |  |
   | --- |
   |  |
2. 输入字符（包括数字、标点符号、特殊字符和空格）。字母不区分大小写。在键入字符时会对表格进行筛选，而仅显示包含匹配内容的行。Wwise 会对所有的列进行搜索，在 File Manager 中的时候除外（只会对 **File** 列进行搜索）。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 在 List View、Query Editor、MIDI Keymap Editor 和 Reference View 中，不会搜索被隐藏的子对象（所以它们会被滤掉）。 |
3. 若要关闭“搜索”字段，请单击“搜索”字段右侧的 Close（关闭）图标或按下 Ctrl+F3（在 macOS 上按下 Command+F3）。

## 在 Wwise 中 Undo 和 Redo 操作

您可撤消您在 Wwise 中执行的大部分操作，如更改属性值、移动对象，或创建事件。如果您错误地撤消了某一操作，则可以恢复至上一个操作之前的值或状态。

要撤消某个操作，请点击  **Edit > Undo ><操作名称>** ，或按下 **Ctrl+Z**。您最多可撤消前 200 个操作。

要恢复某一操作，请点击  **Edit > Redo ><操作名称>** ，或按下 **Ctrl+Y**。您可为每个撤消操作调用一个恢复命令。

---