# Multiband Compressor

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [Wwise 插件](../../00-Wwise-插件.md) > [Audio Device 效果器插件](../00-Audio-Device-效果器插件.md) > [Mastering Suite](00-Mastering-Suite.md) > Multiband Compressor

### Multiband Compressor

Multiband Compressor 模块用于压缩超出阈值的音量，最多支持四个频段。您可以随意设定用于分割各个频段的频率。

![](../../../../../images/sms_compressor.png)

每个频段都可设置以下参数：

- *Crossover Frequency*（分频频率）：在多高的频率分割频段（在坐标图中标示为竖线）。
- *Threshold*（阈值）：在多高的电平开始应用压缩。
- *Ratio*（比率）：要应用多大幅度的压缩，相当于实际增益每增高 1 dB 时电平会超出阈值多少。
- *Attack*: Time, in seconds, for the compression to be fully applied after the level has gone over the threshold.
- *Release*: Time, in seconds, for the compression to stop being applied after level returned below the threshold.
- *Knee*（拐点）：在接近和超过阈值时应用多大幅度的压缩（数值越大，幅度越小）。
- *Gain*（增益）：在压缩之后应用多高的补偿增益。

您可以根据需要设置如何在声道之间链接各项压缩属性，相应地来选择三种不同的模式：*No Link*、*All Channels* 和 *Partial Link*。在后两种模式下，会根据针对各个声道计算得出的最大压缩值来应用压缩。

- *No link*（不链接）：单独向每个声道应用压缩。
- *All channels*（所有声道）：统一向所有声道应用最大压缩。
- *Partial link*（部分链接）：使用 Link Strength 值来控制声道的压缩。对于对应声道，按照最大值应用压缩；对于其他声道，则按照相对于最大值的 Link Strength 比率应用压缩。

*Partial link* 模式提供两个参数来控制如何向链接在一起的声道（即压缩幅度小于最大值的声道）应用压缩：

- *Link Strength*（链接强度）：在压缩其他声道（即压缩幅度小于最大值的声道）时在最大压缩值的基础上应用相应的比率。这样方便控制如何按照相对于最大值的比率 (0% ~ 100%) 向所述声道应用压缩。
- *Stereo Link*（立体声链接）：允许将左右一对声道链接起来。这样可以强行向任意声道对统一应用压缩。

#### 使用 Mastering Suite 进行压缩

下图展示了压缩器会应用怎样的处理：将输入信号分开，按照频段进行压缩，然后再合并起来。

![](../../../../../images/sms_compressor_schema.png)

您可以向各个频段应用不同幅度的压缩；这样便可实施更加精细的配置，从而移除不需要的效果（如 pumping）。这在使用单频段压缩器时是做不到的。

Multiband Compressor 所用的压缩算法旨在平滑地调节信号能量，使得其在输出到人耳时听起来比较自然。换句话说，它会根据针对每个频段计算得出的输入信号的均方根 (RMS) 值来控制压缩比率。因此，它无法控制突发峰值（若要控制突发峰值，请使用 [“Limiter”一节](04-Limiter.md "Limiter") 模块）。

![](../../../../../images/sms_compressor_threshold_rms.png)

---