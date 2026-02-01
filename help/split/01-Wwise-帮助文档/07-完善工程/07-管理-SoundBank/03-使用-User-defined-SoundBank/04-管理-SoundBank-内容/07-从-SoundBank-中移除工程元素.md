# 从 SoundBank 中移除工程元素

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [完善工程](../../../00-完善工程.md) > [管理 SoundBank](../../00-管理-SoundBank.md) > [使用 User-defined SoundBank](../00-使用-User-defined-SoundBank.md) > [管理 SoundBank 内容](00-管理-SoundBank-内容.md) > 从 SoundBank 中移除工程元素

#### 从 SoundBank 中移除工程元素

在从 SoundBank 中移除元素时，所有相应 Event、对象结构和媒体文件也会被移除。

虽然无效的工程元素在生成过程中会被 Wwise 忽略，且不会导致错误或占用额外的空间，但还是建议将其从 SoundBank 中移除以保证工程的完好度。无效的 Event 和对象结构出现在 SoundBank Editor 上，它们的名称后面会带“Missing”一词。

**从 SoundBank 中移除工程元素的方法是：**

1. 将 SoundBank 加载到 SoundBank Editor。
2. 在 Add 选项卡上，选择您要移除的若干个对象。
3. 按 **Delete** 键。

   此时工程元素连同任何相应的事件、对象结构或媒体文件就从 SoundBank 中移除掉了。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 如果某个对象或媒体文件被 SoundBank 中的多个工程元素引用，则移除其中一个工程元素并不会自动移除该对象或媒体文件，因为其它工程元素仍在引用它。 |

---