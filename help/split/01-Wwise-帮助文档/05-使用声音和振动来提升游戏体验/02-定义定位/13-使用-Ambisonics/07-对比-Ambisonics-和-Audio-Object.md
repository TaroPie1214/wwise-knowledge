# 对比 Ambisonics 和 Audio Object

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [使用声音和振动来提升游戏体验](../../00-使用声音和振动来提升游戏体验.md) > [定义定位](../00-定义定位.md) > [使用 Ambisonics](00-使用-Ambisonics.md) > **对比 Ambisonics 和 Audio Object**

### **对比 Ambisonics 和 Audio Object**

Ambisonics 格式适合用于包括 Binauralizer 在内的各种 3D 渲染器。相较于 Audio Object（音频对象），其可确保由效果器和 3D 渲染器本身对固定数量的声道进行处理，不过在方向性传达方面不那么精准。最终的精确度与所选 Ambisonics 阶数 (1 ~ 5) 成正比。

另一方面，基于对象的管线可在方向性传达方面提供更高的精度。这是因为它会保留每个 Audio Object 的 3D 位置信息而不考虑处理成本。对此，声音设计师需要通过其他方式（如声部限制或 [“3D Audio Bed Mixer”一节](../../../10-Wwise-插件/04-效果器插件/01-3D-Audio-Bed-Mixer.md "3D Audio Bed Mixer") 插件）来控制 Audio Object 的数量及处理成本。

#### 融合 Ambisonics 和 Audio Object

Wwise 中基于对象的管线支持结合 Audio Object 使用其他格式（包括 Ambisonics）。也就是说，两种表示形式之间并不是相互排斥的。比如，您可以使用 Audio Object 来保留声音的元数据，以充分利用 Audio Object 提供的方向性渲染优势。同时，针对其余声音使用 Ambisonics。在采用 Audio Object 配置时，所有没有保留为 Audio Object 的声音都会输出到 Bed。Ambisonics 最为适合表示 Bed。其空间表示相对于旋转具有不变性，所有方向上的精度都是完全一致的。

#### Setting up an ambisonic bed in the context of Audio Objects

顶层音频总线必须采用 Audio Object 来表示，不过我们为 Bed 创建了 Ambisonics 子总线，以将下混的 Ambisonics 声音强制输出到该总线。直接输出到父总线的声音将被视作 Audio Object。Ambisonics Bed 也会被视作单个多声道对象。

![](../../../../../images/pe_ambisonic_bed.png)

目前，Wwise 没有针对对象配套提供 Software Binauralizer 效果器。不过，有些平台在 Audio Device（音频设备）层面支持对对象实施双耳处理。比如，Windows Sonic。In that case, the Main Audio Bus inherits the Audio Object configuration of the Audio Device, and the ambisonic bed can be made its direct child.

如需详细了解 Audio Device 在基于对象的音频管线中的效用，请参阅 [“System Audio Device 的作用”一节](../../../03-设置工程/07-建立输出总线的结构/03-了解基于对象的音频/02-System-Audio-Device-的作用.md "System Audio Device 的作用")。

---