# Contents Editor: Sound Voice

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [Audio tab](../00-Audio-tab.md) > [Containers hierarchy: sound and motion objects](00-Containers-hierarchy-sound-and-motion-objects.md) > Contents Editor: Sound Voice

#### Contents Editor: Sound Voice

这个Contents Editor 可让您快速访问与音频源关联的属性。您必须点击音频源才会显示相关列标题。

在使用 Sound Voice（语音）对象时，Contents Editor（内容编辑器）将通过语言标题栏来区分同时使用的不同语言版本。您可以使用语言标题栏上的向上和向下箭头来展开和折叠不同的语言分区。

| 界面元素 | 描述 |
| --- | --- |
|  | 点击列标题区 **Configure Columns**（配置列）快捷方式（右键点击）选项。p  此时将会打开 [“Object Property Settings”一节](../../12-搜索和工程全局编辑/06-Object-Property-Settings.md "Object Property Settings")。指定要显示的列及其顺序。  |  |  | | --- | --- | | [备注] | 备注 | | You cannot configure the columns for Source Contents Editors. | |
| [name] | 对象的名称。 |
| Inc. （Language（语言）） | 包含该语言。决定是否包含指定语言的源。  |  |  | | --- | --- | | [备注] | 备注 | | 若语言显示为斜体，则表示其没有关联源（音频文件或源插件）。 | |
| Use | 使用。对于语言，它包含 Link/Unlink（链接/取消链接）图标，方便为各平台应用不同的属性设置。有关详细信息，请参阅[“Linking or unlinking property values”一节](../../../../08-使用-Wwise/03-了解-Property-Editor/11-使用-Property-Editor.md#linking_unlinking_property_values "Linking or unlinking property values")。  对于源，则决定声音对象内哪个版本会被：  - 播放。 - 包含在 SoundBank（音频包）中。  此选项仅在声音对象内具有多个源时才可见。 |
| Audio File | 音频文件。源链接到的音频文件的名称。 |
| Make-up Gain | 补偿增益。声部的音量增益（单位为分贝 (dB)），应用于所有其它音量调整后，。Make-up Gain 在各个 Container 之间是累加的。  请参阅 [理解声部管线](../../../../07-完善工程/01-管理输出/05-了解声部管线.md "了解声部管线") 以了解声音将如何经过处理、路由以及在哪些环节可以应用音量和效果器。  有关响度归一化的详细信息，请参阅 [使用响度归一化或补偿增益来调节音量](../../../../07-完善工程/01-管理输出/04-使用-Loudness-Normalization-或-Make-up-Gain-调节音量.md "使用 Loudness Normalization 或 Make-up Gain 调节音量") 。  |  |  | | --- | --- | | [备注] | 备注 | | 默认滑杆范围从 -96 至 +12。您可以通过直接输入值，或在编辑控件上移动鼠标来输入超出限制范围的值。 |  Default value: 0  Range: -200 to 200  Units: dB |
| Duration | 音频源的时长。 |
| Notes | 备注。对象属性的额外信息。 |
|  | 向声音对象中添加新的源。  当您点击 Add Source 按钮时，将显示可添加的可用源列表。  |  |  | | --- | --- | | [备注] | 备注 | | 声音对象还可包含多种插件源。Contents Editor 中显示的列标题取决于您使用的插件。在使用插件源时，您可能遇到以下情况：  - 给定平台上不支持该插件。 - 给定机器中没有安装该插件。    如果当前平台上不支持您使用的插件，则该源在 Contents Editor 中将显示为灰色。如果没有安装该插件，则 Contents Editor 中将显示它；但 **Use** 按钮与 **Notes** 字段之间不会显示通常显示的属性控件，而显示“Source plug-in not installed”（未安装源插件）消息。 | |

**相关主题**

- [“使用插件创建 Source”一节](../../../../03-设置工程/05-管理工程中的媒体文件/08-使用插件创建-Source.md "使用插件创建 Source")
- [“Customizing object properties per platform”一节](../../../../07-完善工程/02-管理平台和语言版本/01-Authoring-across-platforms.md#customizing_object_properties_per_platform "Customizing object properties per platform")
- [“Selecting sources per platform”一节](../../../../07-完善工程/02-管理平台和语言版本/01-Authoring-across-platforms.md#selecting_sources_per_platform "Selecting sources per platform")
- [“Adding objects to the Contents Editor”一节](../../../../08-使用-Wwise/04-认识-Contents-Editor-视图/16-使用-Contents-Editor/02-Adding-objects-to-the-Contents-Editor.md "Adding objects to the Contents Editor")
- [“Re-ordering objects within the Contents Editor”一节](../../../../08-使用-Wwise/04-认识-Contents-Editor-视图/16-使用-Contents-Editor/03-Re-ordering-objects-within-the-Contents-Editor.md "Re-ordering objects within the Contents Editor")
- [“Expanding or collapsing lists”一节](../../../../08-使用-Wwise/04-认识-Contents-Editor-视图/16-使用-Contents-Editor/05-Expanding-or-collapsing-lists.md "Expanding or collapsing lists")
- [“Deleting objects”一节](../../../../08-使用-Wwise/04-认识-Contents-Editor-视图/16-使用-Contents-Editor/06-Deleting-objects.md "Deleting objects")
- [“Auditioning objects and sources within the Contents Editor”一节](../../../../08-使用-Wwise/04-认识-Contents-Editor-视图/16-使用-Contents-Editor/07-Auditioning-objects-and-sources-within-the-Content.md "Auditioning objects and sources within the Contents Editor")

---