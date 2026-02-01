# 自定义对象的 State 属性

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [与游戏互动](../../00-与游戏互动.md) > [使用 State](../00-使用-State.md) > [将 State 指派给对象和总线](00-将-State-指派给对象和总线.md) > 自定义对象的 State 属性

### 自定义对象的 State 属性

将 State Group 指派给对象后，您可以自定义该对象在各 State 下的属性。

**为对象自定义 State 属性值的方法如下：**

1. 将对象加载到 Property Editor 中。
2. Switch to the States tab of the Primary Editor.
3. 通过单击 **Properties**（属性）按钮来打开 **State Properties**（状态属性）对话框。
4. 选中受 State Group（状态组）影响的属性，然后单击 **OK**（确定）按钮。
5. 为各个 State（状态）设置属性值。

在工程中使用 State 之前，有必要先了解 State 值会如何与现有属性值和其他适用修改因子（如 RTPC）进行交互。

在将修改因子应用于现有属性值时，会按照以下某一方式决定最终属性值：

- **Absolute**（绝对值）：使用由 RTPC 决定的值，忽略对象的现有属性值。仅可应用一个 RTPC，不支持应用 State（状态）。
- **Sum All Values**（累加所有值）：将由 RTPC 或 State 决定的值添加到对象的现有属性值。
- **Use Highest Value**（使用最大值）：使用由 RTPC 和对象的现有属性值决定的最大值。
- **Boolean**（布尔值）：使用逻辑 OR 结合由 RTPC 或 State 决定的值。也就是说，若仅设置了一个 RTPC 或 State 值，则设置最终属性值。在这种情况下，会忽略对象的现有属性值。

应用修改因子时所用的方式决定是否使用对象的原始属性值。若属性为绝对值或布尔值，则禁用原始属性控制。否则，原始属性控制保持可用状态。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 应用修改因子时所用的方式是预定义的且无法更改。 |

|  |  |
| --- | --- |
| [备注] | 备注 |
| 有些属性可能具有 Sum All Values 或 Use Highest Value 设置。请参阅[“了解滤波器属性行为（LPF 和 HPF）”一节](../../../03-设置工程/06-Building-your-sound-and-motion-hierarchies/04-工程层级结构中的属性介绍/03-了解滤波器属性行为（LPF-和-HPF）.md "了解滤波器属性行为（LPF 和 HPF）") |

---