# 为 State Group 内的 State 之间的切换设置过渡

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [与游戏互动](../00-与游戏互动.md) > [使用 State](00-使用-State.md) > 为 State Group 内的 State 之间的切换设置过渡

## 为 State Group 内的 State 之间的切换设置过渡

为了同一 State Group（状态组）内各 State（状态）之间能平滑过渡，您可以定义状态过渡的时长。设置过渡时长时，有两个选项：

- [“Defining transitions for all States in a State Group”一节](02-为-State-Group-内的-State-之间的切换设置过渡.md#defining_transitions_for_all_states_in_state_group "Defining transitions for all States in a State Group")为 State Group 中所有 State 切换设置相同的过渡时长。
- [“Customizing transitions between States in a State Group”一节](02-为-State-Group-内的-State-之间的切换设置过渡.md#customizing_transitions_between_states_in_state_group "Customizing transitions between States in a State Group")为 State Group 内的 State 切换设置不同的过渡时长。

### Defining transitions for all States in a State Group

您可以为 State Group（状态组）内的所有 State（状态）切换设置统一的过渡时长。

**为选定 State Group 中所有 State 切换设置过渡时长的方法如下：**

1. 在 Project Explorer 中，切换至 Game Syncs 选项卡。
2. 在 States 层级中，双击 State Group 将其加载到 Property Editor 中。
3. In the **Default Transition Time** field, define a
   transition time for all the States in the selected State Group.

|  |  |
| --- | --- |
| [备注] | 备注 |
| 如果未定义 Custom Transition Time，将使用默认过渡时间。 |

### Customizing transitions between States in a State Group

为让游戏中的 State 改变更逼真，您可能不希望 State Group 内所有 State 切换时过渡时间都相同。在 Custom Transition Time（自定义过渡时间）列表中，可以为任意两个 State 间的切换定义特殊的过渡时长，反向切换时，也可以采用相同的自定义过渡时长。例如，在 Rain State 切换至 Snow State 和反向切换时，可能希望其过渡时间相同。

**为选定 State Group 内 State 之间的切换设置自定义过渡时间的方法如下：**

1. 在 Project Explorer 中，切换至 Game Syncs 选项卡。
2. 在 States 层级中，双击 State Group 将其加载到 Property Editor 中。
3. In the Primary Editor, click **Insert**.

   Transition Time 列表中将新增一行。
4. 在 From 列中，选择源 State。
5. 在 Time 列中，设置两个 State 之间的过渡时间。
6. 在 To 列中，选定目标 State。
7. 要为两个切换方向设置相同的过渡时间，请勾选双向复选框（标记为：<->）。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 您可以点击 **Insert** 添加更多的自定义设置，如果要删除设置，请点击 **Remove**。 |

**相关主题**

- [Wwise Fundamentals Module 6: Using States](https://www.audiokinetic.com/en/courses/wwise101/?source=wwise101&id=using_states)

---