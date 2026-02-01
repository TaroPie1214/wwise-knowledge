# Conversion category: Containers hierarchy objects

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [Audio tab](../00-Audio-tab.md) > [Common tabs and categories: audio structures](00-Common-tabs-and-categories-audio-structures.md) > Conversion category: Containers hierarchy objects

#### Conversion category: Containers hierarchy objects

The properties in the Conversion category allow you, among other things, to apply Conversion Setting ShareSets to an object. 在将 Conversion Settings 应用于对象时，必须决定是采用 ShareSet（共享集）还是自定义实例形式来应用 Conversion Settings。您可以随时使用 Edit（编辑）按钮来编辑 Conversion Settings。

The Conversion category also allows you to enable loudness normalization to adjust
the volume.

|  |  |
| --- | --- |
| [备注] | 备注 |
| 在将 Conversion Settings 共享集应用于父对象时，这些设置会自动应用于所有子对象。不过，您可以在层级结构中的任何层级上不沿用这些设置，而是选择 Override parent 选项并应用不同的 ShareSet。 |

| Conversion | |
| --- | --- |
| 界面元素 | 描述 |
| **Conversion Settings** | |
| Override Conversion Settings | 不沿用父对象。决定 Conversion Settings 是从父对象继承还是在当前层级定义。  如果对象是顶层对象，则 Override parent 选项将不可用。  Default value: false |
| Conversion Settings | 可作用于对象的转码设置实例列表。所选实例的名称将显示在相应文本框中。  要删除转码设置实例，请选择 **None** （无）选项。 |
| **Loudness Normalization** | |
| Override parent | 不沿用父项。确定响度归一化设置是从父项继承，还是在层级结构的当前层级定义。  如果对象是顶层对象，则 Override parent 选项将不可用。  Default value: false |
| Enable Loudness Normalization | 启用响度归一化。确定响度归一化是否激活。  对源做归一化，方法是应用一个自动增益，这个增益是通过源录音中测到的响度所计算得到的。  有关响度归一化的详细信息，请参阅 [使用响度归一化或补偿增益来调节音量](../../../../07-完善工程/01-管理输出/04-使用-Loudness-Normalization-或-Make-up-Gain-调节音量.md "使用 Loudness Normalization 或 Make-up Gain 调节音量") 页面。  Default value: false |
| Loudness Normalization Type | 响度归一化类型。定义归一化的响度测量类型。  - Integrated (default)：大致遵循 ITU-R BS 1770 标准。 - Momentary Max：通过极短 (100 ms) 的窗口估算获得的最高响度值。  有关响度归一化的详细信息，请参阅 [使用响度归一化或补偿增益来调节音量](../../../../07-完善工程/01-管理输出/04-使用-Loudness-Normalization-或-Make-up-Gain-调节音量.md "使用 Loudness Normalization 或 Make-up Gain 调节音量") 页面。  Default value: Integrated |
| Loudness Normalization Target | 响度归一化目标。决定归一化的目标响度级 (LUFS)。  有关响度归一化的详细信息，请参阅 [使用响度归一化或补偿增益来调节音量](../../../../07-完善工程/01-管理输出/04-使用-Loudness-Normalization-或-Make-up-Gain-调节音量.md "使用 Loudness Normalization 或 Make-up Gain 调节音量") 页面。  Default value: -23  Range: -96 to 0  Units: dB |

**相关主题**

- [“Assigning Conversion Settings ShareSets to objects”一节](../../../../07-完善工程/01-管理输出/10-对音频文件做转码/03-Assigning-Conversion-Settings-ShareSets-to-objects.md "Assigning Conversion Settings ShareSets to objects")
- [“对音频文件做转码”一节](../../../../07-完善工程/01-管理输出/10-对音频文件做转码/04-对音频文件做转码.md "对音频文件做转码")
- [“Creating audio Conversion Settings ShareSets”一节](../../../../07-完善工程/01-管理输出/10-对音频文件做转码/01-Creating-audio-Conversion-Settings-ShareSets.md "Creating audio Conversion Settings ShareSets")

---