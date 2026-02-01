# Device ID not recognized by the platform or is disabled.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Device ID not recognized by the platform or is disabled.

#### Device ID not recognized by the platform or is disabled.

“设备 ID 无法被平台识别或已被禁用”。在尝试调用 [`AK::SoundEngine::AddOutput()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a15ab79f954a307902f529d8ccde8ad48.html) 或 [`AK::SoundEngine::ReplaceOutput()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a81521a4611d3891c499ec9c5eb421ac2.html) 时，提供的 [`AkOutputSettings::idDevice`](https://www.audiokinetic.com/library/edge/?source=SDK&id=struct_ak_output_settings_a0e145d97af362b7f3267b64ca0e38054.html) 值无效。此 ID 通常为特定于平台的操作系统或设备驱动程序的硬件设备标识符 (HID)。一般情况下，会通过平台的服务对其进行检索。

**推荐的解决步骤：**

- 使用 Debug 版本库，将调试程序连接至游戏，然后重现相同场景。
- 检查提供的 [`AkOutputSettings::idDevice`](https://www.audiokinetic.com/library/edge/?source=SDK&id=struct_ak_output_settings_a0e145d97af362b7f3267b64ca0e38054.html) 值是否是有效的设备 ID。
- 在 Windows 上，检查提供的 [`AkOutputSettings::idDevice`](https://www.audiokinetic.com/library/edge/?source=SDK&id=struct_ak_output_settings_a0e145d97af362b7f3267b64ca0e38054.html) 是否与 [`AK::GetDeviceID()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_a84b3896b7b5b223c72b5ea826fae6bd8.html) 调用返回的值匹配（该调用使用的 `IMMDevice` 的当前状态为 Active 或 Unplugged）。比如，在最初枚举之后，设备的状态可能已经发生改变。

---