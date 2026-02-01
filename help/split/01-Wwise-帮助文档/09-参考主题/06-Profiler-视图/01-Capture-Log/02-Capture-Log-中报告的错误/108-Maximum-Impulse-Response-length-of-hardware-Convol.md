# Maximum Impulse Response length of hardware Convolution Reverb reached.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Maximum Impulse Response length of hardware Convolution Reverb reached.

#### Maximum Impulse Response length of hardware Convolution Reverb reached.

“使用了与 Sound Engine 运行时条件不匹配的 Convolution Reverb 参数生成音频包。将无法听到‪湿声路径的音频信号。”与 AK Convolution Reverb 相关。启用了硬件加速，最终的 Impulse Response 长度大于支持的长度。

**推荐的解决步骤：**

- 禁用硬件加速或调节 `Reverb, Pre Delay`（Reverb 预延迟）参数的值。

---