# The playing sound is assigned the same Early Reflection Auxiliary Bus in the Authoring Tool that has been set via AK::SpatialAudio::SetImageSource. Use a unique bus to avoid image source conflicts.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > The playing sound is assigned the same Early Reflection Auxiliary Bus in the Authoring Tool that has been set via AK::SpatialAudio::SetImageSource. Use a unique bus to avoid image source conflicts.

#### The playing sound is assigned the same Early Reflection Auxiliary Bus in the Authoring Tool that has been set via AK::SpatialAudio::SetImageSource. Use a unique bus to avoid image source conflicts.

“在设计工具中将正在播放的声音指派给了通过 AK::SpatialAudio::SetImageSource 设置的同一早期反射辅助总线。为避免镜像声源冲突，请使用不同的总线。”Wwise 设计工具中指派给声音的 Early Reflections Auxiliary Bus（早期反射辅助总线）与传给 [`AK::SpatialAudio::SetImageSource`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_aab4d85317c62724c00d25ba8913fb503.html) 的总线发生冲突。

**可能的原因：**

- 在 Wwise 设计工具中将某条 Early Reflections Auxiliary Bus 指派给了声音，而该 Auxiliary Bus 所用的总线与传给 API 函数 [`AK::SpatialAudio::SetImageSource`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_aab4d85317c62724c00d25ba8913fb503.html) 的总线相同，并且在播放同样的游戏对象。单个 Reflect 插件无法同时接收来自几何构造 API 和 SetImageSource API 的镜像声源数据。

**推荐的解决步骤：**

- 若同时使用几何反射 API 和 SetImageSource API，请务必为 SetImageSource 单独指派一条 Auxiliary Bus，并确保其不同于 Wwise 设计工具中用来在同一游戏对象上播放声音的 Auxiliary Bus。为此，可复制包含 Reflect 插件的相应 Auxiliary Bus，并将其指派给存在冲突的声音。这样可确保为该声音创建一条不同的总线。

---