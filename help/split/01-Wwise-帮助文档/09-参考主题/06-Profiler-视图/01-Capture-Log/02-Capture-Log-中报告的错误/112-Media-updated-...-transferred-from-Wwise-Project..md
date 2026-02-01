# Media updated: ... transferred from Wwise Project. Glitches might be heard. Previous media from other sources (bank, prepared, etc) will be ignored.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Media updated: ... transferred from Wwise Project. Glitches might be heard. Previous media from other sources (bank, prepared, etc) will be ignored.

#### Media updated: ... transferred from Wwise Project. Glitches might be heard. Previous media from other sources (bank, prepared, etc) will be ignored.

“已更新媒体: 从 Wwise 工程传输了…。可能会听到毛刺噪声。将忽略之前通过其他源(音频包、预备的媒体等)加载的媒体。”在 Wwise 工程中添加或修改了给定媒体文件。在将 Wwise 连接到游戏时，其会基于新增或修改的媒体来更新游戏。这种媒体更新不是永久的；磁盘上的文件不会被修改。在这种情况下，将忽略所有通过音频包加载方式加载到内存中的媒体版本。

这条消息还表明已部署的游戏版本中的 SoundBank（音频包）不是最新的。虽然无需立即加以更新，但游戏在连接 Wwise 时的声音效果会跟部署更改后不一样。

**该错误可能由以下操作引发：**

- 在现有容器中添加新的 Sound（音效）或 Voice（语音）文件。
- 使用新的文件作为 Sound、Voice 或 Music Track（音乐轨）源替换现有文件。
- 在 Source Editor（源编辑器）中更改 Begin（开头）或 End（结尾）标记或其他 Source 属性。
- 更改 Sound、Voice 或 Music Track 的 Conversion Settings（转码设置）。
- 更改 AK Convolution Reverb 的 Impulse Response（冲激响应）。
- 添加新的 AK Convolution Reverb。
- 更改其他源或效果器插件的插件特定媒体。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 若不想让 Wwise 更新游戏中的媒体，请在连接到游戏时在 Remote Connections 对话框的列表中选择 **Profile Only**。 |

---