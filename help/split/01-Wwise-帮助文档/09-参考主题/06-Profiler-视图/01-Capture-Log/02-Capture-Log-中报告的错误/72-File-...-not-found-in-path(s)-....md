# File ... not found in path(s): ...

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > File ... not found in path(s): ...

#### File ... not found in path(s): ...

“未在以下路径中找到文件…: …。”无法找到指定文件。在这种情况下，会列出搜索的路径。

**可能的原因：**

- 没有设置 SoundBank 路径，或设置的文件夹不正确。
- 没有在测试主机上正确部署文件。
- Wwise 工程没有生成该文件。
- 没有将该文件打包到部署包中。

**推荐的解决步骤：**

- 若使用 Wwise 中提供的默认 I/O 代码，请确认 `CAkDefaultIOHookBlocking::SetBasePath` 或 `CAkDefaultIOHookBlocking::AddBasePath`) 调用指向正确的目录。
- 确保正确地生成 SoundBank 或 WEM 文件。
- 确保正确地生成 SoundBank 并将其部署到目标上。
- 若使用 Unity，请确保在对游戏进行打包前 Unity 工程的 StreamedAssets 目录下存在该文件。
- 若使用自定义 I/O 挂钩，请调试自定义 I/O 挂钩代码。

---