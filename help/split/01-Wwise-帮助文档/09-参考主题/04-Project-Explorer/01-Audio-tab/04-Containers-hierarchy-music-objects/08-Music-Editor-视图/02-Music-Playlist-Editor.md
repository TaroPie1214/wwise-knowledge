# Music Playlist Editor

[Wwise 帮助文档](../../../../../00-Wwise-帮助文档.md) > [参考主题](../../../../00-参考主题.md) > [Project Explorer](../../../00-Project-Explorer.md) > [Audio tab](../../00-Audio-tab.md) > [Containers hierarchy: music objects](../00-Containers-hierarchy-music-objects.md) > [Music Editor 视图](00-Music-Editor-视图.md) > Music Playlist Editor

##### Music Playlist Editor

音乐播放列表编辑器。您可以在 Music Playlist Editor 中组合 Music Playlist Container 的内容。您可以在 Music Playlist Container 中排列段落和组的播放顺序，然后定义其属性。Playlist Container 中的组可使用步进模式（step）或连续模式（continuous）进行随机或顺序播放。

您必须先至少添加一个段落或组，Music Playlist Editor 中的大多数选项才可用。请参阅 [“定义 Music Playlist Container 的播放行为”一节](../../../../../06-创建互动音乐/03-定义音乐对象播放行为/02-定义-Music-Playlist-Container-的播放行为.md "定义 Music Playlist Container 的播放行为")。

| 界面元素 | 描述 |
| --- | --- |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| |  | | --- | |  |  (Play indicator) | 播放标志。在播放期间，指示当前正在播放的组或段落。 |
| Play Mode | 组／段落。Music Playlist Container 中按特定播放顺序排列的对象列表。  播放列表确定在游戏引擎调用 Playlist Container 时播放的对象和播放的顺序。  有四种可用的组与段落：  - **Sequence continuous**:序列连续模式。每次播放组时，依次按顺序播放该组中的所有音乐对象。 - **Sequence step**:序列步进模式。每次播放组时，仅播放组中的一个音乐对象。下次播放该组时，将播放组中的下一个音乐对象。 - **Random continuous**:随机连续模式。每次播放组时，随机逐一播放该组中的所有音乐对象。 - **Random step**:随机步进模式。每次播放组时，仅随机播放所选组中的一个音乐对象。  Default value: Sequence Continuous |
| Random type | Defines whether a group uses standard or shuffle mode.  - **Standard**:标准模式。保持容器中的对象池完整。播放某个对象后，该对象不会从可播放的对象列表中移除，因此可重复播放。 - **Shuffle**:洗牌模式。在播放对象将它们从对象池中移除。此选项避免在播放完所有对象之前重复播放声音。在重置列表时，最后播放的对象不会重复播放。  该选项仅适用于 Random Group。  Default value: Standard |
| Avoid Repeat | 避免重复。确定在重复播放某个对象之前必须播放的其它对象的个数。  您选择的是 Standard 还是 Shuffle 模式将影响该选项的行为。  在 Standard 模式中，完全随机选择播放对象，但最后播放的 x 个对象将从列表中弃用。  在 Shuffle 模式中，重置列表时，最后播放的 x 个对象将从列表中排除。  若非循环 Random Group 设为 Shuffle 和 Continuous，则 Limit Repetition To 选项不会对分组的播放产生影响。  此选项仅适用于 Random Group。  Default value: 1  Range: 0 to 999 |
| Weight | 权重。当播放容器时选中该对象的概率。  此选项仅适用于 Random Group。  Default value: 50  Range: 0.001 to 100 |
| Loop Count | 循环计数。组或组内对象将播放的次数。最终结果取决于正在循环播放的组的类型：  - Sequence Continuous 组：循环计数定义每次播放组时整个组将播放的次数。 - Sequence Step 组：循环计数定义每次播放组时组内对象将播放的次数。例如，有六个段落且循环计数为 2 的 Sequence Step 组将在第一次播放组时播放段落 1 和 2，在第二次播放组时播放段落 3 和 4，以此类推。  Random Continuous 组：循环计数定义组每次播放时整个组将播放的次数。 - Random Step 组：循环计数定义每次播放组时组内将播放的对象个数。  默认值：1 范围：1 至 32,767  要将循环次数设置为无限循环，请将循环数设置为 1，然后点击下箭头。 |
|  | 创建所选组的子组。For information on creating, moving, and deleting groups, see [“定义 Music Playlist Container 的播放行为”一节](../../../../../06-创建互动音乐/03-定义音乐对象播放行为/02-定义-Music-Playlist-Container-的播放行为.md "定义 Music Playlist Container 的播放行为").  |  |  | | --- | --- | | [技巧] | 技巧 | | Right-click a group to open a shortcut menu with the options Cut, Copy, Paste, and Delete. | |

---