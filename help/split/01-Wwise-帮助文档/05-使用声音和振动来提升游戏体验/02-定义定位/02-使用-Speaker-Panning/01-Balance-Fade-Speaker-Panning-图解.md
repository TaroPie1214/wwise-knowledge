# Balance-Fade Speaker Panning 图解

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [使用声音和振动来提升游戏体验](../../00-使用声音和振动来提升游戏体验.md) > [定义定位](../00-定义定位.md) > [使用 Speaker Panning](00-使用-Speaker-Panning.md) > Balance-Fade Speaker Panning 图解

### Balance-Fade Speaker Panning 图解

在将 Speaker Panning（扬声器声像摆位）设为 **Balance-Fade**（平衡-淡变）时，可使用 Speaker Panner 来调节对象的 Output Bus（输出总线）中各个声道的音量。在选择该模式时，**Edit...**（编辑...）按钮将变为启用状态，同时会打开 Speaker Panner（扬声器声像摆位器）。Speaker Panner 包含一个二维坐标图，其中设有 X 和 Y 坐标以及中心控制点。您可以将控制点拖到坐标图内的任意位置，来调节 Output Bus 的各个声道的音量。靠近控制点的声道的音量会增高，远离控制点的声道的音量会降低。

若对象的源音频包含的声道多于 Output Bus，会先根据[下混行为](../../../07-完善工程/01-管理输出/12-下混行为/00-下混行为.md "下混行为")对内容进行下混。若源音频包含的声道少于 Output Bus，会先对内容进行上混（即向后方延展）。For example, stereo channels are replicated in the surround channels. Surround channels of a 4.x/5.x configuration are replicated in the side/back channels of a 6.x/7.x configuration.

实际音量调节取决于 Output Bus 配置。比如，在 Output Bus 为立体声时，Y 坐标不会产生任何影响。有关详细示例，请参阅以下章节。

|  |  |
| --- | --- |
| [备注] | 备注 |
|  |

A quad upmix to 5.1 configuration is similar to the stereo upmixes described in the
following examples. The difference is that in a quad upmix, the front and back pair
are populated from the corresponding source pairs.

#### Volume modulation

下表中的截图阐释了在 5.x 声道总线上对 5.x 声道输入实施声像摆位的情形。输入的声道由彩色方块表示，其会被放在各自的位置上。也就是说，输入的左前声道 (FL) 只在总线的 FL 声道中播放，输入的中置声道 (C) 只在总线的 C 声道中播放（以此类推）。

| 在 5.x 声道总线上对 5.x 声道输入实施声像摆位 | |
| --- | --- |
| Speaker Panner | Output Bus 电平表 |
| |  | | --- | |  |    X = 0，Y = 0。 | |  | | --- | |  |    输入的 FL 声道只在总线的 FL 声道中播放，输入的 C 声道只在总线的 C 声道中播放（以此类推）。 |
| |  | | --- | |  |    X = -50，Y = 0。  输入声道 C、FR、SR 依据各自音量按比例淡出。 | |  | | --- | |  |    右侧声道（FR 和 SR）以 33% 的音量播放，C 声道以 50% 的音量播放。 |
| |  | | --- | |  |    X = -100，Y = 0。 | |  | | --- | |  |    只有左侧声道（FL 和 SL）能听到声音。 |

#### 上混

在输入的声道少于输出时，会先对输入进行上混再实施声像摆位。下表中的截图阐释了在 5.x 声道总线上对立体声输入实施声像摆位的情形。

|  |  |
| --- | --- |
| [注意] | 注意 |
| In Balance-Fade mode, the Z coordinate only applies to 7.1.4 sounds or busses routed to a 7.1.4 bus. Otherwise, no upmixing occurs towards the height speakers. |

| 在 5.x 声道总线上对 2.0 声道输入实施声像摆位 | |
| --- | --- |
| Speaker Panner | Output Bus 电平表 |
| |  | | --- | |  |    X = 0，Y = 0。  先将立体声输入上混为 5.1 再实施声像摆位。 | |  | | --- | |  |    环绕声声道（SL 和 SR）的音量等于前置声道（FL 和 FR）的音量。 |
| |  | | --- | |  |    X = 0，Y = 50。  先将立体声输入上混为 5.1 再实施声像摆位。 | |  | | --- | |  |    前置声道（FL 和 FR）的音量大于环绕声声道（SL 和 SR）的音量。 |
| |  | | --- | |  |    X = -50，Y = 100。  先将立体声输入上混为 5.1 再实施声像摆位。不过，在 Y = 100 时，环绕声声道的音量会降到 0。 | |  | | --- | |  |    FL 声道的音量为 FR 声道的两倍，环绕声声道（SL 和 SR）保持静音。 |

---