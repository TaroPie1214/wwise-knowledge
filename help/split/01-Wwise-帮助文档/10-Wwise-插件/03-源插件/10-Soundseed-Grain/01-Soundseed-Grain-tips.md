# Soundseed Grain tips

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [Wwise 插件](../../00-Wwise-插件.md) > [源插件](../00-源插件.md) > [Soundseed Grain](00-Soundseed-Grain.md) > Soundseed Grain tips

### Soundseed Grain tips

While exploring the Soundseed Grain granular synthesis, keep the following tips in mind.

1. [“Press Start Capture”一节](01-Soundseed-Grain-tips.md#press_start_capture "Press Start Capture")
2. [“Preview: edit in external editor”一节](01-Soundseed-Grain-tips.md#Preview_Edit_in_External_Editor "Preview: edit in external editor")
3. [“Using saw up mode for scanning file/implement time scaling effects”一节](01-Soundseed-Grain-tips.md#Using_saw_up_mod_for_scanning_file "Using saw up mode for scanning file/implement time scaling effects")
4. [“设计 3D 环境声”一节](01-Soundseed-Grain-tips.md#Designing_3D_ambiences "设计 3D 环境声")
5. [“Sound positioning settings”一节](01-Soundseed-Grain-tips.md#sound_Positioning_settings "Sound positioning settings")
6. [“Soundseed Grain 设计”一节](01-Soundseed-Grain-tips.md#SoundSeed_Grain_Design "Soundseed Grain 设计")
7. [“Amplitude and filter are best used with grain modulation”一节](01-Soundseed-Grain-tips.md#Amplitude_and_Filter_are_best_used_with_grain_modulation "Amplitude and filter are best used with grain modulation")
8. [“Using markers in a macro window”一节](01-Soundseed-Grain-tips.md#Using_markers_in_a_macrowindow "Using markers in a macro window")

#### Press Start Capture

在 Wwise 中，必须明确启动实时监控。为此，可在工具栏中单击 Start Capture（开始捕获）按钮 ![](../../../../../images/btn_start_capture.png)。同时，确保启用 Show Live Data（显示实时数据）选项 ![](../../../../../images/btn_live_off.png)，除非要查看之前时间点的数据。在启动捕获后，会同时激活 Grain Visualizer（粒子观察器）、Slider Feedback（滑杆反馈）和 VU Meter（电平表）。如此一来，便可使用合成器十分方便地完成设计。

#### Preview: edit in external editor

Soundseed Grain 不支持直接预览已经加载但尚未粒化的文件。若想试听文件内容，请右键单击波形视图，并选择 **Edit in External Editor**（在外部编辑器中编辑），然后选用适合的编辑器。详请参阅[“Managing external editors for audio”一节](../../../02-入门/04-个性化您的工作空间/04-设置用户偏好.md#selecting_external_audio_editors "Managing external editors for audio")。

#### Using saw up mode for scanning file/implement time scaling effects

为了让 Position（位置）按照顺序扫描文件，进而应用时间缩放效果（单独应用时间拉伸和音高变换），可以直接将 Saw up+（上锯齿波+）调制器指派给 Position 属性。

1. 在 Soundseed Grain 中加载文件。
2. 选择适合的调制器。在此，我们选用 Mod 3（调制器 3），因为其默认 Waveform（波形）便是 Saw up+。
3. 在 Modulator（调制器）视图中，将所选调制器的 Waveform 类型设为 **Saw up+**，并将 Time/Freq（时间/频率）模式设为 **Period**（周期），然后将 Period 设为文件的时长（如 Waveform 视图左下角所示）。文件时长显示为秒，而调制器周期以毫秒为单位，所以要将该值乘以 1,000。比如，若文件时长为 2.00 秒，则将调制器周期设为 2,000。
4. 在 Modulator Assignment（调制器指派）视图中，将 Property（属性）设为 Position，并将 Modulator 设为所选调制器（本例中为 Mod 3），然后将 Amount（数量）设为 100。

|  |
| --- |
|  |

若减小调制器的 Period，则 Soundseed Grain 会以更快的速度扫描文件。在必要时，可为调制器的 Period 应用 RTPC。另外，还可选用不同的波形。比如，使用矩形 LFO 实现对文件的 ping-pong 扫描。

#### 设计 3D 环境声

对于 3D 环境声，在设计 Soundseed Grain 音色时，要尽可能提高声场的沉浸感和环绕程度，比如将播放时的散布百分比设为 100%。然后，Wwise 会在声音的 Spread（散布）值小于 100 时将其收缩成点声源。

#### Sound positioning settings

1. 选中应用了合成器的声音。
2. 在 Property Editor（属性编辑器）的 Positioning（定位）选项卡中，将 3D Spatialization（3D 空间化）模式设为 Position（位置）或 Position + Orientation（位置 + 朝向）。将 Attenuation（衰减）共享集设为 Spread 曲线。

|  |
| --- |
|  |

|  |  |
| --- | --- |
| [备注] | 备注 |
| 除了使用 Attenuation ShareSet，还可将声音用作 Spatial Audio **Room**（Spatial Audio 房间），然后让 Wwise Spatial Audio 根据听者与该 Room 的 Portal（门户）的距离来调制散布百分比。有关 Room 和环境声的更多详细信息，请参阅 [Wwise Spatial Audio SDK 文档](https://www.audiokinetic.com/library/edge/?source=SDK&id=spatial__audio.html)。 |

#### Soundseed Grain 设计

在 Soundseed Grain 中创建环绕环境声时，通常会使用单声道或多声道文件，然后围绕听者生成 3D 空间化粒子。

1. 请确保输出配置为多声道。为了获得最佳效果，最好与输出总线的配置保持一致。不过也完全可以输出一阶 Ambisonics，然后在三阶 Ambisonics 总线中混音。
2. 将 Positioning 模式设为 3D Spatialization。
3. 通过 Azimuth（方位角）和 Elevation（高度角）实施随机调制。
4. 根据需要设置 Spread（比如设为 100 便会充满整个空间）。假如使用的是多声道素材，请确保 Spread 大于 0，否则会将所有粒子视为点声源，并下混为单声道。

|  |
| --- |
|  |

#### Amplitude and filter are best used with grain modulation

Amplitude（振幅）属性与 Level（电平）属性的效果相同，只不过其表示为百分比而非分贝，所以一般不太直观。它的主要作用是生成不同振幅的粒子。比如，若将 Amplitude 设为 0，并将 Amplitude 指派给 Random+（随机+）调制器，同时将 Amount 设为 100，则会随机生成振幅介于 0 和 100% 之间的粒子。为了获得同样的效果，也可将 Amplitude 设为 50，并使用双极 Random 调制器，同时将 Amount 设为 50。

Filter（滤波器）与 Amplitude 相似。有多少个同时播放的粒子，就会应用多少个滤波器。假如希望滤波设置不随时间变化，那么出于性能方面的考虑，虽然每个滤波器占用的资源并不多，但最好还是使用 EQ 插入效果器。不过，假如要为各个粒子应用不同的滤波设置，请结合使用滤波器实施粒子调制。

|  |
| --- |
|  |

#### Using markers in a macro window

为了制作发动机声音，您可能已经导入了录音，并为每一分段设置了不同的 RPM 或发动机状态。然后，您希望合成器根据所需状态在一系列文件分段中随机选取粒子。对此，可将每个分段视为一个宏窗口，并从中选取粒子。为了制作这种宏窗口，可以在 RTPC 的基础上应用粒子调制。

1. 将 Position 属性指派给 RTPC，然后绑定到相应的游戏参数（如 RPM）。此 RTPC 用来定义宏窗口的左侧边界。
2. 将 Position 属性指派给 Random+ 调制器，并根据需要设置 Amount。该 Amount 用来定义宏窗口的宽度（表示为文件时长的百分比）。
3. 若要使窗口的宽度随 RPM 变化，则使用 RTPC 将其绑定到 RPM。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 除上述方法外，也可使用双极 Random 调制器波形。在这种情况下，Position RTPC 用来定义窗口的中心而非左侧边界。 |

|  |  |
| --- | --- |
| [备注] | 备注 |
| 对于发动机声音，可能需要对每次轰鸣位置进行标记，并使用 Snap to markers（对齐到标记）选项。 |

|  |
| --- |
|  |

---