# Plug-in does not support Audio Objects bus configuration.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Plug-in does not support Audio Objects bus configuration.

#### Plug-in does not support Audio Objects bus configuration.

“插件不支持‘音频对象’总线配置”。此错误表示在总线配置为 Audio Objects 的总线上对所列效果器或对象处理器插件进行了实例化，而这种运作方式对该插件来说是无效的。要么针对总线在 Property Editor（属性编辑器）中将总线配置显式设为了 **Audio Objects**（音频对象），要么另一插件对总线进行了隐式设置。

**推荐的解决步骤：**

- 将总线改为支持的配置：在属性页面将配置显式设为合适的声道配置（非 Audio Objects），或者在 Effects（效果器）列表中检查前面应用的插件。当中可能有插件将配置改为了 Audio Objects。

---