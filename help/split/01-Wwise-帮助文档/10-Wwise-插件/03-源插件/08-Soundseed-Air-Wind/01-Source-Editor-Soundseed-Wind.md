# Source Editor: Soundseed Wind

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [Wwise 插件](../../00-Wwise-插件.md) > [源插件](../00-源插件.md) > [Soundseed Air Wind](00-Soundseed-Air-Wind.md) > Source Editor: Soundseed Wind

### Source Editor: Soundseed Wind

Source Editor 显示与 Soundseed Wind 插件相关的所有属性。

要了解 Soundseed Wind 插件的概况，请参阅[“Soundseed Air Wind”一节](00-Soundseed-Air-Wind.md "Soundseed Air Wind")。

| 界面元素 | 描述 |
| --- | --- |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Name | 用户为该 Soundseed Wind 插件所取的名称。 |
| Source Plugin | 源插件。源插件的类型。 |
| Notes | 备注。Soundseed Wind 插件的其它相关信息。 |
| **Effect Settings** | |
| Deflectors | 导流体。场景中可通过一系列导流体属性与风进行互动的对象。 |
| ID | 导流体的标识号。 |
| [M] | 将该导流体设置为静音。这有助于风声场景的制作。  可以同时将多个导流体设置为静音。无论导流体静音与否，Wwise 都将对所有导流体进行渲染。 |
| [S] | 将其它导流体设置为静音，来单独监听所选的导流体。这有助于风声场景的制作。  可以同时对多个导流体进行 Solo。无论导流体 Solo 与否，Wwise 都将对所有导流体进行渲染。  已经存在其它 Solo 导流体时，要想 Solo 某个导流体，只需按住 Ctrl 并点击 Solo 按钮即可。当前导流体的 Solo 按钮将点亮，并清除已选择的其它所有 Solo 按钮。 |
| Frequency | 暴露在中等速风下时，导流体的中心共振频率。  在 Deflector Positions 坐标图视图中，Frequency 值将决定导流体圆圈的大小。  单位：Hz  Default value: 440  Range: 20 to 20000  Units: Frequency |
| Q Factor | 品质因数。导流体共振曲线的尖锐程度或陡峭程度。品质因数与带宽成反比，因此较大的 Q 值对应窄带宽，而较小的 Q 值对应较宽带宽。  高 Q 值适用于模拟规则或圆形表面，而低 Q 值适合模拟不规则表面。  Default value: 10.0  Range: 0.1 to 50 |
| Gain | 增益。导流体信号的放大量。增大该值可以“增强”导流体信号。减小该值可“减弱”或衰减导流体信号。  在 Deflector Positions 坐标图视图中，增益值还决定导流体圆圈的颜色。深灰色对应高增益值，而浅灰色对应低增益值。  Default value: 0  Range: -24 to 24  Units: dB |
| |  | | --- | |  | | 在 Deflector 列表中添加新的导流体，并在 Deflector Positions 坐标图视图中创建导流体对象。  您也可以通过在 Deflector Positions 坐标图视图中双击任意位置，来创建新的导流体。 |
| |  | | --- | |  | | 从 Deflector 列表和 Deflector Positions 坐标图视图中删除所选导流体。 |
| **Deflector Positions（导流体位置）** | |
| (坐标图) | 导流体相对于扬声器的位置的图形表示，基于 4.0 扬声器环境显示。  要在坐标图视图内改变导流体位置，只需点击其内圈，然后将其拖至新位置即可。 |
|  | 基于坐标图视图的中心进行放大。 |
|  | 将坐标图视图重置为默认的 1:1 缩放比例。 |
|  | 基于坐标图视图的中心进行缩小。 |
| X | 导流体的 X 轴坐标。X 值的单位为 Max Distance（最大距离）值的百分比。 |
| Y | 导流体的 Y 轴坐标。Y 值的单位为 Max Distance（最大距离）值的百分比。 |
| Maximum Distance | 最大距离。定义风声场景的最大尺寸。  在坐标图视图中，最大距离以外圈表示。由于外圈位置固定，因此当您更改最大距离值时，将会相应地调整最小距离圈的大小。  虽然在修改最大距离值时，场景中的导流体看起来没有发生移动，但实际上其位置已根据最大距离值进行了调整。  Default value: 10.0  Range: 1.0 to 100.0 |
| **Properties** | |
| (固定/取消固定) | 当选择另一条曲线时，该属性曲线是否仍保留在坐标图视图中。  当选择 Pin 图标时，无论是否选择该曲线，曲线都会显示在坐标图视图中。 |
| |  | | --- | |  |  （颜色块） | 该颜色即为坐标图视图中相应属性曲线的颜色。 |
| Wind Speed | 风速。风的平均速度。风速会使场景中的导流体产生音高偏置。  Default value: 0  Range: -2400 to 2400 |
| Direction | 风向。起风的方向。  角度将映射至如下方向：  - 0 度 — 北（前） - 90 度 — 东（右） - 180 或 -180 度 — 南（后） - -90 度 — 西（左）  Default value: 0  Range: -180 to 180 |
| Variability | 多样性。因阵风造成的风速变化量。  在属性值缓慢变化时，Soundseed Wind 将产生最佳效果。因此，同时使用高 Variability （多样性）、高 Gustiness（阵风）和高 Q 值很可能会产生不良效果。  Default value: 0.25  Range: 0.0 to 1.0 |
| Gustiness | 阵风。风速随时间变化的可能性。  Default value: 0.5  Range: 0.0 to 1.0 |
| Frequency Shift | 频率偏移。全局属性，定义所有导流体中心频率的上下偏移量。  Default value: 0.0  Range: -4.0 to 4.0 |
| Q Factor Shift | 品质因数。全局属性，定义所有导流体 品质因数的上下偏移量。  Default value: 0.0  Range: -4.0 to 4.0 |
| Gain Offset | 增益偏置。全局属性，定义所有导流体增益的偏置量。该属性可以用作主增益控制。  Default value: 0.0  Range: -96.3 to 24.0  Units: dB |
| Value | 相应属性的设定数值。 |
| Random | 随机（+/-）。相应属性值的正负偏置，定义了属性可能的值域。例如，为属性值添加随机值 1 表示属性的可能值域为 [（值 - 1）至（值 +1）]。  定义 Random 值后，每次播放风声时，Wwise 都会从值域（值 +/- 随机）范围内随机选择一个值。  Default value: 0.0  Range: 0.0 to 3600.0 |
| Automate | 自动化。在声音时长内，可以使用自动化曲线来调整属性值。  勾选该选项后，您就可以在坐标图视图中编辑相应属性的自动化曲线。  Default value: false |
| **Time** | |
| Duration | 风声音源的长度（单位为秒）。  通过将父声音对象的 Loop 属性设置为 Infinite，您可以创建无限循环的风声。  Default value: 10.0  Range: 0.1 to 3600.0 |
| Duration random | 时长随机。Duration 属性的正负偏置，定义了其可能的值域。例如，如果将 Duration 设置为 10，将 Duration random 设置为 5，那么 Duration 的可能值域为（5 至 15），即 [（Duration 值 - 5）至（Duration 值 +5）]。  定义了 Duration random 值后，每次播放风声时，Wwise 都会从值域（值 +/- 随机）范围内随机选择一个值。对于循环播放的声音，每次循环都将使用随机的时长。 |
| Playback rate | 播放速率。时长属性的系数，定义风声的播放速率。例如，值为 2 时，将以 2 倍的速率渲染合成声音，这会使声音短一倍。  如果以动态速率（遵循 Game Parameter）读取循环自动化曲线，则此选项很有用。例如，假设游戏中的角色服用了可以将时间变慢一倍的药物；那么以 0.5 的播放速度循环自动化曲线，将使所有气流声与游戏的时间流逝保持同步。  Default value: 1.0  Range: 0.1 to 10.0 |
| (坐标图) | 以图形来显示属性值自动化曲线，其中 X 轴表示声音的时长，Y 轴表示基于原始属性值的偏置量。  只有选择了 Automate 选项的曲线才能在坐标图视图中进行编辑。您可以通过点击和拖动曲线上的点来移动它们。要添加点，请双击曲线上的任意位置。右键点击曲线的某个部分，可以选择不同的曲线形状。  如果将 RTPC 关联至自动化属性值，则 Wwise 会将自动化曲线中定义的属性值与 RTPC 曲线中定义的值相加。  坐标图视图可以同时显示多条曲线，方法是在列表中选择多个属性或使用固定选项。 |
|  | 基于坐标图视图的中心进行放大。 |
|  | 将坐标图视图重置为默认的 1:1 缩放比例。 |
|  | 基于坐标图视图的中心进行缩小。 |
| X | 所选控制点的 X 轴坐标。  如果选择了多个控制点，则字段显示 0 值，这时可以针对所有已选控制点的当前值，进行统一的增大或减小。例如，如果您选择两个控制点并在 X 文本框中输入 -5，则两个控制点都将向左移动 5 个单位。 |
| Y | 所选控制点的 Y 轴坐标。  如果选择了多个控制点，则字段显示 0 值，这时可以针对所有已选控制点的当前值，进行统一的增大或减小。例如，如果您选择两个控制点并在 Y 文本框中输入 -5，则两个控制点都将向下移动 5 个单位。 |
| **Attenuation（衰减）** | |
| Minimum Distance | 最小距离。到场景中心距离在此半径范围内的导流体，将不应用衰减（0 dB）。  有关 Soundseed Wind 所用衰减模型的详细信息，请参阅 [Soundseed Air Wind](00-Soundseed-Air-Wind.md "Soundseed Air Wind") 页面。  Default value: 5.0  Range: 0.1 to 50 |
| Roll-off Factor | 衰减系数。指定衰减曲线的斜率，值越高，曲线越陡，或者衰减越快。  值为 1 时，在最小距离以外，导流体的距离每增加一倍，将产生 -6 dB 衰减。衰减系数为 2 时，曲线会更陡峭，导流体衰减速度加快一倍。相反，衰减系数为 0.5 时，曲线会更平缓，导流体衰减速度放慢一倍。  有关 Soundseed Wind 所用衰减模型的详细信息，请参阅 [Soundseed Air Wind](00-Soundseed-Air-Wind.md "Soundseed Air Wind") 页面。  Default value: 1  Range: 0.0 to 4 |
| **Settings（设置）** | |
| Dynamic range | Determines the dynamic range or the ratio between the highest and lowest levels in the wind signal that can result from changes in wind speed.  值越小，动态范围越窄，即风速的变化对电平变化的影响越小。在风速变化相同的情况下，值越大，风声信号的电平范围越宽。  Default value: 0.5  Range: 0 to 1 |
| Channels | 声道。声道输出配置。您可以选择以下任一选项：  - **1.0** —— 以单声道输出，无空间定位。 - **2.0** —— 以立体声输出，采用左右空间定位。 - **4.0** —— 以 4.0 声道输出，采用环绕声空间定位。  单位：°  Default value: 2.0 |

---