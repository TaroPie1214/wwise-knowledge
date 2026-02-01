# Microsoft Spatial Sound: Too many dynamic objects. Some sounds may not play.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Microsoft Spatial Sound: Too many dynamic objects. Some sounds may not play.

#### Microsoft Spatial Sound: Too many dynamic objects. Some sounds may not play.

“Microsoft Spatial Sound: 动态对象太多。有些声音可能无法播放。”系统没有足够的 Audio Object 可用。所有超出限值的 3D Audio Object 声音都将在音频 Bed 中实施混音。

**推荐的解决步骤：**

- 关闭其他使用 Audio Object（音频对象）的应用程序。
- 在 Wwise 的 Authoring Audio Preferences（设计工具首选项）中禁用 Audio Object（音频对象）。请参阅 [“Reserving system audio objects”一节](../../../../02-入门/04-个性化您的工作空间/05-Setting-authoring-audio-preferences.md#allow_system_audio_objects "Reserving system audio objects")。

---