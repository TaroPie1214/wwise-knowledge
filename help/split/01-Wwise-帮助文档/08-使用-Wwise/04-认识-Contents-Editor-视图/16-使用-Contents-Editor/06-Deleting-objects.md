# Deleting objects

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [使用 Wwise](../../00-使用-Wwise.md) > [认识 Contents Editor 视图](../00-认识-Contents-Editor-视图.md) > [使用 Contents Editor](00-使用-Contents-Editor.md) > Deleting objects

### Deleting objects

如果不再需要某个对象或源，您可以在 Contents Editor 中删除它。处于测试目的，您可以导入多个源，决定需要哪个版本后再删除其余的源。在 Contents Editor 中删除对象或源时，也会在工程中删除它们。此操作不会自动删除工程 .cache 文件夹中的相关已转码音频文件。要删除 Orphan File（落单文件），您需要清空音频缓存。关于如何管理这些 Orphan File 的详细信息，请参阅[“清除缓存”一节](../../../03-设置工程/05-管理工程中的媒体文件/06-清除缓存.md "清除缓存")。

**在 Contents Editor 中删除对象的方法如下：**

1. 选择您要删除的对象所对应的图标。
2. 执行以下操作之一：

   - 按 **Delete** 键。
   - 右键点击对象，并在快捷菜单中选择 **Delete**。

   选定的对象或源将从 Contents Editor 和 Project Explorer 的 Audio 选项卡中移除。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 在 Contents Editor 中删除某个对象也会将其从工程中删除。从 Playlist（播放列表）或 Switch 列表中移除对象时，则不会删除，而只会从列表中移除。 |

---