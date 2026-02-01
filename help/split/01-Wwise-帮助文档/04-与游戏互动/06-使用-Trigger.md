# 使用 Trigger

[Wwise 帮助文档](../00-Wwise-帮助文档.md) > [与游戏互动](00-与游戏互动.md) > 使用 Trigger

## 使用 Trigger

Trigger（触发器）是一种 Wwise 元素，跟其他 Game Sync（游戏同步器）一样会被游戏调用。触发器会定义 Wwise 将做出怎样的特定响应来反映游戏中的情节变化。More specifically, a Trigger responds to a spontaneous occurrence in the game and launches a Stinger. Stinger 是一种短乐句，它会与当前音乐叠加并混合播放，以音乐的形式来对游戏做出响应。For more information about how Triggers and Stingers work together, see [*使用 Stinger*](../06-创建互动音乐/08-使用-Stinger.md "使用 Stinger").

For example, in a fighting game, when a character lands a powerful kick, you can intensify
the impact of that action with a Stinger. Before you create a Stinger, you must create a
Trigger, perhaps named High kick, to be called at these points in the game, and you must choose
a short Music Segment to associate with the Trigger.

下图展示了游戏关键时刻用来播放 Stinger 的 Trigger 机制。

![](../../../images/000051_01e_online.png)

In Wwise Authoring, Triggers are represented by this icon: ![](../../../images/trigger_icon.png).

## Creating Triggers

You can create Triggers in the Game Syncs tab of the Project Explorer.

**To create a new Trigger:**

1. 在 Project Explorer 中，切换至 Game Syncs 选项卡。
2. 在 Triggers 层级，执行以下操作之一：

   - Select a Work Unit or Virtual Folder and in the Project Explorer toolbar click ![](../../../images/btn_create_new_trigger.png)
     **Create new 'Trigger'**.
   - 右键点击 Work Unit 或 Virtual Folder，然后从快捷菜单中选择 <**New Child > Trigger**。
3. 将默认名称替换成更合适的命名。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | Each Trigger name must be unique and consist of only letters, digits, and underscores. 只有字母或下划线可以作为首字符。 |

## Deleting Triggers

Keep in mind that if you delete a Trigger that is assigned to a Stinger, the association
with the Music Segment for the Stinger is removed.

**To delete Triggers:**

1. 在 Project Explorer 中，切换至 Game Syncs 选项卡。
2. In the Triggers section, select the Triggers you want to delete and do either of the
   following:

   - 按 **Delete** 键。
   - Right-click and select **Delete** from the shortcut
     menu.

---