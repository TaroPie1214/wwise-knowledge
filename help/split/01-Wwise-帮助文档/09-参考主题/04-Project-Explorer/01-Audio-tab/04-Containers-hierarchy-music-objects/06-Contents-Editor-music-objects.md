# Contents Editor: music objects

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [Audio tab](../00-Audio-tab.md) > [Containers hierarchy: music objects](00-Containers-hierarchy-music-objects.md) > Contents Editor: music objects

#### Contents Editor: music objects

通过 Contents Editor，您可以快速访问 Music Switch Container（音乐切换容器）、Music Playlist Container（音乐播放列表容器）和 Music Segment（音乐片段）相关的常见属性，以及它们的音频源。

| 界面元素 | 描述 |
| --- | --- |
|  | 点击列标题区 **Configure Columns**（配置列）快捷方式（右键点击）选项。p  此时将会打开 [“Object Property Settings”一节](../../12-搜索和工程全局编辑/06-Object-Property-Settings.md "Object Property Settings")。指定要显示的列及其顺序。  |  |  | | --- | --- | | [备注] | 备注 | | You cannot configure the columns for Source Contents Editors. | |
| Inclusion | 启用。决定是否在生成 SoundBank 时在其中包含相应元素。如勾选，则包含该元素。如未勾选，则不会包含该元素。  为了针对各个平台来优化声音设计，有时需在特定平台上弃用某些元素。在默认情况下，此复选框会应用于所有平台。使用复选框左侧的 [Link 标志](../../../../08-使用-Wwise/03-了解-Property-Editor/11-使用-Property-Editor.md#linking_unlinking_property_values "Linking or unlinking property values") 来取消链接相应元素。然后，便可根据平台来自定义复选框的状态。  若取消选中此选项，则将禁用编辑器中的属性和行为选项。  Default value: true |
| Voice Volume（声部音量）。 | 对象输出到总线或发送至辅助总线之前的衰减（电平或振幅）。有关音量的详细信息，请参阅[“了解声部管线”一节](../../../../07-完善工程/01-管理输出/05-了解声部管线.md "了解声部管线")。  默认值：0 范围：-400 至 400 单位：dB  |  |  | | --- | --- | | [备注] | 备注 | | 默认滑杆范围从 -96 至 +12 dB。您可以通过直接输入值或在编辑控件上移动鼠标来输入超出限制范围的值。 | |
| Voice Low-pass Filter | 声部低通滤波器。基于指定频率值针对高频进行衰减的递归滤波器。  此滤波器的单位表示低通滤波的百分比，其中 0 表示无低通滤波（信号不受影响）而 100 表示最大衰减。  有关更多详细信息，请参阅 [Wwise 中 LPF 和 HPF 值与截止频率的对应关系](../../../../03-设置工程/06-Building-your-sound-and-motion-hierarchies/04-工程层级结构中的属性介绍/02-定义相对属性（音量、音高、LPF、HPF）/01-Low-pass-和-High-pass-Filter-值与截止频率的关系.md#wwise_lpf_value_cutoff_frequencies "Wwise 中 LPF 和 HPF 值与截止频率的对应关系") 页面。  单位：%  Default value: 0  Range: 0 to 100 |
| Notes | 备注。对象属性的额外信息。 |

**相关主题**

- [“定义 Music Switch Container 内各个音乐对象的行为”一节](../../../../06-创建互动音乐/03-定义音乐对象播放行为/03-定义-Music-Switch-Container-的内容和行为.md#defining_behaviors_of_music_objects_within_music_switch_containers "定义 Music Switch Container 内各个音乐对象的行为")
- [“Customizing object properties per platform”一节](../../../../07-完善工程/02-管理平台和语言版本/01-Authoring-across-platforms.md#customizing_object_properties_per_platform "Customizing object properties per platform")
- [“通过随机化属性值来改善播放”一节](../../../../03-设置工程/06-Building-your-sound-and-motion-hierarchies/05-通过随机化属性值来改善播放.md "通过随机化属性值来改善播放")
- [“Adding objects to the Contents Editor”一节](../../../../08-使用-Wwise/04-认识-Contents-Editor-视图/16-使用-Contents-Editor/02-Adding-objects-to-the-Contents-Editor.md "Adding objects to the Contents Editor")
- [“Re-ordering objects within the Contents Editor”一节](../../../../08-使用-Wwise/04-认识-Contents-Editor-视图/16-使用-Contents-Editor/03-Re-ordering-objects-within-the-Contents-Editor.md "Re-ordering objects within the Contents Editor")
- [“Expanding or collapsing lists”一节](../../../../08-使用-Wwise/04-认识-Contents-Editor-视图/16-使用-Contents-Editor/05-Expanding-or-collapsing-lists.md "Expanding or collapsing lists")
- [“Deleting objects”一节](../../../../08-使用-Wwise/04-认识-Contents-Editor-视图/16-使用-Contents-Editor/06-Deleting-objects.md "Deleting objects")
- [“Auditioning objects and sources within the Contents Editor”一节](../../../../08-使用-Wwise/04-认识-Contents-Editor-视图/16-使用-Contents-Editor/07-Auditioning-objects-and-sources-within-the-Content.md "Auditioning objects and sources within the Contents Editor")

---