# Sequence Container tab

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [Audio tab](../00-Audio-tab.md) > [Common tabs and categories: audio structures](00-Common-tabs-and-categories-audio-structures.md) > Sequence Container tab

#### Sequence Container tab

In the Sequence Container tab you can add and sort the playlist objects in a Sequence Container. 请参阅 [“创建序列容器”一节](../../../../05-使用声音和振动来提升游戏体验/01-定义对象播放行为/02-定义-RandomSequency-Container-的播放行为/02-创建序列容器.md "创建序列容器")。

| Sequence Container （序列容器） | |
| --- | --- |
| 界面元素 | 描述 |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| (Add to Playlist) | Click to add an object from the Contents editor. |
| (Remove Selected from Playlist) | Click to remove the selected objects from the playlist. |
| Playlist Object | When you create a Sequence Container, an empty Playlist is added to the Sequence Container Tab. You can populate it so that objects are played back in a particular order. 请参阅 [“创建播放列表”一节](../../../../05-使用声音和振动来提升游戏体验/01-定义对象播放行为/02-定义-RandomSequency-Container-的播放行为/03-创建播放列表.md "创建播放列表")。 |
| Waveform | The waveform of the Sound SFX or Sound Voice. |
| Weight | 权重。在播放容器时选择该对象的播放概率。  将容器中各个对象的权重相加，为各个对象指定的数字相对于权重和代表在所有对象中选择播放该对象的几率。例如，如果容器内有两个对象，权重值分别为 1 和 100，则第一个对象将有 1/101 的播放几率，而第二个对象将有 100/101 的几播放率。  Default value: 50  Range: 0.001 to 100 |

---