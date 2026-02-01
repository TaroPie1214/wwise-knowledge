# Opus decoder failure.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Opus decoder failure.

#### Opus decoder failure.

Opus 解码器遇到了损坏的流，无法继续解码声音。声音会停止播放。

**可能的原因：**

- 声音启用了 [Zero Latency](../../../../05-使用声音和振动来提升游戏体验/01-定义对象播放行为/01-定义对象的播放行为/00-定义对象的播放行为.md#streaming_media "流播放媒体")（零延迟）选项，在消耗 Zero Latency 缓冲后，SoundBank（音频包）中的媒体部分与流播放的 WEM 文件不匹配。这可能是因为：

  - 在游戏中打包或部署 SoundBank（音频包）和 WEM 时出现错误。若未能复制其中一个文件，则会导致此问题。
  - 两个 SoundBank 中的声音重复，进而导致 Zero Latency 部分重复。若仅重新生成了一个 SoundBank，则可能出现此问题。
  - 在游戏中加载了旧的 SoundBank。
- 在读取此音频流时，I/O 挂钩出现问题。通常与自定义 I/O 挂钩的使用有关。
- 存在内部 Wwise 漏洞。

**推荐的解决步骤：**

- 重新生成 SoundBank。
- 清理音频文件缓存，并重新转码 WEM 文件。您可以通过 File（文件）菜单清理文件缓存，也可手动删除 .cache 文件夹中相应的 WEM 文件。
- 在 Conversion Settings（转码设置）中使用别的编解码器。
- 若此问题依然存在，请联系 Audiokinetic 技术支持部门。

---