# 在 SoundBank 中启用插件媒体

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [完善工程](../../../00-完善工程.md) > [管理 SoundBank](../../00-管理-SoundBank.md) > [使用 User-defined SoundBank](../00-使用-User-defined-SoundBank.md) > [管理 SoundBank 内容](00-管理-SoundBank-内容.md) > 在 SoundBank 中启用插件媒体

#### 在 SoundBank 中启用插件媒体

有些效果器（如 AK Convolution Reverb）需要有媒体文件才能工作。比如，AK Convolution Reverb 需要冲激响应文件作为它的插件媒体。这些插件媒体文件需要包含在 SoundBank 中，效果器才能在游戏中正常工作。您还需要确保在需要实例化效果器时加载包含启用了这些媒体文件的 SoundBank。

在 SoundBank 中启用插件媒体文件有很多方法：

- 您可以在 SoundBank 的启用列表中插入 Shareset 效果器对象。
- You can insert the owner object (bus, Auxiliary Bus or Containers hierarchy object) inside the inclusion list of a SoundBank.
- You can insert the Event inside the inclusion list of a SoundBank, if the Effect is owned by an Containers hierarchy object.

通过查看 SoundBank Editor／Edit 选项卡可验证 SoundBank 中是否包含插件媒体文件。

---