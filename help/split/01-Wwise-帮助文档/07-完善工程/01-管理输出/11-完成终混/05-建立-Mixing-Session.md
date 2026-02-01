# 建立 Mixing Session

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [完善工程](../../00-完善工程.md) > [管理输出](../00-管理输出.md) > [完成终混](00-完成终混.md) > 建立 Mixing Session

### 建立 Mixing Session

在使用 Mixing Desk（混音台）对游戏音频的混音进行微调前，需要创建 Mixing Session（混音会话）并为其添加总线或对象。Mixing Session 跟 Preset（预设）或 SoundCaster 会话类似，其也会将 Mixing Desk 的内容存储到工程中以便日后使用。每个 Mixing Session 都会保存在 Project Explorer（工程资源管理器）的 Sessions（会话）选项卡中的对应 Work Unit（工作单元）下。

为便于轻松识别界面中的 Mixing Session，Wwise 使用了独特的图标来予以表示。

| 图标 | 代表 |
| --- | --- |
| |  | | --- | |  | | Mixing Session（混音会话） |

#### 创建 Mixing Session

在使用 Mixing Desk 前，需要创建 Mixing Session。Mixing Session 包含一系列总线和对象并以调音台的形式予以呈现。Mixing Session 中的每条总线和每个对象都会显示一组滑杆和属性值控件以便对游戏的音频混音进行微调。

您可以在 Wwise 中的以下位置创建 Mixing Session：

- Project Explorer 的 Sessions 选项卡。
- 在 Mixing Desk 内。

**通过 Project Explorer 创建 Mixing Session：**

1. 在 Project Explorer 中，切换至 Sessions 选项卡。
2. 在 Mixing Sessions 标题下方，执行以下任一操作：

   选择工作单元或虚拟文件夹，然后在 Project Explorer 工具栏中点击 **Mixing Session** 图标。

   右键点击工作单元或虚拟文件夹，然后在快捷菜单中点击 **New Child** > **Mixing Session**。

   新建的 Mixing Session 将被添加到 Virtual Folder（虚文件夹）或 Work Unit（工作单元）。
3. 将默认名称替换为最能代表 Mixing Session 的名称。
4. 双击新建的 Mixing Session 来将其加载到 Mixing Desk 中。

   接下来，就可以为 Mixing Session 添加总线和对象了。

**通过 Mixing Desk 创建新的 Mixing Session：**

1. 在 Mixing Desk 中，点击 Mixing Session Selector 按钮 (**>>**)，然后从列表中选择 **New**。

   这时会打开 New Mixing Session（新建混音会话）对话框。
2. 选择要在其中新建 Mixing Session 的 Work Unit。
3. 在 Name（名称）字段中，将默认名称替换为最能代表 Mixing Session 的名称。
4. 单击 **OK**（确定）。

   这时会创建 Mixing Session。接下来，就可以为其添加总线和对象了。

#### 将对象/总线添加到 Mixing Session

在创建 Mixing Session（混音会话）后，就可向其添加工程内的总线和对象了。将总线或对象添加至 Mixing Desk 时，将会创建一个混音通道条。通过混音通道条，您可以总览对象或总线的属性设置。它还包含一组控件，让您可以监视各种活动、修改属性、设置效果和状态，以及设置定位属性。

![](../../../../../images/mixing_strip_Online.png)

|  |  |
| --- | --- |
|  | 混音通道条。 |

您可以向 Mixing Desk 中添加以下对象：

- Busses
- Property Containers
- 容器
- 声音
- 音乐容器
- Music Segments（音乐段落）
- Music Track

|  |  |
| --- | --- |
| [备注] | 备注 |
| 若 Mixing Session 包含与已从工程中卸载的对象或总线相关的通道条，则该通道条将为空。 |

**将对象/总线添加至混音会话的方法如下：**

1. 通过执行以下任一操作来将 Mixing Session 加载到 Mixing Desk 中：

   - 单击 Mixing Desk Selector 按钮 (**>>**) 并从列表中选择 Mixing Session。
   - 在 Project Explorer（工程资源管理器）的 Sessions（会话）选项卡中双击 Mixing Session。
2. 从 Project Explorer 中，将总线或对象拖至 Mixing Desk。

   此时在 Mixing Desk 中将创建一个混音通道条，代表该对象或总线。
3. 继续添加对象和总线至 Mixing Desk 中。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | Mixing Desk 中包含多个通道条时，一条蓝色插入线会标明通道条的目标位置。 |

#### 对 Mixing Session 内的通道条重新排序

在将总线和对象添加到 Mixing Session 后，可将通道条从某一位置拖到另一位置来随意地对其进行排序。

**对 Mixing Session 内的通道条重新排序：**

1. 将 Mixing Session（混音会话）加载到 Mixing Desk（混音台）中。
2. 点击混音通道条的标题栏，然后将其拖至 Mixing Desk 中的新位置。

   蓝色插入线将显示混音通道条的目标位置。
3. 根据需要继续重新排列混音器通道条。

#### 在 Mixing Session 内调节通道条的宽度

若发现混音通道条过窄或过宽，则可按照如下所述调节其宽度。在下图中，左侧通道条偏窄，右侧通道条偏宽。

![](../../../../../images/Mixer_strips_LS_online.png)

**调整混音通道条宽度的方法如下：**

1. 将 Mixing Session（混音会话）加载到 Mixing Desk（混音台）中。
2. 点击 Mixing Desk 的网格部分。
3. 执行以下操作之一：

   要将混音通道条调宽，请按下 **Ctrl** 键，同时向上滚动鼠标滚轮，或点击滚动条旁边的 **+** 符号。

   要将混音通道条调窄，请按下 **Ctrl** 键，同时向下滚动鼠标滚轮，或点击滚动条旁边的 **-** 符号。

#### 从 Mixing Session 中移除通道条

在 Mixing Session 中，随时都可从 Mixing Desk 移除一个或多个通道条。

**从 Mixing Session 中移除通道条：**

1. 执行以下操作之一：

   - 右键点击通道条的标题栏，然后从菜单中选择 **Remove**。
   - 点击要移除的通道条的标题栏，然后按下 **Delete** 键。

   通道条此时将从调音台中移除。

---