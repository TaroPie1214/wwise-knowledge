# About the properties of music objects

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [创建互动音乐](../00-创建互动音乐.md) > [Building your interactive music hierarchies](00-Building-your-interactive-music-hierarchies.md) > About the properties of music objects

## About the properties of music objects

The properties of a music object are divided into two categories:

- **Relative properties** - Cumulative properties that are defined at each level of the hierarchy, for volume and Low-Pass Filter. 其总和决定最终属性值。了解各相对属性的最大和最小值限制至关重要，各属性的值域如下：

  - Volume（音量）：（-200, +200）单位为 dB
  - Low-pass filter（低通滤波器）：（0, 100）以百分比表示
  - High-pass filter: (0, 100) in percent

  |  |  |
  | --- | --- |
  | [备注] | 备注 |
  | Pitch is not considered for music objects for any platform. |
- **绝对属性** —— 在特定层级（通常为最高层级）上定义的属性，可以传递给其下所有子音乐对象，例如输出通路。但在各层级上，都可以选择 Override（不沿用）父对象的绝对属性。

  |  |  |
  | --- | --- |
  | [备注] | 备注 |
  | 您可以使用声音对象（包括音乐文件）生成振动数据。有关使用现有声音对象生成振动的详细信息，请参阅[“通过现有声音生成振动效果”一节](../../05-使用声音和振动来提升游戏体验/05-管理-Motion/03-为游戏创建振动效果/01-通过现有声音生成振动效果.md "通过现有声音生成振动效果")。 |

与声音对象类似，音乐对象也带有属性标记，说明该属性值是否与其它平台 Link（链接），是否与 RTPC（实时参数控制）中的游戏参数关联，以及是否启用了 Randomizer（随机化器）。

有关为属性值建立链接/取消链接、使用 RTPC 以及随机化属性值的详细信息，请参阅以下几节：

- [“Customizing object properties per platform”一节](../../07-完善工程/02-管理平台和语言版本/01-Authoring-across-platforms.md#customizing_object_properties_per_platform "Customizing object properties per platform")
- [“使用 Game Parameter 控制属性值”一节](../../04-与游戏互动/05-使用-RTPC/03-使用-Game-Parameter-控制属性值/00-使用-Game-Parameter-控制属性值.md "使用 Game Parameter 控制属性值")
- [“通过随机化属性值来改善播放”一节](../../03-设置工程/06-Building-your-sound-and-motion-hierarchies/05-通过随机化属性值来改善播放.md "通过随机化属性值来改善播放")

---