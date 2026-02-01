# Bank or Media pointer not aligned to ... bytes.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Bank or Media pointer not aligned to ... bytes.

#### Bank or Media pointer not aligned to ... bytes.

“Bank 或 Media 指针未对齐至…字节。”若使用  [`AK::SoundEngine::LoadBank`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a496b9917fe035f301bcff0accd61f80f.html)（内存指针版本）或  [`AK::SoundEngine::SetMedia`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_ae93bba30404755a4d2e592c3bfbf340c.html) 且传递的数据指针没有对齐到预期粒度，则将出现此错误。具体因平台和编解码器而异。默认要求为 16 字节。

**可能的原因：**

- 媒体指针没有对齐到默认的 16 字节。

**推荐的解决步骤：**

- 在加载数据前分配内存并确保对齐无误。

---