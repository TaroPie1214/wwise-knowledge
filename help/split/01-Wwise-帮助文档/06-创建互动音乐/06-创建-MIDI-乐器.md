# 创建 MIDI 乐器

[Wwise 帮助文档](../00-Wwise-帮助文档.md) > [创建互动音乐](00-创建互动音乐.md) > 创建 MIDI 乐器

## 创建 MIDI 乐器

## 设计 Synth One 乐器

若源插件能够理解 MIDI 消息，便可通过其来创建 MIDI 乐器。

**创建源插件乐器（例如：合成器）的方法如下：**

1. Create an empty **Sound** object on the **Containers hierarchy.**
2. 在 Project Explorer（工程浏览器）中，选择该声音。
3. 在 Contents Editor 中，点击 **Add Source>>**。
4. 从选择器菜单中，选择 **Synth One**。
5. 从 **Views**（视图）菜单中，选择 Source Editor（源编辑器）（Shift+X）。
6. Click on the **Sound** object on the Containers hierarchy to see it in the Source Editor.
7. 在 Source Editor 中，将 **Frequency Mode**（频率模式）设置为 **MIDI Note**（MIDI 音符）。

现在，乐器可作为音乐对象内的 MIDI 目标引用（例如：音乐段落）。

## 设计简单的采样 MIDI 乐器

Sampled instruments can use all Containers hierarchy containers (Blend Containers, Switch Containers, Random Containers, Sequence Containers and Sounds) for their design. 实现的复杂性将随着乐器设计复杂性而增长。最简单的采样乐器应为单采样点乐器。

**创建单采样点乐器的方法如下：**

1. 在 Project Explorer 中，选择要创建乐器的位置。
2. 从 **Views** 菜单中，选择 **Audio File Importer**（音频文件导入器）（Shift+I）。
3. 单击 **Add Files...**（添加文件...）。
4. 浏览找到 .wav 文件，然后点击 OK（确定）。
5. 再次点击 OK，以完成导入操作。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| You can also Drag & Drop a WAV file on the Containers hierarchy directly. |

现在，乐器可作为音乐对象内的 MIDI 目标引用（例如：音乐段落）。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 使用 Source Editor 修剪导入的样本。通常，您希望删除源开头的任何空白。 |

## 了解 MIDI 音符追踪

The MIDI note tracking parameters can be found in the MIDI category of the Property Editor for the Containers hierarchy objects. 这些参数决定在播放期间是否在收到 MIDI 消息时改变声音对象的音高。If the played sound is pitch-shifted, it is according to the note of the MIDI message, and the note represented by the object's source; it's root note.

The note tracking parameters can be specified and/or overridden in any of the instrument's Containers hierarchy objects. For more information about properties in the Containers hierarchy, refer to [“工程层级结构中的属性介绍”一节](../03-设置工程/06-Building-your-sound-and-motion-hierarchies/04-工程层级结构中的属性介绍/00-工程层级结构中的属性介绍.md "工程层级结构中的属性介绍"). MIDI 音符跟踪参数包括：

- **Override parent**（不沿用父项）：如果勾选，则对象将忽略其上级对象的音符跟踪参数。
- **Enable**（启用）：如果设置该选项，则对象的声音在播放时将会改变音高。音高平移量由接收到的MIDI事件的音符与 **Root Note** 值决定。
- **Root note**：由对象的源所代表的音符。

## 了解 MIDI 筛选器

The MIDI filters can be found in the MIDI category of the Property Editor for the Containers hierarchy objects. 在收到有关复杂对象结构的 MIDI 消息时，您可以使用 MIDI 筛选器来选择要播放的子对象。

MIDI 筛选器指定将基于以下项来播放相应的子对象：

- MIDI 音符音高。
- MIDI 音符力度。
- MIDI 声道。

因为在声音音高逐渐偏离根音时做重采样可能会产生副作用，所以您可能会需要使用不同根音上的多个录制样本来覆盖乐器的整个音域。在内存受限时有一种技术通常能实现好的效果: 在每个八度音阶范围内只能使用几个不同样本根音，并且将这些音符的音高上调或下调以覆盖八度音阶的全部 12 个半音。

以下是乐器两个八度音阶将根音音高下调二度和上调小二度的示例。

- **乐器（混合容器）**

  - 根音：C3 - 范围：Bb2 至 C#3
  - 根音：E3 - 范围：D3 至 F3
  - 根音：G#3 - 范围：F#3 至 A3
  - 根音：C4 - 范围：Bb3 至 C#4
  - 根音：E4 - 范围：D4 至 F4
  - 根音：G#4 - 范围：F#4 至 A4

在播放容器时，混合容器同时播放各个子对象。然而，筛选器会阻止与筛选器规则不匹配的子对象。

## 了解 MIDI Event

The MIDI Events properties can be found in the MIDI group of the Property Editor for the Containers hierarchy objects. 在收到 MIDI 消息时，MIDI 事件属性用于确定对象是否必须要播放。对象可在发生 note-on（音符开）事件或 note-off（音符关）事件时播放。请注意，这些属性仅用于启动对象的播放。要停止播放对象，必须为属性指派包络（请参阅[“使用包络”一节](../04-与游戏互动/05-使用-RTPC/05-使用包络.md "使用包络")）。

典型的情形是在 **Note-On** 时 **Play**（播放）。

**创建循环乐器的方法如下：**

- 在 Project Explorer 中，选择要循环的声音。
- In the Property Editor, enable **Loop** on the
  Sound.
- In the Property Editor, set the **Play On** property to
  **Note-On**.
- 从 **Views** 菜单中，打开 Source Editor（Shift+X）。
- 再次察看声音。
- 在 Source Editor 中，移动 **Loop Start**>（循环开始）和 **>Loop End**>（循环结束）光标以排除 WAV 文件的起音区段和释放区段。
- 调整**Crossfade duration**（交叉淡化时长），直到无法听到循环点。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 乐器的循环可通过 **Break on Note-Off**（音符关时中断）属性进行停止。如果该属性已设置，则音符关事件会在允许当前对象完成播放的同时停止循环声音的播放。请记得在源编辑器中设置 **Loop Start** 和 **Loop End** 光标，以便为最终循环播放所需的时长。 |

另一个情形是在释放乐器（即音符关）时播放特定声音。例如，它可用于触发吉他音符结束时的弦闷音。您应创建以下对象和设置：

- Blend Container（混合容器）

  - 起音+循环声音：播放 = Note-On
  - 释放声音：播放 = Note-Off

## 在 MIDI Event 上添加淡入和淡出

在您希望向乐器添加动态时，您可以使用连接到乐器的 **Voice Volume**（声部音量）的 **Envelope**（包络）。

要向 **Voice Volume** 添加 **Envelope**，请参阅[“使用包络”一节](../04-与游戏互动/05-使用-RTPC/05-使用包络.md "使用包络")。

## 使用 MIDI 数据控制对象属性值

可以使用以下 MIDI 消息来控制对象属性值：

- MIDI 音符力度。
- MIDI 音符音高（音符号）。
- MIDI 音符频率。
- MIDI 音符触后。
- MIDI CC 值（0-127，包括调制轮）。
- MIDI 弯音。

典型情形是使用 **MIDI Note Velocity**（MIDI 音符力度）控制乐器的 **Voice Volume**。

**使用 MIDI Note Velocity 控制 Voice Volume 的方法如下：**

1. In the Project Explorer, select an object from the Containers hierarchy.
2. In the Primary Editor, go to the RTPC tab.
3. 点击 **RTPC** 列表中的 [>>] 按钮以添加新的条目。
4. 从选择器菜单中，选择 **Voice Volume**。
5. 为 X 轴点击 [>>] 选择器。
6. 从选择器菜单中，选择 **MIDI > MIDI Note Velocity**。
7. 调整 RTPC 图中的声部音量曲线。

## 使用 MIDI Keymap Editor

The MIDI Keymap Editor view can be used to edit all MIDI properties for Containers hierarchy objects.

**打开该视图的方法如下：**

1. From the Wwise menu, select **Views > Editors > MIDI Keymap
   Editor**.

**为多个对象设置相同属性值的方法如下：**

1. 在 MIDI Keymap Editor 中选择要编辑的对象。
2. 为其中一个所选对象设置属性值。

   所选对象现在已设置为相同值。

**偏移多个对象的属性值的方法如下：**

1. 在 MIDI Keymap Editor 中选择要编辑的对象。
2. 按住 ALT 键并移动其中一个所选对象的属性滑杆。

   所选对象的属性值于是就被偏置了。

**在 MIDI Keymap Editor 中添加属性的方法如下：**

1. 打开 MIDI Keymap Editor 视图设置（Ctrl+Alt+V）。
2. 选择要添加的属性。
3. 按 OK。

   新列现在添加上了。

## 使用 MIDI 键盘测试乐器

在设计 MIDI 乐器时，您可以使用外部 MIDI 键盘设备测试乐器。

**将设备连接到 Wwise的方法如下：**

1. 在 **Project** 菜单中，选择 **Control Surface Devices**（控制设备）。
2. 点击 **Add**（添加）按钮。
3. 为设备命名。
4. 点击 OK。

   设备现在添加到列表里了。
5. 在 **Receive From**（输入端）列中，选择 MIDI IN（MIDI 输入）设备。

   此时将会显示 **Connected**（已连接）消息。
6. 在 **Send To**（输出端）列中，选择 MIDI OUT（MIDI 输出）设备。

   此时将会显示 **Connected**（已连接）消息。
7. 点击 Close（关闭）。

   设备现在就可以用了。

**将键盘键绑定到当前选中项的方法如下：**

1. 从 **Views** 菜单中，选择 **Control Surface Bindings**（Ctrl+Shift+Q）。
2. 通过点击视图左上方的 [>>] 按钮，创建新的控制设备会话。
3. 点击 **Current Selection**（当前选中项）组（文件夹）。
4. 点击 **Add Binding**（添加绑定）按钮。
5. 点击 **Property/Command**（属性/命令）选择器按钮以打开菜单。
6. 选择 **Object Command > Pass MIDI Note**（对象命令 > 传递 MIDI 音符）。
7. 保存工程。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 确保 **Current Selection** 组在控制设备工具栏中处于激活状态并且您已经在 Project Explorer 中选择了一个对象。 |

在创建会话和绑定后，在 Project Explorer 中选择一个对象将自动为 MIDI 乐器加载该对象，并随时可以播放。

## 将 MIDI 从 DAW 连通到 Wwise

可以使用虚拟 MIDI 连接器将来自外部应用程序（DAW 或数字音频电脑）的 MIDI 消息连通到 Wwise。在使用 Wwise 内置的乐器时在 DAW 中制作 MIDI 音乐非常有用。

通过创建包含所有乐器的混合容器并使用 MIDI Channel 筛选器区分乐器，您可以同时创建多个乐器。

- **Mac:** 您将要使用的是内置 IAC Driver。从 Applications/Utilities 下启动 Audio MIDI Setup 来开始操作。如果不显示 MIDI Studio，请在 **Window** 中选择 **Show MIDI Window**。单击 **MIDI Device**，双击 IAC Driver 图标，并选中 **Device is online** 选项将其激活。添加任意数量的端口后，它们将显示在您的 DAW 中。端口可用于发送或接收 MIDI Note、MIDI Control Change 和 MIDI Sync 消息。
- **Windows:** 由于 Windows 不自带虚拟 MIDI 驱动程序，您必须下载该程序。在 Windows 上， Mac 的 IAC Bus 替代工具中最知名的是 MIDI Yoke，它是 [MIDI OX Utility](http://www.midiox.com/) 的组件。此驱动程序的另一个替代工具是 Tobias Erichsen 的 [loopMIDI](http://www.tobias-erichsen.de/software/loopmidi.html) ，可以用于将 MIDI 消息从 DAW 输出到 Wwise。您需要将应用程序创建的虚拟 MIDI 端口添加到 Wwise 的控制设备中去。

---