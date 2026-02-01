# Could not connect to audio input device. Audio input callback will not be called.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Could not connect to audio input device. Audio input callback will not be called.

#### Could not connect to audio input device. Audio input callback will not be called.

“无法连接到音频输入设备。将不会调用音频输入回调。”Audio Device 无法将回调连接到硬件音频输入设备。在 iOS 上，必须通过 System Audio Device（系统音频设备）来设置输入回调才能使用话筒输入。

**可能的原因：**

- 为音频输入配置的硬件设备无法发出单声道信号。

**推荐的解决步骤：**

- 在 iOS 系统设置中配置不同的音频输入设备。
- 若多个输入设备依然存在此错误，请联系 Audiokinetic 技术支持部门。

---