# Speaker Panner

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Project Explorer](../00-Project-Explorer.md) > [Audio tab](00-Audio-tab.md) > Speaker Panner

### Speaker Panner

Speaker Panner（声像摆位器）的行为取决于对象所对应 Property Editor（属性编辑器）内 Positioning（定位）选项卡中的 Speaker Panning（扬声器声像摆位）设置。在默认情况下，Speaker Panning 将设置为 **Direct Assignment**（直接指派）。此时，无论听者或游戏对象的位置或朝向如何，都会将 2D 声音和音乐的声道直接指派给输出总线的对应声道。这时无法使用 Speaker Panner 视图。

不过，您可以选择通过其他两个 Speaker Panning 选项来启用 Speaker Panner 视图。然后，便可按照以下所述使用其调节源音频与输出总线各个声道的关联方式：

- **Balance-Fade**（平衡-淡变）：Speaker Panner 包含一个二维坐标图，其中设有 X 和 Y 坐标以及中心圆点。X 坐标用于控制左右扬声器平衡，Y 坐标用于控制前后扬声器平衡。您可以将圆点拖到此坐标图内的任意位置，来*调节输出总线各个声道的音量*。离圆点较近的声道的音量会增大，离圆点较远的声道的音量会减小。

  |  |  |
  | --- | --- |
  | [备注] | 备注 |
  | 在输出总线为立体声时，Y 坐标不会产生任何影响。在圆点位于坐标图中央时，7.1 声道配置的各个旁置扬声器均处于最大电平状态。  The Z coordinate only works for 7.1.4 sounds routed to 7.1.4 busses. Only the height channels are heard when Z is 100, and only the channels of the plane are heard when the Z is -100. |
- **Steering**（转向）：Speaker Panner 包含一个三维坐标图，其中设有 X、Y 和 Z 坐标以及中心圆点。X 坐标用于控制左右配比，Y 坐标用于控制前后配比，Y 坐标用于控制上下配比。您可以将圆点拖到此坐标图内的任意位置，来*调节输出总线各个声道的源音频配比*。配比将依据相对于圆点的位置进行计算。

  |  |  |
  | --- | --- |
  | [备注] | 备注 |
  | 坐标图中并未显示 Z 轴；我们可以通过 Z 轴滑杆来查看和调节它的值。而且，它对高度分层中不含声道的配置没有影响。 |

| 界面元素 | 描述 |
| --- | --- |
| Name | 对象的名称。 |
| Notes | 备注。对象属性的额外信息。 |
| (坐标图) | 坐标图。以图形形式显示 5.1 环境中圆点相对于听者和扬声器的位置。  |  |  | | --- | --- | | [备注] | 备注 | | 您可以在对象所对应 Property Editor 的 Positioning 选项卡中使用 **Center %** 滑杆来定义中置声道。 | |
|  | 基于坐标图视图的中心进行放大。 |
|  | 将坐标图视图重置为默认的 1:1 缩放比例。 |
|  | 基于坐标图视图的中心进行缩小。 |
| Pan Left-Right | 声像摆位左右。定义圆点在 X 轴上的坐标。  Default value: 0  Range: -100 to 100 |
| Pan Front-Rear | 声像摆位前后。定义圆点在 Y 轴上的坐标（不会影响立体声配置。）  Default value: 0  Range: -100 to 100 |
| Pan Up-Down | 声像摆位上下。定义圆点在 Z 轴上的坐标（对高度分层中不含声道的配置没有影响）。  |  |  | | --- | --- | | [备注] | 备注 | | 只有将 Speaker Panning 模式设为 Steering，或设为 Balance-Fade 并将 7.1.4 声音或总线输出到 7.1.4 总线，才会显示 Z 轴滑杆。 |  |  |  | | --- | --- | | [备注] | 备注 | | 坐标图中并未显示 Z 轴；我们可以通过 Z 轴滑杆来查看和调节它的值。 |  Default value: 0  Range: -100 to 100 |

**相关主题**

- [“使用 Speaker Panning”一节](../../../05-使用声音和振动来提升游戏体验/02-定义定位/02-使用-Speaker-Panning/00-使用-Speaker-Panning.md "使用 Speaker Panning")
- [“将音频信号传送到中置扬声器”一节](../../../05-使用声音和振动来提升游戏体验/02-定义定位/09-将音频信号传送到中置扬声器.md "将音频信号传送到中置扬声器")

---