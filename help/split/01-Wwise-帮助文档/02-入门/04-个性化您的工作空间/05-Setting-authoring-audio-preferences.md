# Setting authoring audio preferences

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [入门](../00-入门.md) > [个性化您的工作空间](00-个性化您的工作空间.md) > Setting authoring audio preferences

## Setting authoring audio preferences

The settings described in the following sections only affect local audio playback in Wwise
Authoring. They do not affect in-game audio playback or the game sound engine buffer size. And
they do not affect playback when Wwise is connected to a remote platform.

### Setting the output latency

Output latency is the time delay between the moment an Event is triggered and the moment
the sound is played. When you are playing sounds in Wwise Authoring, the sound engine uses
prefilled buffers to reduce latency. You can adjust the latency by changing the number of
output buffers and the number of samples per buffer.

Lower latency shortens the delay but increases the risk of audio problems such as
dropouts caused by voice starvation. Higher latency can prevent voice starvation, but
increases playback delay. By default Wwise uses four buffers with 512 samples each. You can
try changing this if you are experiencing audio problems.

Changing the Output Buffer Count resets the sound engine, so changes made to sound
object property values through Events are lost. For example, if you are auditioning a sound
that had its volume reduced through an Event, and then you change the Output Buffer Count,
the sound returns to its original volume.

**To set the output latency:**

1. From the menu bar, click **Audio > Authoring Audio
   Preferences**.
2. In the Authoring Audio Preferences dialog, select an **Output
   Buffer Count**. Note, you cannot change this setting while sounds are being
   played back or when you are connected to a game.
3. Set the **Samples Per Output Buffer**.
4. Review the **Output Latency** field. It displays a
   value calculated from the **Output Buffer Count** and the
   **Samples Per Output Buffer**.
5. Click **OK** to save your settings and close the
   dialog.

### Setting the Music Track look-ahead time

In Wwise Authoring, audio playback is always streamed. If you have enabled streaming for
a Music Track in the Property Editor, the **Look-ahead time
(ms)** property for that Music Track is used. If you have not enabled streaming,
the **Music Track look-ahead time (ms)** defined in the
Authoring User Preferences dialog is used. This setting can help you avoid desynchronization
and voice starvation when playing music objects in Wwise Authoring.

**设置音乐轨预读时间的方法如下：**

1. From the menu bar, click **Audio > Authoring Audio
   Preferences** to open the Authoring User Preferences dialog.
2. In the **Music Track look-ahead time (ms)** field,
   enter a time from 0 - 10,000 milliseconds.
3. Click **OK** to save your settings and close the
   dialog.

### Enabling multi-core rendering (Windows only)

Multi-core rendering uses multiple CPU cores for audio rendering.

**To enable multi-core rendering:**

1. From the menu bar, click **Audio > Authoring Audio
   Preferences** to open the Authoring User Preferences dialog.
2. Enable **Multi-Core Rendering**.
3. Click **OK** to save your settings and close the
   dialog.

### Reserving system audio objects

When **Allow System Audio Objects** is enabled, Wwise
reserves system audio objects, preventing any game or application running alongside Wwise
from acquiring them. We recommend you enable this if you are trying to audition System Audio
Objects from within Wwise.

If you are trying to hear system audio objects from a game running alongside Wwise on the same PC, disabled this option. 这样可禁止 Wwise 保有系统对象，从而允许游戏获取它们。The result is that any audio object that would normally have been sent from Wwise as a system audio object is instead mixed to the Main Mix.

|  |  |
| --- | --- |
| [备注] | 备注 |
| “另一进程正在使用 Microsoft Spatial Sound 对象。可能会对某些音频对象实施混音。”在 Windows 上，所有当前运行的进程（包括游戏和应用）只能共用一定数量的 Microsoft Spatial Sound 对象。有些 Windows 版本存在漏洞，会禁止活跃的 Spatial Sound 媒体流获取已被另一进程释放的对象。To acquire them, the stream must be restarted. To circumvent this bug, you might have to restart the sound engine. |

**To reserve system audio objects:**

1. From the menu bar, click **Audio > Authoring Audio
   Preferences** to open the Authoring User Preferences dialog.
2. Enable **Allow System Audio Objects**.
3. Click **OK** to save your settings and close the
   dialog.

### Selecting audio output devices

By default, all sound played in Wwise uses your system's default playback device. You
can specify the Audio Device and Hardware Device associated with each top level bus.

**To select the output devices:**

1. From the menu bar, click **Audio > Authoring Audio
   Preferences**. This opens the Authoring User Preferences dialog where top
   level busses are listed in a table. See [“使用表格”一节](../03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") for
   details.
2. For each **Top Level Bus**, select an **Audio Device and Hardware Device**.

   - The list of devices contains all the devices supported by the currently active
     Audio Device plug-ins, so a hardware device can be present multiple times in the
     list if it is supported by multiple plug-ins.
   - When set to **Default**, the device is selected by the Audio Device plug-in used by the bus. 若该 Audio Device 插件不可用，则使用系统的默认音频设备。
3. Click **OK** to save your settings and close the
   dialog.

### Setting the main mix channel configuration

To set the main mix channel configuration:

1. From the menu bar, click **Audio > Main Mix Channel
   Configuration**.
2. Select an option from the following:

   - **Use Audio Device**: The speaker setup
     configuration for your system. On Windows this is defined in the Control
     Panel.
   - **2.0 (Speaker Panning)**: A stereo setup optimized
     for speakers. See [“Speaker and headphone panning rules”一节](../../05-使用声音和振动来提升游戏体验/02-定义定位/12-Speaker-and-headphone-panning-rules.md "Speaker and headphone panning rules") for
     details.
   - **2.0 (Headphone Panning)**: A stereo setup
     optimized for headphones. See [“Speaker and headphone panning rules”一节](../../05-使用声音和振动来提升游戏体验/02-定义定位/12-Speaker-and-headphone-panning-rules.md "Speaker and headphone panning rules")
     for details.
   - **5.1**: A surround speaker setup using L, R, C,
     SL, SR, and LFE channels. If selected while the Windows Control Panel is set to
     stereo, the audio system will probably downmix to stereo.
   - **7.1**: A surround speaker setup using L, R, C,
     SL, SR, BL, BR, and LFE channels. If selected while the Windows Control Panel is set
     to stereo, the audio system will probably downmix to stereo.

---