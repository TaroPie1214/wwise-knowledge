# Invalid float in parameter ... of function ...

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Invalid float in parameter ... of function ...

#### Invalid float in parameter ... of function ...

“函数…的参数…中的浮点值无效。”指定浮点参数为非数字 (NAN) 或无穷大 (+/- INF)，两者都不能用作声音引擎的函数中的输入参数。

**推荐的解决步骤：**

- 检查游戏代码中对所述函数的所有调用。确认各项输入参数。
- 打开 [Profiler Settings](../../../01-工程/10-Profiler-Settings.md "Profiler Settings")（性能分析器设置），启用 **API Calls**（API 调用），并重现所遇情况。查看新的 API 调用值无效错误。

---