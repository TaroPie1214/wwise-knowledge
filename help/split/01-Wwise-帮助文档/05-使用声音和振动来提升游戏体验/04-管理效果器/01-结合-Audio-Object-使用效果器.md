# 结合 Audio Object 使用效果器

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用声音和振动来提升游戏体验](../00-使用声音和振动来提升游戏体验.md) > [管理效果器](00-管理效果器.md) > 结合 Audio Object 使用效果器

## 结合 Audio Object 使用效果器

效果器对 Audio Object（音频对象）的处理方式取决于将效果器插入到了哪种类型的总线上以及效果器是否为对象处理器。以下章节详细介绍了各种可能情况：

- [“将效果器插入到混音总线上”一节](01-结合-Audio-Object-使用效果器.md#effects_on_mixing_bus "将效果器插入到混音总线上")
- [“将效果器插入到 Processing Audio Objects 状态的总线上”一节](01-结合-Audio-Object-使用效果器.md#effects_on_audio_objects_bus "将效果器插入到 Processing Audio Objects 状态的总线上")
- [“对象处理器”一节](01-结合-Audio-Object-使用效果器.md#object_processor_instantiation "对象处理器")

### 将效果器插入到混音总线上

在将效果器插入到混音总线上时，始终在开始处理总线时实施混音。因此，多个总线输入将被混音到单个音频流。另外，在混音阶段还会应用定位转换。总线上所插入的各个效果器仅实例化一次，预混音频流会向效果器依次馈送音频信号。总的来说，处理成本与声道数量成正比。

注意，在总线被实例化多次且各个实例与不同的 Game Object（游戏对象）关联时，会针对每个总线实例将效果器实例化一次。

下图展示了带有效果器的混音总线的内部处理流程：

![](../../../../images/bus_internal_processing_mixing.png)

|  |  |
| --- | --- |
|  | 将声部输出到总线；在混音时对其信号进行采样。 |
|  | 从之前的混音总线得到基于声道的格式。 |
|  | 从之前的总线 Processing Audio Objects 得到一系列 Audio Object。 |
|  | 将所有输入（包括声部、基于声道的输入和 Audio Object）混合在一起。 |
|  | 通过内部混音创建基于声道的格式；不保留单独的 Audio Object。 |
|  | 由效果器操控基于声道的格式。 |
|  | 由总线输出基于声道的格式。  |  |  | | --- | --- | | [备注] | 备注 | | 有些效果器可以改变总线的输出格式。比如，即便总线被配置为了单声道，照样可以输出 Audio Object。 | |

### 将效果器插入到 Processing Audio Objects 状态的总线上

|  |  |
| --- | --- |
| [注意] | 注意 |
| Processing Audio Objects 状态的总线不支持以下效果器：  - **AK Convolution Reverb**：针对每个 Audio Object 运行一个效果器实例会导致性能问题。 - **Matrix Reverb**：针对每个 Audio Object 运行一个效果器实例会导致性能问题。 - **Peak Limiter**：在 Audio Object 层级应用峰值限制会造成不稳定。在设定 Audio Object 时，可将 Mastering Suite 插件用在 Audio Device 上来应用峰值限制。 - **Recorder**：该效果器无法运行多个实例。 - **RoomVerb**：针对每个 Audio Object 运行一个效果器实例会导致性能问题。 - **Auro Headphone**：不支持。  若把该效果器插入到此类总线上，将无法在运行时对其进行处理。 |

在将效果器用在 Processing Audio Objects 状态的总线上时，有几点需要注意。除非效果器是[“对象处理器”一节](01-结合-Audio-Object-使用效果器.md#object_processor_instantiation "对象处理器")，否则有多少个 Audio Object，就会将每个效果器实例化多少次。比如，若在 Audio Object 总线上插入了 Parametric EQ，并将 10 个 Audio Object 输出到了该总线，则 Parametric EQ 将被实例化 10 次。总的来说，处理成本与输出到总线的 Audio Object 数量成正比。

下图展示了处于 Processing Audio Objects 状态并带有效果器的总线的内部处理流程：

![](../../../../images/bus_internal_processing_not_mixing.png)

|  |  |
| --- | --- |
|  | 将声部输出到总线；在混音时对其信号进行采样。 |
|  | 从之前的混音总线得到基于声道的格式。 |
|  | 从之前的总线 Processing Audio Objects 得到一系列 Audio Object。 |
|  | 将所有不属于 Audio Object 的输入（比如声部和基于声道的输入）转换为单独的 Audio Object。除此之外，还有提供给总线的其他 Audio Object。 |
|  | 创建一系列 Audio Object。 |
|  | 由效果器单独操控各个 Audio Object。 |
|  | 由总线输出一系列 Audio Object。 |

### 对象处理器

某些 Wwise 效果器本身就支持 Audio Object。此类效果器称为对象处理器，其仅针对每个总线实例化一次。

- **3D Audio Bed Mixer**：该效果器会被实例化一次，将传入的 Audio Object 转到三种输出中的一种：Main Mix、Passthrough Mix 或一系列未经混音的 3D Audio Object。
- **Compressor/Expander**：该效果器会被实例化一次，在内部下混时仅执行一次分析。所有 Audio Object 都会应用增益衰减。
- **Meter**：该效果器会被实例化一次，在内部下混时仅执行一次分析。所有 Audio Object 只会进行一次动态处理。因此，将输出单个 Game Parameter（游戏参数）值。
- **Mastering Suite**：Mastering Suite 同样与 Audio Object 兼容，其 Multiband Compressor 对 Audio Object 的处理方式与 Compressor 类似。
- **Parametric EQ**：Parametric EQ 只需实例化一次就可对所有 Audio Object 运行相同的 EQ 处理并在内部追踪各个 Audio Object 的滤波器状态。

Reflect 也支持 Audio Object，不过方式有所不同。Reflect 通常会插入到单声道总线上，其可在父总线的配置为 Audio Objects 时输出 Audio Object。随后会针对每个早期反射声输出一个 Audio Object。也就是说，最终可能会产生大量 Audio Object。

---