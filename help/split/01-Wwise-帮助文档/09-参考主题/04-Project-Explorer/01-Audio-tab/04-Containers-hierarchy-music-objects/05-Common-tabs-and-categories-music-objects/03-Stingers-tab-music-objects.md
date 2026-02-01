# Stingers tab: music objects

[Wwise 帮助文档](../../../../../00-Wwise-帮助文档.md) > [参考主题](../../../../00-参考主题.md) > [Project Explorer](../../../00-Project-Explorer.md) > [Audio tab](../../00-Audio-tab.md) > [Containers hierarchy: music objects](../00-Containers-hierarchy-music-objects.md) > [Common tabs and categories: music objects](00-Common-tabs-and-categories-music-objects.md) > Stingers tab: music objects

##### Stingers tab: music objects

插播乐句。Stingers 选项卡可用于创建和定义插播乐句。插播乐句是与当前播放音乐叠加并混音的简单乐句。在游戏中，Stinger 被称为触发器。在此选项卡中，您可以将 Music Segment 映射到 Trigger，并定义调用触发器时音乐片段的播放选项。

| General | |
| --- | --- |
| 界面元素 | 描述 |
| [name] | 对象的名称。 |
| (Object Color) | 显示对象的颜色。单击图标可打开颜色选择器。    选择一种颜色并将其应用于对象。在为对象选择某种颜色时，会在选定方块上显示调色板图标，并在右下角标注黄色三角（如图所示）。  若要沿用父对象的颜色，请选中颜色选择器最左侧的方块。 |
| (Mute and Solo) | 控制对象的 Mute（静音）和 Solo（单独播放）状态，也会显示该对象是否处于被动静音和 Solo 状态。  将对象静音会使其在当前监听中无法听到。让对象 Solo 会使工程中的所有其它对象无声。  粗体的 **M** 或 **S** 表明已为对象主动设置了 Mute 或 Solo 状态。褪色的非粗体 **M** 或 **S** 表明对象的 Mute 或 Solo 状态是由于其它对象状态而被动设置的。  将对象静音会让其子对象被动静音。  让对象 Solo 会使同级对象被动静音，并让子对象和父对象被动 Solo。  |  |  | | --- | --- | | [技巧] | 技巧 | | 在点击 Solo 按钮的同时按住 Ctrl 键，可以强制仅 Solo 该 Solo 按钮所在的对象。 |  |  |  | | --- | --- | | [备注] | 备注 | | Mute 和 Solo 仅用于监视目的，而不会保存在工程中或存储在 SoundBank（声音包）中。 | |
| (Show references) | 指示工程中有多少元素包含对对象的直接引用。若存在对对象的引用，则图标显示为橙色；若不存在此类引用，则图标显示为灰色。  通过单击该按钮，可打开 [“Reference View 视图”一节](../../../12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")，并在 **References to:**（引用:）字段中查看对象的名称。 |

| Stingers | |
| --- | --- |
| 界面元素 | 描述 |
| **Stinger 设置** | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Trigger （触发器） | 使用当前 Stinger 的 Trigger 名称。 |
|  | 打开选择器菜单, 您可以在其中选择要通过哪个 Trigger 调用当前的 Stinger。 |
| Segment To Play | Trigger 事件发生时将播放的 Music Segment 名称。 |
|  | 打开 Project Explorer - Browser， 您可以在其中选择 Trigger 调用 Stinger 时将播放的片段。 |
| Play Segment At | 段落播放时机。确定在哪个时间点播放 Stinger。以下选项可用：  - **Immediate**:立即播放。 - **Next Grid**:在下一个预定义网格间隔处播放。网格是可对音乐对象进行虚拟分割的任意方法。通过向音乐对象添加另一个粒度级别，您可以高度灵活地为插播乐句定义同步点。 - **Next Bar**:在下一小节处播放。 - **Next Beat**:在下一拍处播放。 - **Next Cue**:在下一提示点处播放。下一提示点可以是 Entry、Exit 或自定义提示点。 - **Next Custom Cue**:在下一自定义提示点处播放。 - **Entry Cue**:在入口提示点处播放。 - **Exit Cue**:在出口提示点处播放。  Default value: Immediate |
| Custom cue match name | 匹配的提示点名。确定可选作“Play At”位置的自定义提示点。如果未指定任何名称，则任何自定义提示点都将匹配。  字符串比较不区分大小写，但它必须完全匹配（没有通配符）。  此选项仅在“Play At”设置为“Next Cue”或“Next Custom Cue”时才能使用。  名称匹配仅影响自定义提示点的选择；它不会影响入口或出口提示点的适用性。 |
|  | 向 Stinger 表中添加一行，用来在这一行中定义以下内容：  将会触发 Stinger 的 Trigger。  将会播放的 Music Segment。  Music Segment 将开始播放的时间点。 |
|  | 从 Stinger 列表中删除当前选定的 Stinger 及其相关组件。 |
| **Stinger 选项** | |
| Don’t play this Stinger again for x seconds. | 在 x 秒内不再播放此插播乐句。在经过 x 秒后才能再次使用该 Stinger。  若 Trigger 在 x 秒内调用此 Stinger，则将忽略或弃用 Trigger。Capture Log 中将显示消息，说明无法播放该 Stinger。注意，Don’t play Stinger again for x seconds 基于插播乐句的同步点，即插播乐句的入口提示点出现的时间点。  例如，对于一个 1 秒每拍的段落，其 Stinger 前导段长 1.5 秒，同步规则为“下一拍”，而且在 3 秒内不再播放 Stinger。试想，在发布 Trigger 时，此段落刚好播放到整拍。由于前导段长 1.5 秒，因此插播乐句的入口提示点无法与段落的下一拍同步，而会与再下一拍同步（即 2 秒后）。因此，接下来 5 秒内所发布的 Trigger（同步点之前的 2 秒以及不再播放的 3 秒）将全部弃用。  此外，当前时刻值也被算在内。例如，“不再播放”时间设为 0 时，在当前 Trigger 到达同步点之前，将弃用其他 Trigger。这样就不会在同一精确时间播放两个或更多 Stinger。  Default value: 0  Range: 0 to 3600 |
| Allow playing Stinger in next segment (if applicable) | 允许在下一段落中播放插播乐句（如适用）。决定是否可在播放列表内下一段落中播放此 Stinger。若 Trigger 调用了 Stinger，且在当前段落中下一个播放 Stinger 的时机太晚，则不播放 Stinger。但若选中此选项，将在播放列表内下一段落中首次出现符合条件的机会时播放 Stinger。Stinger 入点在 Play At 字段中定义。  Default value: Yes |

**相关主题**

- [“添加 Stinger”一节](../../../../../06-创建互动音乐/08-使用-Stinger.md#adding_stingers "添加 Stinger")
- [“移除 Stinger”一节](../../../../../06-创建互动音乐/08-使用-Stinger.md#removing_stingers "移除 Stinger")
- [“定义 Stinger 的播放设置”一节](../../../../../06-创建互动音乐/08-使用-Stinger.md#defining_playback_settings_for_stingers "定义 Stinger 的播放设置")
- [“预览 Stinger”一节](../../../../../06-创建互动音乐/08-使用-Stinger.md#auditioning_stingers "预览 Stinger")

---