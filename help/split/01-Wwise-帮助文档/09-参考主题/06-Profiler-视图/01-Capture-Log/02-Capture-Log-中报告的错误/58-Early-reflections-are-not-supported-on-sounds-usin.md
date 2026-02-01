# Early reflections are not supported on sounds using 3D Position: Listener with Automation. The assigned early reflections bus will be ignored.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Early reflections are not supported on sounds using 3D Position: Listener with Automation. The assigned early reflections bus will be ignored.

#### Early reflections are not supported on sounds using 3D Position: Listener with Automation. The assigned early reflections bus will be ignored.

“不支持针对使用‘3D 定位: 听者自动化’的声音应用早期反射。将忽略指派的早期反射总线。”在使用早期反射总线时，必须将声音的 3D Position（3D 定位）设为 **Emitter**（发声体）或 **Emitter with Automation**（发声体自动化）。不过，注意在使用 Emitter with Automation 时仍然只会从发声体位置计算反射。对于反射的来源，将忽略自动化偏置。有关如何针对声音设置早期反射的详细信息，请参阅 [`Spatial Audio`](https://www.audiokinetic.com/library/edge/?source=SDK&id=spatial__audio.html) 页面。

**推荐的解决步骤：**

- 在声音的 General Settings（常规设置）选项卡中清空 Early Reflections Auxiliary Bus（即设为 None），或者在 Positioning（定位）选项卡中将 3D Position 改为 **Emitter**。

---