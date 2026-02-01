# 在 State 之间复制属性值

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [与游戏互动](../../00-与游戏互动.md) > [使用 State](../00-使用-State.md) > [将 State 指派给对象和总线](00-将-State-指派给对象和总线.md) > 在 State 之间复制属性值

### 在 State 之间复制属性值

若要为多个 State 使用相似的 State 值，可定义相应设置一次，然后将 State 值复制到其他 State。以下章节描述了两种可用方式：

- [“Copying State values to States in any State Group”一节](03-在-State-之间复制属性值.md#copying_state_values_to_any_group "Copying State values to States in any State Group")
- [“Copying State values within the same State Group”一节](03-在-State-之间复制属性值.md#copying_state_values_within_group "Copying State values within the same State Group")

#### Copying State values to States in any State Group

Using this method, you can copy and paste State values between different State Groups and between different object types, including between the Busses and Containers hierarchies. 甚至，还可选择多个目标对象并将值一键粘贴到所有目标对象。

**将 State 值复制到任意 State：**

1. In the States tab of the Primary Editor, select the State whose values you want to copy.
2. 右键单击并在快捷菜单中选择 **Copy**（复制）或者按下 **Ctrl+C**。
3. 在与目标对象对应的 States（状态）选项卡中，选择要将 State 值复制到的所有 State。
4. 右键单击并在快捷菜单中选择 **Paste**（粘贴）或者按下 **Ctrl+V**。针对所有目标对象重复步骤 3 和 4。

   这时会将 State 值复制到目标对象。之后便可根据需要自定义复制的内容（参见“[“自定义对象的 State 属性”一节](02-自定义对象的-State-属性.md "自定义对象的 State 属性")”）。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 所有在源对象中自定义而未在目标对象中自定义的属性都会被复制到目标对象。在目标对象中自定义而未在源对象中自定义的属性的所有 State 值都会设为 0 或禁用。 |

#### Copying State values within the same State Group

Using the Copy State Values dialog, you can copy the values of a State to an existing or newly-created State within the same State Group. 另外，还可指定哪些与 State Group 关联的对象会受源对象的 State 值影响。

**在同一 State Group 内复制 State 值：**

1. 在以下任一视图中单击 **Copy State Values** 按钮：

   - States tab in the Primary Editor.
   - Mixing Desk。

   The Copy States Values dialog opens.

   |  |  |
   | --- | --- |
   | [技巧] | 技巧 |
   | You can also right-click a State and select **Copy State Values** from either the States tab of the Primary Editor or from within the Mixing Desk. |
2. 点击 **State Group** 选择器（**>>**），并选择要复制自定义属性值的 State 所在的 State Group。
3. 点击 **From** 选择器（**>>**），并选择要复制自定义属性值的 State。

   采用该 State Group 的所有对象都将显示在 Affected Object 列表中。
4. 点击 **To** 选择器（**>>**），并执行下列操作之一：

   - 要将自定义属性值复制到新 State，请选择 **New**，为新 State 命名并点击 **OK**。
   - 要将自定义属性值复制到现有 State，则只需从列表中选择该 State 即可。

   Wwise 将分别处理 **Affected Object** 列表中的对象。
5. 在 **Use**（使用）列中，针对所有要使用新的 State（状态）设置的对象选中复选框。
6. 单击 **OK**（确定）来将 State（状态）设置应用于所选对象。

---