# Source file is of different format than expected.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Source file is of different format than expected.

#### Source file is of different format than expected.

“源文件格式与预期不同。”在流播放文件或外部源所用编解码器与相关 SoundBank（音频包）结构或 [`AK::SoundEngine::PostEvent()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html) 调用中所述不同时，将出现此错误。

**可能的原因：**

- 近期在工程的 Conversion Settings（转码设置）中更改了编解码器。
- 对于 External Source（外部源），[`AK::SoundEngine::PostEvent()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html) 调用所对应 [`AkExternalSourceInfo`](https://www.audiokinetic.com/library/edge/?source=SDK&id=struct_ak_external_source_info.html) 结构中传递的格式中指定的编解码器与实际文件格式不一致。

**推荐的解决步骤：**

- 确保生成所有 SoundBank 和 WEM 文件（流播放文件），并将其部署至目标平台。
- 若使用 External Source，请验证 WSOURCES 文件中所指定 Conversion Settings 中使用的编解码器。

---