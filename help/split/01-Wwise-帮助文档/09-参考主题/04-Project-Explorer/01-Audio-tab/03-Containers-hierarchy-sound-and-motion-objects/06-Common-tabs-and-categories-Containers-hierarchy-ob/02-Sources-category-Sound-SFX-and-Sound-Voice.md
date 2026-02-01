# Sources category: Sound SFX and Sound Voice

[Wwise 帮助文档](../../../../../00-Wwise-帮助文档.md) > [参考主题](../../../../00-参考主题.md) > [Project Explorer](../../../00-Project-Explorer.md) > [Audio tab](../../00-Audio-tab.md) > [Containers hierarchy: sound and motion objects](../00-Containers-hierarchy-sound-and-motion-objects.md) > [Common tabs and categories: Containers hierarchy objects](00-Common-tabs-and-categories-Containers-hierarchy-ob.md) > Sources category: Sound SFX and Sound Voice

##### Sources category: Sound SFX and Sound Voice

See [“利用 Source Editor 编辑音频源”一节](../../../../../05-使用声音和振动来提升游戏体验/01-定义对象播放行为/01-定义对象的播放行为/01-利用-Source-Editor-编辑音频源.md "利用 Source Editor 编辑音频源") for details on modifying the Sources properties.

| Audio File Source | |
| --- | --- |
| 界面元素 | 描述 |
| **Specific** | |
| Channel Configuration Override | 声道配置。列出音频源可用的声道配置，可选择将其显示在坐标图中。  音频波形始终按照 Wwise 的规定排序显示声道。对于 5.1，对应 L + R + C + SL + SR + LFE（坐标图左侧，从上到下）。对于一阶 Ambisonics，对应 W + Y + Z + X。  Wwise 按照显示顺序解释所选声道配置并将其输出到坐标图中。音频源声道配置可按以下文件排序模式进行解释：  - **SMPTE**:在默认情况下，Wwise 将文件顺序诠释为 SMPTE（Microsoft 标准），除非其包含 Ambisonics 标头。对于 5.1，将显示为 5.1(L,R,C,LFE,SL,SR)。不过，列表中会显示默认设置及 Detect [channelconfig]。其中，channelconfig 表示检测到的配置。对于 5.1，将显示为 Detect [5.1(L,R,C,LFE,SL,SR)]。 - **FuMa**:在默认情况下，Wwise 将 Ambisonics Component Ordering 以及一阶、二阶和三阶 Ambisonics 的声道排序解释为 FuMa。对于一阶 Ambisonics，将显示为 4(Ambisonics) (FuMa)。不过，列表中会显示默认设置及 Detect [channelconfig]。其中，channelconfig 表示检测到的配置。对于一阶 Ambisonics，将显示为 Detect [4(Ambisonics)(FuMa)]。FuMa 没有定义高阶 Ambisonics。高阶 Ambisonics 仅解释为 AmbiX (经过 SN3D 归一化的 ACN 排序)。 - **Anonymous**:匿名 Channel Config 选项直接按照坐标图中的显示顺序来标记声道编号。一阶 Ambisonics 文件将显示为 4 (Anonymous)；在坐标图中直接显示为 1 + 2 + 3 + 4。同样地，5.1 文件将显示为 6 (Anonymous)；在坐标图中直接显示为 1 + 2 + 3 + 4 + 5 + 6。 - **Film**:除 Ambisonics 文件外，列表中的备选文件排序为 Film。对于 5.1，将显示为 5.1(L,C,R,SL,SR,LFE)。 - **AmbiX**:对于 Ambisonics，列表中的备选文件排序为 AmbiX（经过 SN3D 归一化的 ACN 排序）。对于一阶 Ambisonics，将显示为 4(Ambisonics)(AmbiX)。  Default value: 0 |
| Make-Up Gain | 补偿增益。原始音频文件音量电平的增加量或降低量。  Default value: 0  Range: -24 to +24  Units: dB |
| Trim Start | 裁剪起点。定义裁剪起始位置。转码和播放期间不包含裁剪起点位置左侧的任何内容。  单位：s  Default value: -0.001 |
| Trim End | 裁剪终点。定义裁剪结尾位置。转码和播放期间不包含裁剪终点右侧的任何内容。  单位：s  Default value: -0.001 |
| Override file loop points | 不沿用文件循环点。定义正在使用的循环点：  - **Checked**:使用工程中的循环点。 - **Unchecked**:使用 WAV 文件中的循环点。  Default value: false |
| Loop Start | 循环起点。定义循环开头。  |  |  | | --- | --- | | [备注] | 备注 | | 只有当父声音启用了循环时才使用循环点。 |  Default value: -0.001 |
| Loop End | 循环终点。定义循环结尾。  |  |  | | --- | --- | | [备注] | 备注 | | 只有当父声音启用了循环时才使用循环点。 |  Default value: -0.001 |
| Crossfade duration | 交叉淡变时长。定义位于循环点周围的、在每次循环时应用交叉淡变的区域。它可以让循环更流畅，可用于清除特定循环点处可能发生的卡嗒声和爆音。  单位：ms  Default value: 0  Range: 0 to 60000 |
| Crossfade Shape | 交叉淡变形状。交叉淡变曲线的形状。列表选项为：  - Logarithmic (Base 3) - Sine - Logarithmic (Base 1.41) - Inverted S-Curve - Linear - S-Curve - Exponential (Base 1.41) - Reciprocal Sine - Exponential (Base 3)  Default value: Sine |
| Marker Input Mode | 标记输入模式。决定如何管理标记。您可以选择以下选项之一：  - **Import From File**: 使用原始音频文件中保存的标记。 - **Detect From Transients**：自动检测音频文件中的瞬态起始点，并在测得位置添加标记。在选择此选项时，将显示检测灵敏度滑杆。检测灵敏度用于控制瞬态起始点检测算法的灵敏度。 - **Manual Markers**: 手动放置标记。  |  |  | | --- | --- | | [备注] | 备注 | | 在移动、移除或新增标记后，将自动切换为手动模式。 |  Default value: Import From File |
| Marker Detection Sensitivity | 标记检测灵敏度。瞬态检测算法的灵敏度。灵敏度值越大，产生的瞬态标记越多。  Default value: 0  Range: 0 to 100 |
| Fade-in Duration | 淡入时长。淡入曲线的时长。  单位：ms  Default value: 0  Range: 0 to 3600 |
| Fade-in Curve | 淡入曲线。淡入曲线的形状。列表选项为：  - Logarithmic (Base 3) - Sine - Logarithmic (Base 1.41) - Inverted S-Curve - Linear - S-Curve - Exponential (Base 1.41) - Reciprocal Sine - Exponential (Base 3)  Default value: Sine |
| Fade-out Duration | 淡出时长。淡出曲线的时长。  单位：ms  Default value: 0  Range: 0 to 3600 |
| Fade-out Curve | 淡出曲线。淡出曲线的形状。列表选项为：  - Logarithmic (Base 3) - Sine - Logarithmic (Base 1.41) - Inverted S-Curve - Linear - S-Curve - Exponential (Base 1.41) - Reciprocal Sine - Exponential (Base 3)  Default value: Reciprocal Sine |

---