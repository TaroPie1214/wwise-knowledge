# 将 Sub-Track 与 Switch 和 State 关联

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [创建互动音乐](../00-创建互动音乐.md) > [使用 Music Track 和 Music Segment](00-使用-Music-Track-和-Music-Segment.md) > 将 Sub-Track 与 Switch 和 State 关联

## 将 Sub-Track 与 Switch 和 State 关联

为了增加配乐的多样性，可以通过切换开关组（Switch Group）/状态组（State Group）来决定播放哪些子音轨。为此，必须将 Track Type 设置为 Switch。有关如何使用这些上述行为和音轨的详细信息，请参阅 [“定义 Music Track 的播放行为”一节](01-定义-Music-Track-的播放行为.md "定义 Music Track 的播放行为")。

要将子音轨关联至切换开关/状态，必须先为音轨选择切换开关组/状态组。The track's Switch/State Group is selected via the controls in the **Switch Type** box of the track's Property Editor.

通过 Transitions （过渡）选项卡设置音轨随切换开关/状态改变而发生的变化行为。有关如何使用过渡的详细信息，请参阅 [*使用 Transition*](../07-使用-Transition/00-使用-Transition.md "使用 Transition")。

**将子音轨关联至切换开关/状态的方法如下：**

1. 右键点击子音轨的标题栏（黄色栏）。
2. 在快捷菜单中选择 **Association**。
3. 选择现有切换开关/状态，或新建一个切换开关/状态。

   子音轨将被关联至该切换开关/状态。

   切换开关/状态名称将显示在子音轨顶部。

---