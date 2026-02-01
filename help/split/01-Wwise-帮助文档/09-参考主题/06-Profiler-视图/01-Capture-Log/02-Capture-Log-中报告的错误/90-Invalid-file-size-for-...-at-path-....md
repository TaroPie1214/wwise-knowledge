# Invalid file size for ... at path ...

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Invalid file size for ... at path ...

#### Invalid file size for ... at path ...

“路径…下…的文件大小无效。”I/O 挂钩报告的文件大小为 0 字节。此错误仅会在游戏写入了自定义底层 I/O 挂钩时出现。

**推荐的解决步骤：**

- 采用 Debug 库编译并运行游戏。在出现此问题时会触发断言。在这种情况下，请让程序员调试自定义 I/O 挂钩代码。

---