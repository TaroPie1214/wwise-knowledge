# Release Notes 2023.1.0

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Release Notes 2023.1.0

The following sections list and describe the changes to Wwise between version 2022.1.8 and version 2023.1.0.  
此处提供了有关平台的特定信息：

[Windows 2023.1.0](windows_releasenotes_2023_1_0.html)

有关早期版本的信息，请参阅 [过往版本的发行说明](previousreleases.html) 章节。

- [新增功能](whatsnew_2023_1_0.html#generic_feature_changes_2023_1)
- [API 改进](whatsnew_2023_1_0.html#generic_api_changes_2023_1)
- [行为改进](whatsnew_2023_1_0.html#generic_behavior_changes_2023_1)
- [性能改进](whatsnew_2023_1_0.html#generic_perf_changes_2023_1)
- [其他改进](whatsnew_2023_1_0.html#generic_misc_2023_1)
- [漏洞修复](whatsnew_2023_1_0.html#generic_bugs_2023_1)
- [社区报告的漏洞修复](whatsnew_2023_1_0.html#generic_community_bugs_2023_1)
- [Beta 版发布以来社区报告的漏洞修复](whatsnew_2023_1_0.html#generic_post_beta_bugs_2023_1)

# 新增功能

- **WG-29468** 现在支持最多为每个对象应用 255 个效果器。
- **WG-39278** (WAAPI) 在 [ak.wwise.core.object.delete](ak_wwise_core_object_delete.html) 、 [ak.wwise.core.object.move](ak_wwise_core_object_move.html) 、 [ak.wwise.core.object.copy](ak_wwise_core_object_copy.html) 、 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 和 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 中添加了对 Work Unit 的支持。
- **WG-42230** (Spatial Audio) 现在角落和边缘位置都设置了衍射路径。这样可以大大减少对象绕到障碍物后面时路径突然切入/切出的情形，使得音频输出更为平滑。
- **WG-44681** (WAAPI) 现在可使用 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 来通过 WAAPI 创建和组织 Music Switch Container。
- **WG-47295** (WAAPI) 使用对象列表重写了 Sequence Container 对象模型。现在可通过 WAAPI 执行序列相关操作。
- **WG-52539** 向 IAkPluginServiceMixer 接口添加了新的函数。现在插件可使用 Wwise 中现有的高性能双二阶滤波器，不需要再单独开发定制的实现方案。
- **WG-53279** 为 Reflect 插件添加了便捷的解决方案，以减轻反射声和直达声之间的干扰造成的相位偏移问题。
- **WG-54869** (WAAPI) [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 现在支持为多种对象类型导入音频文件。其中包括 Work Unit、Virtual Folder、Container、Sound、Audio File Source、Music Segment、源插件和效果器插件。
- **WG-57314** 向 Integration Demo 添加了 Motion 和 Reflect 插件。另外还对其进行了修改，以便将来演示其他插件。
- **WG-57421** (WAAPI) 添加了函数 [ak.wwise.core.profiler.saveCapture](ak_wwise_core_profiler_savecapture.html) 以便保存性能分析器捕获会话。
- **WG-58608** (WAAPI) 添加了版本控制 API。详见 [ak.wwise.core.sourceControl.add](ak_wwise_core_sourcecontrol_add.html) 、 [ak.wwise.core.sourceControl.checkOut](ak_wwise_core_sourcecontrol_checkout.html) 、 [ak.wwise.core.sourceControl.commit](ak_wwise_core_sourcecontrol_commit.html) 、 [ak.wwise.core.sourceControl.delete](ak_wwise_core_sourcecontrol_delete.html) 、 [ak.wwise.core.sourceControl.getSourceFiles](ak_wwise_core_sourcecontrol_getsourcefiles.html) 、 [ak.wwise.core.sourceControl.getStatus](ak_wwise_core_sourcecontrol_getstatus.html) 、 [ak.wwise.core.sourceControl.move](ak_wwise_core_sourcecontrol_move.html) 、 [ak.wwise.core.sourceControl.revert](ak_wwise_core_sourcecontrol_revert.html) 和 [ak.wwise.core.sourceControl.setProvider](ak_wwise_core_sourcecontrol_setprovider.html) 章节。
- **WG-58676** (WAAPI) 在返回选项中引入了 JSON 匿名对象访问器以便按对象对属性进行分组。
- **WG-59020** Steering 声像摆位器现在可输出到 Ambisonics 总线。
- **WG-59482** (Spatial Audio) Wwise Spatial Audio 库现在可在内部执行 Room 几何包含关系检测计算。之前需要使用 `AK::SpatialAudio::SetGameObjectInRoom` API 将 Game Object 指派给 Room。现在只要使用 `AkRoomParams::GeometryInstanceID` 为各个 Room 指派了几何构造就可自动执行这种计算。若要覆盖内部 Room 几何包含关系检测计算值，请调用 `AK::SpatialAudio::SetGameObjectInRoom`。Wwise 会停止针对给定 Game Object 自动更新 Room。在此之后，可调用 `AK::SpatialAudio::UnsetGameObjectInRoom` 来恢复内部 Room 几何包含关系检测计算。同时，向 `AkRoomParams` 添加了新的成员：`AkRoomParams::RoomPriority`。在 Game Object 实际处于两个 Room 内时（比如某个 Room 处在另一 Room 内），内部 Room 几何包含关系检测算法会使用其来决定要向哪个 Room 指派 Game Object。在这种情况下，会指派给具有更高优先级的 Room。
- **WG-59684** 现在单击 Capture Log、Audio Object 3D Viewer 和 Game Object 3D Viewer 中的 Display options 按钮会在单独的视图中打开选项。
- **WG-60166** (WAAPI) 在返回选项中添加了相应支持，以便联用数个返回多个对象的访问器。比如，children.name
- **WG-60274** (WAAPI) 对结合 WAAPI 使用版本控制系统的用户体验做了改进。
- **WG-60358** Wwise 现在会自动计算听者和发声体的 Room 指派。可通过调用 `SetGameObjectInRoom` 来覆盖自动指派的 Room，并通过调用 `UnsetGameObjectInRoom` 来重新予以启用。
- **WG-60615** (WAAPI) 添加了新的函数以暴露版本控制操作。
- **WG-60616** (WAAPI/WAQL) 添加了新的访问器：mediaId、conversionHash 和 contentHash。
- **WG-60834** 为 Tab Delimited Import 添加了新的 **OriginalsSubFolder** 列标题。
- **WG-61101** (WAAPI) 添加了 [ak.wwise.core.log.addItem](ak_wwise_core_log_additem.html) 和 [ak.wwise.core.log.clear](ak_wwise_core_log_clear.html) 以执行相应日志操作。
- **WG-61119** 现在察看 Audio Device 会像其他对象一样在底部显示 Meter 和 Effects 选项卡。对于 Bus，底部也会显示 Meter 选项卡。Meter 视图现在可设为锁定模式。这样就可显示 4 个以上电平表来对不同对象做电平测量。
- **WG-61181** 添加了 Audio Device Meter 视图。在选中 Audio Device 时，会在 Object Tab 底部显示该视图。该 Meter 视图替代了之前集成在 Audio Device Editor 中的电平表。
- **WG-61312** 现在可调节 SoundCaster 列表的大小。
- **WG-61374** 将 Property Editor 替换为了 Voice Profiler 布局中的 Object Tab 以便显示对象的属性。
- **WG-61962** 音频文件分析和 WEM 生成现在可共用多条线程。
- **WG-61965** (WAAPI) 向 [ak.wwise.ui.project.open](ak_wwise_ui_project_open.html) 添加了参数 autoCheckOutToSourceControl。
- **WG-62000** (Spatial Audio) 针对高阶衍射路径对路径计算做了改进。为了设法找到最短的路径，对绕过多个边缘的路径进行了优化，使得衍射系数更为精确。
- **WG-62069** 为了将 Music Track 转换为 Music Subtrack，向 Music Segment Editor 添加了新的快捷菜单。
- **WG-62096** (WAAPI) 为了能在返回的对象中使用别名，在返回选项中引入了关键字 "as"。
- **WG-62097** (WAAPI) 为了便于处理对象列表，在返回选项中添加了新的函数（如 first、last、count、at 等）。
- **WG-62153** (WAAPI) 现在支持通过 [ak.wwise.core.object.set](ak_wwise_core_object_set.html) 导入插件媒体源。
- **WG-62630** Wwise 现在可计算游戏对象处在哪个 Room 中。
- **WG-62838** "Push All Modified Objects" 模式现在可在连接到游戏时将工程中所有的修改同步至游戏，即便对于之前会话中所做的更改也是如此。在连接后加载 SoundBank 时，会根据需要执行进一步的同步。
- **WG-63206** (WAAPI) 现在支持从性能分析数据检索 Loaded Media 信息。
- **WG-63256** (WAAPI) 现在支持从性能分析数据检索 CPU 用量信息。
- **WG-63257** (WAAPI) 现在支持从性能分析数据检索 Performance Monitor 计数器信息。
- **WG-63492** (WAAPI) 添加了新的实用程序函数 [ak.wwise.debug.generateToneWAV](ak_wwise_debug_generatetonewav.html) 以便生成测试 WAV 文件。
- **WG-63507** 现在会在使用对 Room 定义来说不严密的几何构造时生成错误消息。
- **WG-63574** 为了能在迁移期间执行版本控制操作，向 Project Migration 对话框添加了相应信息。
- **WG-64050** (Spatial Audio) 现在可在 Portal 之间无缝传播反射声。反射声可能会出现在 Portal 的任一端，也可能出现在两个 Portal 之间的 Room 内。
- **WG-64094** (WAAPI) 现在支持从性能分析数据检索 Streamed Media 信息。
- **WG-64095** (Spatial Audio) 新的 Reverb Zone 功能允许将不同的混响效果器指派给 Room 内的给定区域。Reverb Zone 是一种新的 Room。藉此，无需 Portal 就可在 Room 之间模拟声音传播。Reverb Zone 尤其适用于不便通过墙壁来分隔的空间（如遮盖区域、阳台和各种户外空间）。为便于管理 Reverb Zone 添加了两个新的 API 函数：`AK::SpatialAudio::SetReverbZone` 和 `AK::SpatialAudio::RemoveReverbZone`。
- **WG-64118** (WAAPI) 新增了以下与 Mute/Solo 相关的函数：
  - ak.wwise.core.audio.mute
  - ak.wwise.core.audio.solo
  - ak.wwise.core.audio.resetMute
  - ak.wwise.core.audio.resetSolo
- **WG-64159** 在 Game Object 3D Viewer 中的 Game Object List 中添加了 Room ID 列。
- **WG-64180** (WAAPI) 现在可在使用 WwiseConsole 启动 WAAPI 服务器时忽略工程参数。
- **WG-64194** (WAAPI) 添加了 [ak.wwise.ui.project.create](ak_wwise_ui_project_create.html) 和 [ak.wwise.console.project.create](ak_wwise_console_project_create.html) 以便通过 WAAPI 来创建和加载新的工程。
- **WG-64250** 为了给显示曲线的区域留出更多空间，在坐标图绘制方面做了改进。
- **WG-64411** 在 List View 中添加了对对象列表（效果器、RTPC 等）的支持。
- **WG-64882** 现在会对高度声道进行 3D 空间化处理而非直接弃用。
- **WG-65095** 现在可对 Loudness Normalization 做更多配置：不仅可以设置目标响度（默认值为 -23，与之前版本的目标响度对应），还可基于 Momentary Max 值而非 Integrated 进行归一化处理（对较短的音效来说效果通常会更好）。同时，还可在 List View 中以列的形式显示测得的响度值，并通过 WAAPI 和 WAQL 来查询。
- **WG-65100** 添加了四个 User Layout 以便根据自身工作流程来创建自定义布局。
- **WG-65118** 向 `AK::Wwise::Plugin::Host` 服务添加了 GetProjectLicenseID。该服务已更新到版本 2。
- **WG-65177** 现在在 Source Editor 的时间线标尺任意位置单击或拖动都会自动设置播放光标时间。在拖动光标时，会在工具提示中显示时间。
- **WG-65191** 在 Wwise 设计工具中使用 Recorder 效果器时，现在可在 **Authoring Tool Output Path** 中包含 "%s" 来将日期和时间添加到文件名中。这样的话，每次调用 Recorder 效果器都会创建新的文件，而非重复使用相同的文件名并覆盖相应内容。
- **WG-65226** 在 3D 查看器中添加了用于显示过渡区的选项。
- **WG-65437** 向 \*.project.create WAAPI 函数添加了平台参数。您可以借助这个新的参数来指明新工程所支持的平台。
- **WG-66122** 在 .cache 下的文件为只读状态的情况下，现在会在加载工程时显示错误消息。
- **WG-66350** 对于 Sound SFX 对象，现在会在 List View 中默认显示波形。
- **WG-66562** 在 Multi Editor 中添加了对效果器列表的支持。
- **WG-66725** 在 Wwise Project Settings 中，现在可指定保存工程和 SoundBank 文件时应用的行结束符 (LF 或 CRLF)。
- **WG-67403** 现在即便未选中 **Override parent** 也可从 Property Editor 的 Positioning 选项卡打开 Attenuation Editor。
- **WG-67559** 添加了实验性的 Live Media Transfer 功能。有关如何予以启用的详细信息，请参阅 [User Preferences](https://www.audiokinetic.com/library/edge/?source=Help&id=user_preferences)。

# API 改进

- **WG-53660** Sound Engine 节点（音频、总线和输出设备）现在最多支持 255 个效果器。您可以使用以下函数来在插槽 0-254 上设置效果器（参数 in\_uFXIndex）：
  - `AK::SoundEngine::SetActorMixerEffect`
  - `AK::SoundEngine::SetBusEffect`
  - `AK::SoundEngine::SetOutputDeviceEffect`
- **WG-61084** 因为移除了混音器插件，所以从 `AkSpeakerVolumeMatrixCallbackInfo` 移除了 `IAkMixerInputContext`。
- **WG-61344** 移除了 AK\_SCHEDULER\_BLOCKING 计划程序类型标记和相关的 IAkIOHookBlocking 接口。IAkIOHookDeferredBatch 现在是唯一的底层 I/O 挂钩接口。
- **WG-62665** 将函数 `OutputSearchedPaths` 由 `AK::StreamMgr::IAkFileLocationResolver` 移到了 `AK::StreamMgr::IAkLowLevelIOHook`。
- **WG-63463** 更正了错误代码名称 "AK\_CannotAddItseflAsAChild" 中的拼写错误。
- **WG-63988** 将 `EstimateHFDamping()` 的返回值由 AKRESULT 改为了 AkReal32。现在会直接返回 HF Damping 值。移除了参数 \_\_ AkReal32 out\_hfDamping。
- **WG-64048** (Spatial Audio) 添加了 `AkSpatialAudioInitSettings::uMaxEmitterRoomAuxSends` 来限制单个发声体可生成的 Game-defined Auxiliary Sends 的最大数量。
- **WG-64966** 移除了 `AkMemSettings::bUseDeviceMemAlways`，代之以新的设置 `AkMemSettings::bEnableSeparateDeviceHeap`。`AkMemSettings::bEnableSeparateDeviceHeap` 方便仅使用一个通用的内存堆。若已将 `AkMemSettings::bUseDeviceMemAlways` 设为 true，则应将 `AkMemSettings::bEnableSeparateDeviceHeap` 设为 false；若已为 `AkMemSettings::AllocDeviceVM` 和 `AkMemSettings::FreeDeviceVM` 设置自定义内存挂钩，则应为 `AkMemSettings::AllocVM` 和 `AkMemSettings::FreeVM` 做相应设置。
- **WG-65130** (Spatial Audio) 移除了 `AkGeometryParams::EnableTriangles`，将其替换为了 `AkGeometryInstanceParams::UseForReflectionAndDiffraction`。
- **WG-65303** 简化了 `AK::StreamMgr::IAkLowLevelIOHook` 接口：
  - I/O 函数不需要再提供返回值。
  - 现在只需针对各项操作来发送回调（每次都要调用，没有例外）。
- **WG-65602** (Spatial Audio) 为了对 Spatial Audio 的不断演进提供相应支持，更改了 [AkSpatialAudioInitSettings](struct_ak_spatial_audio_init_settings.html "Initialization settings of the spatial audio module.") 的默认值。对于大部分工程，不妨先设为默认设置。稍后可根据需要适当进行调节。针对特定产品和平台，在性能和品质之间求得平衡。
- **WG-66128** (Spatial Audio) 弃用了 `AkGeometryInstanceParams::RoomID`。在未来版本中会移除该参数。建议不要使用 RoomID，最好保留为默认值 (-1)。
- **WG-66185** 添加了新的 SDK 函数 `AK::SoundEngine::IsPluginRegistered`。
- **WG-66667** 将 `AKPLATFORM::AllocVM` 和 `AKPLATFORM::FreeVM` 的示例函数及其他一些虚拟内存相关函数和定义由 AkPlatformFuncs.h 移到了 AkMemoryMgrFuncs.h。鉴于这些改动，可能需要在代码中修改或添加某些头文件内容来解决编译器错误。
- **WG-67001** 向 `AkMarkerCallbackInfo` 添加了 size 成员；向 `AddOutputCaptureMarker` 添加了 size 参数；对 Wwise Wave Viewer 中同时显示的标记点做了修复。
- **WG-67058** 将 AK\_SIMD 的核心类型由 `AkSimd.h` 移到了 `AkSimdTypes.h`。对此，可能需要修改代码中的某些头文件内容来解决编译错误。

# 行为改进

- **WG-31188** 将 .akd 文件内容移到了工程的 .cache 文件夹内的数据库。现有 .akd 文件可以删除。
- **WG-47959** 现在提供给 WwiseConsole 来与现有工程交互的参数是跟主机当前工作目录而非工程目录相对的。
- **WG-59985** 对于使用 redirectOutput 选项的命令扩展，现在会以隐藏窗口的形式启动进程。
- **WG-61331** 在 Voice Monitor 的 **Bus** 字段中，现在会默认选择 **Master Audio Bus**。
- **WG-61333** 在 Voice Inspector 的 Contribution List 中，现在会默认展开 Spatial Audio 射线。右键单击 Contribution List 可使用新的 **Auto Expand Spatial Audio** 选项来禁用此功能。
- **WG-61770** 通过连续投射少量射线对射线追踪引擎做了改进。射线的投射不再取决于振动阈值设置（参见 [AkSpatialAudioInitSettings](struct_ak_spatial_audio_init_settings.html) 章节）。在射线追踪引擎的调用当间不会再清除射线。这些射线会一直保留，直到其变为无效状态。通过连续投射射线可在帧之间更好地分摊 CPU 负荷并减少 CPU 峰值的出现。同时，将默认的初级射线数降到了 10。
- **WG-62723** 在通过 Project Explorer 快捷菜单来创建使用源插件的 Sound SFX 时，现在会像所有其他新建的对象一样先将焦点移到对象名称再移到 Object Tab。
- **WG-62888** 在将 Wwise 连接到游戏时，现在无需重新生成 SoundBank 即可更新 AK Convolution Reverb IR。
- **WG-63600** 现在会在 Multi Editor、Keyboard Shortcuts and Commands 对话框和 List View 的 Object Property Settings 对话框中默认显示列表搜索筛选器。
- **WG-64024** (Wwise Console) 现在可针对 [waapi-server](ak_wwise_cli_waapiserver.html) 操作选择 `project` 参数。
- **WG-64046** (Spatial Audio) Portal Spread 计算现在会将听者偏离 Portal 前端的角度考虑在内。
- **WG-64358** 在 Capture Log、Game Object 3D Viewer 和 Audio Object 3D Viewer 的选项对话框中，将 Reset 按钮由右下角移到了左下角以免跟平常放置的 Cancel 按钮混淆。
- **WG-64817** Wwise 工具栏现在会在只有一项任务的情况下显示后台运行的任务的名称。否则，会显示正在执行和暂停执行的任务数。
- **WG-65038** (Spatial Audio) 在 Room 有几何构造可用的情况下，几何透射损失现在会覆盖 Room 透射损失。之前，Spatial Audio 会取几何（表面）透射损失值和 Room 透射损失值的最大值。不过，这样对既有透明表面又有不透明表面的 Room 来说会很麻烦。对于这样的 Room，只能将 Room 透射损失值设为最低的表面透射损失值。如此以来，混响和房间底噪就会是完全可闻的。通过在有几何构造可用时忽略 Room 透射损失值，现在可将 Room 透射损失设为具有代表性的平均值，并将其有效地用于混响空间化和房间底噪透射模拟。
- **WG-65089** 在结合 Spatial Audio 使用 `SetObjectObstructionAndOcclusion()` 时，现在只会将声障值和声笼值发送到直达路径。
- **WG-65361** 在两帧之间更改与镜像声源关联的声学材质时，Reflect 插件的输出信号现在会先闪避再淡入。之前，只会影响镜像声源的成分，而且方式较为粗暴。注意，建议使用不同的镜像声源 ID 来处理声学材质的实时切换。

# 性能改进

- **WG-53649** 将 Parametric EQ 由原地处理效果器转换为了原地对象处理器。也就是说，现在只会每条 Audio Objects 总线实例化一次，而不会每个 Audio Object 都实例化一次。这样可以节省一定的内存并大幅提升性能。比如，在 Audio Objects 总线上运行很多单声道 Audio Object 时，吞吐性能最多可提高 4 倍。注意，即便其现在被视为对象处理器，但行为或功能并无其他明显改变。
- **WG-57311** 减少了由 Spatial Audio 执行的小内存分配的数量。
- **WG-59366** 现在会异步获取 Work Unit 的 Source Control 状态图标。这样可以加快工程加载和部分版本控制操作的速度。而且，Refresh Icons 命令执行得也会更快。
- **WG-61576** 大幅提升了各种 Event Action（如 Stop All、Pause All、Seek All 和 Resume All 等）的性能。这样可以基本消除在执行这些操作的过程中 CPU 用量突然增加的情形。
- **WG-62148** 略微提升了对音频数据做 RMS 电平测量时的性能。
- **WG-65815** 现在会持续缓存 Originals 文件的音频元数据。这样在基于 Audio Source 时长或声道数运行 Query 或在 SoundBank 生成期间生成 "Estimated Duration" 元数据时运行速度会快很多。在填充缓存后，针对大型工程执行的这些操作现在只需几秒就可完成，不需要花好几分钟的时间。
- **WG-66168** 现在无需将几何构造与 Room 关联便可提升 CPU 性能。
- **WG-66253** 现在会在开始执行各自的混音操作时而非在 `CAkLEngine::ReleaseBuffersAndFeedbackAsync` 期间清理混音总线的音频缓冲区。这样可以消除 `CAkLEngine::ReleaseBuffersAndFeedbackAsync` 的大部分成本。
- **WG-66254** 对于由分贝转换为线性增益时所用的函数，现在对 0.0f 的输入会返回 1.0f 的精确结果而非 0.999039。在实施有些旨在减少应用增益的优化时，现在可以更可靠地检查 1.0f 的结果，使得结果的相关性更强。比方说，这样可以减少 Audio Object 的开销。
- **WG-66256** 对于 3D Audio Mixer 效果器以及 3D Audio 设备相应对象的最终混音和分类，现在会在源缓冲区和目标缓冲区具有相同配置时执行更为简单的下混。
- **WG-66258** 现在会在本地数据库中保留原始文件的音频格式以便在 Wwise 设计工具操作期间更快地进行访问。
- **WG-67234** 大幅提升了 Audio Objects 总线在很多情况下的性能。在源总线和目标总线之间只有一条作为 Audio Object 进行处理的输出连接时，Audio Object 的元数据和音频数据不会再创建单独的内存分配或执行数据的副本。对于具有多条输出连接的总线（由于辅助发送或启用了听者相对通路并绑定到多点定位的游戏对象），仍需要单独的数据副本。
- **WG-67320** 将新的内存分配系统 "Temp Alloc" 集成到了声音引擎中，专门用来处理仅适用于单个 Audio Render 时钟周期的分配。您可以将之用于音频总线的音频缓冲区以及音频对象的元数据。在大部分情况下，这样可以大大减少音频渲染期间执行的内存分配数，提升某些多线程场景下的性能，并略微减少用于内存处理的内存池碎片。有关如何调节和管理这一新系统的详细信息，请参阅 [调节 Temp Alloc 内存](goingfurther_optimizingmempools_reducing_memory.html#goingfurther_optimizingmempools_tempallocs) 章节。注意，作为这一改进的一部分，Voice Graph 中的 Audio Objects 总线将不再支持使用 "Feedback" 连接。这种用例会造成很多其他微妙且致命的问题，因此不再予以支持。对于会因 Wwise Spatial Audio 或其他音频传播处理工具而创建反馈场景的应用，必须确保所有反馈连接的目标总线都是混音总线。

# 其他改进

- **WG-56589** 移除了混音器插件。AK Channel Router 混音器插件现在是效果器插件。所有自定义混音器插件都要迁移到混音器插件。有关更多详细信息，请参阅 [移除了混音器插件](whatsnew_2023_1_migration.html#mixer_plugin_removal) 。
- **WG-57597** 移除了已弃用的 Wwise Motion Generator 源插件。
- **WG-60924** 将用户界面中的术语 "Workgroup" 替换为了更为常用的 "Source Control"。
- **WG-62998** (WAAPI) 移除了文件 `WwiseAuthoringAPI.json`。该文件之前存放在安装目录 `<Wwise>\Authoring\Data\Schemas` 下。现在其被拆分成了多个文件并全部存放在目录 `<Wwise>\Authoring\Data\Schemas\WAAPI` 下。
- **WG-64758** 添加了新的宏 `AK_DISABLE_OPTIMIZATIONS` 和 `AK_ENABLE_OPTIMIZATIONS` 以便有选择性地禁用和启用对部分 Wwise 代码内容的优化。这在调试某些问题时可能会很有用。
- **WG-65150** 现在会随 Wwise 安装 Visual C++ Redistributable 库而非全局性地予以安装。
- **WG-65157** 现在会随 Wwise 设计工具可执行文件一并移动 `Tools`（如 FilePackager）目录下的二进制文件。
- **WG-66118** 基于 Perforce 2023.1 和 OpenSSL 3.1.1 库对 Perforce 版本控制插件进行了升级。
- **WG-68127** 将 SoundBank 生成日志消息由 "Header output path" 改为了 "Root output path"。

# 漏洞修复

- **WG-55217** 已修复：在将列宽重置为默认值时，在 High DPI 模式下显得太小了。
- **WG-58205** 已修复：在 List View 中的 Search 字段为空时不显示键盘快捷方式。
- **WG-58830** 已修复：将属性（如颜色）添加到 Control Surface Session 会损坏工程。
- **WG-60296** 已修复：在察看对象时，光标会移动到 Contents Editor。
- **WG-60477** 已修复：卸载 SoundCaster 中的对象的父级 Work Unit 会触发断言并导致颜色出错。
- **WG-61762** 已修复：SoundBank Manager 下的 Object Tab 的空间不够。对 SoundBank 布局做了更改：移除了 Object Tab，包含了 SoundBank Editor 和 Property Editor。
- **WG-62760** 已修复：在将某一 Sequence Container 添加到另一 Sequence Container 的播放列表时，Wwise 发生崩溃。
- **WG-62910** 已修复：在将视图最大化再关闭之后，重新打开视图会创建全屏视图。
- **WG-63299** 已修复：(Spatial Audio) 在计算特定几何构造上的衍射时，`NudgeToShadowZone()` 触发断言。
- **WG-63332** 已修复：在通过 WAAPI 创建插件时，有时会显示阻止消息对话框。
- **WG-63479** 已修复：在纵向缩小 Project Launcher 对话框时，有时会过早地裁剪底部的按钮。
- **WG-63485** 已修复：在更新 WAV 文件时，有时会重置 AK Convolution Reverb IR 的 Trim Start 和 Trim End。
- **WG-64251** 已修复：在选中 Event 时，Property Editor 标题更新为 "Event Editor"。但在选中音频对象时，标题没有变回 "Property Editor"。
- **WG-64281** 已修复：在不察看对象的情况下，无法使用 Search 工具结果中的快捷菜单。
- **WG-64283** 已修复：Reverb Estimation 服务的 `EstimateHFDamping()` 函数给出的值不正确，跟 HF Damping 的定义不一致。
- **WG-64342** 已修复：WaveViewer.exe 没有输出任何音频。
- **WG-64457** 已修复：在针对大型音频文件生成 AKD 文件后关闭 Wwise 时发生崩溃。
- **WG-64913** 已修复：在从 Offline Rendering 模式切换到 Real-time 模式时发生崩溃。
- **WG-64947** 已修复：直到移动光标才填充 Advanced Profiler 的选项卡。
- **WG-65039** 已修复：序列播放列表中的 Play 图标不够清晰。现在会清晰地显示各种图标以便执行像“播放父对象”和“延迟”这样的操作。
- **WG-65210** 已修复：Object Tab 内的 Secondary Editor 的横向空间无法很好地容纳效果器；在重置布局时，Secondary Editor 没有恢复为默认大小。
- **WG-65331** 已修复：在 Game Object 具有多条与同一辅助总线对应的发送线路但听者不相同时，Voice Inspector 会显示不适用于选定路径的发送值。
- **WG-65358** 已修复：在执行多核音频处理的过程中发生死锁。
- **WG-65377** 已修复：在启用 High DPI 的情况下，User Interface 元素（如分组框）显得太细了。
- **WG-65472** 已修复：修改权重对子级 Switch Container 或 Blend Container 不起作用。
- **WG-65479** 已修复：在设为特定的屏幕分辨率和缩放比例时，无法访问 Error Report 工具中的有些按钮。
- **WG-65593** 已修复：对于基于实例的视图（如 Meter），工具提示中提及更改选定通道而非更改实例。
- **WG-65649** 已修复：在通过 WAAPI 关闭 Wwise 时可能会发生死锁。
- **WG-65766** 已修复：New Project 对话框中的 OK 和 Cancel 按钮有时会被裁剪。
- **WG-65887** 已修复：Game Object 3D Viewer 视图的对比度不佳（尤其是在 Light 主题下）。
- **WG-65926** 已修复：将多声道声源或总线摆位到单声道总线时的响度明显高于将同一声源摆位到非单声道总线时的响度。
- **WG-66129** 已修复：Capture Log 中的有些长错误消息被截断了。
- **WG-66132** 已修复：在通过对象快捷菜单创建 Event 时，Event Editor 为空。
- **WG-66137** 已修复：在 Nuendo Game Audio Connect 插件同步过程中可能会发生崩溃。
- **WG-66305** 已修复：在加载引用未知 State Group 的 SoundBank 时返回故障消息。转而以 0 s 的过渡时间创建缺失的 State Group。
- **WG-66418** 已修复：(WAAPI) 在尝试将 WAV 文件作为 Sound 导入到同名的现有 Voice 时没有报告错误。
- **WG-66589** 已修复：无法在自定义命令 JSON 文件中以字符串的形式提供版本。
- **WG-66621** 已修复：使用箭头按钮增大/减小 Interactive Music 条目中的属性值会破坏 Tab 导航的顺序。
- **WG-66697** 已修复：在同一电脑上打开不同版本的 Wwise 的情形下，只在一个版本的 Wwise 中停靠的视图会在打开其他版本的 Wwise 时消失。
- **WG-66729** 已修复：在为多个对象创建 Event 时，没有打开 Event Editor 窗口。
- **WG-66756** 已修复：在 Debug 版本的 Wwise 中，在有些视图中执行时，部分 **Current View** 快捷方式会触发断言。
- **WG-66764** 已修复：在同时处理大量错误时，Integration Demo 发生崩溃。
- **WG-67112** 已修复：在关联 Music Switch Container 中的 Music Segment 时，没有相应地启用或禁用 Transport Control 和 SoundCaster 中的按钮。
- **WG-67256** 已修复：Project 菜单中的 Language Manager 条目被命名为 Language 而非 Language Manager。
- **WG-67318** 已修复：有时会将无效的音频数据用于总线电平测量以及 Compressor、Expander 和 Reflect 插件。
- **WG-67367** 已修复：Transport Control 的 Game Syncs 列表（RTPC、State Group、Switch Group）缺少某些条目。
- **WG-67441** 已修复：在个别瞬态起始点检测情形下出现计算错误。
- **WG-67941** 已修复：在取消停靠 Voice Monitor 视图时，有些线条看上去是透明的。
- **WG-68223** 已修复：在同时处理多个 Audio Object 时，Compressor 和 Expander 效果器有时会导致出现毛刺噪声。

# 社区报告的漏洞修复

- **WG-39193** 已修复：在重命名后没有更新 Event 的 Short ID。
- **WG-43538** 已修复：在处理 Sequence Container 的 Playlist 时可能会发生崩溃。
- **WG-44631** 已修复：无法使用空格键试听 Search 工具结果中所选的条目。
- **WG-49914** 已修复：(WAAPI) 在保存工程时无法自动签出 Work Unit。参数 autoAddToSourceControl 已添加到 [ak.wwise.core.project.save](ak_wwise_core_project_save.html) 函数。默认值为 false。
- **WG-51233** 已修复：在导入制表符分割的文件时，无法在 Events 层级结构下创建 Work Unit。
- **WG-54872** 已修复：(WAAPI) 命令 FindProjectExplorerSyncGroup1 无法选择多个对象。
- **WG-55164** 已修复：通过 Tab Delimited Import 更改现有对象的属性可能会导致对象重复。
- **WG-60190** 已修复：在将声部输出到 HDR 和非 HDR 总线的混音时，Voice Monitor 在 Bus Input 模式下内容显示有误。
- **WG-60670** 已修复：(Spatial Audio) 在 Emitter 和 Listener 之间存在中间 Room 时，没有为 Portal 应用 Obstruction 和 Occlusion。
- **WG-60975** 已修复：(Spatial Audio) 在进入具有多个 Portal 的 Room 时，声像摆位突然发生变化。
- **WG-62158** 已修复：对于运行高延迟解码的声部，在与寻址命令相同的音频时钟周期内执行 State 过渡时，`CAkSrcMedia::PrepareNextBuffer` 触发断言。
- **WG-63296** 已修复：在出现浮点错误后，Source Editor 错误地报告错误。
- **WG-63450** 已修复：如果工程包含要签出的文件，保存时可能会发生崩溃。
- **WG-63589** 已修复：(WAAPI) ak.wwise.core.profiler.enableProfilerData 中缺少对 "soundbanks" 和 "spatialAudioRaycasting" 的支持。
- **WG-64858** 已修复：在将 SetOfflineRendering 设为 false 来恢复正常播放时，音频没有恢复。
- **WG-64934** 已修复：在连接 Wwise 时，没有在运行时声音引擎中移除 Wwise 中已经移除的 RTPC 曲线。
- **WG-65184** 已修复：在移除效果器时可能会发生崩溃。
- **WG-66145** 已修复：在使用默认参数来调用时，`AK::SoundEngine::ReplaceOutput` 调用触发断言。
- **WG-66303** 已修复：在 File Manager 中执行版本控制操作时可能会发生崩溃。
- **WG-66366** 已修复：在加载包含大量活跃声音的大型 SoundBank 时出现性能问题。
- **WG-66370** 已修复：`AK::SoundEngine::ReplaceOutput` 锁定。
- **WG-66468** 已修复：即便在 SoundBank 设置中启用了 **Use Source Control for Generated Files** 选项，也无法通过版本控制系统管理 `Wwise_IDs.h` 文件。
- **WG-66836** 已修复：对作为虚声部开始播放的流播放 Music Track 的处理不一致。
- **WG-67027** 已修复：在同时出现多个 Music Transition 时，调试当中可能会触发断言。
- **WG-67031** 已修复：(WAAPI) 在导入音频后在日志中发现警告或错误时， [ak.wwise.core.audio.import](ak_wwise_core_audio_import.html) 不再报告错误。现在还会在结果中返回日志。
- **WG-67125** 已修复：在播放与多点定位的 Game Object 绑定并输出到 Audio Objects 总线的声音时，假如启用 Listener Relative Routing 并将 3D Spatialization 设为 None，会针对对应 Game Object 的多个位置分别创建 Audio Object。现在只会创建一个 Audio Object。这样无论设置了多少个 Game Object 位置，都能确保在播声音的响度保持一致。
- **WG-67128** 已修复：在重新加载列表的情况下编辑某些属性时发生崩溃。
- **WG-67187** 已修复：在使用 Convolution IR 信息控件中的箭头键时可能会发生崩溃。
- **WG-67349** 已修复：WAAPI SoundBank 生成当中所用的语言名称不支持某些字符（如短横线）。
- **WG-67469** 已修复：SoundBank XML 文件中的 MaxAttenuation 属性可能会触发“格式无效”错误。
- **WG-68026** 已修复：`AK::SoundEngine::TryUnsetMedia` 无法处理活跃的 MIDI 文件。
- **WG-68039** 已修复：在流播放的声音转为虚声部时没有释放文件句柄。
- **WG-68060** 已修复：在键入 Perforce 密码时可能会发生崩溃。

# Beta 版发布以来社区报告的漏洞修复

- **WG-67276** 已修复：Random Container 的播放时长被报告为 0。
- **WG-67900** 已修复：在通过 MIDI 设备执行 Control Surface Learn 时发生崩溃。
- **WG-67901** 已修复：在导入音频文件时可能会发生崩溃。
- **WG-67988** 已修复：无法取消链接 Output Bus 和其他对象属性。
- **WG-68112** 已修复：对于设为 Continuous 的 Switch Container，既不会停止播放声音，也没有应用 Fade-in/Fade-out。