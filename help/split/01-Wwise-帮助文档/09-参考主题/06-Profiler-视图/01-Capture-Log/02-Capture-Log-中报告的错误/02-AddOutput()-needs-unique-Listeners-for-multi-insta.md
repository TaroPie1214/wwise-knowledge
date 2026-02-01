# AddOutput() needs unique Listeners for multi-instance outputs using the same Audio Device type.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > AddOutput() needs unique Listeners for multi-instance outputs using the same Audio Device type.

#### AddOutput() needs unique Listeners for multi-instance outputs using the same Audio Device type.

“AddOutput() 需要为使用同一音频设备类型的多个输出分别指定不同的听者。”在将同一 Audio Device 类型用于多个输出时（比如对于 Game Controller 音频或振动），无法只使用该 Audio Device 类型来解析声音通路。您必须针对使用同一 Audio Device 类型创建的每个实例分别指定不同的听者。只有这样每个输出才能获得不同的混音。

**推荐的解决步骤：**

- 注册一个新的 Game Object，并将其用作每个使用同一 Audio Device 类型的输出的听者。

**另请参阅：**

- [集成 Secondary Outputs](https://www.audiokinetic.com/library/edge/?source=SDK&id=integrating_secondary_outputs.html)
- [集成 Wwise Motion](https://www.audiokinetic.com/library/edge/?source=SDK&id=integrating_elements_motion.html) 中的“多人游戏考量因素”章节。
- SDK\samples\IntegrationDemo 中的 IntegrationDemoMotion 示例展示了使用振动和音频输出时的这种情况。

---