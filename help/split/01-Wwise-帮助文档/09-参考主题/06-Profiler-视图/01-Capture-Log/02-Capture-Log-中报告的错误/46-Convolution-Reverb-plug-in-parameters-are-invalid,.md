# Convolution Reverb plug-in parameters are invalid, effect is disabled.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Convolution Reverb plug-in parameters are invalid, effect is disabled.

#### Convolution Reverb plug-in parameters are invalid, effect is disabled.

“Convolution Reverb 插件参数无效，效果器被禁用。”若有一个或多个 Convolution Reverb 参数无效，则将出现此错误。

**可能的原因：**

- 所加载的 SoundBank（音频包）并不是为当前平台生成的。在将同一 SoundBank 用于所有平台时可能会出现这种情况。

**推荐的解决步骤：**

- 确认 Wwise 工程中的 Convolution Reverb 参数。
- 重新生成包含插件的 SoundBank。

---