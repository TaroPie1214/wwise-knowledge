# 处理 Control Surface Session 中的冲突

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用 Wwise](../00-使用-Wwise.md) > [使用控制设备](00-使用控制设备.md) > 处理 Control Surface Session 中的冲突

## 处理 Control Surface Session 中的冲突

多个活跃绑定可能会与其 Controller Assignment（控制器指派）发生冲突。注意，无法同时加载多个具有相同键位的绑定。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 通过 Control Surface Session 进行的绑定会从上到下进行加载。在发生冲突时，第一个绑定的优先级最高。这时仅会加载第一个存在冲突的绑定。 |

发现冲突时：

- Control Surface 工具栏中的分组名称旁会显示黄色三角。
- Control Surface Session 视图中的绑定旁会显示黄色消息。

处理冲突的方式有很多种：

- 将 Control Surface Session 视图中的绑定重新排序来更改优先级。
- 使用绑定条目上的快捷菜单来解决冲突。
- 针对其中一个存在冲突的绑定更改控制器指派。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 在有些情况下，可对同一分组中的不同绑定使用相同的控制器指派。例如，您可以创建一个 Effect View Group 用来绑定不同的效果器属性。因为 Effect Editor 每次只能加载一个效果器，所以各个绑定之间并不会发生冲突。 |

---