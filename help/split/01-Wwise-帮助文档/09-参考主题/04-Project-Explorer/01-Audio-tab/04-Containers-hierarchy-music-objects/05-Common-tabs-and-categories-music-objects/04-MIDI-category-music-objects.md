# MIDI category: music objects

[Wwise 帮助文档](../../../../../00-Wwise-帮助文档.md) > [参考主题](../../../../00-参考主题.md) > [Project Explorer](../../../00-Project-Explorer.md) > [Audio tab](../../00-Audio-tab.md) > [Containers hierarchy: music objects](../00-Containers-hierarchy-music-objects.md) > [Common tabs and categories: music objects](00-Common-tabs-and-categories-music-objects.md) > MIDI category: music objects

##### MIDI category: music objects

The properties in the MIDI category allow you to specify the target and tempo of the MIDI content
of a music object. The target can be any playable sound or motion object. The tempo can be specified
as a global value for all MIDI content in the music object, or it can be obtained from the MIDI
files.

| M ID I | |
| --- | --- |
| 界面元素 | 描述 |
| **MIDI Target** | |
| Override parent | 不沿用父项。决定是继承父对象的 MIDI 目标，还是在层级结构的当前层级中定义 MIDI 目标。当没有勾选该选项时，MIDI target 控件是不可用的。  对于顶层对象，此选项将不可用。  Default value: false |
| Target | 目标。定义要将 MIDI Event 全部输出到 Container 中的哪个节点。  包含 MIDI 片段的音轨需要 MIDI 目标。音轨或其上级之一必须指定 MIDI 目标。 |
| **MIDI Clip Tempo** | |
| Override parent | 不沿用父项。决定是继承父对象的 MIDI 片段速度，还是在层级结构的当前层级中定义 MIDI 片段速度。当没有勾选该选项时，MIDI 片段速度是不可用的。  对于顶层对象，此选项将不可用。  Default value: false |
| Source | 源。决定用于播放 MIDI 片段的速度。  **Hierarchy** – 层级结构。从片段上级对象的时间设置获得的速度。  **File** – 文件。从片段的原始 MIDI 文件获得的速度。  请注意，在创建 MIDI 片段时会使用此设置来确定其时长。在片段创建后更改此字段会更改用于表达该片段的速度，但不会更改片段的时长。要更改 MIDI 片段的时长，请使用片段裁剪点。  Default value: Hierarchy |

---