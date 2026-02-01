# Media ... could not be updated from Wwise Project. Previous media, if available, will be used.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Media ... could not be updated from Wwise Project. Previous media, if available, will be
used.

#### Media ... could not be updated from Wwise Project. Previous media, if available, will be used.

“无法通过 Wwise 工程更新媒体…。将使用之前的媒体(如有)。”在将 Wwise 连接到游戏时，其会尝试基于 Wwise 工程中添加或修改的媒体来更新游戏。添加或修改了给定媒体文件，但无法进行更新。通常可从 Capture Log（捕获日志）中的上一行错误看出失败的原因。

这条消息还表明已部署的游戏版本中的 SoundBank（音频包）不是最新的。虽然无需立即加以更新，但游戏在连接 Wwise 时的声音效果会跟部署更改后不一样。

**该错误可能由以下操作引发：**

- 在现有容器中添加新的 Sound（音效）或 Voice（语音）文件。
- 使用新的文件作为 Sound、Voice 或 Music Track（音乐轨）源替换现有文件。
- 在 Source Editor（源编辑器）中更改 Begin（开头）或 End（结尾）标记或其他 Source 属性。
- 更改 Sound、Voice 或 Music Track 的 Conversion Settings（转码设置）。
- 更改 AK Convolution Reverb 的 Impulse Response（冲激响应）。
- 添加新的 AK Convolution Reverb。
- 更改其他源或效果器插件的插件特定媒体。

**推荐的解决步骤：**

- 在 Capture Log 中寻找有关文件故障的线索。
- 在连接到游戏时，在 Remote Connections（远程连接）对话框的列表中选择 **Profile Only**（仅分析）。这样可以避免针对游戏实时更新媒体。

---