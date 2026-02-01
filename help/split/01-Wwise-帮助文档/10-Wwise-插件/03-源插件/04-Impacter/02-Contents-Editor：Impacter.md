# Contents Editor：Impacter

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [Wwise 插件](../../00-Wwise-插件.md) > [源插件](../00-源插件.md) > [Impacter](00-Impacter.md) > Contents Editor：Impacter

### Contents Editor：Impacter

Contents Editor（内容编辑器）方便快速访问与 Impacter 插件关联的一些常用属性。注意，必须单击 Impacter 源才能显示相关列标题。

如需概括了解 Impacter 插件，请参阅 [“Impacter”一节](00-Impacter.md "Impacter") 章节。

| 界面元素 | 描述 |
| --- | --- |
| Name | 名称。Impacter 插件的名称。 |
| Use | 采用。决定声音对象内的哪个源将会被：  - 播放。 - 将被包括在 SoundBank 中。  |  |  | | --- | --- | | [备注] | 备注 | | 只有在声音对象具有多个源时才会显示 Use 选项。 | |
| Notes | 备注。有关 Impacter 插件的其他信息。 |
| Mass | 质量。以独特方式对声音实施时间拉伸、音高变换或信号压缩，来改变听者对发声体大小或重量的直观感受。仅在撞击的开头应用 RTPC 更新。  Default value: 1.0  Range: 0.01 to 2.0 |
| Velocity | 速度。影响撞击的强度，进而改变声音的音色和振幅。仅在撞击的开头应用 RTPC 更新。  Default value: 1.0  Range: 0.05 to 1.0 |
| Position | 位置。塑造声音的音色，产生在表面多个不同位置发生撞击的效果。仅在撞击的开头应用 RTPC 更新。  Default value: 0.0  Range: 0.0 to 1.0 |
| Roughness | 粗糙度。为声音增添金属般的不和谐效果。仅在撞击的开头应用 RTPC 更新。  Default value: 0  Range: 0.0 to 1.0 |
|  | 向声音对象中添加新的源。  当您点击 **Add Source**（添加源）按钮时，会显示一个可以添加的[*源插件*](../00-源插件.md "源插件")列表。 |

---