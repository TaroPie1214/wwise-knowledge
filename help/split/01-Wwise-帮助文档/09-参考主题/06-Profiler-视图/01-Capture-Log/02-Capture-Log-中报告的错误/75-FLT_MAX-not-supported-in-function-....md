# FLT_MAX not supported in function ...

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > FLT\_MAX not supported in function ...

#### FLT\_MAX not supported in function ...

“函数…中不支持 FLT\_MAX。”在有些函数中无法将最大 IEEE 浮点值 FLT\_MAX 用作输入参数值，因为这样会导致不符合预期的行为。在这种情况下，将忽略函数调用。

**推荐的解决步骤：**

- 在游戏代码中查找哪里使用了所述函数，并确认其所用的值是否为有效的浮点值。

---