# 将 HDR Window 用作输入变量

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [完善工程](../../00-完善工程.md) > [管理输出](../00-管理输出.md) > [使用 HDR](00-使用-HDR.md) > 将 HDR Window 用作输入变量

### 将 HDR Window 用作输入变量

The HDR window position can be monitored by looking at the window meter in the HDR category of a bus. 您也可以为它的值指派一个游戏参数。然后就可以通过 RTPC 将该游戏参数映射至任何对象的任何属性。例如，您可以使用窗口位置来改变声音实例的数量上限。

**将游戏参数关联至 HDR 窗口位置的方法如下：**

1. 选中 HDR 总线，在 Property Editor 中察看其内容。
2. In the **Window Top Output Game Parameter** group, browse
   for a Game Parameter.
3. 在 HDR 总线输入中设置游戏参数的范围（单位为分贝）。

You can now monitor the HDR window for that Game Parameter.

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| You can also define a Switch Group that is connected to a Game Parameter used to monitor the Window Top. 有关详细信息，请参阅[“将 Game Parameter 值映射到 Switch”一节](../../../04-与游戏互动/04-使用-Switch/02-将-Game-Parameter-值映射到-Switch.md "将 Game Parameter 值映射到 Switch")。 |

For more information on the HDR window, see [“理解 HDR”一节](../08-理解-HDR.md "理解 HDR").

---