# HDR 和 Wwise 声部管线

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [完善工程](../../00-完善工程.md) > [管理输出](../00-管理输出.md) > [使用 HDR](00-使用-HDR.md) > HDR 和 Wwise 声部管线

### HDR 和 Wwise 声部管线

如上所述，HDR 系统使用 Wwise 设计工具中所设置的逻辑音量，并会忽略音频数据的实际振幅。HDR 系统逻辑将认为声音的电平等同于 HDR 总线输入端的电平，即以 Input bus 模式察看 HDR 总线时，在 Voice Monitor 中所看到的电平。These levels depend on the voice volumes, which are the sum of contributions from the Containers hierarchy, control busses of the Busses hierarchy, actions, RTPC and distance attenuation, as well as on gains of each mixing bus located upstream of the HDR bus in the signal flow. 当多个信号路径通往 HDR 总线，例如当使用辅助发送时，HDR 系统逻辑将使用这些路径中增益最大的一条。

在每个音频帧中，声音引擎将计算 HDR 总线输入端的所有声部音量。随后会执行 HDR 系统逻辑，它会根据 HDR 窗口的位置来计算全局 HDR 增益/衰减，并应用至各个声部。该步骤完成后，将按照正常流程处理声部：首先根据音量阈值对声部进行评估，决定是否为虚声部，然后处理数据并应用音量。

#### Make-Up Gain 和源归一化

HDR 系统的逻辑会忽略由 Wwise 中的两个音量属性：源归一化和补偿增益。这些音量控制独立于逻辑音量，主要用于归一化音频素材，您也可以在将音频导入至 Wwise 之前，在波形编辑器中执行这些操作。例如，您可以使用本地化补偿增益校正两种语言之间的音量差异，但 HDR 系统可以跨语言实现相同的表现。此外，具有可以绕过 HDR 逻辑的音量控制十分重要，源归一化和补偿增益便发挥着这一作用。

请注意，虚声部系统以及 Voice Monitor 计算也不考虑补偿增益和源归一化。但虚声部会将 HDR 信号衰减考虑在内。因此，当声部低于 HDR 窗口时会变为虚声部。

The make-up gain slider in the Property Editor can also be used with HDR for aesthetic purposes. 由于从 HDR 系统角度而言它是不起作用的，因此可将其视为 post-HDR 音量（就信号流而言），您可以通过它来绕过 HDR 窗口更改音量。通常，以高于 HDR 阈值的音量单独播放任何声音，通过系统后都是以同一电平输出。使用补偿增益，您可以有效地以更大音量进行播放。例如，您可能会需要第一人称射击游戏中玩家的枪声远大于其余枪声，这就可以通过 HDR 系统的动态混音功能实现。在这里，可使用补偿增益加强音量。

---