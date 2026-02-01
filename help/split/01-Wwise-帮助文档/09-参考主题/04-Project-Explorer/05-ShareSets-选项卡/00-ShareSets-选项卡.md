# ShareSets 选项卡

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Project Explorer](../00-Project-Explorer.md) > ShareSets 选项卡

## ShareSets 选项卡

Project Explorer（工程资源管理器）的 ShareSets（共享集）选项卡会按 Work Unit（工作单元）显示 ShareSet 的完整列表。在此选项卡中，可创建并管理 ShareSet 及其对应的 Work Unit。Effects（效果器）部分中列有 Wwise 配套提供的 Factory Effects（出厂效果器）。

您可以通过单击加号 (+) 和减号 (-) 来展开和折叠文件夹以便浏览各个文件夹和 Work Unit。ShareSet 选项卡还包含一个工具栏，可让您快速将 ShareSet、Work Unit 和文件夹添加至工程层级结构。

| 界面元素 | 描述 |
| --- | --- |
| （工具栏） | 显示代表工程元素的若干个图标，这些元素可添加作为 Project Explorer 中所选节点的父节点或子节点。  在默认情况下，该工具栏显示可作为选定节点的子项加以添加的所有工程元素。要显示可以添加的父工程元素，请按 Shift 键。  要向所选节点添加子节点，只需点击图标栏中的任一活跃图标即可。要向所选节点添加父节点，只需按住 Shift 键并点击图标栏中的任一活跃图标即可。  根据层级结构中当前所选的对象类型，不同的图标将处于活跃状态。 |
| Effects | 效果器。按照 Virtual Folder（虚拟文件夹）和 Work Unit 显示工程内 Effect 共享集的完整列表。双击效果器 ShareSet 以打开 [“Effect Plug-in Editor”一节](01-Effect-Plug-in-Editor.md "Effect Plug-in Editor")。 |
| Attenuations | 衰减。按照 Virtual Folder 和 Work Unit 显示工程内 Attenuation 共享集的完整列表。双击 Attenuation ShareSet 以打开 [“Attenuation Editor”一节](02-Attenuation-Editor.md "Attenuation Editor")。 |
| Conversion Settings（转码设置） | 转码设置。按照 Virtual Folder 和 Work Unit 显示工程内 Conversion Settings 共享集的完整列表。双击 Conversion Settings 共享集可打开 [“Conversion Settings Editor”一节](03-Conversion-Settings-Editor/00-Conversion-Settings-Editor.md "Conversion Settings Editor")。 |
| Modulators | 调制器。按照 Virtual Folder 和 Work Unit 显示工程内 LFO、Envelope 和 Time Modulator 共享集的完整列表。双击 Modulator ShareSet 以打开 [“Modulator Editor 视图”一节](04-Modulator-Editor-视图/00-Modulator-Editor-视图.md "Modulator Editor 视图")。 |
| Virtual Acoustics | 虚拟声学。按照 Virtual Folder 和 Work Unit 显示工程内 Virtual Acoustics 共享集的完整列表。Virtual Acoustics 目前仅包含 Acoustic Texture（声学材质）。这些材质可配合 [“Reflect”一节](../../../10-Wwise-插件/04-效果器插件/19-Reflect.md "Reflect") 插件来表示不同的材料属性。这些属性（如频率吸收）可模拟不同材料对早期反射声的影响。  比方说，吸声材料对所有声场的吸收率都是 100%，那么就会完全吸收而不产生任何反射。相比之下，反射性较强的材料（如水泥）本身通常会反射一定量的声音，其对所有频段的整体吸收率较低（假设为 10 ~ 30%），而对高频部分的吸收率相对较高。其他材料（如特定木材）一般比水泥的反射性偏弱，而对低频部分的吸收率相对较高。  双击 Texture 可打开 [“Acoustic Texture Editor”一节](05-Acoustic-Texture-Editor.md "Acoustic Texture Editor")。 |
| **For Effects:** | |
| Inclusion | 启用。决定是否在生成 SoundBank 时在其中包含相应元素。如勾选，则包含该元素。如未勾选，则不会包含该元素。  为了针对各个平台来优化声音设计，有时需在特定平台上弃用某些元素。在默认情况下，此复选框会应用于所有平台。使用复选框左侧的 [Link 标志](../../../08-使用-Wwise/03-了解-Property-Editor/11-使用-Property-Editor.md#linking_unlinking_property_values "Linking or unlinking property values") 来取消链接相应元素。然后，便可根据平台来自定义复选框的状态。  若取消选中此选项，则将禁用编辑器中的属性和行为选项。  Default value: true |

**相关主题**

- [“Using the Project Explorer toolbar”一节](../../../08-使用-Wwise/01-认识-Project-Explorer-视图/03-Using-the-Project-Explorer-toolbar.md "Using the Project Explorer toolbar")
- [“创建效果器共享集”一节](../../../05-使用声音和振动来提升游戏体验/04-管理效果器/00-管理效果器.md#creating_effect_sharesets "创建效果器共享集")
- [“删除效果器共享集”一节](../../../05-使用声音和振动来提升游戏体验/04-管理效果器/00-管理效果器.md#deleting_effect_sharesets "删除效果器共享集")
- [“将 Effect ShareSet 转换为自定义实例”一节](../../../05-使用声音和振动来提升游戏体验/04-管理效果器/00-管理效果器.md#converting_effect_sharesets_into_custom_instances "将 Effect ShareSet 转换为自定义实例")
- [“Creating Attenuation ShareSets”一节](../../../05-使用声音和振动来提升游戏体验/02-定义定位/07-应用衰减/01-管理多份衰减.md#creating_an_attenuation_shareset "Creating Attenuation ShareSets")
- [“Deleting Attenuation ShareSets”一节](../../../05-使用声音和振动来提升游戏体验/02-定义定位/07-应用衰减/01-管理多份衰减.md#deleting_an_attenuation_shareset "Deleting Attenuation ShareSets")
- [“Applying Attenuation ShareSets to objects”一节](../../../05-使用声音和振动来提升游戏体验/02-定义定位/07-应用衰减/02-将衰减应用到对象.md#applying_an_attenuation_shareset_to_an_object "Applying Attenuation ShareSets to objects")
- [“Converting Attenuation ShareSets into custom instances”一节](../../../05-使用声音和振动来提升游戏体验/02-定义定位/07-应用衰减/02-将衰减应用到对象.md#converting_attenuation_sharesets_into_custom_instances "Converting Attenuation ShareSets into custom instances")
- [“Creating Work Units in your project”一节](../../../03-设置工程/04-Working-with-a-team/01-将工程分成-Work-Units.md#creating_work_units_in_project "Creating Work Units in your project")
- [“内置音频设备”一节](../../../07-完善工程/01-管理输出/06-内置音频设备.md "内置音频设备")

---