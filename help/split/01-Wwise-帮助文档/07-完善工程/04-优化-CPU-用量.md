# 优化 CPU 用量

[Wwise 帮助文档](../00-Wwise-帮助文档.md) > [完善工程](00-完善工程.md) > 优化 CPU 用量

## 优化 CPU 用量

在 Wwise 中设计音频时，CPU 用量是一个非常重要的考量因素。除此之外，还要考虑性能和品质之间的平衡。若针对多个平台进行设计，则须了解各个平台的技术限制和要求，同时兼顾配套软件所需的 CPU 处理资源。

很多 Wwise 功能和插件都会对 CPU 用量产生影响。本节将简要阐述影响 CPU 用量的主要因素，并据此来提供不同的 CPU 优化策略和窍门。总的来说，这当中包括使用 Profiler（参见[*性能分析*](06-性能分析/00-性能分析.md "性能分析")）监控 CPU 性能，决定有哪些因素需要考量和处理，然后基于本节中的准则来探索可能的解决方案。

每个 Wwise 工程都是不同的。可用的 CPU 处理资源因平台而异，品质和性能要求也各不相同。因此，并没有一套适用于所有情形的具体准则和建议。相反，您需要不断地尝试，在 Wwise 中试听声音，以此来确定最佳设置。以下主要因素会对 CPU 用量产生影响：

- 同时播放的声部数。声部（尤其是实声部）的数量会对 CPU 产生很大的影响。在声部数增加时，CPU 用量会随之增加。
- 效果器。Wwise 音频效果器会消耗 CPU 处理资源，其具体用量因效果器而异，包括将效果器用在何处，以及是否对其进行渲染。
- 音频编解码器。在通过编解码器对音频文件进行转码时会占用 CPU，有些编解码器需要比别的编解码器更多的 CPU 处理资源。
- Spatial Audio。用于控制 3D 声学效果的各种选项和设置可能会对 CPU 用量产生很大的影响。

后续章节会对以上各项做进一步的阐释。

## 监控 CPU 用量

因为很多因素都可能会对 Wwise 中的 CPU 用量产生影响，所以并没有一种简单的方法能满足所有 CPU 用量优化的需要。相反，您必须考虑所有与工程相关的因素，并确定可接受的 CPU 用量水平（可能因平台而异），进而使用 Wwise Profiler 来识别 CPU 用量最多的属性和设置并相应地加以调节。说到底，CPU 性能和声音品质之间的恰当平衡取决于用户自己的判断。

通常，可使用 Profiler（参见[*性能分析*](06-性能分析/00-性能分析.md "性能分析")）在 Capture Session（捕获会话）期间监控性能，确定总体 CPU 用量和峰值，然后在 Advanced Profiler（高级性能分析器）和 Performance Monitor（性能监控器）中查看对 CPU 用量造成影响的具体因素。在这当中，尤其要注意以下几点：

- 在 Advanced Profiler 中，CPU 选项卡会在会话期间显示对 CPU 用量造成影响的各种因素。藉此，可识别占用 CPU 处理资源最多的插件、音频编解码器、效果器等。

  ![](../../../images/advanced_profiler.png)
- 在 Performance Monitor Settings（性能监控器设置）对话框中，选中名称中包含 CPU 字样的所有相关条目。对此，可根据需要将以下选项用在坐标图和列表中：

  - CPU - Plug-in Total
  - CPU - Total
  - Spatial Audio - CPU
  - Spatial Audio - Path Validation CPU
  - Spatial Audio - Portal Path Validation CPU
  - Spatial Audio - Portal Raytracing CPU
  - Spatial Audio - Raytracing CPU

通过结合 Advanced Profiler 和 Performance Monitor 中的选项，可在 Capture Session 期间对 CPU 用量有一个概括的了解。在确定对 CPU 用量造成影响的因素之后，便可参照本节其他部分所述的建议来对工程的性能实施优化。

## 优化声部

同时播放的实声部数（即实际播放的声音数）会对 CPU 用量产生很大的影响。为了降低声部所用的 CPU 处理资源数量，可使用以下设置来减少同时播放的声部数：

- **Playback Limit**（播放限值）：决定同一时间最多可播放多少个声音实例。
- **Priority**（优先级）：决定在超出播放限值时要终止哪些声音或将哪些声音发送到虚声部。
- **Virtual Voices**（虚声部）：表示运行时出现但若降到规定音量阈值以下或超出规定播放限值便不予实际播放的声音。建议的虚声部行为为 Kill if finite else virtual（若非无限循环则终止，否则发送到虚声部）。请参阅 [“Advanced category: sound and motion objects”一节](../09-参考主题/04-Project-Explorer/01-Audio-tab/05-Common-tabs-and-categories-audio-structures/12-Advanced-category-sound-and-motion-objects.md "Advanced category: sound and motion objects")。

有关详细信息，请参阅[*管理优先级*](../05-使用声音和振动来提升游戏体验/03-管理优先级/00-管理优先级.md "管理优先级")。

## 优化效果器

效果器会消耗 CPU 处理资源。总的来说，CPU 用量会随同时播放的效果器实例数增加。不过，有一些额外事项需要注意：

- **声道数**。CPU 用量会随音频声道数增加，而声道数因音频总线而异。比如，单声道声音上应用的三个效果器实例占用的 CPU 处理资源要少于 7.1 总线（八个声道）上应用的单个效果器实例。

  另外，有些效果器（如对象处理器）仅针对每条总线实例化一次。有关效果器、Audio Object 和总线的详细信息，请参阅[“结合 Audio Object 使用效果器”一节](../05-使用声音和振动来提升游戏体验/04-管理效果器/01-结合-Audio-Object-使用效果器.md "结合 Audio Object 使用效果器")。
- **效果器类型**。不同类型的效果器占用的 CPU 处理资源数量也不相同。混响效果器便是个特例。大多效果器的 CPU 用量会随着每个声道应用的效果器数线性增加。相比之下，混响效果器的 CPU 用量的增加速率更为和缓一些。并且，不同类型的混响效果器占用的 CPU 处理资源数量也不相同。比如，Matrix Reverb 的 CPU 用量就比 RoomVerb 少（不过它的选项比较少）。其他效果器（如 Compressor 和 Parametric EQ）的 CPU 用量比混响效果器还少。
- **效果器渲染**。有一种方法可以降低效果器的 CPU 用量，就是对效果器进行渲染来使其成为 WEM 文件本身的一部分。在对效果器实施渲染时，会先对经过渲染的效果器进行处理，再将其打包到 SoundBank（音频包）中。这样的话，它就不会占用运行时处理资源了。您可以通过 [“Integrity Report”一节](../09-参考主题/02-视图/01-Integrity-Report.md "Integrity Report") 来确定哪些效果器适合进行渲染。为此，可选中 Optimizations（优化）选项并运行报告。有关渲染的详细信息，请参阅[“渲染效果器”一节](../05-使用声音和振动来提升游戏体验/04-管理效果器/00-管理效果器.md#rendering_effects "渲染效果器")。
- **旁通效果器**。若有些效果器仅适用于特定情形，您可以根据需要来选择将其旁通。比如，若只有当玩家在游戏中处于特定状态时才会使用某个失真效果器，便可利用 RTPC 来应用与监控玩家状态的 Game Parameter（游戏参数）关联的 Bypass Effect 动作。

## 优化音频编解码器

Wwise 会使用音频编解码器来对音频文件进行压缩和解压。通常，用户需要对音频文件实施压缩以确保其符合工程的内存预算要求。不过，编解码器会占用 CPU 处理资源。一般来说，编解码器输出的音质越高，占用的 CPU 处理资源越多。在决定要使用哪些编解码器时，需要兼顾 CPU 用量、内存用量、存储空间和音频品质。

若要支持多个平台，可通过 Conversion Settings（转码设置）共享集来为不同的平台使用不同的编解码器。有关详细信息，请参阅[“Creating audio Conversion Settings ShareSets”一节](01-管理输出/10-对音频文件做转码/01-Creating-audio-Conversion-Settings-ShareSets.md "Creating audio Conversion Settings ShareSets")。

Wwise 支持以下编解码器：

- **PCM**：PCM 并不是音频编解码器，而是一种未压缩文件格式。它可以提供高品质的声音，并占用极少 CPU 处理资源，但需要大量的内存空间。

  为了最大限度地降低 CPU 用量，可将此格式用于短促、重复的声音或高保真音频。
- **Vorbis**：Vorbis 是一款非常流行的编解码器。它可以提供优质的音频，并占用较少 CPU 处理资源。在 Wwise 中，其针对互动媒体和游戏平台进行了优化。

  为了最大限度地降低 CPU 用量，请避免将该格式用于频繁重复的音频文件，因为其每次播放都要占用 CPU 来解压文件。不过，对于大多数其他类型的声音都可使用 Vorbis。
- **Opus**：Opus 可提供与 Vorbis 类似的音质，但会对文件进行更大幅度的压缩。不过，它会占用比 Vorbis 更多的 CPU 处理资源。它适用于长的不重复的音频源（如对白或环境声）。有关如何对 Opus 文件进行解码的更多详细信息，请参阅 [Wwise SDK](https://www.audiokinetic.com/library/edge/?source=SDK&id=index.html) 中的平台特定章节。
- **ADPCM**：ADPCM 可以提供较高的压缩比，并占用极少的 CPU 处理资源，但相对而言音频品质较低。您可以将其用于移动平台来最大限度地降低 CPU 和运行时内存用量。

## 优化 Spatial Audio

在 Wwise 中，Spatial Audio 是指与 3D 模拟环境下的声音相关的各种设置和配置（如衰减、衍射、反射等）。Spatial Audio 的很多方面都会占用 CPU 处理资源，为此必须测试不同的选项并确定品质和性能之间的恰当平衡。

In Wwise Authoring, many of the options are available in the Property Editor. See
[“Positioning category: Containers hierarchy objects”一节](../09-参考主题/04-Project-Explorer/01-Audio-tab/05-Common-tabs-and-categories-audio-structures/10-Positioning-category-Containers-hierarchy-objects.md "Positioning category: Containers hierarchy objects") and [“Positioning category: Audio and Auxiliary Busses”一节](../09-参考主题/04-Project-Explorer/01-Audio-tab/02-Busses-hierarchy/04-Common-tabs-and-categories-Busses-hierarchy-object/05-Positioning-category-Audio-and-Auxiliary-Busses.md "Positioning category: Audio and Auxiliary Busses")).

Spatial Audio 需要利用 CPU 处理资源来实施与发声体和听者定位、声音衰减、3D 对象的声音反射、衍射等相关的大量计算。Spatial Audio 效果器和设置有多种可能的组合，所以并没有简单普适的 CPU 优化准则。不过，若在 Profiler（性能分析器）中看到 Spatial Audio 占用了大量 CPU 处理资源，以下建议可能会很有帮助：

- 确保空间几何构造尽可能简单。最大限度地减少三角形和衍射边缘的数量。
- 为声音应用有限的衰减。随着最大衰减半径的增大，会需要更多的 CPU 处理资源来搜索路径。在有限衰减曲线达到其最大距离时，曲线会降到工程设置中设定的可闻度阈值以下。
- 避免播放距离太远而听不到的声音，并在超出衰减半径且不会返回时停止播放它们。
- 使用 Room（房间）和 Portal（门户）来分隔相互独立的场景部分。
- 在对 Spatial Audio 进行初始化时，可设置多个 [Spatial Audio Initialization Settings](https://www.audiokinetic.com/library/edge/?source=SDK&id=struct_ak_spatial_audio_init_settings.html) 来控制 CPU 用量：

  - 运用 CPU 负荷均衡。
  - 增大反射和衍射计算所需的移动阈值，藉此以精度为代价来降低 CPU 用量。
  - 减少射线追踪引擎中所用的初级射线数。
  - 减小最大反射阶数。在大部分情况下，一阶和二阶就已足够。
  - 减小衍射阶数。先从四阶开始，不过也可使用二阶或一阶。

有关 Spatial Audio 的详细信息（包括对 CPU 优化的建议），请参阅以下文档：

- 在 Wwise Help 中，参阅[*定义定位*](../05-使用声音和振动来提升游戏体验/02-定义定位/00-定义定位.md "定义定位")。
- 在 SDK 中，参阅 [Spatial Audio](https://www.audiokinetic.com/library/edge/?source=SDK&id=spatial_audio.html)。尤其，参阅[提升性能](https://www.audiokinetic.com/library/edge/?source=SDK&id=raytracing_geometry_guide.html#raytracing_geometry_guide_performance_tweaking)。
- 在 Unreal Integration 文档中，参阅 [Unreal Spatial Audio 教程](https://www.audiokinetic.com/library/edge/?source=UE4&id=spatialaudio.html)。
- 在 Unity Integration 文档中，参阅[在 Unity 中使用 Spatial Audio](https://www.audiokinetic.com/library/edge/?source=Unity&id=pg_spatialaudio.html)。

## 其他有关 CPU 优化的资源

除了本文档，还有一些资源包含有关 CPU 优化的信息：

- [优化 CPU 用量](https://www.audiokinetic.com/library/edge/?source=SDK&id=goingfurther_eventmgrthread.html)探讨了基于 SDK 的优化方案，其可为开发者提供用户界面中没有的额外选项。
- 两篇博文 –[《Wwise CPU 优化：通用指南》](https://blog.audiokinetic.com/wwise-cpu-optimizations-general-guidelines/)和[《如何控制声部 – 优化CPU（第 1 部分）》](https://blog.audiokinetic.com/how-to-get-a-hold-on-your-voices-optimizing-for-cpu-part-1/)– 也探讨了相关优化措施。不过请注意，文中的具体数字可能并不适用于最新的平台。
- The [Performance Optimization](https://www.audiokinetic.com/learning/learn-wwise/wwise-performance-optimization) learning material contains many examples and recommendations for CPU (and memory) optimization. 其以基于 Unity 的《Wwise Adventure Game》示例程序为例做了阐释。

**相关主题**

- [Wwise Fundamentals Module 20: Optimizing your sound design](https://www.audiokinetic.com/en/courses/wwise101/?source=wwise101&id=optimizing_game)

---