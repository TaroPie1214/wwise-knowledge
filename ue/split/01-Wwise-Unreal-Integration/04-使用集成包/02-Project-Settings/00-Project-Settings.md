# Project Settings

|  |
| --- |
| Wwise Unreal Integration Documentation |

Project Settings

所有与 Wwise Integration 相关的设置都会显示在 Unreal Project Settings (**Edit > Project Settings**) 中的 Wwise 分区下。您可以将数据从某一平台设置结构复制粘贴到另一平台设置结构，即便两个结构不完全相同。Unreal 会复制匹配的数据并忽略其余数据。

# Platform Initialization Settings

此分区包含 Unreal Engine 安装包中可用的所有受支持的 Wwise 平台的初始化设置。在编辑器中对设置所作的修改只有在重新启动编辑器后才会生效；不过，若使用 Standalone 游戏模式，则将按照当前设置初始化新的 SoundEngine 实例。

![](../../../images/wwise_windows_settings.png)

## Common Settings

- **Sample Rate**   
  此项表示采样率 (Hz)。默认值为 48000。对于较低的音频品质，使用 24000。支持任何合理有效的采样率。不过，若将采样率设得非常低，声音引擎可能会无法正常运行。
- **Maximum Number of Memory Pools**   
  此项表示最多有多少个内存池。每个加载的 Bank 都需要一个内存池。
- **Maximum Number of Positioning Paths**   
  此项表示最多有多少条自动化路径可供对声音进行定位。
- **Command Queue Size**   
  此项表示 Command Queue 的大小。
- **Samples Per Frame**   
  此项表示每个音频帧的样本数（256、512、1024、2048）。
- **Streaming Look Ahead Ratio**   
  此项表示所有流传输预读启发式算法值的倍数。
- **Number Of Refills in Voice**   
  此项表示声部缓冲区中的重填缓冲区数。对于双缓冲，设为 2。默认值为 4。

### Main Output Settings

- **Audio Device ShareSet**   
  此项表示所要使用的自定义音频设备的名称。在 Wwise 工程的 Audio Device ShareSet 分区中定义自定义音频设备。若将此项保留为空，则通过默认音频设备正常输出。
- **Device ID**   
  此项表示特定于设备的标识符。在使用多个相同类型的设备时使用。若仅使用一个设备，请将该设置保留为 0（默认）。
- **Panning Rule**   
  此项表示要针对输出到立体声总线的信号应用哪种 3D 声像摆位。在 Speakers 模式下，使用前置扬声器的角度。在 Headphones 模式下，将扬声器角度替换为两个间隔 180 度的虚拟话筒之间的 Constant Power 声像摆位。
- **Channel Config Type**   
  该代码通过 uChannelMask 完成对声道的识别。Anonymous：声道掩码 == 0。Standard：必须通过 `AkSpeakerConfigs` 中定义的标准来识别声道。Ambisonic：声道掩码 == 0。声道遵从标准 Ambisonics 阶数。
- **Channel Mask**   
  该位域的声道标识符取决于 `AkChannelConfigType`（最大可设为 20）。
- **Number of Channels**   
  此项表示声道数。通过声道掩码得出，或者直接设为匿名。

### Spatial Audio Settings

![](../../../images/wwise_spatial_audio_settings.png)

- **Max Sound Propagation Depth**   
  此项表示声音最多可穿过多少个 Portal。
- **Movement Threshold**   
  Amount that an emitter or listener has to move to trigger a recalculation of reflections and diffraction. 在设为较大数值时可以减轻 CPU 负荷，不过精度会有所下降。
- **Number Of Primary Rays**   
  此项表示随机射线投射中使用的初级射线数。
- **Reflection Order**   
  此项表示最高反射阶数 (1 ~ 4)。
- **Max Diffraction Paths**   
  Limit the maximum number of diffraction paths computed per emitter, excluding the direct/transmission path. The acoustics engine searches for up to 'Max Diffraction Paths' paths and stops searching when this limit is reached. Setting a low number for uMaxDiffractionPaths (1-4) uses fewer CPU resources, but is more likely to cause discontinuities in the resulting audio. This can occur, for example, when a more prominent path is discovered, displacing a less prominent one. Conversely, a larger number (8 or more) produces higher quality output but requires more CPU resources. The recommended range is 2-8.
- **Max Global Reflection Paths [Experimental]**   
  Set a global reflection path limit among all sound emitters with early reflections enabled. Potential reflection paths, discovered by raycasting, are first sorted according to a heuristic to determine which paths are the most prominent. Afterwards, the full reflection path calculation is only performed on the most prominent 'Max Reflection Paths'. Limiting the total number of reflection path calculations can significantly reduce CPU usage. Recommended range: 10-50. Set to 0 to disable the limit. In this case, the number of paths computed is unbounded and depends on how many are discovered by raycasting.
- **Diffraction Order**   
  此项表示最高衍射阶数（衍射路径当中的弯曲次数）。在衍射阶数较高时，可容纳更加复杂的几何构造，代价是 CPU 用量更高。必须在几何构造上启用衍射才能查找衍射路径。若设为 0，则在所有几何构造上禁用衍射。此参数可限制从听者位置投射以扫描环境的衍射射线的递归深度，以及用于查找发声体和听者之间路径的衍射搜索的深度。To optimize CPU usage, set it to the maximum number of edges you expect the obstructing geometry to traverse.
- **Max Emitter Room Aux Sends**   
  The maximum number of game-defined auxiliary sends that can originate from a single emitter. An emitter can send to its own Room and to all adjacent Rooms if the emitter and listener are in the same Room. If a limit is set, the most prominent sends are kept, based on spread to the adjacent portal from the emitter's perspective. Set to 1 to only allow emitters to send directly to their current Room, and to the Room a listener is transitioning to if inside a portal. Set to 0 to disable the limit. The default value is 3.
- **Diffraction on Reflections Order**   
  此项表示反射路径每一端最多可有多少个衍射点。借助对反射的衍射，可在听者或发声体进出反射的阴影区时将反射平滑地淡入和淡出。When greater than zero, diffraction rays are sent from the listener to search for reflections around one or more corners from the listener. 必须在几何构造上启用衍射才能查找衍射的反射。若设为 0，则禁用对衍射的反射。
- **Max Diffraction Angle Degrees**   
  The largest possible diffraction value, in degrees, beyond which paths are not computed and are inaudible. Must be greater than zero. Default value: 180 degrees. A large value (for example, 360 degrees) allows paths to propagate further around corners and obstacles, but takes more CPU time to compute. A gain is applied to each diffraction path to taper the volume of the path to zero as the diffraction angle approaches fMaxDiffractionAngleDegrees, and appears in the Voice Inspector as 'Propagation Path Gain'. This tapering gain is applied in addition to the diffraction curves, and prevents paths from popping in or out suddenly when the maximum diffraction angle is exceeded. In Wwise Authoring, the horizontal axis of a diffraction curve in the attenuation editor is defined over the range 0-100%, corresponding to angles 0-180 degrees. If fMaxDiffractionAngleDegrees is greater than 180 degrees, diffraction coefficients over 100% are clamped and the curve is evaluated at the rightmost point.
- **Maximum Path Length**   
  此项表示反射/衍射路径的最大长度。
- **CPU Limit Percentage**   
  The maximum amount of computation time allocated for Spatial Audio, as a percentage (0-100) of the current audio frame. When the value is greater than 0, Spatial Audio dynamically adapts the load-balancing spread value between 1 and the specified uLoadBalancingSpread based on current CPU usage and the specified CPU limit. Set to 0 to disable the dynamic load-balancing spread computation.
- **Load Balancing Spread**   
  The number of uLoadBalancingSpread frames over which to spread Spatial Audio task computation. The minimum value is 1, which indicates no load balancing. When a CPU limit is active, this value determines the upper limit of the dynamic load balancing spread, and is not a fixed value.
- **Smoothing Constant (ms) [Experimental]**   
  Enable parameter smoothing on the diffraction paths generated by the Acoustics Engine. Set 'Smoothing Constant (ms)' to a value greater than 0 to define the time constant (in milliseconds) for parameter smoothing. The time constant of an exponential moving average is the amount of time for the smoothed response of a unit step function to reach 1 - 1/e ~= 63.2% of the original signal. A large value (eg. 500-1000 ms) results in less variance but introduces lag, which is a good choice when using conservative values for uNumberOfPrimaryRays (eg. 5-10), uMaxDiffractionPaths (eg. 1-3) or fMovementThreshold ( > 1m ), in order to reduce overall CPU cost. A small value (eg. 10-100 ms) results in greater accuracy and faster convergence of rendering parameters. Set to 0 to disable path smoothing.
- **Adjacent Room Bleed**   
  A global scaling factor that manipulates reverb send values, affecting the proportion of audio sent to adjacent rooms versus the proportion sent to the emitter's current room. This global factor is multiplied by the per-portal AkPortalParams::AdjacentRoomBleed value. Valid range: (0.0 - infinity).   

  |  |  |
  | --- | --- |
  |  | **注記：** Values approaching 0 may result in abrupt portal transitions. |

  When calculating reverb send amounts, each portal's aperture is multiplied by this factor, altering its perceived size:
  - 1.0 (Default): Maintain portals at their true geometric size.
  - > 1.0: Increases the perceived size of all portals, allowing more bleed into adjacent rooms.
  - < 1.0: Decreases the perceived size of all portals, reducing bleed into adjacent rooms.
- **Enable Geometric Diffraction and Transmission**   
  Enables the computation of geometric diffraction and transmission paths for all sources that have the **Enable Diffraction and Transmission** box selected in the Positioning tab of the Wwise Property Editor. 该标记会启用围绕（衍射）和穿过（透射）几何构造的声音路径。通过将 **Enable Geometric Diffraction and Transmission** 设为 false，可确保仅将几何构造用于计算反射。为了实施衍射计算，必须在几何构造上启用衍射边缘。If **Enable Geometric Diffraction and Transmission** is false but a sound has "Enable Diffraction and Transmission" selected in the positioning tab of Wwise Authoring, the sound only diffracts through portals but passes through geometry as if it were not there. 若游戏本身执行声障计算，但仍将几何构造传给 Spatial Audio 来执行反射计算，请禁用此设置。
- **Calc Emitter Virtual Position**   
  在设为 true 时，Wwise Spatial Audio 会计算在 Portal 两侧或几何构造周围发生衍射的发声体的视位置或虚声源位置，然后将该位置发送到声音引擎。
- **Transmission Operation**   
  The operation used to determine transmission loss on direct paths. Default value is Max.
- **Clustering Min Points**   
  Minimum number of emitters in a cluster. Default value is 2. Values less than 2 disable the clustering.
- **Clustering Max Distance**   
  Max distance between emitters to be considered as neighbors. This distance is specified for the reference distance defined by fClusteringDeadZoneDistance. Default value is 500.0.
- **Clustering Dead Zone Distance**   
  Defines a dead zone around the listener where no emitters are clusters. Default value is 1000.0.

## Communication Settings

- **Initialize System Comms**   
  此项表示是否对通信系统进行初始化。有些主机对通信系统的初始化有严格要求。仅在游戏在声音引擎初始化之前已经使用套接字时设为 false。
- **Pool Size**   
  此项表示通信池的大小。
- **Discovery Broadcast Port**   
  Wwise 设计工具通过该端口来广播 Game Discovery 请求以检测网络上运行的游戏。默认值为 24024。不可设为 0。
- **Command Port**   
  此项表示命令声道端口。若设为 0，则请求访问动态/临时端口。
- **Network Name**   
  使用该名称在 Wwise 设计工具内识别此游戏。若保留为空，则使用 `FApp::GetProjectName()`。

## Advanced Settings

- **Use Head Mounted Display Audio Device**   
  在工程当中涉及具有音频功能的头显时启用此项。
- **Max System Audio Objects**   
  此项表示最多预留多少个 System Audio Object。其他处理无法使用这些 System Audio Object。默认值为 128。
- **Enable Multi Core Rendering**   
  在设为 true 时，将 SoundEngine 处理任务分散到 Unreal Engine Task Graph 上。若更改此设置，则须重新启动 Editor。
- **Max Num Job Workers**   
  The maximum number of workers that the Sound Engine can request at any time. 若更改此设置，则须重新启动 Editor。
- **Job Worker Max Execution Time Usec**   
  此项表示为 Sound Engine 处理任务分配的最长时间（毫秒）。若更改此设置，则须重新启动 Editor。
- **IO Memory Size**   
  此项表示 I/O 内存池的大小（自动流）。该值会被向下舍入为 `uGranulrity` 的倍数，然后直接传给 `AK::MemoryMgr::CreatePool()`。
- **IO Granularity**   
  此项表示 I/O 请求粒度（通常设为每个请求的字节数）。
- **Target Auto Stream Buffer Length**   
  此项表示目标自动流缓冲区长度（毫秒）。在流达到缓冲区限值时，除非调度程序空闲，否则只针对 I/O 进行安排。
- **Use Stream Cache**   
  若设为 true，则设备尝试重复使用已经从磁盘进行流传输的 I/O 缓冲区。这在对短的循环声音进行流传输时特别有用。不过，在分配内存时 CPU 用量会有小幅增加，StreamManager 内存池中的内存用量略高。
- **Maximum Pinned Bytes in Cache**   
  此项表示可使用 `AK::SoundEngine::PinEventInStreamCache()` 或 `AK::IAkStreamMgr::PinFileInCache()` 锁定的最大字节数。
- **Enable Game Sync Preparation**   
  若设为 true，则启用 `AK::SoundEngine::PrepareGameSync`。
- **Continuous Playback Look Ahead**   
  此项表示在开始播放后续声音前 Continuous 容器将新声部实例化时设定的预读时间量。此预读时间量允许执行 I/O 处理。对于采用 Trigger Rate 或 Sample-accurate 过渡的 Continuous 容器，可藉此有效降低播放延迟。
- **Monitor Queue Pool Size**   
  此项表示监控队列内存池的大小。Release 版本中会忽略此参数。
- **Maximum Hardware Timeoput Ms**   
  此项表示要在硬件设备触发音频中断前等待多长时间（毫秒）。若在这段时间之后没有中断，声音引擎会恢复为无声模式并继续运行，直到硬件最终再次做出响应。
- **Debug Out Of Range Check Enabled**   
  此项为调试设置，其允许检查处理代码中是否存在超出范围的浮点值和 NaN 浮点值。一般情况下不要启用，因为该设置会占用大量 CPU。若在管线的多个点发现无效值，则会在日志中输出错误消息。
- **Debug Out Of Range Limit**   
  此项为调试设置。其仅在 Debug Out Of Range Check Enabled 为 true 时使用。该项定义样本可具有的最大数值。正常的音频必须控制在 +1/-1 之内。若将该限值设为大于 1 的值，则允许暂时或在短时间内偏离范围。默认值为 16。

# Integration Settings

**Reverb**

- **Max Simultaneous Reverb Volumes**   
  此项表示最多可有多少个 Ak Reverb Volume 同时影响声音。若将该值设为零，则禁用游戏中的所有 Ak Reverb Volume。注意，此设置并不会影响同时带有 Ak Room Component 的 Actor 上绑定的 Ak Late Reverb Component。

**Installation**

- **Wwise Project Path**   
  此项表示 UE 游戏所用 Wwise 工程的存储位置。Wwise 集成包需要使用此路径来创建游戏所需的 Wwise 资源（使用 Unreal Content Browser 或 Build 菜单内的 **Generate SoundBanks** 功能）。该路径与 Unreal 工程的目录相关（与 Unreal Engine 中指定的 `FPaths::ProjectDir()` 相同）。
- **Root Output Path**   
  The location of the folder that contains the Wwise project metadata, specifically the `ProjectInfo.json` file. This file contains the locations of the generated SoundBanks, which are required to play sound in the game. The path is relative to the Unreal project's content directory, as given by `FPaths::ProjectContentDir()`.

  |  |  |
  | --- | --- |
  |  | **注記：** 若要使用 External Source，则须将针对此路径所作的更改反映到 Wwise 工程内的 External Sources 设置中。 |

**Cooking**

- **Wwise Staging Directory**   
  在烘焙过程中暂存文件时将 .bnk 和 .wem 文件复制到该目录。
- **Package as Bulk Data**   
  Determines whether to package Wwise assets into Unreal UAssets during cooking instead of packaging them as individual files, as described in [Packaging Wwise Assets as Bulk Data](using_features_package_as_bulk_data.html).

**Obstruction Occlusion**

- **Default Collision Channel**   
  The default collision channel used for audio obstruction and occlusion calculations.

**Fit to Geometry**

- **Default Fit to Geometry Collision Channel**   
  此项表示在将 Ak Acoustic Portal 和 Ak Spatial Audio Volume 与周围几何构造贴合时使用的默认 Collision Channel 值。

**Reverb Assignment** (Refer to [Automatically Assigning a Reverb Aux Bus](features_editor_reverb_estimation.html#features_editor_reverb_estimation_aux_bus_map) for more information)

- **Default Surface Absorption**   
  The default surface absorption value to use when estimating environment Decay value. It is used for the decay estimations of environments without Acoustic Texture information. 默认值为 0.5。
- **Default Reverb Aux Bus**   
  The default Auxiliary Bus to choose for Automatic Reverb Assignment. Automatic Reverb Assignment can be enabled on Late Reverb components. When their Decay values exceed the highest Decay value in the Reverb Assignment Table, or if the table is empty or nonexistant, the default Auxiliary Bus is chosen. This Auxiliary Bus must have a reverb effect.
- **Reverb Assignment Table**   
  A table that associates Auxiliary Busses with Reverb Decay values. If Automatic Reverb Assignment is enabled on a Late Reverb component, its Decay value is compared to the table's Decay values. The chosen Auxiliary Bus is the one associated with the closest and highest Decay value in the table. If the given Decay value exceeds the highest Decay value in the table, or if the table is empty or nonexistant, the Default Reverb Aux Bus is chosen.   
  Rows must be of type FWwiseDecayAuxBusRow.
  - **Row Name** A unique name for the row.
  - **Decay** The number of seconds it takes for the sound reverberation in an environment to decay by 60 dB. Decay values are represented with floating point numbers. We recommend that consecutive Decay values differ by at least 0.01 to ensure the correct Auxiliary Bus is chosen for a given Decay value.
  - **Aux Bus** The Auxiliary Bus in Wwise Authoring that has a reverb effect to associate with the Decay value of the same row.
- **RTPCs**
  - **HFDamping Name**   
    （原有工作流程）该 RTPC 名称用于设置环境产生的高频阻尼估值。若已设置数值，则使用 "HFDamping" RTPC 值覆盖。
  - **Decay Estimate Name**   
    （原有工作流程）该 RTPC 名称用于估算声压级降低 60 dB 所需的时间。若已设置数值，则使用 "Decay Estimate" RTPC 值覆盖。
  - **Time to First Reflection Name**   
    （原有工作流程）该 RTPC 名称用于设置一阶反射声到达听者位置预计所需的时间。若已设置数值，则使用 "Time to First Reflection" RTPC 值覆盖。
  - **HFDamping RTPC**   
    该 RTPC 用于设置环境产生的高频阻尼估值。
  - **Decay Estimate RTPC**   
    该 RTPC 用于估算声压级降低 60 dB 所需的时间。
  - **Time to First Reflection RTPC**   
    该 RTPC 用于设置一阶反射声到达听者位置预计所需的时间。

**Initialization**

- **Init Bank**   
  The unique Init Bank for the Wwise project, which contains the basic information necessary to properly set up the Sound Engine.
- **Unreal Audio Routing**   
  Audio routing options that determine whether to use Unreal or Wwise audio exclusively, the two together, or to route Unreal audio through AudioLink. For more information, refer to [Selecting Audio Routing Options](using_audio_link.html#using_audio_link_enabling).
- **Wwise Sound Engine Enabled**   
  Indicates whether the Wwise Sound Engine is enabled, depending on the selected audio routing option.
- **Wwise Audio Link Enabled**   
  Indicates whether the Wwise AudioLink is enabled, depending on the selected audio routing option.
- **Default Listener Scaling Factor**   
  The default value of the scaling factor when a default listener is created.
- **Suspend Audio During Focus Loss**   
  Determines whether to suspend audio during loss of focus of the editor or game.
- **Render During Focus Loss**   
  Determines whether to continue rendering audio while audio is suspended during focus loss. Only applicable if **Suspend Audio During Focus Loss** is enabled.

**Localization**

- **Unreal Culture to Wwise Culture**   
  此项用于从 Unreal Culture 代码映射到 Wwise Language。这样可以直接通过 Unreal Culture 代码来调用 **Set Current Audio Culture**。有关详细信息，请参阅 [Localizing Audio Assets](using_features_localization.html) 章节。

**Asset Creation**

- **Default Asset Creation Path**   
  The path in which to create assets dragged from the Wwise Browser.

**Geometry Surface Properties**

- **Verify and Update**   
  Verify each row of the Geometry Surface Properties Table below and remove rows with an invalid Physical Material.
- **Default Acoustic Texture**   
  The default Acoustic Texture set on a surface of a Spatial Audio Volume actor when Fit to Geometry is used and no geometry is hit. The default value is None, which indicates a completely reflective surface.
- **Default Transmission Loss**   
  The default Transmission Loss value set on a surface of a Spatial Audio Volume actor when Fit to Geometry is used and no geometry is hit. The valid range is between 0 and 1. The default value is 0, which indicates that sound can pass through the surface without any loss. A surface with 0 transmission loss is considered transparent. It disables any reflections and does not use the Acoustic Texture.
- **Geometry Surface Properties Table**   
  The table that associates Geometry Surface Properties (Acoustic Texture and Transmission Loss) with Physical Materials. This table is used to retrieve the Geometry Surface Properties according to the Static Mesh's Physical Materials when using the [AkGeometryComponent](pg_features_spatialaudio.html#features_objects_akgeometrycomponent) or when using [Fit to Geometry](sa_fittogeometry.html) with the [AkSpatialAudioVolume](pg_features_spatialaudio.html#features_objects_akspatialaudiovolume).   
  Rows must be of type FWwiseGeometrySurfacePropertiesRow. We recommend that you do not add or remove rows. Rows are updated when Physical Material assets are added to or removed from the project. Rows are also updated when an Acoustic Texture with a name similar to a Physical Material is added to the project.
  - **Row Name** The asset path to a Physical Material in the current project.
  - **Acoustic Texture** The Acoustic Texture to associate with the Physical Material of the same row. Acoustic Textures consist of a group of absorption values representing the percentage by which sound within a relative frequency range is dampened after a reflection.
  - **Transmission Loss** The value by which to filter a sound modeling transmission through geometry.

# User Settings

**Installation**

- **Wwise Windows Installation Path**   
  The location of Wwise Authoring on your Windows development machine. This option will need to be updated when a new version of Wwise Authoring is required by the integration changes.
- **Wwise Mac Installation Path**   
  The location of Wwise Authoring on your Mac development machine. You must update this value when integration changes require you to install a new version of Wwise Authoring.

|  |  |
| --- | --- |
|  | **注記：** If these installation paths are not correctly set, Unreal cannot generate the Wwise SoundBanks required for the game. |

- **Root Output Path User Override**   
  The location of the folder that contains the Wwise project metadata, as determined by a user override in the Wwise User SoundBank Settings. The folder includes the `ProjectInfo.json` file, which contains the paths to the generated SoundBanks.

**WAAPI**

- **WAAPI IP Address**   
  此项表示用于连接到 [Wwise Authoring API (WAAPI)](using_features_waapi.html) 的 IP Address。
- **WAAPI Port**   
  此项表示用于连接到 WAAPI 的 Port。
- **Auto Connect to WAAPI**   
  此项允许通过 WAAPI 将 Unreal Editor 自动连接到 Wwise。
- **Auto Sync Selection**   
  Whether to synchronize the selection between the Wwise Browser and the Wwise Project Explorer.

**Error Message Translator**

- **XML Translator Timeout**   
  此项表示分配给 XML 文件阅读器来搜索 ID 的最长时间（毫秒）。若设为 0，则将其禁用。
- **Waapi Translator Timeout**   
  此项表示分配给通过 WAAPI 连接来搜索 ID 的最长时间（毫秒）。若设为 0，则将其禁用。

Error Translator 用于在有相应信息时将错误消息中的数字 ID 转换为用户可读的名称。您可以通过 `SoundBanksInfo.xml` 或 WAAPI 来实现这一操作。 若 SoundBank 文件旁边有 `SoundBanksInfo.xml` 文件（可选），通过 XML 来实现会更快一些。 WAAPI 的优势在于可直接从 Wwise 实例读取最新信息。不过网络通信速度可能会很慢，因为其在默认情况下是禁用的。

**Assets Reload**

- **Ask for Wwise Assets Reload**   
  此项用于打开相应通知。在 Unreal Editor 中操作时，用户必须先接受该通知再重新加载 Wwise Asset Data。

**Viewports**

- **Visualize Rooms and Portals**   
  此项用于在 Viewport 中直观地呈现 Rooms 和 Portal。须在 Viewport 中启用实时设置。
- **Show Reverb Info**   
  When enabled, information about `AkReverbComponents` is displayed in viewports, above the component's UPrimitiveComponent parent. 须在 Viewport 中启用实时设置。

# Wwise Simple External Source Manager Settings

- **Media Info Table**   
  此表格包含用于在工程中加载各个 External Source 媒体所需的全部信息。此表格中的所有文件都将打包到构建好的工程中。
- **External Source Default Media**   
  该可选表格用于定义 MediaInfoTable 中的默认媒体条目以便在加载 External Source 时一并加载。
- **External Source Staging Directory**   
  此项表示在烘焙工程时要将 External Source 媒体暂存到哪个位置。从该位置加载构建好的工程中包含的 External Source 媒体。

# 初始化 SoundEngine

SoundEngine 初始化步骤在 `FAkSoundEngineInitialization::Initialize()` 方法中执行。在此方法中，会通过 Wwise Initialization Settings 内针对每个平台设定的数值来配置内存、流播放、IO、声音引擎、平台、音乐引擎和通信设置。

有关 SoundEngine 初始化的详细信息，请参阅 Wwise SDK 文档中的“[初始化声音引擎的不同模块](https://www.audiokinetic.com/library/?source=SDK&id=workingwithsdks__initialization.html)”章节。