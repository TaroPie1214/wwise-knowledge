# 处理 Event

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [与游戏互动](../00-与游戏互动.md) > [管理 Event](00-管理-Event.md) > 处理 Event

## 处理 Event

由于在初始集成事件之后无需额外编程，所以您可以试用不同对象、更改现有对象属性、添加和删除动作以及更改动作属性，直到一切如您所愿为止。

### 重命名事件

在创建事件后 Wwise 会自动为该事件提供一个名称。这时最佳的做法是用更具描述性的名称对这个事件重新命名。各个事件不得重名，并且名称名称只能包含字母、数字和下划线。第一个字符必须是字母或下划线。

|  |  |
| --- | --- |
| [备注] | 备注 |
| Unless absolutely necessary, you shouldn't rename an Event after it has been integrated into the game. If you rename an Event after it has been integrated into a game, you must also update any instances of the name in the game. The Event will not work until you do this, including while remote connected in either of the Profile and Edit modes. |

**重命名事件的方法如下：**

1. 在 Event Editor（事件编辑器）中，在 **Name**（名称）字段内点击鼠标。

   该事件的名称处于突出显示状态。
2. 为事件键入新名称。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 您也可以在 Project Explorer 的 Events 选项卡中重命名事件。 |

### 从 Event 中移除 Action

在您试用和建立事件（Event）时，您可能需要从事件中删除若干个动作（Action）。只要事件名称不更改，您可以删除动作而无需额外编程。

**删除 Event 中的 Action**

1. 在 Event Editor 中，选择要从 Event 中删除的 Action。
2. 点击 **Remove**（移除）按钮。

   该动作于是就从事件中删除了。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 您也可以删除 Event 中的 Action，方法是选择 Action 并按 Delete 键，或者选择 Action 快捷菜单中的 Delete选项。 |

### 替换指派给 Event Action 的目标

您可能需要用其它对象替换特定对象，以判断它们在游戏中是否合适。即使在事件已集成到游戏中后，您仍可自由试用不同声音、动作、振动以及动作（Action）等。

**替换指派给 Action 的目标对象的方法如下：**

1. 在事件编辑器中，选择要为其替换对象的动作。
2. 点击 **Browse**（浏览）。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | **Browse** 按钮位于 Event Editor 的底部；不过，在从 Target 列的快捷菜单选择 Set Target 时也会显示 **Browse** 选项。 |

   或打开所选 Action 目标的快捷菜单。

   此时将会显示 Project Explorer - Browser。
3. 浏览层级结构并选择要指派给 Action 的新对象。
4. 单击 **OK**（确定）。

   Action 的新目标对象将显示在 Target 列中。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 将适用于 Action 类型的对象从 Project Explorer 拖至 Event Editor 中的 Event Action，替换 Action 的目标。Action 的新目标对象将显示在 Target 列中。  如果对象不适合 Action，则无法拖动它。 |

### 在 Schematic View 中显示 Event 的对象

如果要查看 Event 中包含的特定对象的工程结构或管线，可通过 Schematic 视图进行快速显示。

**在 Schematic 视图中显示 Event 目标对象管线的方法如下：**

1. 在 Event Editor 中，右键单击要查看其管线的目标对象。

   此时将会显示快捷菜单。
2. 点击 **Show in Schematic View**（显示在对象网络图中）。

   The sound or music 管线 is displayed in the Schematic view.

### 删除 Event

如果您不再需要某事件，则可以将其删除。在删除某个事件之前，您可能会需要验证它是否被团队中其它成员用在工程中的其它部分，以及它是否已包含在其中一个 SoundBank 中了。如果您或团队中的其他人删除了某个包含在 SoundBank 中的事件，那么这样会产生一个无效的事件。Wwise 不会自动从 SoundBank 中删除事件或其它无效工程元素，因此您将需要手动删除它们。为了帮助您在 SoundBank 内找到这些类型的事件和对象结构，Wwise 会通过 SoundBank 编辑器的 Add（添加）选项卡在名称之后添加单词“Missing”（缺失）。有关无效事件的详细信息，请参阅[“从 SoundBank 中移除工程元素”一节](../../07-完善工程/07-管理-SoundBank/03-使用-User-defined-SoundBank/04-管理-SoundBank-内容/07-从-SoundBank-中移除工程元素.md "从 SoundBank 中移除工程元素")。

**删除事件的方法如下：**

1. 执行以下操作之一：

   - 在 Project Explorer 的 Events 选项卡中，右键点击要删除的事件，然后从快捷菜单中选择 **>Delete Selection**。
   - 在 Event Viewer 中，点击要删除的事件，然后按 **Delete** 键。

   于是事件删除掉了。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 如果您误删除了某事件，则可以撤消删除，方法是按 **Ctrl+Z** 或点击 **Edit** > **Undo**。 |

---