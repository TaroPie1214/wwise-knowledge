# Finding the project elements that reference a particular object

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用 Wwise](../00-使用-Wwise.md) > [使用 Search、Query 和 Reference](00-使用-Search、Query-和-Reference.md) > Finding the project elements that reference a particular object

## Finding the project elements that reference a particular object

There might be cases during the development of your project where you want to find all the
elements in your project that contain direct references to a particular object. For example,
you might want to find which Events reference a particular object or which SoundBanks
reference a particular Event. In Wwise, you can do this with the Find All References command
that is accessible from most of the shortcut menus. All elements that reference a particular
object are displayed in the [“Reference View 视图”一节](../../09-参考主题/04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图"), where you can open each project
element, make changes, if necessary, and then move on.

|  |  |
| --- | --- |
| [备注] | 备注 |
| 仅当工程元素直接引用了特定对象或元素时，才会显示在引用视图中。 |

在大多数情况下，您主要搜索引用某一个特定对象的元素，但您也可以查找引用一系列对象的所有元素。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 引用列表不会自动更新，因此，如果对工程做了更改，则需要点击 Refresh 按钮以手动更新引用列表。 |

**查找引用特定对象的工程元素的方法是：**

1. 执行以下操作之一：

   - 右键点击单个或多个工程元素，然后从快捷菜单中选择 **Find all references**（查找所有引用）。
   - 按 Shift+F3 打开 Reference 视图，然后将一个或一系列对象拖到 References to:（引用）字段。
   - 按 Shift+F3 打开 Reference 视图，点击 References to: 字段旁边的 Browse 按钮，选择工程元素，然后点击 **OK**。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 如果在 Project Explorer、Property Editor 或 Reference View 中选择一个对象或元素的同时按下 Shift+F3 组合键，Wwise 则会自动搜索引用选定对象的对象。 |

   引用选定对象的一系列工程元素显示在 Reference 视图中。

---