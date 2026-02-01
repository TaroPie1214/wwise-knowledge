# Getting to know the Busses Console

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [完善工程](../../00-完善工程.md) > [管理输出](../00-管理输出.md) > [完成终混](00-完成终混.md) > Getting to know the Busses Console

### Getting to know the Busses Console

The Busses Console is a mixing console that groups a variety of bus properties into one view so that you can create the final mix of your game audio. 连接至游戏时，您可以一边试听，一边在游戏音频实时播放过程中调节音频和振动的属性。。

您也可以监视与连线至各总线的对象相关的信息，其中包括：

- **Meter** - 显示所有声道的峰值电平。
- **Duck** - 表示总线正在闪避。
- **BG** - 表示总线已绑定背景音乐选项。
- **Bypass** - 表示为该总线选择了 Bypass All 选项。
- **Effect** - 表示该总线应用了效果插件，或一系列效果插件。

![](../../../../../images/mastermixer_view.png)

#### Fine-tuning your mix using the Busses Console

工程中的总线连线完成后，您就可以进行终混，方法是连接至游戏，并在游戏过程中实时微调相关属性。You can use the Busses Console to easily modify the relative properties of each bus in your project. 属性是累积的，这意味着您定义的这些值会与对象属性值相加。

微调混音时，可以静音或单独播放若干条总线，以便专注于游戏声音或振动的某个特定方面，或者排查特定问题。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 更改总线音高不会影响路由至该总线的音乐对象。 |

**To create the final mix using the Busses Console:**

1. 点击工具栏中的 **Remote** 按钮，连接至游戏。

   这时会打开 Remote Connection（远程连接）对话框并列出网络中当前在运行游戏的机器。
2. 从该列表中，选择要连接的设备。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 设备的状态须显示为“Ready”（就绪），才能连接该设备。 |
3. 点击 **Connect**（连接）。

   Wwise 将连接至远程游戏设备。游戏设备的名称显示在工具栏中。
4. From the menu bar, click **View > Busses Console**.

   The **Busses Console** is displayed.
5. 游戏运行过程中可以试听音频或振动。
6. 可以通过输入数值或拖动相应滑杆来调整以下属性：

   **Volume** - 输出信号的电平或振幅。

   **Pitch** - 输出信号的播放速度。

   |  |  |
   | --- | --- |
   | [技巧] | 技巧 |
   | 要静音或单独播放特定总线，请点击相应的 **M** 或 **S** 按钮。 |

---