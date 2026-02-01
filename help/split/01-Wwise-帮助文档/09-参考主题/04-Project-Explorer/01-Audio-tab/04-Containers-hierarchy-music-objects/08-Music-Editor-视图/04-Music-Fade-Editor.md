# Music Fade Editor

[Wwise 帮助文档](../../../../../00-Wwise-帮助文档.md) > [参考主题](../../../../00-参考主题.md) > [Project Explorer](../../../00-Project-Explorer.md) > [Audio tab](../../00-Audio-tab.md) > [Containers hierarchy: music objects](../00-Containers-hierarchy-music-objects.md) > [Music Editor 视图](00-Music-Editor-视图.md) > Music Fade Editor

##### Music Fade Editor

音乐淡变编辑器。在 Music Fade Editor 中，您可以定义当一个音乐对象过渡到另一个音乐对象时所使用的各个淡变的属性。这包括目标对象的淡入效果、源对象的淡出效果和过渡段落的淡入淡出效果。用户可以定义各个淡变的长度和偏置，以及用于进一步自定义过渡的曲线形状。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 要想听到淡变效果，过渡必须具有非零时长。 |

| Option（选项） | 描述 |
| --- | --- |
| Fade | 淡变。当前正在编辑的淡变类型。 |
| Owner | 所有者。过渡所属音乐对象的名称。例如，Music Switch Container 拥有该容器中各段落之间的所有过渡。 |
| (坐标图) | 时间（X 轴）和音乐对象（Y 轴）之间关系的图形表示。 |
|  | 基于坐标图视图的中心进行放大。 |
|  | 将坐标图视图重置为默认的 1:1 缩放比例。 |
|  | 基于坐标图视图的中心进行缩小。 |
| **Fade** | |
| Time | 时长。淡变的时长。  单位：s  Default value: 0  Range: 0 to 60 |
| Offset | 偏置。相关提示点（入口或出口）和淡变之间的时差。  单位：s  Default value: 0  Range: -60 to 60 |
| Fade Curve | 曲线。指定淡变的曲线形状，例如指数型、对数型或 S 型曲线。  Default value: Linear |

**相关主题**

- [“编辑淡变”一节](../../../../../06-创建互动音乐/07-使用-Transition/02-设置-Source-和-Destination-属性.md#editing_fades "编辑淡变")

---