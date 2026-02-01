# Plug-in unsupported channel configuration.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Plug-in unsupported channel configuration.

#### Plug-in unsupported channel configuration.

“插件不支持声道配置”。此错误表示所列插件（源、效果器或混音器）不支持相应对象的声道配置。

**可能的原因：**

- Bus Channel Configuration（总线声道配置）属性与 Mixer（混音器）或 Effect（效果器）插件不兼容。Ambisonics 专用插件可能会出现此错误。其他插件可能不支持其他声道配置。

**推荐的解决步骤：**

- 查看故障插件相关文档。

---