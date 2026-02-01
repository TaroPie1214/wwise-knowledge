# Playing a trigger-rate container as part of a sample-accurate playlist is not supported and will sound out-of-sync.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Playing a trigger-rate container as part of a sample-accurate playlist is not supported and will sound out-of-sync.

#### Playing a trigger-rate container as part of a sample-accurate playlist is not supported and will sound out-of-sync.

“不支持在精确到采样点的播放列表中播放精确到触发率的容器，否则声音会不同步。”此错误表示 Sequence Container（序列容器）或 Random Container（随机容器）将 Transition Type（过渡类型）设为了 **Trigger rate**（触发率），而其父级 Sequence Container 或 Random Container 却将 Transition Type 设为了 **Sample accurate**（精确到采样点）。

Wwise 不支持这样的设置。精确到触发率的容器只会播放一个声音，然后便会静音，直到下一帧。

**推荐的解决步骤：**

- 更改结构或属性来避开这种容器设置。
- 若想执行粒子合成，请试试 SoundSeed Grain 插件。

---