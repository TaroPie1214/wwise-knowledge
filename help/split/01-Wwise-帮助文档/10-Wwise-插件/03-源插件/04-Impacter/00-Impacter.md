# Impacter

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [Wwise 插件](../../00-Wwise-插件.md) > [源插件](../00-源插件.md) > Impacter

## Impacter

Impacter 是一款专门用来处理撞击类声音文件的实时音频源插件。这些文件由具有猝发或瞬态起始点和指数衰减包络的短促声音构成。利用这款插件，您可以按照以下方式操控源声音：

- **Cross-synthesis**（交叉合成）：Impacter 将每个源文件拆分为两个分层：撞击和主体。撞击分层由声音的冲激构成，主体分层则由声音的回响构成。在使用 Impacter 处理一组文件时，该插件会针对每一播放事件将某一文件的撞击分层和另一文件的主体分层随机结合。同时，该插件还允许单独启用或弃用每个文件的撞击和主体分层。
- **Physicality manipulation**（物理操控）：Impacter 允许修改产生撞击声的对象的感知质量、速度、位置和粗糙度。另外，您还可以向这些属性指派随机化参数，来针对各个播放事件创建不同的声音版本。
- **Mapping properties to game physics**（将属性映射到游戏物理）：您可以将各个插件实例与 Game Object（游戏对象）、Event（事件）或 RTPC 关联。另外，还可设定 Impacter 的参数以反映与材质和碰撞相关的游戏引擎物理。

设计工具支持将文件拖放到 Source Editor（源编辑器）中。所有分析都可在设计工具插件内完成处理，无需使用外部分析工具或分析结果文件。工程的 SoundBank（音频包）中包含最终合成模型以供运行时使用。

**局限性**

Impacter 插件中的分析和合成算法非常高效，因为其会对所处理的声音类型作出可靠的假设。它们针对具有猝发或瞬态起始点和指数衰减包络的短促声音进行了专门的设计。这样既可适当处理衰减中的时间变化或二次瞬态，又可保证这些特性不会受到合成参数太大的影响。

其他类型的声音也可拖到该插件中，但在使用给定参数设计声音时可能会产生不合预期的行为。当然，这并不影响我们使用 Impacter 来尝试和探索不同的声音设计。只不过对于徐缓的声音，分析时间会更长一些，而且完成分析之前还会影响设计工具播放声音。

**编辑器**

- [“Source Editor：Impacter”一节](01-Source-Editor：Impacter.md "Source Editor：Impacter")
- [“Contents Editor：Impacter”一节](02-Contents-Editor：Impacter.md "Contents Editor：Impacter")

---