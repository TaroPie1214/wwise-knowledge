# SoundBank 向后兼容性

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [完善工程](../../00-完善工程.md) > [管理 SoundBank](../00-管理-SoundBank.md) > [SoundBank 相关技巧和窍门](00-SoundBank-相关技巧和窍门.md) > SoundBank 向后兼容性

### SoundBank 向后兼容性

在 Wwise 同一大版本下的不同小版本之间，SoundBank（音频包）是完全兼容的。比如，在 2017.1.9 版本的 Wwise 中，您可以正常加载并使用 2017.1.2 生成的 SoundBank。不过，在不同大版本的 Wwise 之间，SoundBank 可能无法兼容。比如，在 2018.1 版本的 Wwise 中，一般无法正常加载并使用 2017.1.2 生成的 SoundBank。您必须在 2018.1 中重新生成 SoundBank。

不过，这一通用规则也有例外情况。若只包含媒体信息（非 Event 或结构信息），则 2016.1 及更高版本中生成的 SoundBank 可与 Wwise 2018.1、Wwise 2017.2.7 及后续版本兼容。注意，这可能不适用于插件媒体。

对于发行时间较长的游戏，会涉及 Wwise 版本更新。为此，建议声音设计师考虑使用这种[仅含媒体的 SoundBank](../02-SoundBank-管理策略/02-细致地管理媒体.md "细致地管理媒体")。这样升级时只需要更新含有结构和 Event 的音频包（容量要小很多）。

---