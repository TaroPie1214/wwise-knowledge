# Building simulations

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [完善工程](../00-完善工程.md) > [创建模拟](00-创建模拟.md) > Building simulations

## Building simulations

Soundcaster 可以提供最大的灵活性来满足您创建模拟时的各种需求。您可以添加您想要使用的任何声音、音乐或振动对象，并可根据需要随意更换它们。创建模拟的过程包括以下步骤：

- [“Creating Soundcaster sessions”一节](01-Building-simulations.md#creating_soundcaster_session "Creating Soundcaster sessions")
- [“Adding objects or Events to the Soundcaster”一节](01-Building-simulations.md#adding_objects_or_events_to_soundcaster "Adding objects or Events to the Soundcaster")

|  |  |
| --- | --- |
| [备注] | 备注 |
| 如果 Session 选项卡中没有 Soundcaster 会话，则不能在 Soundcaster 中开展工作。 |

### Creating Soundcaster sessions

在可以使用 Soundcaster 前，需要创建一个 Soundcaster Session（声音选角器会话）。您可以在 Wwise 的以下两个位置中创建 Soundcaster 会话：

- Project Explorer 的 Session 选项卡。
- Soundcaster 的主控制区。

**在 Project Explorer 中创建 Soundcaster 会话的方法是：**

1. 在 Project Explorer 中，切换至 Sessions 选项卡。
2. 在 Soundcaster Session 标题下，执行以下操作之一：

   - 选择工作单元或虚拟文件夹，然后在 Project Explorer 工具栏中点击 **Soundcaster Session** 图标。
   - 右键点击工作单元或虚拟文件夹，然后在快捷菜单中点击 <**New Child > Soundcaster Session**。

   新的Soundcaster 会话将被添加至虚拟文件夹或工作单元。
3. 将默认名称替换成最适合 Soundcaster 会话的名称。
4. 双击新建的 Soundcaster 会话以在 Soundcaster 中打开该会话。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 在 Project Explorer 中，您可以使用标准的 Windows 快捷键剪切、复制和粘贴 Soundcaster 会话。如果您不再需要 Soundcaster 会话，则可以按 Delete 键来删除它。 |

**在 Soundcaster 中创建新的 Soundcaster 会话的方法是：**

1. 在 Soundcaster 中，点击 Soundcaster Session 选择器开关（**>>**）并从列表中选择 **New**。

   The New Soundcaster Session dialog opens.
2. 为 SoundCaster 会话选择工作单元。
3. 在 Name 字段，将默认名称替换成最适合 Soundcaster 会话的名称。
4. 单击 **OK**（确定）。

   Soundcaster 会话创建完成。

### Adding objects or Events to the Soundcaster

当您为 Soundcaster 添加对象或事件时，就会创建一个模块，用来表示对象或事件及其属性和行为。它还拥有一系列的控件，可以让您修改属性，以及播放声音、音乐和振动对象。

![](../../../../images/module_online.png)

在您准备好对您收集的一些声音、音乐或振动进行混音或测试时，便可以开始向 Soundcaster 中添加不同的模块。您可以将以下任何类型作为模块添加到 Soundcaster 中：

- Busses
- Property Containers
- 容器
- 声音
- 音乐容器
- Music Segment
- Event

|  |  |
| --- | --- |
| [备注] | 备注 |
| 如果 Soundcaster 会话中包含已从工程中卸载的对象或事件模块，则控件将不可用，模块标题将显示为黄色。 |

**向 Soundcaster 中添加对象/事件的方法是：**

1. 执行以下操作之一：

   - 将对象从 Project Explorer 的 Audio 选项卡拖到 Soundcaster 中。
   - 从 Project Explorer 的 Event 选项卡中，将 Event 拖拽到 Soundcaster 内。

   蓝色模块插入标志出现在您拖动对象/事件的位置。松开鼠标键时，选定的对象/事件将作为模块添加到 Soundcaster 中。

### 对 Soundcaster 模块进行重新排序

当您为 Soundcaster 添加对象或事件时，就会创建一个模块。虽然可以按任何顺序播放模块，但您可能会想按特定顺序排列它们，以重建特定序列或为测试提供方便。

**更改 Soundcaster 模块的顺序的方法是：**

1. 将您要移动的模块拖到新位置。

   模块移动完成，在 Soundcaster 中，先前位于该位置上的模块下移了。

### 从 Soundcaster 中移除模块

如果不再需要模块或者准备创建新的模拟，您则可以将模块从 Soundcaster 中移除。

**将模块从 Soundcaster 中移除的方法是：**

1. 执行以下操作之一：

   - 若要移除一个模块，则点击模块标题栏中的 **Close** 按钮。
   - 若要移除所有模块，则点击主控制区中的的 **Clear**。

   于是模块从 Soundcaster 中移除了。

---