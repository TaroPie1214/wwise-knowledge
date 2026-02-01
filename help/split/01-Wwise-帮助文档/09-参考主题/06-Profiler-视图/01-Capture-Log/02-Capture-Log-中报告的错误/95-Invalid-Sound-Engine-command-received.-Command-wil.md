# Invalid Sound Engine command received. Command will be skipped.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Invalid Sound Engine command received. Command will be skipped.

#### Invalid Sound Engine command received. Command will be skipped.

The game attempted to send an unrecognized command ID to the Sound Engine through the Command Buffer API.

**可能的原因：**

- A programming mistake in the game code.
- The game uses a dynamically linked version of the Sound Engine, and the game is compiled against the wrong version of the Wwise SDK header files.

**推荐的解决步骤：**

- Verify that all command IDs sent through the Command Buffer API correspond to values
  listed in the `AkCommand` enum.
- Make sure the game is compiled using the Wwise SDK header files included with the Sound Engine DLL.

---