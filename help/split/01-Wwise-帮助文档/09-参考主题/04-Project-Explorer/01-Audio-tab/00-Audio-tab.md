# Audio tab

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Project Explorer](../00-Project-Explorer.md) > Audio tab

## Audio tab

在 Project Explorer 中的 Audio 选项卡中，您可以使用树形视图创建和管理工程素材的层级结构，此视图与 Windows 资源管理器或 Mac Finder 十分相似。You can organize your assets using several different types of objects such as regular folders like you would find in Windows, and other objects that are specific to Wwise such as Music Segments, containers, and Property Containers.

您可以通过点击加号 (+) 和减号 (-) 标记来展开和折叠各种类型的文件夹和对象，从而浏览树形结构。在此选项卡中，可重命名、剪切、复制、粘贴和删除对象，创建 Event（事件），导入并转换媒体文件。您还可以将若干个对象在文件夹之间和其它对象之间拖放，也可以拖放至 Wwise 界面内的不同视图。Audio 选项卡还包含一个工具栏，可让您快速将对象、总线和文件夹添加至工程层级结构。

要访问 Project Explorer 的命令，请在 Project Explorer 中右键点击对象。

| 界面元素 | 描述 |
| --- | --- |
| （工具栏） | 显示代表工程元素的若干个图标，这些元素可添加作为 Project Explorer 中所选节点的父节点或子节点。  在默认情况下，该工具栏显示可作为选定节点的子项加以添加的所有工程元素。要显示可以添加的父工程元素，请按 Shift 键。  要向所选节点添加子节点，只需点击图标栏中的任一活跃图标即可。要向所选节点添加父节点，只需按住 Shift 键并点击图标栏中的任一活跃图标即可。  根据工程层级结构中当前所选的对象类型，不同的图标将变成活跃状态。 |
| [“Audio Devices”一节](01-Audio-Devices/00-Audio-Devices.md "Audio Devices") | A complete list of Audio Devices in your project sorted by Work Units and Virtual Folders. Double-click an Audio Device to open the [“Audio Device Editor：System”一节](01-Audio-Devices/01-Audio-Device-Editor：System.md "Audio Device Editor：System").  |  |  | | --- | --- | | [备注] | 备注 | | 列出的音频设备是 sink（底层硬件抽象层）插件，它们是第三方或开发商使用 SDK 的 sink 插件框架创建的。They are only available to those who have created and/or incorporated these plug-ins into Wwise. 相应地它们没有工具栏图标。因此，创建时需要从 Audio Devices 部分的 Work Unit 快捷菜单选择 **New Child**（新建子对象）。在 **Work Unit** and **Virtual Folder** 选项下，会列出所有可用的 Audio Device 插件。These Audio Devices are also automatically added to the Init.bnk file. |  |  |  | | --- | --- | | [技巧] | 技巧 | | 如需深入了解如何开发 Audio Device 插件，请参阅  [SDK 文档](https://www.audiokinetic.com/library/?source=SDK&id=soundengine__plugins__audiodevices.html) 。 | |
| [“Busses hierarchy”一节](02-Busses-hierarchy/00-Busses-hierarchy.md "Busses hierarchy") | 对象层级结构顶部的总线层级结构，可让您定义工程内各种声音、音乐和振动结构的通路。  将不同的结构编组至总线后，您可以修改属性（如音量和音高），定义行为（如闪避），并可对整组应用效果器。  双击总线以打开 Bus Property Editor。 |
| [“Containers hierarchy: sound and motion objects”一节](03-Containers-hierarchy-sound-and-motion-objects/00-Containers-hierarchy-sound-and-motion-objects.md "Containers hierarchy: sound and motion objects") | Actor-Mixer 层级结构。工程内素材的层级结构。The Containers hierarchy can be comprised of a series of sound, motion, and music objects, organized in containers and folders. Click an object to open it in an object tab. |
| For objects in the Devices and Containers hierarchies: | |
| Inclusion | 启用。决定是否在生成 SoundBank 时在其中包含相应元素。如勾选，则包含该元素。如未勾选，则不会包含该元素。  为了针对各个平台来优化声音设计，有时需在特定平台上弃用某些元素。在默认情况下，此复选框会应用于所有平台。使用复选框左侧的 [Link 标志](../../../08-使用-Wwise/03-了解-Property-Editor/11-使用-Property-Editor.md#linking_unlinking_property_values "Linking or unlinking property values") 来取消链接相应元素。然后，便可根据平台来自定义复选框的状态。  若取消选中此选项，则将禁用编辑器中的属性和行为选项。  Default value: true |

  

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| To open the selected items in the default External Editor, press Ctrl+E. 有关详细信息，请参阅[“在外部编辑器中编辑音频文件”一节](../../../03-设置工程/05-管理工程中的媒体文件/07-在外部编辑器中编辑音频文件.md "在外部编辑器中编辑音频文件")。 |

**相关主题**

- [“Setting display options”一节](../../../08-使用-Wwise/01-认识-Project-Explorer-视图/01-Setting-display-options.md "Setting display options")
- [“Using the Project Explorer toolbar”一节](../../../08-使用-Wwise/01-认识-Project-Explorer-视图/03-Using-the-Project-Explorer-toolbar.md "Using the Project Explorer toolbar")
- [“添加父对象”一节](../../../03-设置工程/06-Building-your-sound-and-motion-hierarchies/03-Building-sound-and-motion-hierarchies.md#building_actor_mixer_hierarchy_adding_parent_objects "添加父对象")
- [“Adding objects to the Containers hierarchy”一节](../../../03-设置工程/06-Building-your-sound-and-motion-hierarchies/03-Building-sound-and-motion-hierarchies.md#adding_objects_to_actor_mixer_hierarchy "Adding objects to the Containers hierarchy")
- [“Managing objects in the Containers hierarchy”一节](../../../03-设置工程/06-Building-your-sound-and-motion-hierarchies/03-Building-sound-and-motion-hierarchies.md#managing_objects_in_actor_mixer_hierarchy "Managing objects in the Containers hierarchy")
- [“Working with music objects”一节](../../../06-创建互动音乐/02-Building-your-interactive-music-hierarchies/04-Working-with-music-objects.md "Working with music objects")
- [“Creating Work Units in your project”一节](../../../03-设置工程/04-Working-with-a-team/01-将工程分成-Work-Units.md#creating_work_units_in_project "Creating Work Units in your project")

---