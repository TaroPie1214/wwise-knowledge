# Invalid transform in function ...

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Invalid transform in function ...

#### Invalid transform in function ...

“函数…中的变换无效。”传给指定函数的向量无效。

**可能的原因：**

- `AkTransform` 的前部和顶部向量没有相互正交。
- `AkTransform` 的前部和顶部向量的模（长度）均不等于 1，或有一个不等于 1。

**推荐的解决步骤：**

- 分析游戏执行的 API 调用：打开 [Profiler Settings](../../../01-工程/10-Profiler-Settings.md "Profiler Settings") (Alt-G)，并启用 **API Calls**（API 调用）。重新测试场景，并检查函数在此错误之前收到的参数。

---