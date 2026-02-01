# Critically high number of active playback instances.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Critically high number of active playback instances.

#### Critically high number of active playback instances.

The critically high number of active playback instances can negatively affect performance and lead to system instability.

**推荐的解决步骤：**

- Identify and resolve any possible resource leaks, such as the following:

  - Blend, Switch, Random, or Sequence containers in "Continuous" playback mode.
  - Infinitely looping containers that are triggered but never stopped.

  One type of pattern is known to cause this problem: infinitely looping containers in trigger rate mode that trigger other continuous sounds at regular intervals. Avoid this type of pattern.

---