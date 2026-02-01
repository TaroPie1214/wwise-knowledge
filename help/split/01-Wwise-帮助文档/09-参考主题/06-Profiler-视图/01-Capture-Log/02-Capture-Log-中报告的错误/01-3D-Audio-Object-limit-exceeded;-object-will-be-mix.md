# 3D Audio Object limit exceeded; object will be mixed.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > 3D Audio Object limit exceeded; object will be mixed.

#### 3D Audio Object limit exceeded; object will be mixed.

“超出 3D Audio Object 限值，将对对象实施混音。”将对原本要作为独立 3D Audio Object 单独发送到系统的声部实施混音。原因是已经有太多独立 3D Audio Object 在播放了。

对于支持独立对象的 3D 音频系统，通常会限制可同时播放的对象数量。比如，Windows Sonic for Headphones 在 Windows 10 上最多支持 112 个单独的 3D 对象（有关详细信息，请参阅 Microsoft 的 [Spatial Sound 文档](https://docs.microsoft.com/en-us/windows/win32/coreaudio/spatial-sound)）。

每次新的声部超出该限值，Capture Log（捕获日志）中都会显示此错误。

**推荐的解决步骤：**

- 若不打算在 3D 空间中对此声部实施定位，请将其 3D Spatialization（3D 空间化）属性改为 **None**（无）。
- 若不打算将此声部作为独立对象进行发送，而只是想避免显示该错误消息，请通过混音总线输出声音。除此之外，若受制于混音层级结构，则可将 “Wwise System Output Settings” Metadata ShareSet（元数据共享集）与声音绑定，并将 **Mix Behavior**（混音行为）属性设为 **Mix to main**（混音到主混音）。
- If you would rather opt out of using a system's discrete 3D audio objects capabilities when it doesn't support a certain number of objects, increase the value of the **System Minimum Object Requirement** property of the System ShareSet used by the main bus. 注意，也可针对各个平台分别执行此操作。
- To opt out of discrete 3D Audio Objects entirely, deselect the **Enable Objects** property of the System ShareSet used by the main bus.

---