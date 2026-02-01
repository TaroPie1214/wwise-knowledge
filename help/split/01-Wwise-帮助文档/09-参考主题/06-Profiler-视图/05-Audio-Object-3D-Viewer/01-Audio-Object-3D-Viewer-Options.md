# Audio Object 3D Viewer Options

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Profiler 视图](../00-Profiler-视图.md) > [Audio Object 3D Viewer](00-Audio-Object-3D-Viewer.md) > Audio Object 3D Viewer Options

### Audio Object 3D Viewer Options

Audio Object 3D Viewer Options（音频对象 3D 查看器选项）允许选择要在 [“Audio Object 3D Viewer”一节](00-Audio-Object-3D-Viewer.md "Audio Object 3D Viewer") 中显示的选项。

| 界面元素 | 描述 |
| --- | --- |
| **General** | |
| Show Grid | 显示网格。在 3D 视图中显示网格线和数值。 |
| Linear Threshold (meters) | 线性阈值(米)。若从原点的距离低于此值，则以 Linear Scaling 方式显示网格；若高于此值，则以 Logarithmic Scaling 方式显示网格。这两种缩放方式的用法如下：  - **Linear Scaling**（线性缩放）：在显示 Audio Object 时按照与听者的距离进行线性缩放。在 Audio Object 与听者的距离相对有限时，这种缩放方式比较有用。为了方便参照距离，会相应地显示头部模型（可使用 **Inter-Ear Distance (cm)** 设置配置大小）。  |  |  |   | --- | --- |   | [备注] | 备注 |   | When the game connects the scaling factor of game units per meter will be automatically set in the view settings. In order to get an accurate head scaling, ensure the game units per meter value is set correctly. | - **Logarithmic Scaling**（对数缩放）：在显示 Audio Object 时按照与听者的距离进行对数缩放。在将 Audio Object 置于空间较大的环境（如外部世界）时，这种缩放方式比较有用。 |
| Grid Max (meters) | 网格最大(米)。为所有要显示的 Audio Object 设定的最大值。超出此范围的所有 Audio Object 都将显示在网格范围之外。 |
| Grid Size | 网格大小。在采用 Logarithmic Scaling 时（在 Linear Threshold 以外），将按比例放大和缩小网格。这种效果跟普通的缩放类似。在采用 Linear Scaling 时（在 Linear Threshold 以内），网格、头部和球体都不会缩放。 |
| Grid Units | 网格单位。允许用户选择如何显示网格数值（距离）。可用选项包括 **Meters**（米）和 **Game Units**（游戏单位）。您可以使用 **Game Units To Meters** 设置来指定两者之间的比率。 |
| Show X-Y-Z Axis | 显示 X-Y-Z 轴。在左下角显示三个轴。这些轴与听者坐标系对应。 |
| Inter-Ear Distance (cm) | 耳间距离 (cm)。按 Linear Scaling 模式设置两耳之间的距离。  |  |  | | --- | --- | | [备注] | 备注 | | Audio Object 与头部的距离必须采用相同的单位来显示。Use the Game Units Per Meter setting in order to change the number of game units in a meter. | |
| Game Units Per Meter | Sets the scaling factor of the game units per meter for the view. 比如，在游戏单位为厘米时，该值就是 100。  若游戏通过  [`fGameUnitsToMeters`](https://www.audiokinetic.com/library/edge/?source=SDK&id=struct_ak_init_settings_acbb4594e7634edbe91adec361e2cf111.html) 初始化设置予以设定，则无需调节此设置。 |

---