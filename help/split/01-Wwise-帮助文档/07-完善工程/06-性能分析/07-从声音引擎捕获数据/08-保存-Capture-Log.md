# 保存 Capture Log

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [完善工程](../../00-完善工程.md) > [性能分析](../00-性能分析.md) > [从声音引擎捕获数据](00-从声音引擎捕获数据.md) > 保存 Capture Log

### 保存 Capture Log

每次启动捕获会话时 Wwise 都会清空 Capture Log。若在连接远程平台的情况下执行捕获会话，则会话期间捕获的所有数据将自动保存到名为 ProfilingSession.prof 的 PROF 文件。每次启动新的远程捕获会话都会新建一个文件，并在文件名称结尾附加相应的递增编号。在 Profiler Settings 中，可指定要保留多少个文件。另外，还可选择手动将捕获的数据保存到 TXT 文件。两种文件类型的用法如下：

- PROF 文件可在 Wwise 中打开并会填充 Profiler、Voice Profiler 和 Game Object Profiler 布局的所有视图，就跟刚刚完成捕获会话一样。
- TXT 文件只会保存 Capture Log 视图中的信息。各列和排序保持不变。TXT 文件既可使用外部文本编辑器打开，也可导入到外部电子表格程序。

**手动保存 Capture Log：**

1. 在 Capture Log 中，点击 **Save Log**（保存日志）。

   Save As（另存为）窗口将打开。
2. 浏览至希望保存文件的位置。
3. 在 **File name** 中输入文件名称。
4. 根据需要选择文件扩展名：TXT 或 PROF（如可用）。
5. 点击 **Save**（保存）。

   这时将把 Capture Log 的内容保存为文件。

---