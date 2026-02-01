# 使用插件创建 Source

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [设置工程](../00-设置工程.md) > [管理工程中的媒体文件](00-管理工程中的媒体文件.md) > 使用插件创建 Source

## 使用插件创建 Source

Wwise 的开放式体系结构使您能够通过创建源插件（Source Plug-in）来提升音频效果。Wwise 的开放式体系结构使您能够通过创建源插件来增强音频和振动。这些插件（例如合成器和物理建模）可轻松集成到 Wwise 中，并可用于创建声音和振动对象。您还可以修改插件属性以创建更广泛的音效和振动效果。

Wwise 自带不少的源插件。

**可用的源插件**

- Audio Input（音频输入）
- External Source（外部源）
- Motion（振动）
- Silence
- Sine（正弦波）
- Soundseed Air Wind\*
- Soundseed Air Woosh\*
- Tone Generator

  \* - 如果您计划为您的游戏开发、集成和发布 Soundseed Air，则需要购买单独的授权。有关详细信息，请联系 Audiokinetic 销售团队，邮件地址是： [sales@audiokinetic.com。](mailto:sales@audiokinetic.com)

**添加源插件的方法如下：**

1. 将对象加载到 Property Editor 中。
2. 在 Contents Editor 中，点击 **Add Source**。

   Source 菜单中将会显示可用的源插件列表。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 为特定平台创建的源插件，在所有其它平台的源插件列表中将显示为不可用。 |
3. 选择要添加的源插件。

   源已添加到对象中，并在 Contents Editor 中显示为新条目。
4. 双击源插件以在 Source Plug-in Property Editor（源插件属性编辑器）中显示完整的属性列表。
5. 根据需要，编辑属性。

---