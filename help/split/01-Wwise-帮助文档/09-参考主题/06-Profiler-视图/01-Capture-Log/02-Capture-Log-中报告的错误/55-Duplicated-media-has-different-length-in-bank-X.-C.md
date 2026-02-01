# Duplicated media has different length in bank X. Check previously unloaded bank. Stopping sound.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Duplicated media has different length in bank X. Check previously unloaded bank. Stopping sound.

#### Duplicated media has different length in bank X. Check previously unloaded bank. Stopping sound.

“音频包 X 中的重复媒体拥有不同的时长。检查之前卸载的音频包。停止播放声音”。在满足以下所有条件时会出现此错误：

- 两个或多个音频包中存在重复的媒体。比如，将一个声音添加到了两个音频包，或者两个不同的声音使用了位于两个不同音频包中的同一媒体文件。
- 某个音频包仅包含 Prefetch 部分（用于 Zero Latency Streaming）。
- 另一音频包包含更长的 Prefetch 部分（用于 Zero Latency Streaming）或整个媒体。
- 当前有个正在播放的声音使用了此媒体。
- 卸载了某个包含所述媒体的音频包。

若满足上述所有条件，则将在 Bank Unloaded（已卸载音频包）消息之后马上显示上述消息。此消息将包含其中涉及的某个音频包的名称，Bank Unloaded 消息则指向另一音频包。另外，Capture Log（捕获日志）的 Wwise Object（Wwise 对象）列将显示之前播放且使用了这些媒体副本的声音。该声音会立即停止播放。

**可能的原因：**

- 从旧的构建版本加载了过时的音频包，其包含过期数据。
- Wwise 工程包含两个不同 Prefetch 时长的单独声音，它们位于两个不同的音频包中。

**推荐的解决步骤：**

- 清空 Wwise 工程的 .cache 文件夹，重新生成 SoundBank，然后重新打包（如有必要）并重新部署至目标平台。
- 在 Wwise 工程中找到错误消息所指的声音。找到使用同一媒体文件的另一声音。确保两者始终使用相同的 Zero Latency（零延迟）时长。

---