# 使用 State

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [与游戏互动](../00-与游戏互动.md) > [使用 State](00-使用-State.md) > 使用 State

## 使用 State

State（状态）需要隶属于 State Group（状态组），才能供 Wwise 对象使用。可以按逻辑将各各种 State 划分成 State Group 来简化管理。例如，您可能会发现将与游戏主人公相关的 State 组合在一起非常有用。然后您可以创建一个名为 Main Character 的 State Group，向其中添加 State，再将这些 State 应用到与主人公相关联对象的属性上去。在游戏中，您知道主人公将可能经历以下 State：吃惊、镇定和高度紧张。将它们组合在一起，然后定义与单个 State 相关的属性变化非常有用。

|  |
| --- |
|  |

After you have set up your State structure, you can subscribe objects to State Groups in the
Primary Editor and customize the State properties as needed.

为了帮助您在界面中轻松找到 State Group 或 State，Wwise 使用独特的图标来标识它们。

| 图标 | 代表 |
| --- | --- |
| |  | | --- | |  | | State Group |
| |  | | --- | |  | | State（状态） |

### 创建 State Group

您可以在 Wwise 的以下两个位置之一创建您需要的所有 **State Group**：

- [Project Explorer](01-使用-State.md#to_create_new_state_group_for_project_from_project_explorer "在 Project Explorer 中为工程创建新 State Group 的方法是：")
- [States tab of the Primary Editor](01-使用-State.md#to_create_new_state_group_for_project_from_states_tab_of_property_editor "To create a new State Group for your project from the States tab of the Primary Editor:")

**在 Project Explorer 中为工程创建新 **State Group** 的方法是：**

1. 在 Project Explorer 中，切换至 Game Syncs 选项卡。
2. 在 **States** 层级中，执行以下操作之一：

   - 选择工作单元或虚拟文件夹，然后点击 Project Explorer 工具栏中的 **State Group**（对白事件）图标。
   - 右键点击工作单元或虚拟文件夹，然后在快捷菜单中点击 <**New Child > State Group**。

   新 State Group 将添加到列表中。
3. 将默认名称替换为更合适的名称。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | State Group 之间不能重名，并且仅包括字母、数字和下划线。只有字母或下划线可以作为首字符。 |
4. 根据需要，继续添加 State Group。

**To create a new State Group for your project from the States tab of the Primary
Editor:**

1. In the States tab of the Primary Editor, click **Add
   >>.**

   此时 State 的选择器菜单将打开。
2. Select **New**
3. 选择要创建新 State Group 的工作单元。
4. 在 Name 字段中，将默认名称替换成更合适的名称。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | State Group 之间不能重名，且只能包括字母、数字和下划线。只有字母或下划线可以作为首字符。 |
5. 点击 **OK** 以创建并采用新的 State Group。

### 创建 State

当游戏调用 State 时，State 会响应游戏条件，从而令对象的属性发生变化。State 间的过渡可以在 State Group Editor（状态组编辑器）中设置。

**创建新 State 的方法如下：**

1. 在 Project Explorer 中，切换至 Game Syncs 选项卡。
2. 在 States 层级中，执行以下操作之一：

   - 选择 State Group，并点击 Project Explorer 工具栏中的 **State** 图标。
   - 右键点击 State Group，并在快捷菜单中选择 **New Child > State**。

   新 State 将被添加到 State Group 中。
3. 将默认名称替换为更合适的命名。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 同一 State Group 中的 State 不能重名，且只能包括字母、数字和下划线。只有字母或下划线可以作为首字符。 |
4. 继续按需创建 State。

### 删除 State 或 State Group

您可能想要删除工程中不再需要的 State（状态）或 State Group（状态组）。记住，删除 State Group 也会删除其中所有的 State。State 删除后将不能再用于之前的对象和预设。

States are integrated in the game using one of two mechanisms:

- They can be integrated by calling an Event with a **Set State** action. In this case, deleting a State or State
  Group will create problems in Wwise as the called State will no longer be
  available.
- They can be integrated by calling the State Group and the State itself. In
  this case, the sound designer who intends to delete the State or State Group
  should advise the audio programmer of the change.

在删除前，请使用 State Group 快捷菜单中的 **Find All References**（查找所有关联）命令来查找哪些对象使用了该 State Group 。

**删除 State Group 的方法如下：**

1. 在 Project Explorer 中，切换至 Game Syncs 选项卡。
2. 在 **States** 层级中，右键点击要删除的 State Group 或 State，并选择 **Delete Selection**。

   选定的 State 或 State Group 将被删除。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 如果您误删了 State 或 State Group，可以按 **Ctrl+Z** 或点击 **Edit > Undo** 来撤消删除。 |

---