# Invalid floating point value detected : non-finite(or NaN) priority.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Invalid floating point value detected : non-finite(or NaN) priority.

#### Invalid floating point value detected : non-finite(or NaN) priority.

“检测到无效浮点值: 非有限或 NaN 优先级”。检测到声音的 Priority（优先级）参数为无效值。系统将不会计算部分声音的优先级。

**可能的原因：**

- 为 SoundEngine API 提供了无效的输入值。这种情况通常由 RTPC 或 Position 导致。

**推荐的解决步骤：**

- 打开 [Profiler Settings](../../../01-工程/10-Profiler-Settings.md "Profiler Settings")（性能分析器设置），启用 **API Calls**（API 调用），并重现所遇情况。查看新的 API 调用值无效错误。
- 若该问题依然存在，请联系 Audiokinetic 技术支持部门。

---