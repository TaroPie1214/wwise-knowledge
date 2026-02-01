# 了解 Mixing Desk

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [完善工程](../../00-完善工程.md) > [管理输出](../00-管理输出.md) > [完成终混](00-完成终混.md) > 了解 Mixing Desk

### 了解 Mixing Desk

Mixing Desk 是一个灵活强大的调音台，它能把各种各样的属性放到同一个视图中，以供实时细调游戏的混音。用户可以在 Mixing Desk 中添加任意对象或总线，然后定义总线连线、应用效果器和衰减共享集、编辑状态属性，并修改各个独立对象和总线的各种属性。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 在 Wwise 中，默认情况下您可以按 **F8** 来切换到 Mixer 布局。 |

如果您启动捕获会话，则还可在 Mixing Desk 中查看各个对象的活动，包括某声部何时播放、是否闪避总线以及是否旁通了效果器。各个音频对象还可静音或者独奏，便于单独调节混音通路中的对象。

Mixing Desk 基本上就是一个网格，每列是一个混音器工具栏，每行对应于 Wwise 中的一组常用属性。每个混音器工具栏绑定至一个对象，对象的名称显示在各个工具栏的顶部和底部。

![](../../../../../images/mixingdesk.png)

For more information about the Mixing Desk, see [Mixing Desk and Mixing Sessions](https://www.audiokinetic.com/library/edge/?source=Help&id=master_mixer_mixing_desk).

|  |  |
| --- | --- |
|  | Select or create a Mixing Desk. |
|  | Property sets. |
|  | Mixer strips. |

通道条中的各个属性设置都有一个快捷菜单。这些菜单包含与所选属性相关的一组命令。例如，当右键点击 Effect（效果器）插槽（0-3）时，就可以编辑插入效果器的各种属性，可以设置一个新的效果器，或者旁通当前效果器等等。为了访问快捷菜单，只需要在调音台通道条上用右键点击各个属性设置。

Mixing Desk 内的所有元素都会被保存在一个 Mixing Session 中。这样就可以为游戏的不同元素创建不同的 Mixing Session 了。而且，还可设置 Mixing Session 并在稍后继续对游戏的音频混音进行微调。

---