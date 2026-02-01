# Invalid channel configuration specified for SetSidechainMixConfig. Audio Objects configuration is not supported.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Invalid channel configuration specified for SetSidechainMixConfig. Audio Objects configuration is not supported.

#### Invalid channel configuration specified for SetSidechainMixConfig. Audio Objects configuration is not supported.

This error originates from [`AK::SoundEngine::SetSidechainMixConfig`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a89e4bddb45ad3fea4a03f69a3e0b2fc5.html). It indicates that an invalid channel configuration was passed as a parameter when calling the API. This may be a result of the AkChannelConfig not being initialized properly, or attempting to use an Audio Objects configuration for the Sidechain Mix.

**推荐的解决步骤：**

- Enusre the AkChannelConfig parameter is correctly initialized in code.

---