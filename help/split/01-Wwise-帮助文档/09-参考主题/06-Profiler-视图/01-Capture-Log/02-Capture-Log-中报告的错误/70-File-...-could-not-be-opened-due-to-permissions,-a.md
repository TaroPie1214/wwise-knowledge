# File ... could not be opened due to permissions, access rights or conflicting open modes. (Found in path(s): ...).

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > File ... could not be opened due to permissions, access rights or conflicting open modes. (Found in path(s): ...).

#### File ... could not be opened due to permissions, access rights or conflicting open modes. (Found in path(s): ...).

**可能的原因：**

- 别的应用程序在独占模式下打开了文件。
- 文件在访问权限受保护的目录下。
- 未停止录音即尝试读取由 Recorder 效果器插件实施的录音。

**推荐的解决步骤：**

- 检查给定文件夹的用户权限。
- 检查版本控制系统对所报告文件的设置。
- 检查电脑的防病毒设置。
- 若与 Recorder 效果器插件实施的录音相关，请务必停止录音。

---