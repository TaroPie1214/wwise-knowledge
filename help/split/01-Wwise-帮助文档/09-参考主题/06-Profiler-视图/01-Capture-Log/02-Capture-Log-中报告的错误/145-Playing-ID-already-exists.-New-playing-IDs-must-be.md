# Playing ID already exists. New playing IDs must be generated when posting events.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Playing ID already exists. New playing IDs must be generated when posting events.

#### Playing ID already exists. New playing IDs must be generated when posting events.

A PostEvent command was received from the client for an existing playing ID.

**可能的原因：**

- The client has posted more than one event using the same playing ID through the Command Buffer API.

**推荐的解决步骤：**

- Use the function ak\_generate\_playing\_id() to generate a new playing ID when constructing a PostEvent command.

---