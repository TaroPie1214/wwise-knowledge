# External source missing from PostEvent call.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > External source missing from `PostEvent` call.

#### External source missing from `PostEvent` call.

“PostEvent 调用缺少外部源。”[`AK::SoundEngine::PostEvent`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html) 调用中的 Event（事件）需要替换一个或多个 External Source（外部源）文件。部分所需源没有提供 API 调用。请注意，一个 Event 中可包含多个 External Source，运行时必须在代码中全部提供。而且，External Source ID 还要匹配。

**推荐的解决步骤：**

- 在 Wwise 工程中，确认 Event 的目标以及 Event 中需要多少个 External Source。留意字符串或数字标识符。这些 ID 必须提供给 `PostEvent`。在调用 `PostEvent` 时，请确保数组中包含相同数量的 External Source 且 ID 全部与 Wwise 工程中的 ID 匹配。

**另请参阅：**

- [集成 External Source](https://www.audiokinetic.com/library/edge/?source=SDK&id=integrating__external__sources.html)

---