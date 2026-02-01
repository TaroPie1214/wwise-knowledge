# AK::SoundEngine::AddOutput: Output already exists, not added a second time. Shareset: ... Device: ...

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > AK::SoundEngine::AddOutput: Output already exists, not added a second time. Shareset: ... Device: ...

#### AK::SoundEngine::AddOutput: Output already exists, not added a second time. Shareset: ... Device: ...

“AK::SoundEngine::AddOutput: 输出已经存在，不能再次添加。共享集: …设备:…”游戏代码调用了 [`AK::SoundEngine::AddOutput`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a15ab79f954a307902f529d8ccde8ad48.html) 函数并尝试添加系统中已经存在的音频输出。此项并非严重错误。现有输出会继续正常工作。

**推荐的解决步骤：**

- 移除函数调用。
- 重新估算参数 in\_settings.audioDeviceShareset 和 in\_settings.idDevice 以指向不同的物理设备。

---