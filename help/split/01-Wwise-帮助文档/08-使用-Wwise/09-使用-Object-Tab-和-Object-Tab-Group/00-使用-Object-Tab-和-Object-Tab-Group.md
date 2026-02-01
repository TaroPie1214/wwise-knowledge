# 使用 Object Tab 和 Object Tab Group

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用 Wwise](../00-使用-Wwise.md) > 使用 Object Tab 和 Object Tab Group

## 使用 Object Tab 和 Object Tab Group

Object Tab Group（对象选项卡分组）设在 Designer（设计师）布局的中央位置。其可能不包含、包含一个或多个 Object Tab（具体取决于所作选择）。Wwise 中的任何对象都可显示在 Object Tab 中，其会根据各个对象的特性自动进行调整。Object Tab 方便在一个位置集中显示并快速访问与对象最为相关的各种编辑器。

![](../../../images/otg_tabs.png)

|  |  |
| --- | --- |
|  | Object Tab Group。 |
|  | 三个示例 Object Tab。 |

界面中设有两种类型的 Object Tab：Recycle（回收）和 Keep Open（保持打开）。通常，Object Tab Group 中打开的第一个选项卡为 Recycle 选项卡。这意味着，每次在 Project Explorer 内选中某个对象，Recycle 选项卡都会在同一 Object Tab 中换掉之前选中的对象。回收图标会表明选项卡类型。

若要在选项卡中保持打开对象，可双击选项卡或右键单击选项卡并选择 **Keep Open**。这样会将选项卡由 Recycle 选项卡转换为 Keep Open 选项卡。同时，会移除回收（Recycle）图标。在将选项卡转换为 Keep Open 选项卡后，无法再将其恢复为 Recycle 选项卡。随后在 Project Explorer 中选择对象时，会自动打开新的 Recycle 选项卡并显示所选对象。新打开的这个选项卡始终显示在当前选定 Object Tab 的右侧。

|  |  |
| --- | --- |
| [备注] | 备注 |
| Object Tab Group 内同一时间只能有一个 Recycle 选项卡处于打开状态。 |

**在 Recycle 选项卡中查看对象：**

- 在 Project Explorer（工程资源管理器）中选中任意对象。

**若要在 Keep Open 选项卡中查看对象，请执行以下任一操作：**

- 将 Wwise 中的对象拖到 Object Tab Group（对象选项卡分组）的标题栏上。您可在现有 Object Tab区域内选择放置选项卡的位置。
- From the Change Selection Channel menu in the title bar, select **Open New Tab On Double-Click** and then double-click any object in Wwise. 这时会在当前选定 Object Tab 右侧打开新的 Object Tab。

  |  |  |
  | --- | --- |
  | [备注] | 备注 |
  | **Open New Tab On Double-Click** is on by default. Deselect this option if you don't want an Object Tab to be opened when you double-click an object in Wwise. |
- 右键单击 Wwise 中的任意对象，并单击 **Open in New Tab**（在新的选项卡中打开）。这时会在当前选定 Object Tab 右侧打开新的 Object Tab。

**若要关闭 Object Tab，请执行以下任一操作：**

- 单击选项卡右上角的 **x**。
- 右键单击选项卡并选择 **Close**（Ctrl+F4 或 Ctrl+W）。
- 中键单击选项卡。

**若要重新排列 Object Tab Group 内的 Object Tab：**

- 向左或向右拖动选项卡。

Object Tab 和 Object Tab Group 均可停靠和取消停靠。有关详细信息，请参阅 [“Docking and undocking views and Object Tabs”一节](../../02-入门/04-个性化您的工作空间/02-处理布局/01-Docking-and-undocking-views-and-Object-Tabs.md "Docking and undocking views and Object Tabs") 章节。

---