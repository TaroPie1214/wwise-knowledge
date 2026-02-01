# Unsupported feedback connection to Audio Objects bus.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Unsupported feedback connection to Audio Objects bus.

#### Unsupported feedback connection to Audio Objects bus.

“对音频对象总线的反馈连接不受支持。”在 Voice Graph（声部图）中检测到活跃的反馈连接，而其以 Audio Objects（音频对象）总线为目标。对 Audio Objects 总线的反馈连接是不受支持的。因此，建议将总线配置改为对输入连接实施下混的配置。比如，Same as Main Mix（与主混音相同）或特定扬声器配置。另外，若反馈连接并非由复杂音频传播或空间音频设置所致，则可设法避免造成反馈连接的情形。反馈连接之所以出现，通常是因为某些发声体-听者关系在 Voice Graph 中形成了循环。

---