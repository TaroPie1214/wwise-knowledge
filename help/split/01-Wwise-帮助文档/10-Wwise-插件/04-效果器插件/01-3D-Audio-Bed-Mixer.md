# 3D Audio Bed Mixer

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [Wwise 插件](../00-Wwise-插件.md) > [效果器插件](00-效果器插件.md) > 3D Audio Bed Mixer

## 3D Audio Bed Mixer

（请参阅下文的 [“3D Audio Bed Mixer properties”一节](01-3D-Audio-Bed-Mixer.md#wwise_3daudiobedmixer_properties "3D Audio Bed Mixer properties")。）

3D Audio Bed Mixer 插件可通过对 Audio Object（音频对象）实施混音来减少发送到总线的 Audio Object 数量。藉此，降低 Audio Object 处理所消耗的 CPU 资源数量。该插件一般插入到 Audio Objects 总线上，其可能会生成三种输出：Main Mix、Passthrough Mix 和一系列未经混音的 Audio Object（符合条件的话会在管线末端升级为 [System Audio Object](../../14-词汇表.md#glossary_system_audio_object "System Audio Object")）。

该插件会复制 System Audio Device（系统音频设备）的 Audio Object 输出机制的行为。有关此机制的详细信息，请参阅“[“System Audio Device 的作用”一节](../../03-设置工程/07-建立输出总线的结构/03-了解基于对象的音频/02-System-Audio-Device-的作用.md "System Audio Device 的作用")”章节。

The 3D Audio Bed Mixer plug-in can only be inserted on a bus; it cannot be inserted on
objects in the Containers hierarchy.

### Main Mix

Main Mix（主混音）代表空间化 Bed，其通常使用环绕声或 Ambisonics 声道配置来围绕听者构建由剧情声音构成的声景。这种混音适合在终端实施双耳处理。

3D Audio Bed Mixer 始终为 Main Mix 生成单个 Audio Object。在默认情况下，该插件会查询管线末端的 Audio Device 来确定 Main Mix 配置。除此之外，也可在插件属性中设置 Main Mix 的声道配置。

倘若代表 Main Mix 的 Audio Object 到达 Audio Device，肯定会在 Audio Device 对应的 Main Mix 中实施混音。

### Passthrough Mix

Passthrough Mix（直通混音）是用于直接摆位到用户耳机的平面立体声 Bed。其专门用来旁通双耳处理。

3D Audio Bed Mixer 有时并不会为 Passthrough Mix 生成 Audio Object。这取决于 **Passthrough Mix** 属性及管线末端的 Audio Device 的 3D Audio 能力。在默认情况下，只有 Audio Device 支持 Passthrough Mix 才会生成 Passthrough Mix。

倘若为 Passthrough Mix 生成了 Audio Object 且其到达 Audio Device，肯定会在 Audio Device 对应的 Passthrough Mix（如有）中实施混音。

### 适宜 System Audio Object

适宜 System Audio Object 是指符合所有要求并可由 Audio Device 升级为 [System Audio Object](../../14-词汇表.md#glossary_system_audio_object "System Audio Object") 的 Audio Object。

3D Audio Bed Mixer 可能会决定不在 Main Mix 或 Passthrough Mix 中实施混音而直接让适宜 System Audio Object 通过。这取决于相应属性及管线末端的 Audio Device 的 [3D Audio](../../14-词汇表.md#glossary_3daudio "3D Audio") 能力。在默认情况下，只有 Audio Device 提供相应支持，该插件才会输出适宜 System Audio Object。

适宜 System Audio Object 的最大数量可通过插件的 **System-Eligible Audio Object Limit** 属性来控制。所有超出此限值的适宜 System Audio Object 都将实施混音。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 该插件不会考虑 Audio Device 的 System Audio Object 限值，因为其无法保证其他适宜 System Audio Object 不会到达 Audio Device。 |

下图简要阐释了插件的行为。

![](../../../../images/3d_audio_bed_mixer_plugin.png)

|  |  |
| --- | --- |
|  | 将声部输出到总线。 |
|  | 从之前的混音总线得到基于声道的格式。 |
|  | 从之前的总线 Processing Audio Objects 得到一系列 Audio Object。 |
|  | 按照以下方式把对总线的输入提供给插件：  - 若总线处于 Mixing（正在混音）状态，则将所有输入（包括声部、基于声道的输入和 Audio Object）混合在一起，并作为单个 Audio Object 提供给插件。 - 若总线处于 Processing Audio Objects（正在处理音频对象）状态，则将所有不属于 Audio Object 的输入（比如声部和基于声道的输入）转换为单独的 Audio Object。在此之后，会将其与总线收到的所有其他 Audio Object 一起传给插件。 |
|  | 插件查询 System Audio Device 设置。这些设置会影响插件的行为（如下表中所述）。 |
|  | 检查总线收到的 Audio Object 是否为适宜 System Audio Object。不符合要求的 Audio Object 将被输出到 Main Mix。 |
|  | 应用 System-Eligible Audio Object Limit。超出此限值的 Audio Object 将被输出到 Main Mix。 |
|  | 未做 3D 空间化处理的单声道和立体声 Audio Object 将被输出到 Passthrough Mix。 |

### 3D Audio Bed Mixer properties

| 界面元素 | 描述 |
| --- | --- |
| Name | 名称。效果器实例的名称。  效果器实例是一组效果器属性设置。它们可以是两种类型之一：自定义或共享集。自定义实例只能由一个对象使用，然而共享集可在多个对象之间共享。 |
| (Object Color) | 显示对象的颜色。单击图标可打开颜色选择器。    选择一种颜色并将其应用于对象。在为对象选择某种颜色时，会在选定方块上显示调色板图标，并在右下角标注黄色三角（如图所示）。  若要沿用父对象的颜色，请选中颜色选择器最左侧的方块。 |
| Inclusion | 启用。决定是否在生成 SoundBank 时在其中包含相应元素。如勾选，则包含该元素。如未勾选，则不会包含该元素。  为了针对各个平台来优化声音设计，有时需在特定平台上弃用某些元素。在默认情况下，此复选框会应用于所有平台。使用复选框左侧的 [Link 标志](../../08-使用-Wwise/03-了解-Property-Editor/11-使用-Property-Editor.md#linking_unlinking_property_values "Linking or unlinking property values") 来取消链接相应元素。然后，便可根据平台来自定义复选框的状态。  若取消选中此选项，则将禁用编辑器中的属性和行为选项。  Default value: true |
| (Show references) | 指示工程中有多少元素包含对对象的直接引用。若存在对对象的引用，则图标显示为橙色；若不存在此类引用，则图标显示为灰色。  通过单击该按钮，可打开 [“Reference View 视图”一节](../../09-参考主题/04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")，并在 **References to:**（引用:）字段中查看对象的名称。 |
| Notes | 备注。Effect 的其它信息。 |
| Metering | 电平测量。指示当前正在测量电平的对象的名称。 |
|  | 允许浏览其他要测量电平的对象。  |  |  | | --- | --- | | [备注] | 备注 | | 只有对于包含 VU 电平表的效果器，Effect Editor 中才会显示电平测量界面元素。 | |
|  | 设置 Effect Editor 中选定标签页的显示方式。默认情况下，整体面板中仅显示一个选定标签页。不过，您可以通过单击分隔器按钮将面板沿横向或纵向一分为二，显示两个不同的标签页。当前所选选项将以高亮背景色显示。  |  |  | | --- | --- | | [备注] | 备注 | | 无法同时在两个面板中显示同一标签页。若选中的标签页已在另一面板中显示，则另一面板将自动显示另一标签页。 | |

|  |  |
| --- | --- |
| Main Mix Configuration | 主混音配置。由插件生成的 Main Mix 的声道配置。在选择 **Same as Audio Device** 时，将依据总线管线末端 Audio Device 的性能选择该配置。这种行为等同于选择 **Same as Main Mix** 作为总线本身的 Bus Configuration。  Default value: Same as Audio Device |
| Passthrough Mix | 直通混音。决定插件是否要生成代表直通（非空间化）混音的附加 Audio Object。  - **When Audio Device supports it**:插件查询总线管线末端的 Audio Device 来决定是否生成直通混音。只有 Audio Device 支持，才会生成直通混音。 - **Always**:无论 Audio Device 是否支持，都会生成直通混音。 - **Never**:无论 Audio Device 是否支持，都不生成直通混音。  |  |  | | --- | --- | | [备注] | 备注 | | 若不生成直通混音，将转而在 Main Mix 中对原本要在 Passthrough Mix 中混音的 Audio Object 进行混音。 |  Default value: When Audio Device supports it |
| Preserve System-Eligible Audio Objects | 保留适宜系统音频对象。决定插件是否让带有 3D 空间化效果的 Audio Object 通过而不在 Main Mix 中对其进行混音。  - **When Audio Device supports it**:插件查询总线管线末端的 Audio Device 来决定是对适宜 System Audio Object 进行混音还是让其通过。若 Audio Device 支持 System Audio Object，将保留 System Audio Object，否则将对其进行混音。 - **Always**:保留适宜 System Audio Object，直至达到 System-Eligible Audio Object Limit，而无论 Audio Device 是否支持。 - **Never**:始终在 Main Mix 中对适宜 System Audio Object 进行混音，而无论 Audio Device 是否支持。  Default value: When Audio Device supports it |
| System-Eligible Audio Object Limit | 适宜系统音频对象限值。插件可输出的适宜 System Audio Object 的最大数量。所有超出此限值的适宜 System Audio Object 都将实施混音。  |  |  | | --- | --- | | [备注] | 备注 | | 该限值仅在保留 System Audio Object（由 Preserve System-Eligible Audio Objects 属性决定）时适用。 |  Default value: 64  Range: 0 to 512 |

---