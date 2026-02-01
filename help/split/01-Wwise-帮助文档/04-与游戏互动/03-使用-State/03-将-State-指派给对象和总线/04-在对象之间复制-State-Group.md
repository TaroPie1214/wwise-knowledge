# 在对象之间复制 State Group

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [与游戏互动](../../00-与游戏互动.md) > [使用 State](../00-使用-State.md) > [将 State 指派给对象和总线](00-将-State-指派给对象和总线.md) > 在对象之间复制 State Group

### 在对象之间复制 State Group

若要为多个不同的对象使用相似的 State Group，可为某个对象定义 State Group，然后将这些 State Group 及关联 State、属性和 State 值复制到另一对象。You can copy and paste State Groups between different object types, including between the Busses and Containers hierarchies.

**复制 State Group：**

1. In the States tab of the Primary Editor, select all of the State Groups you want to copy. 只需在按住 Ctrl 的同时在 State Group 或关联 State 的任意位置单击即可选中。
2. 右键单击并在快捷菜单中选择 **Copy**（复制）或者按下 **Ctrl+C**。
3. 在目标对象的 States（状态）选项卡中，右键单击并在快捷菜单中选择 **Paste**（粘贴）或者按下 **Ctrl+V**。

   这时会将 State Group 及关联 State、属性和 State 值复制到目标对象。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 若已将某个 State Group 指派给目标对象，则：  - 同时在源 State 和目标 State 中自定义的属性的所有 State 值都会在目标 State 中改写。 - 所有在源对象中自定义而未在目标对象中自定义的属性都会被复制到目标对象。 - 在目标对象中自定义而未在源对象中自定义的属性的所有 State 值都会设为 0 或禁用。 |

   之后便可根据需要修改复制的内容（参见“[“自定义对象的 State 属性”一节](02-自定义对象的-State-属性.md "自定义对象的 State 属性")”）。

---