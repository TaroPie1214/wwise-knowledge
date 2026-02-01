# Type mismatch while loading bank. Object ... is a ... in the currently loading bank. It was a ... in bank ...

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Type mismatch while loading bank. Object ... is a ... in the currently loading bank. It was a ... in bank ...

#### Type mismatch while loading bank. Object ... is a ... in the currently loading bank. It was a ... in bank ...

“加载音频包时类型不匹配。对象…是当前加载的音频包中的…。它之前是音频包…中的…。”此错误表示 Wwise 中所用的唯一标识符存在冲突。两个对象共用两个不同 SoundBank 中的同一标识符。

**可能的原因：**

- 通常情况是主机测试目录下存在未使用且没有更新的 SoundBank。
- 极个别情况下是存在真正的标识符冲突。

**推荐的解决步骤：**

- 删除测试主机上的所有 .bnk 文件。
- 在 Wwise 工程中更改所述对象的名称，然后重新生成 SoundBank（音频包）。
- 联系 Audiokinetic 技术支持部门，因为这也有可能是个内部漏洞。

---