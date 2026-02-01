# 将 State 指派给对象和总线

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [与游戏互动](../../00-与游戏互动.md) > [使用 State](../00-使用-State.md) > 将 State 指派给对象和总线

## 将 State 指派给对象和总线

为工程创建并设置 State 后，您可以将 State Group（状态组）和 State（状态）指派给对象和总线，用来让声音、音乐和振动与游戏中的场景相匹配。然后即可有针对性地调节各场景的声音、音乐或振动属性，以进一步区分。

对象须先采用 State Group，然后其中的所有 State 将自动指派到该对象。每个对象都可以采用多个 State Group。You can also assign State Groups at each level in the Busses and Containers hierarchies.

State 属性始终是相对的。When you apply a State, the effect on the object's properties will be cumulative.

|  |
| --- |
|  |

**将 State Group 指派给对象：**

1. 将对象加载到 Property Editor 中。
2. Switch to the States tab of the Primary Editor.
3. Click the group selector (**>>**) button and select the State Group that you want to assign to the object.

   相关 State 将出现在列表中，对象将采用选定 State Group 中的 State。

---