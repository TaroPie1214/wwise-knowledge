# Not enough memory in I/O pool to start stream.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Not enough memory in I/O pool to start stream.

#### Not enough memory in I/O pool to start stream.

“I/O 池中内存不足，无法启动流播放”。I/O 池没有足够的内存，无法读取流播放文件头。声音将终止。

**推荐的解决步骤：**

- 增大 I/O 池中的内存量。在初始化序列中，初始化 Streaming Manager（流播放管理器）之前设置  [`AkDeviceSettings::uIOMemorySize`](https://www.audiokinetic.com/library/edge/?source=SDK&id=struct_ak_device_settings_a75893592924a59881fe2cbca4e4ddd04.html)。
- 连接 Wwise Profiler 并检查 Streaming 选项卡。检查流播放声部数量上有没有异常。
- 减少流播放声音，同时使用虚声部和播放限制。

**推荐的解决步骤：**

- [管理音量较低的对象](https://www.audiokinetic.com/library/edge/?source=Help&id=managing_low_volume_objects)
- [限制对象的播放实例](https://www.audiokinetic.com/library/edge/?source=Help&id=limiting_object_playback_instances)
- [Audiokinetic Stream Manager 初始化设置](https://www.audiokinetic.com/library/edge/?source=SDK&id=streamingmanager__settings.html)

---