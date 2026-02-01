# Switch Group ... has no Switch Values at all. Switch container will do nothing.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Switch Group ... has no Switch Values at all. Switch container will do nothing.

#### Switch Group ... has no Switch Values at all. Switch container will do nothing.

“切换开关组…没有任何切换开关值。切换开关容器将不起作用。”在开始播放 Switch Container 时，若其所用的 Switch Group 没有任何 Switch 值，则将出现此错误。

**推荐的解决步骤：**

- 确保 Wwise 工程中的 Switch Group（切换开关组）具有 Switch 值。
- 确保生成使用此 Switch Group（切换开关组）的 Init 和其他 SoundBank（音频包），并在主机上正确地加以部署。

---