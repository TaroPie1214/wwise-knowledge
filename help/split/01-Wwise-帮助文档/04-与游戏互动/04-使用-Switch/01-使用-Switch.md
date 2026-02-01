# 使用 Switch

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [与游戏互动](../00-与游戏互动.md) > [使用 Switch](00-使用-Switch.md) > 使用 Switch

## 使用 Switch

在 Wwise 中，需要先将 Switch（切换开关）置于 Switch Group（切换开关组）中才能使用。通过用 Switch Group 对 Switch 进行编组，您可以高效管理游戏中不同条件下的声音、音乐和振动对象。例如，为了管理角色的各种脚步声，可以创建名为“Ground Textures”的 Switch Group。然后在 Wwise 中为游戏中每种地面材质创建对应的 Switch。根据游戏条件，您可以创建针对碎石地、草地和混凝土的 Switch。

|  |
| --- |
|  |

有了 Switch Group 和 Switch，就可创建 Switch Container 并将对象指派给 Switch 了。关于使用 Switch 和 Switch Container 的详细信息，请参阅[“定义 Switch Container 的内容和行为”一节](../../05-使用声音和振动来提升游戏体验/01-定义对象播放行为/03-定义-Switch-Container-的内容和行为.md "定义 Switch Container 的内容和行为")。

为了帮您在界面中轻松识别 Switch 或 Switch Group，Wwise 采用独特的图标来标识它们。

| 图标 | 代表 |
| --- | --- |
| |  | | --- | |  | | Switch Group |
| |  | | --- | |  | | Switch（切换开关） |

### Creating Switch Groups

按逻辑将 Switch（切换开关）编组成 Switch Group（切换开关组）非常有用，用起来也更方便。您可以在 Project Explorer（属性编辑器）的 Game Syncs（游戏同步器）选项卡中创建所有需要的 Switch Group。

**为工程创建新 Switch Group 的方法如下：**

1. 在 Project Explorer 中，切换至 Game Syncs 选项卡。
2. 在 Switches 层级，执行以下操作之一：

   - 选择 Virtual Folder 或 Work Unit，然后点击 Project Explorer 工具栏中的 **Switch Group** 图标。
   - 右键点击 Virtual Folder 或 Work Unit，从快捷菜单中选择**New Child** > **Switch Group** 。

   新的 Switch Group 将被添加到列表中。
3. 将默认名称替换成更合适的命名。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | Switch Group 之间不能重名，且只能包含字母、数字和下划线。只有字母或下划线可以作为首字符。 |
4. 继续按需添加 Switch Group。

### Creating Switches

游戏元素（例如地面）具有的不同条件在 Wwise 中要有相应的 Switch。您可以在 Project Explorer（属性编辑器）的 Game Syncs（游戏同步器）选项卡中创建 Switch。

**创建新 Switch 的方法如下：**

1. 在 Project Explorer 中，切换至 Game Syncs 选项卡。
2. 在 Switch Groups 列表中，执行下列操作之一：

   - 选择 Switch Group，并点击 Project Explorer 工具栏中的 **Switch** 图标。
   - 右键点击 Switch Group，从快捷菜单选择 **New Child > Switch**。

   新的 Switch 将被添加到 Switch Group 中。
3. 将默认名称替换成更合适的命名。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | Switch Group 中的 Switch 之间不能重名，且只能包含字母、数字和下划线。首字母只能是字母或下划线。 |
4. 继续按需创建 Switch。

### Deleting Switches or Switch Groups

您可能想删除不再需要的 Switch（切换开关）或 Switch Group（切换开关组）。记住，删除 Switch Group 时也会删除其中的所有 Switch，

删除 Switch 或 Switch Group 前，请检查 Switch 是如何集成到游戏中的。Switch 的集成方式有两种机制：

- 通过调用带有 Set Switch 动作的事件 —— 删除 Switch 或 Switch Group 后，在 Wwise 中会造成问题，因为事件调用的 Switch 将不存在。
- 通过调用 Switch Group 或 Switch 本身 —— 要删除 Switch 或 Switch Group 时，声音设计师应告知程序员。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 这将导致与其关联的对象和预设无法找到它们。 |

**删除 Switch 或 Switch Group 的方法如下：**

1. 在 Project Explorer 中，切换至 Game Syncs 选项卡。
2. 在 Switch Group 列表中，右键点击要删除的 Switch Group 或 Switch，然后选择 **Delete Selection**。

   所选 Switch 或 Switch Group 将被删除。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 如果误删了 Switch 或 Switch Group，可以按 **Ctrl+Z** 或点击 **Edit > Undo** 来撤消删除。 |

---