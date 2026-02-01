# The Audio Device specified by AddOutput() or Init() could not be initialized.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > The Audio Device specified by AddOutput() or Init() could not be initialized.

#### The Audio Device specified by AddOutput() or Init() could not be initialized.

“无法初始化 AddOutput() 或 Init() 指定的音频设备。”在初始化新的音频输出时发生未知错误。此错误通常与第三方 Audio Device 插件（音频输出插件）的使用有关。

**可能的原因：**

- 此平台上不支持所述插件。
- 该插件不支持所需的音频扬声器配置。
- 发生了特定于该插件的未知错误。

**推荐的解决步骤：**

- 确认 Audio Device（音频设备）插件文档中的扬声器配置限制，并确保在 `AkInitSettings::outputSettings` 中传递有效的配置。
- 使用 Debug 版本库，将调试程序连接至游戏，然后重现相同场景。确认 Debug（调试）日志中是否显示有其他信息。
- 查明传递至 [`AK::SoundEngine::AddOutput()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a15ab79f954a307902f529d8ccde8ad48.html) 的相关 ShareSet（共享集）中使用了哪个插件，并联系插件供应商。

---