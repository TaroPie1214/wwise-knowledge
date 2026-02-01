# Cannot initialize with ambisonic channel configuration, reverting to standard configuration.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Cannot initialize with ambisonic channel configuration, reverting to standard configuration.

#### Cannot initialize with ambisonic channel configuration, reverting to standard configuration.

“无法初始化 Ambisonics 声道配置，将恢复为标准配置。”在初始化 3D 音频服务时，硬件拒绝了指定声道配置。将禁用 Ambisonics 输出，所有音频都将按照基于普通声道的配置实施混音。

**可能的原因：**

- 主机的音频设置明确禁用 3D Audio。
- 3D Audio 处理库或硬件被另一进程占用（通常为 Unreal 或 Unity）。

**推荐的解决步骤：**

- 确保禁用 Unreal 或 Unity 的音频系统。
- 检查主机上系统的音频设置或音频输出属性。

---