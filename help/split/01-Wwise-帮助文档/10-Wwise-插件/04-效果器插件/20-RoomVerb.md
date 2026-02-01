# RoomVerb

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [Wwise 插件](../00-Wwise-插件.md) > [效果器插件](00-效果器插件.md) > RoomVerb

## RoomVerb

（请参阅下文的 [“RoomVerb properties”一节](20-RoomVerb.md#wwise_roomverb_properties "RoomVerb properties")。）

您可以使用 RoomVerb 混响器插件来模拟游戏声学空间内的声音反射。 该插件效果器为多功能混响，拥有大量控件，可让您重建任意类型的空间。 与高度优化的 Matrix Reverb 插件相比，该混响插件使用更多的 CPU，但凭借其更多的控制，您可以实现更为逼真的效果。

许多 RoomVerb 属性都可以实时编辑，并使用 RTPC 映射到特定的 Game Parameter。通过 RTPC 执行的属性变化将即时应用并经过合理插值，因此不会产生任何音频副作用。对于无法映射至 Game Parameter 的属性，在 Wwise 内仍可在播放过程中随时更改。不过在有些情况下，更改这些属性会导致重置 Effect（效果器），在一定程度上影响听感。

RoomVerb 插件在其算法中考虑以下概念：

- **模态（或频率）密度** —— 模态是音频信号频域表示中的峰值。 当模拟大多数的声学空间时，增加模态密度可改善混响的逼真度。减低模态密度可能导致嗡嗡声。
- **Echo density** —— 回声密度。混响算法每秒产生的回声量。 该数字过低时，会产生尖锐的声音。 该数字过高时，会听到非常“密实”的混响尾声。

### RoomVerb processing pipeline

当 RoomVerb 效果器插件作用于声音时，音频信号分将为以下两部分：

- **干声信号** —— 直接信号，或信号不经过处理的部分。
- **湿声信号** —— 经过处理的信号，或应用 RoomVerb 效果器设置的信号部分。

RoomVerb 的湿声部分包括两个主要部分。 信号的第一个部分包括早期反射（ER）分量，第二个部分包括混响分量。 可自由选择是否使用 ER 分量，方便优化 Effect 处理和内存分配。Effect 插件内的各项设置可定义实际的 ER 和混响单元，它们将与原始干声信号一起，重新混音并使用同一信号输出。下图显示应用了 RoomVerb 效果的声音的处理管线。

|  |
| --- |
|  |

### RoomVerb properties

| 界面元素 | 描述 |
| --- | --- |
| Name | 名称。效果器实例的名称。  效果器实例是一组效果器属性设置。它们可以是两种类型之一：自定义或共享集。自定义实例只能由一个对象使用，然而共享集可在多个对象之间共享。 |
| (Object Color) | 显示对象的颜色。单击图标可打开颜色选择器。    选择一种颜色并将其应用于对象。在为对象选择某种颜色时，会在选定方块上显示调色板图标，并在右下角标注黄色三角（如图所示）。  若要沿用父对象的颜色，请选中颜色选择器最左侧的方块。 |
| Inclusion | 启用。决定是否在生成 SoundBank 时在其中包含相应元素。如勾选，则包含该元素。如未勾选，则不会包含该元素。  为了针对各个平台来优化声音设计，有时需在特定平台上弃用某些元素。在默认情况下，此复选框会应用于所有平台。使用复选框左侧的 [Link 标志](../../08-使用-Wwise/03-了解-Property-Editor/11-使用-Property-Editor.md#linking_unlinking_property_values "Linking or unlinking property values") 来取消链接相应元素。然后，便可根据平台来自定义复选框的状态。  若取消选中此选项，则将禁用编辑器中的属性和行为选项。  Default value: true |
| (Show references) | 指示工程中有多少元素包含对对象的直接引用。若存在对对象的引用，则图标显示为橙色；若不存在此类引用，则图标显示为灰色。  通过单击该按钮，可打开 [“Reference View 视图”一节](../../09-参考主题/04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")，并在 **References to:**（引用:）字段中查看对象的名称。 |
| Notes | 备注。Effect 的其它信息。 |
| Metering | 电平测量。指示当前正在测量电平的对象的名称。 |
|  | 允许浏览其他要测量电平的对象。  |  |  | | --- | --- | | [备注] | 备注 | | 只有对于包含 VU 电平表的效果器，Effect Editor 中才会显示电平测量界面元素。 | |
|  | 设置 Effect Editor 中选定标签页的显示方式。默认情况下，整体面板中仅显示一个选定标签页。不过，您可以通过单击分隔器按钮将面板沿横向或纵向一分为二，显示两个不同的标签页。当前所选选项将以高亮背景色显示。  |  |  | | --- | --- | | [备注] | 备注 | | 无法同时在两个面板中显示同一标签页。若选中的标签页已在另一面板中显示，则另一面板将自动显示另一标签页。 | |

|  |  |
| --- | --- |
| **Early Reflections（早期反射）** | |
| Enable Early Reflections | 早期反射。指定是否计算和处理信号的早期反射分量。  Default value: true |
| ER pattern | ER 模式。包含预定义早期反射到达时间（单位为毫秒）和增益（线性）的模式，它们是特定声学空间的特征。 |
| ER Room Size | Determines the time scaling applied to the ER pattern.  零值表示选择的 ER 模式不做时间缩放，值为 100 表示在接收各个早期反射前的时间加一倍，值为 -100 表示所选 ER 模式花费时间减半。 请注意，第一次早期反射的时间是了解建模声学空间大小的一条良好的感知线索。  Default value: 0  Range: -100 to 100 |
| ER Rear Delay | 后置延迟。发送至前置和后置声道的早期反射之间的延迟。  在结合矩阵编码系统（如 Dolby Pro Logic 2）对环绕声信号使用非零 Rear Delay 时，可能会听到一些副作用（通常作梳状滤波效应）。 比如，在 Xbox 360 平台上使用模拟立体声输出时，就可能会出现这种情况。  单位：ms  Default value: 0  Range: 0 to 100 |
| **Reverb** | |
| Pre Delay | 预延迟。指定直达声与密集混响尾音开头之间的时间。 虽然预延迟支持 Exclusive RTPC，但其仅可用于在播放之前实施初始化。若使用 RTPC 在播放期间实时更改预延迟，则将反复重新初始化延迟缓冲区，进而导致混响信号突然静音或陡然变化。  单位：ms  Default value: 25  Range: 0 to 1000 |
| Decay Time | 衰减时间。声音的低频从其原始幅度降低 60 dB 所花费的时间。  单位：s  Default value: 1.2  Range: 0.2 to 10 |
| HF Damping | HF 阻尼。衰减系数，用于控制高频相对于低频的混响时间。  当该比率的值小于 1 时，高频混响时间比低频混响时间长。  Default value: 2.25  Range: 0.5 to 10 |
| Density | 密度。直接修改感知模态密度。 较低的值通常会导致出现一定量的嗡嗡声，而较高的设置会导致声音频率较平，并伴有嘈杂的混响尾声。  此属性与插件的内存和 CPU 用量成正比，因为模态密度高的话延迟线也会比较长。这些较长的延迟线类似于较大的空间，因此该属性有时可用于控制感知到的空间大小。 该属性与“Room shape”（空间形状）和“Quality”（品质）属性紧密配合来起作用。  单位：%  Default value: 80  Range: 0 to 100 |
| Room Shape | Determines the perceived coloration of the reverb by controlling (along with the Density property) the delay lengths used by the algorithm while maintaining a constant modal density. 通常来说，高空间形状设置意味着最长和最短延迟长度之间存在较少差异。 这类似于常规形状的空间，例如立方体。 Room Shape 设置越小，延迟线之间的发散则越大。  建议您对各个 Density 值试验一下不同的 Room Shape 设置。  单位：%  Default value: 100  Range: 0 to 100 |
| Quality | 品质。决定算法使用的混响单元数量。较高的 Quality 值可显著改善混响的音频品质，但 CPU 占用将成比例地增加。  如果要提升 Quality，则最好降低 Density 值，反之亦然。 较低的 Quality 值（如 2）通常不能提供逼真的混响所需的回声密度。 较高的 Quality 值可能会模拟出反射性更强的空间。  单位：混响数量  Default value: 8  Range: 2 to 16 |
| Diffusion | 漫反射。直接控制混响的回声密度特征。 较低的 Diffusion 值有时会导致尖锐的声音，此时可明显听到各个回声。较高的 Diffusion 值会形成更密集的混响尾音。 较高的 Diffusion 还意味着瞬态信号将由于其能量随时间扩散而渐渐模糊。 该属性的效果在具有陡峭瞬态部分的声音素材上最为明显，如小军鼓敲击声。  单位：%  Default value: 100  Range: 0 to 100 |
| Stereo Width | 立体声宽度。决定在左声道（前或后）和右声道（前或后）中输出的 ER + 混响内容之间的相似性。 这可以形成更强的空间感，方法是扩大早期反射和混响的立体声散布（Spread）。  当使用零值时，左声道和右声道的 ER + 混响输出相同。 因此可获得一定的内存和 CPU 优化。 值为 180 表示各侧收到完全不同的 ER + 混响信号。 当通过耳机监视时该效果会更明显，因为耳机没有会减弱效果的扬声器串扰（cross-talk）。  该属性对于 1.0（单声道）或 1.1 声道声音没有效果。  单位：°  Default value: 180  Range: 0 to 180 |
| **Tone** | |
| Enable Tone | 乐音。指定是否将架式滤波器和峰值滤波器作用于混响信号的各种分量。 勾选后，您可以应用最多三种不同的滤波器。 每种滤波器也可插入信号链中的不同点。  Default value: false |
| Filter Band Insert | 插入。确定信号链中的滤波器应用点。 提供以下插入点：  - **Off**:不应用任何滤波器。 - **ER only**:向信号的早期反射部分应用滤波器。 - **Reverb only**:向信号的混响尾音部分应用滤波器。 - **ER + Reverb**:向信号的早期反射和混响尾音部分及应用滤波器。  未选择早期反射选项时，无论选择了哪个插入点，ER 分量将总是被忽略。  Default value: ER + Reverb |
| Filter Band Curve | 曲线。确定可作用于信号的滤波类型。 可以使用以下筛选器：  - **Low shelf** —— 底架。增强或削减低频率，高频不受影响。 - **Peaking** —— 峰值。增强或削减特定频率区域，较低和较高频率不受影响。 该频率区域的宽度可使用 Q 属性进行控制。 - **High shelf** —— 高架。增强或削弱高频率，低频不受影响。  Default value: High shelf |
| Gain | 增益。所选频带的音频信号放大量。 增加该值，可增强音频信号。 减小该值将削弱音频信号。  单位：dB  Default value: 0  Range: -32 to 32 |
| Filter Band Frequency | 评率。频谱中将受到增益影响的部分。  单位：Hz  Default value: 10000  Range: 20 to 20000  Units: Frequency |
| Filter Band Q | 品质因数。中心频率周围将受增益变化影响的区域。 低 Q 值表示带宽会较宽，相反，高 Q 值表示带宽会较窄。  仅当 Curve 属性设置为峰值时，Q 属性才可用。  Default value: 1  Range: 0.1 to 10 |
| **Input Levels（输入电平 ）** | |
| Center Input Level | 中置。确定中置声道向混响算法贡献的信息量。  Default value: 0  Range: -96.3 to 0  Units: dB |
| LFE Input Level | 确定 LFE 声道向混响算法贡献的信号量。  Default value: -96.3  Range: -96.3 to 0  Units: dB |
| **Reverb Levels（混响电平）** | |
| Front Level | 前置。控制作用于左前和右前声道的后期混响量。 该属性控制不会影响可显式控制的中置声道。  该属性不会影响没有后置声道的声道配置。 此时，控制湿声电平（ER + 混响）会更为直观。  Default value: 0  Range: -96.3 to 0  Units: dB |
| Rear Level | 后置。控制作用于左后和右后声道的后期混响量。  该属性不会影响没有后置声道的声道配置。 此时，控制湿声电平（ER + 混响）会更为直观。  Default value: 0  Range: -96.3 to 0  Units: dB |
| Center Level | 中置。 控制作用于中置声道（如果有该声道）的后期混响量。  Default value: 0  Range: -96.3 to 0  Units: dB |
| LFE Level | 控制作用于 LFE 声道（如果有该声道）的后期混响数量。  Default value: -96.3  Range: -96.3 to 0  Units: dB |
| **Output Levels（输出电平）** | |
| Dry Level | 干声电平。确定作用于直接路径声音的增益系数。  Default value: -96.3  Range: -96.3 to 0  Units: dB |
| ER Level | 确定作用于早前反射信号的增益系数。  未选择 Early reflections（早期反射）复选框时，该控制不起任何作用。  Default value: -20  Range: -96.3 to 0  Units: dB |
| Reverb Level | 混响电平。确定作用于混响信号（混响尾音）的增益系数。  Default value: -20  Range: -96.3 to 0  Units: dB |
| Estimated memory usage | 预计内存占用。用于生成该效果的预计内存占用量。（KB） 该预计假设采用环绕声配置。 如果没有左后声道和右后声道，则使用的内存将稍低于显示的数量。  对于 Windows 平台，该值假设声音品质 (AkSoundQuality) 设置为 High（48 kHz 采样率）。 如果声音品质设置为 Low（24 kHz 采样率），则预计的内存量通常为显示的值的一半。 |

---