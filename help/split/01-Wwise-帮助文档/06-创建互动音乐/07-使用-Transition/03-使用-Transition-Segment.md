# 使用 Transition Segment

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [创建互动音乐](../00-创建互动音乐.md) > [使用 Transition](00-使用-Transition.md) > 使用 Transition Segment

## 使用 Transition Segment

为了让过渡的效果更好，有时会另选一段音乐，让它在 Source（源）结束前就开始播放，并持续到 Destination（目标）开始之后。连接所用的这段音乐叫做 Transition Segment（过渡段），在 Wwise 中的所有过渡中都可以使用。下图说明了从 Source 对象到 Destination 对象的过渡中，Transition Segment 将如何播放。

|  |
| --- |
|  |

用户也可以用 Source 对象、Destination 对象及 Transition Segment 三者的 Pre-entry（前导段）与 Post-exit（后尾段）进行组合，让过渡更加平滑无缝。

任何 Music Segment（音乐段落）都可以作为过渡段 ，关于如何创建段落，请参阅 [*使用 Music Track 和 Music Segment*](../04-使用-Music-Track-和-Music-Segment/00-使用-Music-Track-和-Music-Segment.md "使用 Music Track 和 Music Segment")。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 如果过渡段所在的 Work Unit（工作单元）已从工程中卸载，该过渡段将显示为黄色。 |

**使用 Transition Segment 的方法如下：**

1. 将 Music Switch Container 或 Music Playlist Container 加载至 Property Editor 中。
2. Switch to the Transitions tab of the Secondary Editor.
3. 选中过渡矩阵中的过渡规则。
4. 选中 **Use transition segment**（使用过渡段落）。
5. 执行以下操作之一：

   - 将段落从 Project Explorer 拖至 **Transition Segment** 中。

     ![](../../../../images/btn_browse_icon.png)
   - 点击 **Browse** 按钮 (...)，在 Project Explorer - Browser 中选择段落。
6. 如果要播放过渡段的 Pre-entry，请勾选 **Play pre-entry**。
7. 如果播放过渡段时需要淡入，请勾选 **Fade-in**。
8. 如果要播放过渡段的 Post-exit，请勾选 **Play transition post-exit**。
9. 如果停止过渡段时需要淡出，请选择 **Fade-out**。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 如需详细了解如何编辑 Transition Segment 的 Fade-in 和 Fade-out 属性，请参阅[“编辑淡变”一节](02-设置-Source-和-Destination-属性.md#editing_fades "编辑淡变")。 |

---