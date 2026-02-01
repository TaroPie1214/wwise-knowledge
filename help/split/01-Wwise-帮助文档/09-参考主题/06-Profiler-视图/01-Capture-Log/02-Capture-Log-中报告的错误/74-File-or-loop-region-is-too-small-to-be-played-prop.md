# File or loop region is too small to be played properly.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > File or loop region is too small to be played properly.

#### File or loop region is too small to be played properly.

“文件或循环区域太短，无法正确播放。”文件中的循环点间隔时间不够长。若文件中没有循环点，会将文件设为整个进行循环，但是它太短了。

**可能的原因：**

- 在循环区域短于一个音频帧时，硬件解码器可能会报告此错误。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 音频帧的长度在声音引擎初始化时由 [`AkInitSettings.uNumSamplesPerFrame`](https://www.audiokinetic.com/library/edge/?source=SDK&id=struct_ak_init_settings_a2438a18ece872c83175f70d7f70d659b.html) 的值定义。 |

**推荐的解决步骤：**

- 在 Wwise 的 Source Editor（源编辑器）中，增长循环区域。然后，重新生成并重新部署 SoundBank（音频包）。
- 使用其它编解码器。所有软件编解码器都可处理短小的循环。然后，重新生成并重新部署 SoundBank（音频包）。

---