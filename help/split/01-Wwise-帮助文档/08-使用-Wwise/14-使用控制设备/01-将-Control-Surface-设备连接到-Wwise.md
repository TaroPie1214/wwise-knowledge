# 将 Control Surface 设备连接到 Wwise

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用 Wwise](../00-使用-Wwise.md) > [使用控制设备](00-使用控制设备.md) > 将 Control Surface 设备连接到 Wwise

## 将 Control Surface 设备连接到 Wwise

Wwise 支持两类控制设备协议：

- MIDI 协议
- Mackie HUI MIDI 映射协议（MCU Pro）

**在您开始前：**

- 确保设备物理连接到计算机。
- 确保设备已打开。
- 确保您已为设备安装正确的驱动程序。

|  |  |
| --- | --- |
| [备注] | 备注 |
| Wwise 原本不支持 Open Sound Control（开放声音控制，OSC）协议。但 TouchOSC 等应用程序支持 MIDI 并且可与 TouchOSC Bridge 一起使用。 |

**将设备连接到 Wwise的方法如下：**

1. 从 **Project**（工程）菜单中，选择 **Control Surface Devices**（控制设备）。
2. 点击 **Add**（添加）按钮。
3. 为设备命名。
4. 点击 OK（确定）。

   设备现在添加到列表里了。
5. 在 **Receive From**（输入端）列中，选择 MIDI IN（MIDI 输入）设备。

   此时将会显示 **Connected**（已连接）消息。
6. 在 **Send To**（输出端）列中，选择 MIDI OUT（MIDI 输出）设备。

   此时将会显示 **Connected** 消息。
7. 点击 Close（关闭）。

   设备现在就可以用了。

|  |  |
| --- | --- |
| [备注] | 备注 |
| Control Surface Devices 设置就存储在本地计算机上。 |

---