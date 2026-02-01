# 使用 Stinger

[Wwise 帮助文档](../00-Wwise-帮助文档.md) > [创建互动音乐](00-创建互动音乐.md) > 使用 Stinger

## 使用 Stinger

为了让互动音乐给游戏提供更多反馈，您可以在游戏关键时刻播放 Stinger（插播乐句）。Stinger 是一种简短乐句，可以与当前播放的音乐叠加并混合播放。游戏会调用与 Stinger Music Segment（插播乐句音乐段落）相关联的 Trigger（触发器），从而播放 Stinger。关于使用 Trigger 的详细信息，请参阅 [*使用 Trigger*](../04-与游戏互动/06-使用-Trigger.md "使用 Trigger")。

假设前面例子中勇敢的考古学家正在探索神庙并忙着搜寻遗迹。在其一边漫步一边考察周边环境时，会播放探索音乐。在找到宝藏时则会播放一小段别的音乐，来彰显这一振奋人心的发现。但探索音乐不会停止，游戏会调用 Trigger，让一个名为“Found it”的 Stinger 与当前音乐叠加播放，来表示这是重要时刻。Stinger 播完后，探索音乐将继续播放。

|  |
| --- |
|  |

要让 Stinger 与当前音乐叠加播放，需进行以下操作：

- 将音乐对象与 Trigger 关联。
- 将 Music Segment 映射至 Trigger，从而创建 Stinger。
- Define how the Stinger will play back.

## Using Stingers with music hierarchies

Since Stingers can be created at different levels in the hierarchy, you can assign the
same Trigger to different segments. This means that while the top-level music object might use a
Trigger called, "Treasure", any of its child objects can also use the "Treasure"
Trigger. In this case, the child object would associate the "Treasure" Trigger with a
different segment. This automatically overrides the parent Trigger/Stinger association and
increases the range of Stingers that you can play at important moments in the game. Since only
one Stinger can play for a specific Trigger in the hierarchy of music objects, it is the
associated Stinger of the currently playing child object that will play.

## 添加 Stinger

You can create Stingers for music objects in the Stingers tab of the music object Primary Editor. Wwise 允许通过两种方式添加 Stinger：

- 在 Project Explorer（工程资源管理器）中进行拖放。
- Using the buttons in the Primary Editor.

您可以任选其一，也可结合使用。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 如果 Stinger 关联的段落已从工程中卸载，该段落将高亮显示为黄色。 |

**从 Project Explorer 中拖拽添加 Stinger 的方法如下：**

1. Load a music object into the Property Editor and switch to the Stingers tab of the
   Primary Editor.
2. From the Game Syncs tab of the Project Explorer, drag a Trigger to the Stingers list.

   Stinger 将自动创建，并由刚刚拖拽的 Trigger 触发。默认情况下，Trigger 不会关联至任何 Music Segment（音乐段落），即显示 Nothing（无段落）。
3. 要将 Music Segment 与 Trigger 关联，请切换至 Project Explorer 的 Audio（音频）选项卡，然后将 Music Segment 拖至 Segment to Play（要播放的段落）一栏。

   该 Music Segment 将替换默认“Nothing”选项，并与该 Trigger 关联。
4. 在 Play At（播放位置）列中选择以下选项之一，来定义何时播放段落：

   - **Immediate** —— 立即切换状态。如果为 Music Track（音乐轨）设置了 Look-ahead Time（预读时间），则须等到这段时间过后才能播放该 Stinger。
   - **Next Grid** -- 下一网格线。在下一网格线处播放 Stinger。通过 Grid，可以按想要的频率将音乐对象进行虚拟划分。
   - **Next Bar** -- 下一小节。在下一小节处播放 Stinger。
   - **Next Beat** -- 下一拍。在下一拍播放 Stinger。
   - **Next Cue** -- 下一提示点。在下一提示点处播放 Stinger。下一提示点可以是 Entry Cue（入口提示点）、Exit Cue（出口提示点）或者 Custom Cue（自定义提示点）。
   - **Next Custom Cue** -- 下一自定义提示点。在下一个自定义提示点处播放 Stinger。
   - **Entry Cue** -- 入口提示点。在入口提示点处播放 Stinger。
   - **Exit Cue** -- 出口提示点。在出口提示点处播放插播乐句。
5. Repeat steps 2-4 to continue adding Stingers as needed.

**To insert a Stinger using the buttons in the Primary Editor:**

1. On the Stingers tab of the Primary Editor, click **Add**.

   这时会打开 Project Explorer - Browser（工程资源管理器 - 浏览器）对话框。
2. 选择要指派给音乐对象的 Trigger，并单击 **OK**（确定）。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 要为 Stinger 选择其它 Trigger，请在 Trigger 列中点击 **选择器** 按钮（>>），浏览并选择所需的 Trigger。 |
3. 选择 Trigger 并单击 **OK**。

   Trigger 将添加至 Stinger。
4. 在 **Segment to Play** 列中，点击 "Browse" 按钮 (...)。

   Project Explorer-Browser 将打开。
5. 转到要使用的段落，并单击 **OK**。

   该段落将添加至 Stinger。
6. - **Immediate** —— 立即切换状态。如果为 Music Track（音乐轨）设置了 Look-ahead Time（预读时间），则须等到这段时间过后才能播放该 Stinger。
   - **Next Grid** -- 下一网格线。在下一网格线处播放 Stinger。通过 Grid，可以按想要的频率将音乐对象进行虚拟划分。
   - **Next Bar** -- 下一小节。在下一小节处播放 Stinger。
   - **Next Beat** -- 下一拍。在下一拍播放 Stinger。
   - **Next Cue** -- 下一提示点。在下一提示点处播放 Stinger。下一提示点可以是 Entry Cue（入口提示点）、Exit Cue（出口提示点）或者 Custom Cue（自定义提示点）。
   - **Next Custom Cue** -- 下一自定义提示点。在下一个自定义提示点处播放 Stinger。
   - **Entry Cue** -- 入口提示点。在入口提示点处播放 Stinger。
   - **Exit Cue** -- 出口提示点。在出口提示点处播放 Stinger。
7. 根据需要继续添加 Stinger。

## 定义 Stinger 的播放设置

在为音乐对象创建 Stinger 后，可定义特定的设置来控制 Stinger 在游戏中如何播放。要使 Stinger 达到最佳效果，需要考虑以下两个问题：

- **播放 Stinger 后，要等多长时间才能再次播放**。Stinger 的作用是增加音乐编曲的表现力，因此播放时一定不要过多、过频繁，以免弱化其作用。
- **段落所剩时间不足以播放 Stinger 时怎么办。** 如果 Trigger 调用了 Stringer，但在播放时机到来前当前段落就会结束，则不会播放该 Stinger。不过，可选择在播放列表的下一段落中首次遇到符合条件的机会时播放该段落。如果未勾选该选项，该 Stinger 将终止。

**定义 Stinger 播放设置的方法如下：**

1. On the Stingers tab of the Primary Editor, in the **Don't play this Stinger again for x seconds** field, type the number of seconds that must elapse before the Stinger can play again. 若 Trigger（触发器）在指定时间内调用该 Stinger，则该 Trigger 将被忽略。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | “don't play stinger again for（不要再次播放插播乐句）”的起始时间指的是 Stinger 的同步点，即 Stinger 段落入口提示点的时间。 |
2. 若当前段落剩余时间不够而需在下一段落中播放 Stinger，请选中 **Allow playing the Stinger in next segment**（允许在下一段落中播放插播乐句）选项。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 若未选中该选项，则 Stinger 将被终止。 |

## 移除 Stinger

您可以删除不需要的 Stinger（插播乐句）。

**从 Stinger 列表中移除 Stinger 的方法如下：**

1. 在 Stingers 选项卡中，选择要移除的 Stinger。
2. 点击 **Remove**（删除）。

   所选 Stinger 将从列表中移除。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 在删除 Stinger 时，不会影响关联的 Trigger（触发器）或 Music Segment（音乐段落）。 |

## 预览 Stinger

创建 Stinger（插播乐句）段落后，可以在 Transport Control（播放控制）中单独预览该段落或与其它段落一起试听，从而验证叠加播放效果。Stinger 允许在不同层级中创建，因此您可以为同一 Stinger 进行不同的段落设置。Only one Stinger, however, may play for a specific Trigger in the hierarchy of music objects and it is the child object that determines which Stinger will play. For example if you created a Stinger using the Trigger “Treasure” at the Music Switch Container level, and used the same Trigger “Treasure” for a Stinger in the child object Playlist Container, and then you loaded the Music Switch Container in the Transport Control, and called the Trigger, only the Playlist Container Stinger would play.

In addition, you can also create simulations in the Soundcaster and profile your simulation in the Profiler to monitor performance issues. 关于模拟和性能分析的详细信息，请参阅：

- [“Building simulations”一节](../07-完善工程/03-创建模拟/01-Building-simulations.md "Building simulations")
- [“使用 Performance Monitor 进行监控和故障排查”一节](../07-完善工程/06-性能分析/09-使用-Performance-Monitor-进行监控和故障排查.md "使用 Performance Monitor 进行监控和故障排查")

|  |  |
| --- | --- |
| [备注] | 备注 |
| 如果 Stinger 关联的段落已从工程中卸载，该段落将高亮显示为黄色。您将无法预览该 Stinger，除非其所在的 Work Unit（工作单元）被重新加载至工程。 |

**在 Transport Control 中预览 Stinger 的方法如下：**

1. 将 Stinger 段落加载至 Transport Control。

   |  |
   | --- |
   |  |
2. 点击 **Play** 图标。

   Stinger 段落将播放。

**预览 Stinger 与当前音乐叠加播放效果的方法如下：**

1. 将音乐对象加载至 Transport Control。
2. 点击 **Play** 图标。

   Transport Control 中的音乐对象将播放。
3. 在 Game Syncs 区域中，点击 **Triggers** 按钮来显示列表。

   |  |
   | --- |
   |  |
4. 点击 **Call Trigger**（调用触发器）图标。

   相应的 Stinger 将与当前音乐对象叠加播放。您可以继续选择其他 Trigger 并播放与之对应的 Stinger 来试听其在游戏中的效果。

---