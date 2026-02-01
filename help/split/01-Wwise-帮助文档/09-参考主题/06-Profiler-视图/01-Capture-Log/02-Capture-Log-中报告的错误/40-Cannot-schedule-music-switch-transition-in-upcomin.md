# Cannot schedule music switch transition in upcoming segments: using Exit Cue.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Cannot schedule music switch transition in upcoming segments: using Exit Cue.

#### Cannot schedule music switch transition in upcoming segments: using Exit Cue.

“无法在下一段落中安排音乐切换容器过渡: 使用出口提示点”。在 Music Switch Container（音乐切换容器）无法按照规定的过渡规则安排音乐过渡时，将出现此错误。比如，当前状态所对应的播放列表包含很短的段落，因为淡入/淡出或目标前导段很长，所以规则要求将过渡点设在很久以后。这时便会出现所述情况。播放列表无法提前安排 64 个以上的段落。

**推荐的解决步骤：**

- 调整淡变时间。
- 调整前导段时间。
- 降低 Music Switch Container 的复杂度。

---