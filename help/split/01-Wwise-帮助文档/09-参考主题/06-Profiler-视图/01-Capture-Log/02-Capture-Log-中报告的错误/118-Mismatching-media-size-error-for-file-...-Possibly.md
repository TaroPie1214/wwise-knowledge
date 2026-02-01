# Mismatching media size error for file ... Possibly caused by mismatching sound bank or WEM resources.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Mismatching media size error for file ... Possibly caused by mismatching sound bank or WEM resources.

#### Mismatching media size error for file ... Possibly caused by mismatching sound bank or WEM resources.

“文件…存在媒体大小不匹配错误。可能是因为音频包或 WEM 资源不匹配。”只有使用 [Zero Latency](../../../../05-使用声音和振动来提升游戏体验/01-定义对象播放行为/01-定义对象的播放行为/00-定义对象的播放行为.md#streaming_media "流播放媒体")（零延迟）选项的声音才会触发此错误。它表示 Wwise 检测到 WEM 文件的大小跟生成引用它的 SoundBank 时的大小不一样。这通常表示在生成、打包或部署 SoundBank 和 WEM 文件时出现了问题。这一流程一般会由游戏引擎进行处理。

**可能的原因：**

- 在游戏中打包或部署 SoundBank（音频包）和 WEM 时出现错误。若未能复制其中一个文件，则会导致此问题。
- 两个 SoundBank 中的声音重复，进而导致 Zero Latency 部分重复。若仅重新生成了一个 SoundBank，则可能出现此问题。
- 在游戏中加载了过时的 SoundBank。
- 在读取此音频流时，I/O 挂钩出现问题。通常与自定义 I/O 挂钩的使用有关。
- 存在内部错误。

**推荐的解决步骤：**

- 重新生成 SoundBank。
- 清理音频文件缓存，并重新转码 WEM 文件。您可以通过 File（文件）菜单清理文件缓存，也可手动删除 .cache 文件夹中相应的 WEM 文件。
- 删除测试主机上的所有 .bnk 和 .wem 文件。
- 在 Conversion Settings（转码设置）中使用别的编解码器。
- 若此问题依然存在，请联系 Audiokinetic 技术支持部门。

---