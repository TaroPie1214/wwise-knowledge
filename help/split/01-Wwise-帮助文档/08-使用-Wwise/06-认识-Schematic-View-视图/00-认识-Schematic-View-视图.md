# 认识 Schematic View 视图

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用 Wwise](../00-使用-Wwise.md) > 认识 Schematic View 视图

## 认识 Schematic View 视图

The Schematic View displays a graphical representation of the structure of your Wwise
project. You can use the Schematic View to get an overview of a project, locate project objects,
or analyze project structure one object at a time. The Schematic View includes icons
representing each project object, the object names, and lines and nodes representing their
relationships. You can customize how the Schematic View displays project object details as
well.

![](../../../images/schematic_view.png)

## Identifying project objects and connectors

The Schematic View is made up of icons representing project objects and connectors representing their relationship to one another. 下表描述了工程对象之间的连线。有关代表工程对象的图标的信息，请参阅[“理解 Wwise 中的视觉元素”一节](../../02-入门/03-Wwise-界面基础知识/01-理解-Wwise-中的视觉元素.md "理解 Wwise 中的视觉元素")。

| 图标 | 名称 | 描述 |
| --- | --- | --- |
| |  | | --- | |  | | 实线 | 这些线用于连接父对象和子对象。 |
| |  | | --- | |  | | 虚线 | 此类线用于将总线连接到子对象，以演示通路。 |
| |  | | --- | |  | | 加号（白色） | 点击将展开示意图，并显示对象的所有子项。 |
| |  | | --- | |  | | 加号（黄色） | 如果当前没有显示对象的所有子项，则点击它将显示所有子项。  |  |  | | --- | --- | | [备注] | 备注 | | 若针对其他对象选中了 **Show in Schematic View** 或子对象与当前搜索条件不匹配，则将隐藏子对象。 | |
| |  | | --- | |  | | 减号 | 点击它将折叠对象的所有子项。 |

## Setting the Schematic View display options

您可以通过使用 Schematic View Setting 来自定义示意图中各个工程对象要显示的信息。

**To specify the information to be displayed in the Schematic View:**

1. Click the options icon in the upper right corner of the Schematic View.

   The Schematic View Settings dialog opens.
2. 从以下信息类型中选择：

   - **Icon Strip** —— 显示一排代表对象属性的图标。如果对象属性已经改变，则图标显示为白色，您则可以将鼠标悬浮在它上方以了解详细信息。如果属性仍为默认值，图标则会变成灰色。
   - **Mute/Solo** —— 显示各个对象的静音和 Solo 按钮。
   - **Bus** —— 显示为对象指定通路的总线。
   - **Conversion Setting** ——显示对象正在使用的转码设置 ShareSet。
   - **Effect** —— 显示已应用到对象的任何效果器。
   - **Positioning Type**（定位类型）：显示应用于对象的定位类型（No Positioning、3D Emitter、3D Emitter with Automation、3D Listener with Automation）。
   - **Game Parameters**（游戏参数）：显示通过 RTPC 影响对象的 Game Parameter。
   - **State Group** —— 显示对象指定的状态组。
   - **Advanced Settings** —— 显示对对象高级设置所做的任何更改（例如播放数限制或音量阈值）。
   - **Volume** —— 显示指定到对象的音量。
   - **Pitch** —— 显示指定到对象的音高。

     |  |  |
     | --- | --- |
     | [备注] | 备注 |
     | 不显示音乐对象的音高，因为音高不适用于它们。 |
   - **Low Pass** —— 显示指定到对象的低通滤波器。
3. 单击 **OK**（确定）。

   Schematic View 显示您为各个工程对象选择的信息。

## Searching for project objects

You can find a project object quickly in the Schematic View by using the Search
function.

**To search for a project object in the Schematic View:**

1. 在 **Search** 字段中，输入您要查找到的工程对象的名称。

   此时，Wwise 会高亮显示与所输入名称匹配的工程对象，并隐藏不相关的对象。
2. Click **Reset** to erase the Search field and reset the
   Schematic View.

|  |  |
| --- | --- |
| [备注] | 备注 |
| 搜索不区分大小写，在您输入搜索项的同时开始查找对象。搜索引擎从字首开始检查，因此当输入“gun”时将找到“gun”、“big\_gun”和“gunner”，而不是“shotgun”。 |

## Showing project objects

You can simplify the project schema presented in the Schematic View by specifying one
project object to be highlighted.

**To highlight a project object in the Schematic View:**

1. In the Schematic View, right-click a project object.

   此时将会显示快捷菜单。
2. 从快捷菜单中选择 **Show in Schematic View**。

   此时将显示选定对象的总线通路。对象高亮显示，并且无关的对象被隐藏。
3. To reset the Schematic View, click **Clear**.

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| You can also drag an object from the Project Explorer to show it in the Schematic View. 还可以在 Property Editor 或 Contents Editor 中点击右键，然后选择 **Show in Schematic View**。 |

## Editing project objects directly

You can use the controls displayed under each project object in the Schematic View to edit the object. 这些控件的工作原理与 Property Editor 中的控件相同。有关如何使用这些控件的详细信息，请参阅[*Wwise 界面基础知识*](../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md "Wwise 界面基础知识")。

|  |
| --- |
|  |

使用 Schematic View Setting 显示这些控件。有关这些设置的详细信息，请参阅[“Setting the Schematic View display options”一节](00-认识-Schematic-View-视图.md#setting_schematic_view_display_options "Setting the Schematic View display options")。

## Editing project objects in the Property Editor

If you prefer to edit object properties directly, you can quickly open the Property
Editor for a project object from the Schematic View.

**为工程对象打开 Property Editor 的方法是：**

1. In the Schematic View, right-click a project object.

   此时将会显示快捷菜单。
2. 从快捷菜单中选择 **Edit**。

   此时将为该工程对象打开 Property Editor 。

|  |  |
| --- | --- |
| [备注] | 备注 |
| You can leave the Schematic View open while you work in this Property Editor. The changes you make to a project object in the Property Editor are reflected immediately in the Schematic View. |

**相关主题**

- [Wwise Fundamentals Module 13: Submixing with Additional Audio Busses](https://www.audiokinetic.com/en/courses/wwise101/?source=wwise101&id=submixing_with_additional_audio_busses)

---