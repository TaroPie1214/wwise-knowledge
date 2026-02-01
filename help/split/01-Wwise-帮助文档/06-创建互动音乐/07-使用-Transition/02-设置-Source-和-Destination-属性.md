# 设置 Source 和 Destination 属性

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [创建互动音乐](../00-创建互动音乐.md) > [使用 Transition](00-使用-Transition.md) > 设置 Source 和 Destination 属性

## 设置 Source 和 Destination 属性

在默认情况下，过渡时会直接从某个音乐对象切换到另一音乐对象。过渡规则的强大之处在于您可以自定义 Source（源）和 Desitination（目标）对象，并创建独特的音乐过渡。通过设置 Source 和 Desitination 属性，可以使对象间的过渡听起来平滑、流畅。

为了让对象间的过渡更加灵活可控，可以为 Source 和 Desitination 分别设置多个不同的 Exit（切出）点和 Entry（切入）点。您也可以在 Desitination 对象中选择随机时刻切入。这样按照过渡规则播放时每次切入点都不同，可以减少过渡的重复听感。

设置 Source 和 Desitination 属性时，请注意这些属性仅对该过渡规则有效。例如，假设您的过渡矩阵中存在从 Happy Music（愉快情绪）到 Sad Music（悲伤情绪）的过渡规则，以及从 Happy Music 到 Scary Music（恐惧情绪）的过渡规则。如果希望两个规则中 Happy Music 源都在第一个 Custome Cue（自定义提示点）切出，就需要在两个规则中分别设置。

|  |  |
| --- | --- |
| [备注] | 备注 |
| Source 和 Desitination 允许设置多种属性，但具体属性是否可用将取决于对象和所属容器的类型。 |

**设置 Source 属性的方法如下：**

1. 将 Music Switch Container 或 Music Playlist Container 加载至 Property Editor 中。
2. Switch to the Transitions tab of the Secondary Editor.
3. 选中过渡矩阵中的过渡规则。

   接下来，就可以编辑此过渡规则的 Source 属性了。
4. 如果 Source 对象位于切换容器内，请从 **Exit source at** （切出点）列表中选择下列之一：

   **Immediate（立刻）：**立即停止播放 Source。

   **Next Grid（下一网格线）：**在下一个网格线停止播放 Source。通过 Grid（网格线），可以按任意间隔长度来划分音乐对象。

   **Next Bar（下一小节）：**在下一小节停止播放 Source。

   **Next Beat（下一拍）：**在下一拍停止播放 Source。

   **Next Cue（下一提示点）**：在下一个提示点停止播放 Source，可以是 Custom Cue，也可以是 Exit Cue（出口提示点）。

   **Next Custom Cue（下一自定义提示点）**：在下一个 Custom Cue 停止播放 Source。如果当前 Music Segment（音乐段落）不包含 Custom Cue，则 Wwise将继续播放下一段落，直到遇到 Custom Cue 为止。

   **Exit Cue（出口提示点）：**在出口提示点处停止播放 Source。
5. 如果您选择 Next Cue 或 Next Custom Cue，就可以在 **Match** 文本框中输入提示点名称，精确筛选对该过渡规则有效的提示点。
6. 如果过渡时希望播放 Source 的 Post-exit（后尾段），请选择 **Play post-exit**。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 仅当 Source 在 Exit Cue 退出，以及在 Exit Cue 处或其后淡出时才会播放 Source 的后尾段，否则过渡时将不会播放后尾段。 |
7. 如果 Source 结束时需要淡出，请选择 **Fade-out**。

**设置 Destination 属性的方法如下：**

1. 将 Music Switch Container 或 Music Playlist Container 加载至 Property Editor 中。
2. Switch to the Transitions tab of the Secondary Editor.
3. 选中过渡矩阵中的过渡规则。

   接下来，就可以编辑此过渡规则的 Destination 属性了。
4. 若 Destination 为 Music Playlist Container，则可选择要首先播放容器里的哪个条目。单击“浏览”按钮 **[...]**，并为 **Jump to**（跳转到）选项指定对应的条目。
5. 若 Destination 为 Music Switch Container，请从 **Sync to**（同步到）列表中选择以下选项之一：

   **Entry Cue（入口提示点）：**将从入口提示点处开始播放 Destination。

   **Same Time as Playing Segment（与现有音乐时间相同）：**Destination 开始播放的位置将与 Source 段落切出的时间点相同。例如，如果 Source 段落已经播了 10 秒，则 Destination 也将从 10 秒处开始播放。

   **Random Cue（随机提示点）**：从随机选择的提示点处开始播放 Destination。勾选该选项即选择了所有提示点，包括 Entry Cue（入口提示点）和所有 Custom Cue。

   **Random Custom Cue（随机自定义提示点）**：将从随机选择的 Custom Cue 处开始播放 Destination。如果段落中没有自定义提示点，则使用入口提示点。

   **Last Exit Position**（上次退出位置）：根据上次 Destination 的段落播了多久施加相应的时间偏置，然后再开始播放 Destination。例如，若上次 Destination 的第三个段落播了 15 秒，则将从 15 秒处开始播放 Destination。
6. 若选用了 Random Cue 或 Random Custom Cue，则可通过 Custom Cue Filter（自定义提示点筛选器）进一步精确筛选有效的开始位置。

   **Match（匹配名称）：**只有用了该名称的提示点才会被选为开始位置。

   **Match source cue name（匹配源提示点名称）：**仅当提示点与 Source 段落所用提示点名称相同时，才会作为开始位置。
7. 过渡时如果要播放 Destination 的 Pre-entry（前导段），请选择 **Play pre-entry（播放前导段）**。
8. 若在开始播放 Destination 时需要淡入，请选择 **Fade-in**（淡入）。

### 编辑淡变

Fade-in（淡入）和 Fade-out（淡出）是分别指派给 Destination（目标）和 Source（源）音乐对象的两个特殊属性。也可以用于 Transition Segment（过渡段落）的开头和结尾。音乐对象切入和切出时，您可以用淡变让过渡变得更为平滑，很能设置各淡变的长度，时间偏置及曲线形状，进一步修正淡变听感。

**To edit a fade-out:**

1. On the Transitions tab of the Secondary Editor, make sure **Fade-out** is selected, and then click **Edit**.

   **Music Fade Editor**（音乐淡变编辑器）将打开。
2. 在 **Time** 文本框中，键入淡出的持续时间。
3. 在 **Offset** 文本框中，可以指定 Exit Cue（出口提示点）到淡出结束的时长。
4. 在 **Curve** 列表中，选择淡出的曲线形状。

   音乐将按照指定的方式淡出。

**To edit a fade-in:**

1. On the Transitions tab of the Secondary Editor, make sure **Fade-in** is selected, and then click **Edit**.

   **Music Fade Editor**（音乐淡变编辑器）将打开。
2. 在 **Time** 文本框中，键入淡入的持续时间。
3. 在 **Offset** 文本框中，可以指定从淡入开始到 Entry Cue（入口提示点）的时长。
4. 从 **Curve** 列表中，选择淡入的曲线形状。

   这时音乐会按照指定的方式淡入。

---