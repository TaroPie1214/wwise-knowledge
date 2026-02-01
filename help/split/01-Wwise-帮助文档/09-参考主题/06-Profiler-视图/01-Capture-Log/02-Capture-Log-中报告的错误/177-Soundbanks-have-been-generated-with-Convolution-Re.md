# Soundbanks have been generated with Convolution Reverb parameters that do not match Sound Engine runtime conditions. No wet path will be heard.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Soundbanks have been generated with Convolution Reverb parameters that do not match Sound Engine runtime conditions. No wet path will be heard.

#### Soundbanks have been generated with Convolution Reverb parameters that do not match Sound Engine runtime conditions. No wet path will be heard.

“使用了与 Sound Engine 运行时条件不匹配的 Convolution Reverb 参数生成音频包。将无法听到‪湿声路径的音频信号。”与 AK Convolution Reverb 相关。若 Impulse Response（冲激响应）文件具有与 Sound Engine（声音引擎）不同的采样率，则将出现此错误。

**推荐的解决步骤：**

- 默认生成的 Convolution Reverb Impulse Response 用于在 Sound Engine 中以 48 KHz 的频率播放。因此，有必要在初始化时通过调用 `AK::SouneEngine::Init` 来强制使用 Sounde Engine 的采样率。

---