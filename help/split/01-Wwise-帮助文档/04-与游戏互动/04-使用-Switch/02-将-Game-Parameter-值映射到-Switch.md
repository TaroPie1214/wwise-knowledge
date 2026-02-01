# 将 Game Parameter 值映射到 Switch

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [与游戏互动](../00-与游戏互动.md) > [使用 Switch](00-使用-Switch.md) > 将 Game Parameter 值映射到 Switch

## 将 Game Parameter 值映射到 Switch

In Wwise, you can also use Game Parameter values to drive Switch changes. 创建 Switch Group 和 Game Parameter 后，就可以将参数值映射到 Switch。例如汽车碰撞声，如果您使用 RTPC 来驱动 Switch 切换，那么撞击声和振动效果可以根据冲击力大小而有所不同。通过用冲击力值来触发 Switch 切换，可以轻松确保在发生碰撞时播放正确的对象。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 将 Game Parameter 值映射到 Switch 之前，需要创建并定义游戏参数。关于创建和定义游戏参数的详细信息，请参阅[“Creating Game Parameters”一节](../05-使用-RTPC/02-管理-RTPC-中使用的-Game-Parameter.md#creating_game_parameter "Creating Game Parameters")。 |

**将 Game Parameter 值映射到 Switch 的方法如下：**

1. 在 Project Explorer 的 Game Syncs 选项卡中，双击想要通过游戏参数值来驱动的 Switch Group。

   Switch Group 将加载到 Switch Group Property Editor 中。
2. 勾选 **Use Game Parameter** 复选框。

   坐标图视图将启用，Y 轴将显示 Switch Group 中的 Switch 列表。
3. 在 Game Parameter 列表中，选择用于驱动 Switch 切换的游戏参数。

   X 轴将显示所选 Game Parameter 的值域。
4. 在坐标图视图中，双击 X 轴方向的 Game Parameter 曲线来添加点，然后拖拽该点至目标 Switch。

   Switch 的变化将映射到指定的游戏参数值。
5. 双击曲线来继续添加点，并映射到所需的 Switch。

---