# Missing music node parent. Make sure all banks containing music structures are completely loaded.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Missing music node parent. Make sure all banks containing music structures are completely loaded.

#### Missing music node parent. Make sure all banks containing music structures are completely loaded.

“缺少音乐节点父对象。确保完全加载了包含音乐结构的所有音频包。”此错误消息表示用户可添加不属于同一音乐树的过渡段落，然后从 SoundBank 中明确弃用该过渡段落的父对象。

**推荐的解决步骤：**

- 在音乐 SoundBank（音频包）中包含父对象。
- 必要时加载缺少的音乐 SoundBank（音频包）。
- 在同一树中为过渡段落重新设置父对象。

---