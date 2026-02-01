# AkOutputDeviceID not found as an active device in call to function ...

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > AkOutputDeviceID not found as an active device in call to function ...

#### AkOutputDeviceID not found as an active device in call to function ...

“在调用函数…时无法找到与 AkOutputDeviceID 匹配的活跃设备。”若 Wwise 无法找到与所提供 [`AkOutputDeviceID`](https://www.audiokinetic.com/library/edge/?source=SDK&id=_common_2_ak_types_8h_ab608859e8c575f46ce18433e32aa2ccd.html) 匹配的声音引擎在用设备，则将出现此错误。

**推荐的解决步骤：**

- 使用 Debug 版本库，将调试程序连接至游戏，然后重现相同场景。
- 检查供替换所用的 [`AkOutputDeviceID`](https://www.audiokinetic.com/library/edge/?source=SDK&id=_common_2_ak_types_8h_ab608859e8c575f46ce18433e32aa2ccd.html) 是否与 [`AK::SoundEngine::Init`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a9a26da64092b97243844df77cbcdbf5f.html) 期间使用的 [`AkOutputDeviceID`](https://www.audiokinetic.com/library/edge/?source=SDK&id=_common_2_ak_types_8h_ab608859e8c575f46ce18433e32aa2ccd.html) 匹配。注意，若所提供 [`AkInitSettings::settingsMainOutput`](https://www.audiokinetic.com/library/edge/?source=SDK&id=struct_ak_init_settings_a9c5254abf13a5c3bf60ddd27c48db4d7.html) 中的 `audioDeviceShareset` 为 0，则初始 [`AkOutputDeviceID`](https://www.audiokinetic.com/library/edge/?source=SDK&id=_common_2_ak_types_8h_ab608859e8c575f46ce18433e32aa2ccd.html) 将是 System 共享集的 ID。该共享集使用所提供 [`AkInitSettings::settingsMainOutput`](https://www.audiokinetic.com/library/edge/?source=SDK&id=struct_ak_init_settings_a9c5254abf13a5c3bf60ddd27c48db4d7.html) 中的 `idDevice` 混音。
- 检查供替换所用的 [`AkOutputDeviceID`](https://www.audiokinetic.com/library/edge/?source=SDK&id=_common_2_ak_types_8h_ab608859e8c575f46ce18433e32aa2ccd.html) 是否与之前通过 [`AK::SoundEngine::AddOutput()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a15ab79f954a307902f529d8ccde8ad48.html) 或 [`AK::SoundEngine::ReplaceOutput()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a81521a4611d3891c499ec9c5eb421ac2.html) 返回的 [`AkOutputDeviceID`](https://www.audiokinetic.com/library/edge/?source=SDK&id=_common_2_ak_types_8h_ab608859e8c575f46ce18433e32aa2ccd.html) 匹配。
- 检查是否使用所述 [`AkOutputDeviceID`](https://www.audiokinetic.com/library/edge/?source=SDK&id=_common_2_ak_types_8h_ab608859e8c575f46ce18433e32aa2ccd.html) 调用了 [`AK::SoundEngine::RemoveOutput()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a0932ed2a3669258ecc3bbe6448314020.html)。

---