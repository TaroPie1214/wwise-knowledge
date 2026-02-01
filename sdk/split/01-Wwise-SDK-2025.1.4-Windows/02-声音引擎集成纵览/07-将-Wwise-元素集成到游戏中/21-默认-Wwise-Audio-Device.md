# 默认 Wwise Audio Device

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

默认 Wwise Audio Device

Audio Device（音频设备）是指各个支持的平台提供的所有物理输出和虚拟输出。Wwise 默认支持多种 Audio Device。其中有些仅适用于部分平台。 此页面提供 Wwise 中可用的各种默认 Audio Device 的平台专有信息。有关默认 Audio Device 的详细信息，请参阅[内置音频设备](https://www.audiokinetic.com/library/edge/?source=Help&id=builtin_audio_devices)。

# 系统

系统。系统提供的默认音频输出。它可以输出所有平台上的音频。

# 通信

Windows:

- 通信。与 Windows 的“声音播放设备”属性选项卡中选择的“通信”设备匹配。

# DVR Bypass

某些平台具有 DVR 功能，可让游戏玩家记录和发布其游戏过程。对于可能属于游戏音频或用户可更换音乐的一部分的、受版权保护的音乐，这会带来一些法律问题。虽然游戏制作公司有权在他们的游戏中使用该音乐，但终端用户无权以任何形式分发它。因此，平台要求中通常会注明禁止录制用户背景音乐。利用此虚拟 Audio Device，可选择不将混音发送到 DVR，而是之后在主输出中单独混音。

# Game Controller Speaker

游戏控制器扬声器。有些平台的游戏控制器上配有扬声器，每位玩家都可以有单独的输出。

Windows:

- 与 System 音频输出的功能匹配。

# Game Controller Headphones

游戏控制器耳机。有些平台允许将耳机连接到游戏控制器，每位玩家都可以有单独的输出。

Windows:

- 与 System 音频输出的功能匹配。

# Auxiliary

Windows:

- 与 System 音频输出的功能匹配。

# No Output

无输出。这是一个不输出任何音频的虚拟设备。它可以用于测试，并支持所有平台。

# Targeting Specific System Devices

指向特定系统设备。在有些平台上，可根据需要将上述音频设备配置为输出到特定系统设备。若将值设为 0，则使用默认设备。若要将音频设备配置为特定系统设备，请根据本节所述规则来设置 `AkOutputSettings::idDevice`。

Windows：

- 使用 `AK::GetDeviceID` 或 `AK::GetDeviceIDFromName` 获取正确的设备 ID。若将其设为 0，则使用 Audio Properties 中显示的默认 Windows 设备。

参见
:   - [集成二路输出](integrating_secondary_outputs.html)