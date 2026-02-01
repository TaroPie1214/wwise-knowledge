# 使用 Transition

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [创建互动音乐](../00-创建互动音乐.md) > 使用 Transition

## 使用 Transition

要让互动音乐听起来很自然，关键在于音乐的 Transition（过渡）。没有平滑的过渡，游戏配乐就无法保持连续无缝的变化。将各段音乐粗暴地组合在一起会让人感到极不和谐，并会削弱游戏的真实感。要避免这些问题，可通过 Wwise 自定义音乐对象之间的过渡以尽可能做到无缝衔接。

每当一个音乐对象（称为 Source，即源对象）停止播放，后一个音乐对象（称为 Destination，即目标对象）开始播放，就需要加入平稳的过渡。您可以在各个段落或段落所在容器之间定义过渡。Each transition is carried out automatically by Wwise according to properties you define in the Transitions tab of the Secondary Editor.

您可以指定何时开始过渡以及是否为其加入淡变。另外，还可指定一段音乐作为 Transition Segment（过渡段落）并在过渡的过程中播放。

![](../../../images/transitions_tab2.png)

|  |  |
| --- | --- |
|  | Transition Matrix。 |
|  | Transition Segment 属性。 |
|  | Source 和 Destination 属性。 |

## 使用 Transition – 示例

假设您正在制作一款方块消除游戏。在游戏过程中，玩家时刻处于以下状态之一：游戏进行得很好（方块被快速清除），或游戏进行得很差（方块都堆在了一起）。您为每种情景都制作了很酷的音乐来最大限度地展示它们。为此，还得确保这两段音乐的过渡听起来自然、和谐。

为满足游戏需要，您可以创建名为 Puzzle Sounds 的 Music Switch Container（音乐切换容器），其中包含两个 Music Playlist Container（音乐播放列表容器），分别命名为 Calm 和 Panic。它们分别关联至两种游戏状态，反映游戏情况。在这两个 Playlist Container 之间实现良好过渡可以让游戏配乐引人入胜。下图显示了如何在游戏中实现过渡：

|  |
| --- |
|  |

在本例中，使用淡入和淡出曲线可以让 Playlist Container 之间的过渡变得平滑。两个容器之间的衔接将更加平缓、自然，而且还能避免在过渡时产生嘈杂的噪音。

---