# Environmental Curves Tab

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [工程](../00-工程.md) > [Project Settings](00-Project-Settings.md) > Environmental Curves Tab

### Environmental Curves Tab

In the Environmental Curves tab of the Project Settings dialog, you can define the default curves for obstruction, occlusion, diffraction, and transmission by specifying an Attenuation ShareSet.

| 界面元素 | 描述 |
| --- | --- |
| Project Environmental Curves | The attenuation ShareSet to be used at the project level.  Sounds that don't have an attenuation ShareSet use the Obstruction, Occlusion, Diffraction, and Transmission curves set here.  Alternatively, for sounds that do have an attenuation ShareSet, you can set their Obstruction, Occlusion, Diffraction, and Transmission to use these project curves instead of creating custom ones.  |  |  | | --- | --- | | [备注] | 备注 | | - Although the referenced ShareSet contains distance curves, they aren't used at the project level. Environmental curves are Obstruction, Occlusion, Diffraction, and Transmission curves. - Project curves set to Use Project Obstruction, Occlusion, Diffraction, or Transmission, are treated as set to None. - A ShareSet used at the project level can also be used on an individual sound. For more information see [“应用衰减”一节](../../../05-使用声音和振动来提升游戏体验/02-定义定位/07-应用衰减/00-应用衰减.md "应用衰减"). When a ShareSet is used on an individual sound, the distance curves are used. | |
|  | 确定。关闭 Project Settings 对话框并保存设置。 |
|  | 取消。关闭 Project Settings 对话框而不保存设置。 |

**相关主题**

- [“Defining environmental curves for your project”一节](../../../03-设置工程/01-处理工程/02-定义工程设置/05-Defining-environmental-curves-for-your-project.md "Defining environmental curves for your project")
- [“Attenuation Editor”一节](../../04-Project-Explorer/05-ShareSets-选项卡/02-Attenuation-Editor.md "Attenuation Editor")

---