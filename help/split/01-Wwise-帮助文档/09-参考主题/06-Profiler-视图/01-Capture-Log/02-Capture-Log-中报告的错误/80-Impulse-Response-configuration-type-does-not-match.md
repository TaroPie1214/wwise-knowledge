# Impulse Response configuration type does not match input signal's configuration type.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Impulse Response configuration type does not match input signal's configuration type.

#### Impulse Response configuration type does not match input signal's configuration type.

“使用了与 Sound Engine 运行时条件不匹配的 Convolution Reverb 参数生成音频包。将无法听到‪湿声路径的音频信号。”与 AK Convolution Reverb 相关。Impulse Response（冲激响应）的声道配置与输入信号的配置不兼容。

For more information on Impulse Response compatibility rules, refer to [Multi-channel input signals and impulse responses](../../../../10-Wwise-插件/04-效果器插件/03-AK-Convolution-Reverb（卷积混响）.md#multichannel_input_signals_and_impulse_responses "多声道输入信号和冲激响应").

**可能的原因：**

- The Convolution Reverb effect is placed after an incompatible effect plug-in.
- The Convolution Reverb effect is placed on a Bus with an incompatible channel configuration.
- The Convolution Reverb effect is placed on an object in the Containers hierarchy that uses an incompatible source.

**推荐的解决步骤：**

- If the plug-in is not the first effect in the effect chain, make sure the previous effect outputs a signal compatible with the channel configuration of the Impulse Response.

  If the plug-in is placed on a Bus, change the bus configuration of the Bus containing the plug-in.

  If the plug-in is placed on an object in the Containers hierarchy, make sure the channel configuration of the object's source is compatible with the channel configuration of the Impulse Response.

---