# Cannot open file ... in path(s): ...

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Cannot open file ... in path(s): ...

#### Cannot open file ... in path(s): ...

“无法打开以下路径中的文件…: …。”找到了指定的文件，但无法通过所列路径访问。这通常是文件权限错误，但不同的操作系统可能会给出触发此消息的其他错误。

若没有找到文件，则将显示 [“File ... not found in path(s): ...”一节](72-File-...-not-found-in-path(s)-....md "File ... not found in path(s"): ...") 错误。

**可能的原因：**

- 文件权限阻止当前用户执行的 Read 操作。
- 操作系统返回了未知错误。

**推荐的解决步骤：**

- 针对指定文件检查游戏的部署文件夹下的文件权限。

---