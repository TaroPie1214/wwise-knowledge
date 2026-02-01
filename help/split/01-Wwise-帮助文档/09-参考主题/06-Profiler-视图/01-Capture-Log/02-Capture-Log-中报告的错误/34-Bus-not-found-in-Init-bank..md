# Bus not found in Init bank.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Bus not found in Init bank.

#### Bus not found in Init bank.

在从游戏调用多个函数时，可能会出现此错误。在这种情况下，会报告具体的函数。此错误表示该 Bus ID 在执行调用时不存在。

**可能的原因：**

- Bus ID 拼写有误。
- 未加载 Init SoundBank（初始化音频包），或者加载时出现错误。
- 在更改 Wwise 工程中的总线结构后，未重新生成并重新部署 Init SoundBank。

**推荐的解决步骤：**

- 将总线的数字 ID 与 Init.txt 文件中提供的 ID 进行比对。
- 在游戏构建中重新生成并重新部署 Init.bnk 文件。

---