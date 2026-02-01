# Soundseed Air Wind

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [Wwise 插件](../../00-Wwise-插件.md) > [源插件](../00-源插件.md) > Soundseed Air Wind

## Soundseed Air Wind

Soundseed Air 包含两个独立的插件：Soundseed Wind 和 Soundseed Woosh。Soundseed Wind 插件是一个 Wwise 源插件，它可以模拟在风吹过和绕过对象时的气流声。这些声音是通过使用实时变化的参数集来驱动合成算法得到的。由于风声完全是合成的，因此不需要源音频文件。Soundseed Wind 可以节省游戏的内存，因为您不再需要过去使用的较长循环风声环境 .wav 文件。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 如果您计划为您的游戏开发、集成和发布 Soundseed Air，则需要购买单独的授权。有关详细信息，请联系 Audiokinetic 销售团队，邮件地址是： [sales@audiokinetic.com。](mailto:sales@audiokinetic.com) |

系统会为各个源创建一个 Soundseed Wind scene（Soundseed Wind 场景）。各个场景包含风本身和若干个 deflector （导流体）对象。风的实际移动将通过定义多个不同属性值（如风向、风速和风级）来创建。创建导流体对象并在整个场景中放置它们，来定义当风吹过这些对象时的声音特征。各个导流体对象都有一套自己的属性，包括频率和增益。这将提供强大的功能和灵活性，用来在游戏中创建几乎任何类型的风声。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 虽然 Soundseed Wind 是一种灵活的合成器，但使用缓慢变化的参数时，它可能会产生最佳的效果。较短的风声其实更适合用 Soundseed Woosh 来合成，如果尝试用 Soundseed Wind 来创建，则可能会出现错误和不想要的声音。 |

### Wind propagation through a scene

Soundseed Wind 模拟场景中的风流；Direction（方向）指定风流进入场景的进入点。可以预计到，压力波会首先碰撞距离进入点最近的导流体。然后，气流将在风的推动下在场景中传播。随着气流的传播，您将听到距离进入点更远的导流体对象在遇到压力波时发出的声音。请注意，进入点的风速越高，气流推进的速度就越快。

下图展示了使用属性集来定义风和一系列导流体的典型场景。导流体的尺寸大小和颜色深浅取决于给它们设置的频率和增益属性值。

|  |
| --- |
|  |

### Using automation curves

您可以使用各种其它工具来进一步优化风声。例如，可使用自动化曲线，根据时间来控制风声和导流体属性。您可以通过添加任意数量的点和使用各种曲线形状，来创建复杂的曲线。下图展示了复杂的风速自动化曲线示例。

|  |
| --- |
|  |

### Cyclic nature of automation

当循环播放风声时，自动化曲线进行周期性重复。当 Duration（时长）极短时，可能会遇到这样的现象：随着 Playback rate（播放速率）加快，声音听上去会时快时慢。这是因为各个采样点之间的间隔变得比自动化曲线的实际周期更长造成的。这种情况下，下一个控制采样将变为自动化曲线的下一个周期的起始点。

### Distance-based attenuation

您也可以为风声应用基于距离的衰减。在最小距离之外，导流体距离每增加一倍，就产生 -6 dB 衰减。通过设置以下属性，可以微调场景中导流体的衰减：

- **Minimum distance** —— 最小距离，到场景中心距离在此半径范围内的导流体，将不应用衰减。
- **Roll-off factor** —— 衰减曲线的斜率，值越高曲线就越陡，即衰减越快。例如，衰减系数为 2，风声衰减速度将变为两倍。

下图展示了 Soundseed Air 插件使用的衰减模型。最小距离和最大距离相同的情况下，使用了三种不同的衰减系数，以显示每种情况下衰减将如何应用。

|  |
| --- |
|  |

### Controlling properties using RTPCs

在 Wwise 中，大部分属性都可以使用属性滑杆来进行实时修改。许多属性还可以通过 RTPC 映射至游戏中的参数。属性值旁边有一个特殊标志，显示它是否使用 RTPC。

下表介绍了两种 RTPC 标志：

| 标志 | 名称 | 描述 |
| --- | --- | --- |
| |  | | --- | |  | | RTPC - 开启 | 属性值已使用 RTPC 绑定到游戏中的参数值。 |
| |  | | --- | |  | | RTPC - 关闭 | 属性值未与游戏中的参数值绑定。 |

**编辑器**

- [“Source Editor: Soundseed Wind”一节](01-Source-Editor-Soundseed-Wind.md "Source Editor: Soundseed Wind")
- [“Contents Editor: Soundseed Wind”一节](02-Contents-Editor-Soundseed-Wind.md "Contents Editor: Soundseed Wind")

---