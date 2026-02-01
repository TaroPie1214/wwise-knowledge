# Understanding file length limitations and naming conventions

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [入门](../00-入门.md) > [Wwise 界面基础知识](00-Wwise-界面基础知识.md) > Understanding file length limitations and naming conventions

## Understanding file length limitations and naming conventions

Your operating system might restrict the maximum length of a combined filename and file path. For example, the limit is 260 characters on Windows 10 and 1024 on macOS. A file with a
combined name and path at or near the maximum length might be successfully imported into Wwise
but then produce errors during subsequent conversion.

在 Wwise 中命名工程和对象时，您可使用任何 Unicode 支持的字符。

For the following elements in Wwise only unaccented Roman letters and underscores are
accepted. Numbers can be used but not as the first character. This is to comply with the
naming restrictions of certain game engines.

- SoundBanks
- Event
- Dialogue events（对白事件）
- Effect ShareSets（效果共享集）
- Switch Groups（切换开关组）
- Switches（切换开关）
- State Groups（状态组）
- States（状态）
- RTPC（实时参数控制）游戏参数
- Triggers
- Work Units

---